#include <iostream>
#include <fstream>
#include <string>

int main() {
    std::ifstream inputFile("MyFile.txt", std::ios::binary);
    if (!inputFile.is_open()) {
        std::cerr << "Failed to open input file." << std::endl;
        return 1;
    }

    std::ofstream outputFile("MyOutputFile.txt", std::ios::binary | std::ios::trunc);
    if (!outputFile.is_open()) {
        std::cerr << "Failed to open output file." << std::endl;
        return 1;
    }

    char ch;
    while (inputFile.get(ch)) {
        outputFile.put(ch);
    }

    inputFile.close();
    outputFile.close();

    std::cout << "File copied successfully." << std::endl;

    return 0;
}
