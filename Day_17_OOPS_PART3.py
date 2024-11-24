from abc import abstractmethod, ABC


class SampleVilla(ABC):

    @abstractmethod
    def rooms(self):
        pass

    @abstractmethod
    def bathroom(self):
        pass

    @abstractmethod
    def toilets(self):
        pass

    @abstractmethod
    def living_room(self):
        pass

    @abstractmethod
    def kitchen(self):
        pass

    @abstractmethod
    def parking(self):
        pass

    @abstractmethod
    def terrace(self):
        pass

    @abstractmethod
    def water_motor(self):
        pass

    @abstractmethod
    def eb_meter(self):
        pass



class VillaNo1(SampleVilla):

    def __init__(self):
        pass

    def rooms(self):
        print("2 BedRooms")

    def bathroom(self):
        print("2 bathroom")

    def toilets(self):
        print("2 toilets")

    def living_room(self):
        print("1 living Room")

    def kitchen(self):
        pass

    def parking(self):
        pass

    def terrace(self):
        pass

    def water_motor(self):
        pass

    def eb_meter(self):
        pass

    def automatic_door_system(self):
        print("Automatic Door System Applied")


# obj1 = VillaNo1()


class Payment(ABC):

    @abstractmethod
    def send_money(self):
        pass

    @abstractmethod
    def receive_money(self):
        pass

    @abstractmethod
    def validate_sender_receiver(self):
        pass


class CreditCardPayment(Payment):

    def send_money(self):
        card_car_number = 9925903590239
        reciever_bank_details = 'axis bank'
        # send_money

    def receive_money(self):
        pass

    def validate_sender_receiver(self):
        pass

    def validity(self):
        pass

    def apply_interest(self):
        pass


class DebitCardPayment(Payment):

    def send_money(self):
        pass

    def receive_money(self):
        pass

    def validate_sender_receiver(self):
        pass

    def validity(self):
        pass


class UPI(Payment):

    def send_money(self):
        UPI_ID = 'UOKNJSNFN'
        # SEND

    def receive_money(self):
        pass

    def validate_sender_receiver(self):
        pass

    def per_day_limit(self):
        pass


class Parent:

    def __init__(self, name):
        self.name = name

    def show_name(self):
        print(f'From Parent - Name', self.name)

class Parent2:

    def __init__(self, age):
        self.age = age

class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)
        self.name = name
        self.age = age

    def show_name(self):
        print('From Child - Name', self.name)

    def show_name_with_age(self):
        super().show_name()
        print(f'Name: {self.name} Age: {self.age}')



obj = Child('Vimal', 31)
obj.show_name()
obj.show_name_with_age()
