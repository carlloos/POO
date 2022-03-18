from timezone import Timezone


class Bank:

    interest_rate = 0
    operation_number = 0

    def __init__(self, acc_number, first_name, last_name, time_zone, balance = 0):
        self.acc_number = acc_number
        self._first_name = first_name
        self._last_name = last_name
        self.time_zone = time_zone
        self._balance = balance

    @classmethod
    def update_interest(cls, value):
        cls.interest_rate = value

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        if value < 0:
            print("Operation denied: Balances need to be zero or higher!\n")
            print(f'X_{self.acc_number}_{self.return_tz()}_{Bank.operation_number}')
            Bank.operation_number += 1
        else:
            self._balance = value

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def fist_name(self, value):
        self._first_name = value

    @property
    def last_name(self):
        return self._last_name
    
    @last_name.setter
    def last_name(self, value):
        self._last_name = value


    @property
    def full_name(self):
        return self._first_name+' '+self._last_name


    def deposit(self, value):
        self.balance += value
        print(f'D_{self.acc_number}_{self.return_tz()}_{Bank.operation_number}')
        Bank.operation_number += 1

    def withdraw(self, value):
        if (self.balance - value) < 0:
            print(f"Operation denied: withdraw of {value} result in negative funds!")
            print(f'X_{self.acc_number}_{self.return_tz()}_{Bank.operation_number}')
            Bank.operation_number += 1
        else:
            print(f'W_{self.acc_number}_{self.return_tz()}_{Bank.operation_number}')
            Bank.operation_number += 1


    def deposit_interest(self):
        interest = self.balance *  Bank.interest_rate
        self.balance += interest
        print(f'I_{self.acc_number}_{self.return_tz()}_{Bank.operation_number}')
        Bank.operation_number += 1

    def return_tz(self):
        return Timezone.return_utc_now()

    def check_code(self, code):
        list = code.split('_')
        print(f"Account Number: {list[1]}\nTransaction Code: {list[0]}\nDate Time (UTC format): {list[2]}\nDate Time: {Timezone.datetime_preferred(list[2], self.time_zone)} \nTransaction ID: {list[3]}\n")
