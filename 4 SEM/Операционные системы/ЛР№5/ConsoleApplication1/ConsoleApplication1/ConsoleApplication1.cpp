#include <iostream>
#include <thread>
#include <mutex>

using namespace std;

class BankAccount {
private:
    int balance;
    mutex mtx;

public:
    BankAccount(int initialBalance) : balance(initialBalance) {}

    void takeMoney(int amount) {
        lock_guard<mutex> lock(mtx);
        if (balance >= amount) {
            balance -= amount;
            cout << "Thread " << this_thread::get_id() << " withdrew " << amount << " dollars. Balance: " << balance << endl;
        }
        else {
            cout << "Thread " << this_thread::get_id() << " tried to withdraw " << amount << " dollars, but insufficient funds." << endl;
        }
    }

    int checkBalance() {
        return balance;
    }
};

class Client {
private:
    BankAccount& account;
    int amount;

public:
    Client(BankAccount& acc, int amt) : account(acc), amount(amt) {}

    void operator()() {
        while (account.checkBalance() > 0) {
            account.takeMoney(amount);
            this_thread::sleep_for(chrono::milliseconds(100)); // Pause to simulate time taken to withdraw money
        }
    }
};

int main() {
    int initialBalance = 1000; // Initial balance
    const int numberOfClients = 5; // Number of clients
    int withdrawalAmount = 100; // Amount to withdraw by each client

    BankAccount account(initialBalance);

    cout << "Running with synchronization:" << endl;

    thread clients[numberOfClients];
    for (int i = 0; i < numberOfClients; ++i) {
        clients[i] = thread(Client(account, withdrawalAmount));
    }

    for (int i = 0; i < numberOfClients; ++i) {
        clients[i].join();
    }

    return 0;
}
