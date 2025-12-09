# ================= Инкапсуляция =================
class Product:
    def __init__(self, name, price):
        self.name = name
        self._price = price
        self.__discount = 0

    def get_price(self):
        return self._price * (1 - self.__discount / 100)

    def set_discount(self, percent):
        if percent > 50:
            raise ValueError("Скидка не может быть больше 50%")
        self.__discount = percent

    def apply_extra_discount(self, code):
        if code == "VIP123":
            self.__discount = min(self.__discount + 5, 50)
        else:
            print("Неверный код")

# Проверка Product
p = Product("Iphone", 1000)
p.set_discount(20)
print("Цена со скидкой:", p.get_price())
p.apply_extra_discount("VIP123")
print("Цена после VIP:", p.get_price())
p.apply_extra_discount("wrong")
print("Цена итоговая:", p.get_price())

# ================= Абстракция =================
from abc import ABC, abstractmethod

class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount): pass
    @abstractmethod
    def refund(self, amount): pass

class CardPayment(PaymentMethod):
    def pay(self, amount): print(f"Оплата картой: {amount}")
    def refund(self, amount): print(f"Возврат картой: {amount}")

class CashPayment(PaymentMethod):
    def pay(self, amount): print(f"Оплата наличными: {amount}")
    def refund(self, amount): print(f"Возврат наличными: {amount}")

class CryptoPayment(PaymentMethod):
    def pay(self, amount): print({"type":"crypto","amount":amount,"currency":"USDT"})
    def refund(self, amount): print({"type":"crypto","amount":amount,"currency":"USDT","refund":True})

class PaymentProcessor:
    def __init__(self, method: PaymentMethod): self.method = method
    def process(self, amount): self.method.pay(amount)

# Проверка Payment
PaymentProcessor(CardPayment()).process(100)
PaymentProcessor(CashPayment()).process(50)
PaymentProcessor(CryptoPayment()).process(200)
