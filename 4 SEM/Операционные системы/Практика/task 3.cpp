#include <iostream>
using namespace std;

int main() {
    int i = 1, j = 2, k = 0;
    try {
        if (j == 0)
            throw "Division by zero";
        k = i / j;
        cout << "in try" << endl;
        cout << "k=" << k << endl;
    } catch (const char* error) {
        cout << "in except" << endl;
        cout << "Error: " << error << endl;
        cout << "k=" << k << endl;
    }
    return 0;
}
