#include <windows.h>
#include <stdio.h>

int main(void) {
    HANDLE hFile, hHeap;
    int iRet = 0;
    void* pMem;
    long FileSize = 0, FilePos = 0;
    DWORD iRead = 0, iWrite = 0;
    wchar_t* String; // Используем тип wchar_t для строк

    // Открытие файла для чтения и записи
    hFile = CreateFile(L"MYFILE.TXT", GENERIC_READ | GENERIC_WRITE, 0, NULL, OPEN_EXISTING, FILE_ATTRIBUTE_NORMAL, NULL);
    if (hFile == INVALID_HANDLE_VALUE) {
        wprintf(L"Could not open file\n"); // Используем wprintf для вывода Unicode строк
        return 1;
    }

    // Получение размера файла
    FileSize = GetFileSize(hFile, NULL);
    wprintf(L"FileSize = %ld\n", FileSize); // Используем wprintf для вывода Unicode строк

    // Выделение памяти из кучи для чтения данных из файла
    hHeap = GetProcessHeap();
    pMem = HeapAlloc(hHeap, HEAP_ZERO_MEMORY, FileSize + 2);
    if (pMem == NULL) {
        wprintf(L"HeapAlloc Error\n"); // Используем wprintf для вывода Unicode строк
        CloseHandle(hFile);
        return 1;
    }
    String = (wchar_t*)pMem;

    // Чтение данных из файла
    ReadFile(hFile, pMem, FileSize, &iRead, NULL);
    wprintf(L"Read %lu bytes\n", iRead); // Используем wprintf для вывода Unicode строк

    // Замена всех символов в строке на '1'
    for (FilePos = 0; FilePos < FileSize; FilePos++)
        String[FilePos] = L'1'; // Используем L перед символом для создания широкого символа (wchar_t)

    // Установка указателя файла в начало
    SetFilePointer(hFile, 0, NULL, FILE_BEGIN);
    getchar();

    // Запись данных в файл
    WriteFile(hFile, pMem, FileSize, &iWrite, NULL);
    wprintf(L"Write %lu bytes\n", iWrite); // Используем wprintf для вывода Unicode строк

    // Сброс буферов записи
    iRet = FlushFileBuffers(hFile);
    if (iRet == 0) {
        wprintf(L"FlushFileBuffers Error\n"); // Используем wprintf для вывода Unicode строк
    }

    // Освобождение памяти и закрытие файла
    HeapFree(hHeap, 0, pMem);
    CloseHandle(hFile);

    return 0;
}
