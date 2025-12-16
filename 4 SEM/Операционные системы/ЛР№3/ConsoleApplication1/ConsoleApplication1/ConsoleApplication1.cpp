#include <windows.h>
#include <tlhelp32.h>
#include <psapi.h>
#include <iostream>
#include <vector>

void GetMemoryStatus() {
    MEMORYSTATUS memStatus;
    GlobalMemoryStatus(&memStatus);

    std::cout << "Total physical memory: " << memStatus.dwTotalPhys / (1024 * 1024) << " MB" << std::endl;
    std::cout << "Available physical memory: " << memStatus.dwAvailPhys / (1024 * 1024) << " MB" << std::endl;
    std::cout << "Total virtual memory: " << memStatus.dwTotalVirtual / (1024 * 1024) << " MB" << std::endl;
    std::cout << "Available virtual memory: " << memStatus.dwAvailVirtual / (1024 * 1024) << " MB" << std::endl;
}

void ListProcesses() {
    HANDLE hProcessSnap;
    PROCESSENTRY32 pe32;
    hProcessSnap = CreateToolhelp32Snapshot(TH32CS_SNAPPROCESS, 0);

    if (hProcessSnap == INVALID_HANDLE_VALUE) {
        std::cerr << "CreateToolhelp32Snapshot failed!" << std::endl;
        return;
    }

    pe32.dwSize = sizeof(PROCESSENTRY32);
    if (!Process32First(hProcessSnap, &pe32)) {
        std::cerr << "Process32First failed!" << std::endl;
        CloseHandle(hProcessSnap);
        return;
    }

    do {
        std::wcout << L"Process name: " << pe32.szExeFile << L" (PID: " << pe32.th32ProcessID << L")" << std::endl;

        HANDLE hProcess = OpenProcess(PROCESS_QUERY_INFORMATION | PROCESS_VM_READ, FALSE, pe32.th32ProcessID);
        if (hProcess != NULL) {
            PROCESS_MEMORY_COUNTERS pmc;
            if (GetProcessMemoryInfo(hProcess, &pmc, sizeof(pmc))) {
                std::cout << "    WorkingSetSize: " << pmc.WorkingSetSize / 1024 << " KB" << std::endl;
                std::cout << "    PagefileUsage: " << pmc.PagefileUsage / 1024 << " KB" << std::endl;
            }
            CloseHandle(hProcess);
        }
    } while (Process32Next(hProcessSnap, &pe32));

    CloseHandle(hProcessSnap);
}

int main() {
    GetMemoryStatus();
    ListProcesses();
    return 0;
}
