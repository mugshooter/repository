#include <windows.h>
#include <iostream>

int main() {
    HANDLE hMapFile; // Дескриптор для объекта отображения файла
    LPVOID lpMapAddress; // Указатель на адрес отображенной памяти
    HANDLE hFile; // Дескриптор для файла
    char* String; // Указатель на строку

    // Открытие или создание файла "MyFile.txt" с возможностью чтения и записи
    hFile = CreateFile("MyFile.txt",
        GENERIC_READ | GENERIC_WRITE,
        FILE_SHARE_READ | FILE_SHARE_WRITE,
        NULL,
        OPEN_ALWAYS,
        FILE_ATTRIBUTE_NORMAL,
        NULL);

    if (hFile == INVALID_HANDLE_VALUE) {
        std::cerr << "Could not open file\n";
        return 1;
    }

    // Создание объекта отображения файла с флагом PAGE_WRITECOPY (копирование при записи)
    hMapFile = CreateFileMapping(hFile,
        NULL,
        PAGE_WRITECOPY,
        0, 0,
        "MyFileObject");

    if (hMapFile == NULL) {
        std::cerr << "Could not create file-mapping object.\n";
        CloseHandle(hFile);
        return 1;
    }

    // Отображение файла в память с режимом доступа FILE_MAP_COPY (копирование при записи)
    lpMapAddress = MapViewOfFile(hMapFile,
        FILE_MAP_COPY,
        0, 0, 0);

    if (lpMapAddress == NULL) {
        std::cerr << "Could not map view of file.\n";
        CloseHandle(hMapFile);
        CloseHandle(hFile);
        return 1;
    }

    String = (char*)lpMapAddress; // Приведение указателя к типу char*

    std::cin.get(); // Ожидание нажатия клавиши

    sprintf(String, "Hello, world"); // Запись строки "Hello, world" в отображенную память
    std::cout << String << std::endl; // Вывод строки на экран

    // Размонтирование отображения файла из памяти
    if (!UnmapViewOfFile(lpMapAddress)) {
        std::cerr << "Could not unmap view of file.\n";
    }

    // Закрытие дескрипторов
    CloseHandle(hMapFile);
    CloseHandle(hFile);

    return 0;
}
