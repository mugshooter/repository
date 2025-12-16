#include <iostream>
#include <windows.h>
#include <vector>

constexpr int THREADCOUNT = 2;

HANDLE ghMutex;

DWORD WINAPI WriteToDatabase(LPVOID);

void Cleanup() {
    if (ghMutex != NULL)
        CloseHandle(ghMutex);
}

int main() {
    std::vector<HANDLE> aThread(THREADCOUNT);
    DWORD ThreadID;

    ghMutex = CreateMutex(NULL, FALSE, NULL);
    if (ghMutex == NULL) {
        std::cerr << "CreateMutex error: " << GetLastError() << std::endl;
        Cleanup();
        return 1;
    }

    for (int i = 0; i < THREADCOUNT; i++) {
        aThread[i] = CreateThread(NULL, 0, WriteToDatabase, NULL, 0, &ThreadID);
        if (aThread[i] == NULL) {
            std::cerr << "CreateThread error: " << GetLastError() << std::endl;
            Cleanup();
            return 1;
        }
    }

    WaitForMultipleObjects(THREADCOUNT, aThread.data(), TRUE, INFINITE);

    for (auto& thread : aThread) {
        CloseHandle(thread);
    }
    Cleanup();

    return 0;
}

DWORD WINAPI WriteToDatabase(LPVOID lpParam) {
    UNREFERENCED_PARAMETER(lpParam);

    DWORD dwCount = 0;
    DWORD dwWaitResult;

    while (dwCount < 20) {
        dwWaitResult = WaitForSingleObject(ghMutex, INFINITE);

        switch (dwWaitResult) {
            case WAIT_OBJECT_0:
                try {
                    std::cout << "Thread " << GetCurrentThreadId() << " writing to database..." << std::endl;
                    dwCount++;
                } catch (...) {
                    std::cerr << "Exception occurred while writing to database." << std::endl;
                }
                if (!ReleaseMutex(ghMutex)) {
                    std::cerr << "ReleaseMutex error: " << GetLastError() << std::endl;
                }
                break;
            case WAIT_ABANDONED:
                std::cerr << "Wait for mutex abandoned." << std::endl;
                return FALSE;
        }
    }
    return TRUE;
}
