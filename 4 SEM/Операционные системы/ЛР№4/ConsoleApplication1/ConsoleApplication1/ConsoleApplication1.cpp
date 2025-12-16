#include <windows.h>
#include <tlhelp32.h>
#include <psapi.h>
#include <iostream>

// Функция для получения идентификатора текущего процесса
DWORD getCurrentProcessId() {
    return GetCurrentProcessId();
}

// Функция для получения псевдодескриптора текущего процесса
HANDLE getCurrentProcessHandle() {
    return GetCurrentProcess();
}

// Функция для дублирования дескриптора
HANDLE duplicateProcessHandle(HANDLE hProcess) {
    HANDLE hDuplicate = NULL;
    if (DuplicateHandle(GetCurrentProcess(), hProcess, GetCurrentProcess(), &hDuplicate, 0, FALSE, DUPLICATE_SAME_ACCESS)) {
        return hDuplicate;
    }
    else {
        std::cerr << "Failed to duplicate handle. Error: " << GetLastError() << std::endl;
        return NULL;
    }
}

// Функция для открытия процесса по его идентификатору
HANDLE openProcess(DWORD processId) {
    HANDLE hProcess = OpenProcess(PROCESS_QUERY_INFORMATION | PROCESS_VM_READ, FALSE, processId);
    if (hProcess == NULL) {
        std::cerr << "Failed to open process. Error: " << GetLastError() << std::endl;
    }
    return hProcess;
}

// Функция для закрытия дескриптора
void closeHandle(HANDLE hProcess) {
    if (!CloseHandle(hProcess)) {
        std::cerr << "Failed to close handle. Error: " << GetLastError() << std::endl;
    }
}

// Функция для создания снимка процессов
HANDLE createSnapshot() {
    HANDLE hSnapshot = CreateToolhelp32Snapshot(TH32CS_SNAPPROCESS, 0);
    if (hSnapshot == INVALID_HANDLE_VALUE) {
        std::cerr << "Failed to create snapshot. Error: " << GetLastError() << std::endl;
    }
    return hSnapshot;
}

// Функция для вывода списка процессов
void listProcesses() {
    HANDLE hSnapshot = createSnapshot();
    if (hSnapshot == INVALID_HANDLE_VALUE) {
        return;
    }

    PROCESSENTRY32 pe32;
    pe32.dwSize = sizeof(PROCESSENTRY32);

    if (!Process32First(hSnapshot, &pe32)) {
        std::cerr << "Failed to get first process. Error: " << GetLastError() << std::endl;
        CloseHandle(hSnapshot);
        return;
    }

    do {
        std::wcout << L"Process Name: " << pe32.szExeFile << L" | Process ID: " << pe32.th32ProcessID << std::endl;
    } while (Process32Next(hSnapshot, &pe32));

    CloseHandle(hSnapshot);
}

// Функция для получения информации о памяти процесса
void getProcessMemoryInfo(DWORD processId) {
    HANDLE hProcess = openProcess(processId);
    if (hProcess == NULL) {
        return;
    }

    PROCESS_MEMORY_COUNTERS pmc;
    if (GetProcessMemoryInfo(hProcess, &pmc, sizeof(pmc))) {
        std::cout << "Process ID: " << processId << std::endl;
        std::cout << "Working Set Size: " << pmc.WorkingSetSize << std::endl;
        std::cout << "Pagefile Usage: " << pmc.PagefileUsage << std::endl;
    }
    else {
        std::cerr << "Failed to get memory info for process with ID: " << processId << std::endl;
    }

    closeHandle(hProcess);
}

int main() {
    // Шаг 1: Получение идентификатора текущего процесса
    DWORD processId = getCurrentProcessId();
    std::cout << "Current Process ID: " << processId << std::endl;

    // Шаг 2: Получение псевдодескриптора текущего процесса
    HANDLE hProcess = getCurrentProcessHandle();
    std::cout << "Current Process Handle: " << hProcess << std::endl;

    // Шаг 3: Дублирование дескриптора
    HANDLE hDuplicate = duplicateProcessHandle(hProcess);
    if (hDuplicate != NULL) {
        std::cout << "Duplicate Process Handle: " << hDuplicate << std::endl;

        // Шаг 4: Открытие процесса
        HANDLE hOpenProcess = openProcess(processId);
        if (hOpenProcess != NULL) {
            std::cout << "Open Process Handle: " << hOpenProcess << std::endl;

            // Шаг 5: Закрытие дублированного дескриптора
            closeHandle(hDuplicate);
            std::cout << "Closed Duplicate Handle" << std::endl;

            // Шаг 6: Закрытие дескриптора открытого процесса
            closeHandle(hOpenProcess);
            std::cout << "Closed Open Process Handle" << std::endl;
        }
    }

    // Вывод списка процессов и их информации
    listProcesses();

    // Пример получения информации о памяти текущего процесса
    getProcessMemoryInfo(processId);

    return 0;
}
