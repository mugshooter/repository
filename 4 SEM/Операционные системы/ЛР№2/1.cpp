#include <windows.h>
#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>

int main() {
    // Создание текстового файла и запись чисел в него
    std::ofstream file("numbers.txt");
    if (!file.is_open()) {
        std::cerr << "Failed to create file." << std::endl;
        return 1;
    }
    file << "10 5 20 3 8";
    file.close();
    std::cout << "Numbers written to file successfully." << std::endl;

    // Открытие файла и поиск минимального числа
    std::ifstream inputFile("numbers.txt");
    if (!inputFile.is_open()) {
        std::cerr << "Failed to open file." << std::endl;
        return 1;
    }

    std::vector<int> numbers;
    int num;
    while (inputFile >> num) {
        numbers.push_back(num);
    }
    inputFile.close();

    if (numbers.empty()) {
        std::cerr << "No numbers found in file." << std::endl;
        return 1;
    }

    int minNumber = *std::min_element(numbers.begin(), numbers.end());

    std::cout << "The minimum number in the file is: " << minNumber << std::endl;

    return 0;
}
