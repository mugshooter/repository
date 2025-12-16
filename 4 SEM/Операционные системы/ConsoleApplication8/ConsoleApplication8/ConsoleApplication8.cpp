#include <windows.h>
#include <iostream>
#include <cmath>

// Глобальные переменные
int Sum = 0, iNumber = 5, jNumber = 300000;
HANDLE hFirstSemaphore, hSecondSemaphore;

// Функция второго потока
DWORD WINAPI SecondThread(LPVOID) {
    int i, j;
    double a, b = 1.0;
    for (i = 0; i < iNumber; i++) {
        WaitForSingleObject(hSecondSemaphore, INFINITE); // Ожидание разрешения от второго семафора
        for (j = 0; j < jNumber; j++) {
            Sum = Sum + 1;
            a = sin(b);
        }
        ReleaseSemaphore(hFirstSemaphore, 1, NULL); // Освобождение первого семафора
    }
    return 0;
}

int main() {
    int i, j;
    HANDLE hThread;
    DWORD IDThread;
    double a, b = 1.0;

    // Создание семафоров
    hFirstSemaphore = CreateSemaphore(NULL, 0, 1, "MyFirstSemaphore");
    hSecondSemaphore = CreateSemaphore(NULL, 1, 1, "MySecondSemaphore");

    // Создание второго потока
    hThread = CreateThread(NULL, 0, SecondThread, NULL, 0, &IDThread);
    if (hThread == NULL) {
        std::cerr << "Failed to create thread." << std::endl;
        return 1;
    }

    // Основной поток выполнения
    for (i = 0; i < iNumber; i++) {
        WaitForSingleObject(hFirstSemaphore, INFINITE); // Ожидание разрешения от первого семафора
        for (j = 0; j < jNumber; j++) {
            Sum = Sum - 1;
            a = sin(b);
        }
        std::cout << " " << Sum << " ";
        ReleaseSemaphore(hSecondSemaphore, 1, NULL); // Освобождение второго семафора
    }

    WaitForSingleObject(hThread, INFINITE); // Ожидание завершения второго потока

    // Закрытие дескрипторов семафоров
    CloseHandle(hFirstSemaphore);
    CloseHandle(hSecondSemaphore);

    std::cout << " " << Sum << " ";

    return 0;
}
