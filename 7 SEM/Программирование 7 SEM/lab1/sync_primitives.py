import threading
import time

# 2.2: Банк с Lock
class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance
        self.lock = threading.Lock()

    def deposit(self, amount):
        with self.lock:
            self.balance += amount

    def withdraw(self, amount):
        with self.lock:
            if self.balance >= amount:
                self.balance -= amount

# 2.5: Event
def event_demo():
    event = threading.Event()
    def setter():
        time.sleep(3)
        event.set()
    
    def waiter():
        event.wait()
        print("Event occurred")
    
    threading.Thread(target=setter).start()
    threading.Thread(target=waiter).start()