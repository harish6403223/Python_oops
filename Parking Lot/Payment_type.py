from abc import ABC, abstractmethod

class Payment_type(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def payment(s, cost):
        pass

class UPI(Payment_type):
    def payment(s, cost):
        print("Payment through UPI done rs. "+str(cost))

class Cash(Payment_type):
    def payment(s, cost):
        print("Payment through Cash done rs. "+str(cost))

class Online(Payment_type):
    def payment(s, cost):
        print("Payment through Online banking done rs. "+str(cost))