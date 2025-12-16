#include <iostream>
#include <Windows.h>

int main() {
    // Пример использования функции AnsiToOemBuff
    char inputBuffer[] = "Пример текста для преобразования";
    char outputBuffer[100];
    AnsiToOemBuff(inputBuffer, outputBuffer, sizeof(inputBuffer));

    std::cout << "Преобразованный текст: " << outputBuffer << std::endl;

    // Пример использования функции GetCursorPos
    POINT cursorPos;
    GetCursorPos(&cursorPos);
    std::cout << "Позиция курсора: X = " << cursorPos.x << ", Y = " << cursorPos.y << std::endl;

    // Пример использования функции GetNumberFormat
    double number = 12345.6789;
    wchar_t formattedNumber[20];
    GetNumberFormatW(LOCALE_USER_DEFAULT, 0, std::to_wstring(number).c_str(), nullptr, formattedNumber, sizeof(formattedNumber)/sizeof(formattedNumber[0]));

    std::wcout << L"Форматированное число: " << formattedNumber << std::endl;

    // Пример использования функции SetCaretPos
    SetCaretPos(100, 100);
    std::cout << "Позиция каретки установлена на (100, 100)." << std::endl;

    return 0;
}
