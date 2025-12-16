#include <iostream>
#include <Windows.h>

int main() {
    // Получаем значения цветов
    COLORREF btnFaceColor = GetSysColor(COLOR_BTNFACE);
    COLORREF grayTextColor = GetSysColor(COLOR_GRAYTEXT);
    COLORREF desktopColor = GetSysColor(COLOR_DESKTOP);

    // Выводим значения цветов
    std::cout << "COLOR_BTNFACE: " << btnFaceColor << std::endl;
    std::cout << "COLOR_GRAYTEXT: " << grayTextColor << std::endl;
    std::cout << "COLOR_DESKTOP: " << desktopColor << std::endl;

    return 0;
}
