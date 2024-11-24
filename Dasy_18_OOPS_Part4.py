class A:
    def show(self):
        print('CLASS A FUNCTION CALLED')


class B(A):
    def show(self):
        print('CLASS B FUNCTION CALLED')


class C(A):
    def show(self):
        print('CLASS C FUNCTION CALLED')


class D(B, C):
    pass


d = D()
d.show()

print(D.__mro__)

from abc import ABC, abstractmethod


class PaymentAbstract(ABC):

    @abstractmethod
    def send_money(self, receiver_id):
        pass

    @abstractmethod
    def receive_money(self, sender_details):
        pass

    @abstractmethod
    def validate_sender_receiver(self):
        pass


class Payment(PaymentAbstract):

    def __init__(self, account_number):
        self.account_number = account_number

    def send_money(self, receiver_id):
        print(f"{self.account_number} sending money to {receiver_id}")

    def receive_money(self, sender_details):
        print(f'Amount received from this sender {sender_details} and deposited to the account')

    def validate_sender_receiver(self):
        print('validated sender & receiver')


class UPIPayment(Payment):

    def __init__(self, account_number):
        super().__init__(account_number) # Sending to argument Parent class contructor

    def send_money(self, receiver_id):
        # custom logic
        pass


    def per_day_limit(self):
        print('Checking per day limit')


class CreditCardPayment(Payment):

    def __init__(self, account_number):
        super().__init__(account_number)

    def apply_interest(self):
        print('Applying Interest')


class DebitCardPayment(Payment):

    def __init__(self, account_number):
        super().__init__(account_number)

    def is_card_expired(self):
        return False



upi_obj = UPIPayment('99052803805')
upi_obj.send_money('vicky@hdfc')


class NormalDelivery:

    def collect_location(self):
        print('collect from this location is hotel')


    def deliver_location(self):
        print('deliver to this location')


class Instamart(NormalDelivery):

    def collect_location(self):
        print('Collection location is near by instamart dark store')
