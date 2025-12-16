#include <windows.h>
#include <iostream>

int main() {
    int iRet = 0; // Переменная для хранения результатов функций
    wchar_t Buf[512]; // Буфер для хранения текущего каталога
    int bufSize = 512; // Размер буфера

    // Получение текущего каталога
    iRet = GetCurrentDirectory(bufSize, Buf);
    if (iRet == 0) {
        std::wcerr << L"GetCurrentDirectory error: " << GetLastError() << std::endl;
        return 1;
    }
    std::wcout << L"iRet = " << iRet << L", current directory: " << Buf << std::endl;

    // Создание нового каталога
    iRet = CreateDirectory(L"f:\\tmp1", NULL);
    if (!iRet) {
        std::wcerr << L"CreateDirectory error: " << GetLastError() << std::endl;
        return 1;
    }

    // Установка текущего каталога
    iRet = SetCurrentDirectory(L"f:\\tmp1");
    if (!iRet) {
        std::wcerr << L"SetCurrentDirectory error: " << GetLastError() << std::endl;
        return 1;
    }

    // Получение нового текущего каталога
    iRet = GetCurrentDirectory(bufSize, Buf);
    if (iRet == 0) {
        std::wcerr << L"GetCurrentDirectory error: " << GetLastError() << std::endl;
        return 1;
    }
    std::wcout << L"iRet = " << iRet << L", current directory: " << Buf << std::endl;

    return 0;
}
