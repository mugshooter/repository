#include <windows.h>
#include <iostream>
#include <cmath>

// Функция для выполнения расчетов
void Calculations() {
    int i, N = 50000000;
    double a, b;
    for (i = 0; i < N; i++) {
        b = static_cast<double>(i) / static_cast<double>(N);
        a = sin(b);
    }
}

// Функция потока
DWORD WINAPI SecondThread(LPVOID lpParam) {
    std::cout << "Начало второго потока\n";
    Calculations();
    std::cout << "Конец второго потока\n";
    return 0;
}

int main() {
    DWORD dwThreadId, dwThrdParam;
    HANDLE hThread;

    // Создание второго потока
    hThread = CreateThread(
        NULL,                       // Атрибуты безопасности по умолчанию
        0,                          // Размер стека по умолчанию
        SecondThread,               // Функция потока
        &dwThrdParam,               // Аргумент для функции потока
        0,                          // Флаги создания
        &dwThreadId                 // Получение идентификатора потока
    );

    if (hThread == NULL) {
        std::cerr << "Не удалось создать поток\n";
        return 1;
    }

    // Установка приоритета потока
    SetThreadPriority(hThread, THREAD_PRIORITY_ABOVE_NORMAL);

    // Приостановка потока
    SuspendThread(hThread);

    // Ожидание ввода клавиши
    std::cin.get();

    // Возобновление потока
    ResumeThread(hThread);

    std::cout << "Начало первого потока\n";
    Calculations();
    std::cout << "Конец первого потока\n";

    // Ожидание завершения второго потока
    WaitForSingleObject(hThread, INFINITE);

    // Закрытие дескриптора потока
    CloseHandle(hThread);

    return 0;
}
