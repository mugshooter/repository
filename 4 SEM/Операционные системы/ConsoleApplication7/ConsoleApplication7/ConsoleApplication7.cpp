#include <windows.h>
#include <iostream>

int main() {
    HANDLE hRead, hWrite;
    char BufIn[100], * BufOut = "0123456789";
    int BufSize = 100;
    DWORD BytesOut = 10, BytesIn = 5, bytesRead, bytesWritten;

    // Create a pipe
    if (!CreatePipe(&hRead, &hWrite, NULL, BufSize)) {
        std::cerr << "Create pipe failed.\n";
        return 1;
    }

    // Write data to the pipe
    if (!WriteFile(hWrite, BufOut, BytesOut, &bytesWritten, NULL)) {
        std::cerr << "Write to pipe failed.\n";
        return 1;
    }

    std::cout << "Written into pipe " << bytesWritten << " bytes: ";
    for (DWORD i = 0; i < bytesWritten; i++) {
        std::cout << BufOut[i];
    }
    std::cout << std::endl;

    // Read data from the pipe
    if (!ReadFile(hRead, BufIn, BytesIn, &bytesRead, NULL)) {
        std::cerr << "Read from pipe failed.\n";
        return 1;
    }

    std::cout << "Read from pipe " << bytesRead << " bytes: ";
    for (DWORD i = 0; i < bytesRead; i++) {
        std::cout << BufIn[i];
    }
    std::cout << std::endl;

    // Close pipe handles
    CloseHandle(hRead);
    CloseHandle(hWrite);

    return 0;
}
