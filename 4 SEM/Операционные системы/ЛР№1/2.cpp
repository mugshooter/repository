#include <iostream>
#include <windows.h>
#include <locale.h>


BOOL CALLBACK EnumDateFormatsProc(LPTSTR lpDateFormatString) {
    std::wcout << lpDateFormatString << std::endl;
    return TRUE;
}


int main() {
    // Получение локального времени
    SYSTEMTIME sysTime;
    GetLocalTime(&sysTime);
    std::cout << "Локальное время: " << sysTime.wHour << ":" << sysTime.wMinute << ":" << sysTime.wSecond << std::endl;
   
    // Перечисление форматов даты для английской локали (en-US)
    std::cout << "Форматы даты:" << std::endl;
    EnumDateFormats(EnumDateFormatsProc, MAKELCID(MAKELANGID(LANG_ENGLISH, SUBLANG_ENGLISH_US), SORT_DEFAULT), DATE_SHORTDATE);


    return 0;
}
