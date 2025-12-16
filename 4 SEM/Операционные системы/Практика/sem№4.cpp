#include <iostream>
#include <windows.h>
#include <vector>

constexpr int MAX_SEM_COUNT = 10;
constexpr int THREADCOUNT = 12;

HANDLE ghSemaphore;

DWORD WINAPI ThreadProc(LPVOID);

int main() {
    std::vector<HANDLE> aThread(THREADCOUNT);
    DWORD ThreadID;

    ghSemaphore = CreateSemaphore(NULL, MAX_SEM_COUNT, MAX_SEM_COUNT, NULL);
    if (ghSemaphore == NULL) {
        std::cerr << "CreateSemaphore error: " << GetLastError() << std::endl;
        return 1;
    }

    for (int i = 0; i < THREADCOUNT; i++) {
        aThread[i] = CreateThread(NULL, 0, ThreadProc, NULL, 0, &ThreadID);
        if (aThread[i] == NULL) {
            std::cerr << "CreateThread error: " << GetLastError() << std::endl;
            return 1;
        }
    }

    WaitForMultipleObjects(THREADCOUNT, aThread.data(), TRUE, INFINITE);

    for (auto& thread : aThread)
        CloseHandle(thread);
    CloseHandle(ghSemaphore);

    return 0;
}

DWORD WINAPI ThreadProc(LPVOID lpParam) {
    UNREFERENCED_PARAMETER(lpParam);

    DWORD dwWaitResult;
    bool bContinue = true;

    while (bContinue) {
        dwWaitResult = WaitForSingleObject(ghSemaphore, INFINITE);

        switch (dwWaitResult) {
            case WAIT_OBJECT_0:
                std::cout << "Thread " << GetCurrentThreadId() << ": wait succeeded" << std::endl;
                bContinue = false;
                Sleep(5);
                if (!ReleaseSemaphore(ghSemaphore, 1, NULL)) {
                    std::cerr << "ReleaseSemaphore error: " << GetLastError() << std::endl;
                }
                break;
            default:
                std::cerr << "WaitForSingleObject error: " << GetLastError() << std::endl;
                break;
        }
    }
    return TRUE;
}
