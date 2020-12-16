from datetime import datetime
import random
import database

INPUT_PROMPT = """\n1. Create an account
2. Log into account
0. Exit 
"""

LOGIN_PROMPT = """\n1. Balance
2. Add income
3. Do transfer
4. Close account
5. Log out
0. Exit
"""


class Bank:

    def __init__(self):
        self.card_number = ''
        self.pin = 0
        self.balance = 0

    def generate_card_number(self):
        """
        Generates unique card number using micro-second time stamp.
        Returns the card number
        """
        dateTimeObj = datetime.now()
        random_number = dateTimeObj.strftime("%j%f")
        temp_card_number = '400000' + random_number
        self.card_number = str(temp_card_number) + self.get_checksum(temp_card_number)
        print("\nYour card has been created.")
        print("Your card number:" + '\n' + self.card_number)
        return self.card_number

    def get_checksum(self, card_number):
        """
        Computes checksum using Luhn's algorithm for credit card
        Returns checksum(last digit) 
        """
        temp_array = []
        # Luhn's algorithm
        for i in range(len(card_number)):
            digit = int(card_number[i])
            if i % 2 == 0:
                digit *= 2
            if digit > 9:
                digit -= 9
            temp_array.append(digit)
        mod = sum(temp_array) % 10
        checksum = str(0 if mod == 0 else 10 - mod)
        return checksum

    def generate_pin(self):
        """
        Generates random 4 digit pin
        """
        self.pin = random.randint(999, 9999)
        print("Your card PIN:" + '\n' + str(self.pin))
        return self.pin

    def login_choices(self, connection, login_card_number):
        """
        Provides menu after successful login 
        """
        while True:
            login_choice = input(LOGIN_PROMPT)
            if login_choice == "1":
                print("\nBalance: {}".format(database.get_balance(connection, login_card_number)))
            elif login_choice == "2":
                self.add_income(connection, login_card_number)
            elif login_choice == "3":
                self.do_transfer(connection, login_card_number)
            elif login_choice == "4":
                database.delete_account(connection, login_card_number)
                break
            elif login_choice == "5":
                print("\nYou have successfully logged out!")
                break
            else:
                print("\nBye!")
                quit()

    def add_income(self, connection, login_card_number):
        """
        Accepts Income value and forwads to upadte in database
        """
        income = int(input("\nEnter income: "))
        database.update_income_in_db(connection, income, login_card_number)

    def do_transfer(self, connection, login_card_number):
        """
        This method is for performing transfer.
        It validates reciever's card number and sender's balance
        """
        transfer_card_number = input("\nTransfer\nEnter card number:\n")
        if self.validate_card_number(connection, transfer_card_number, login_card_number):
            transfer_amount = int(input("\nEnter how much money you want to transfer:\n"))
            if transfer_amount > database.get_balance(connection, login_card_number):
                print("\nNot enough money!")
            else:
                database.transfer_balance(connection, transfer_card_number, login_card_number, transfer_amount)
                print("\nSuccess!")

    def validate_card_number(self, connection, card_number, source_card_number):
        """
        Validates card to check if the reciever's card is same as the senders card number, if the card adheres to correct checksum or 
        whether the card exsists
        Returns Binary 
        """
        flag = False
        if card_number == source_card_number:
            print("\nYou can't transfer money to the same account!")
        elif self.get_checksum(card_number[:-1]) != card_number[-1]:
            print("\nProbably you made a mistake in the card number. Please try again!")
        elif not database.validate_card(connection, card_number):
            print("\nSuch a card does not exist.")
        else:
            flag = True
        return flag


bank = Bank()
connection = database.db_connection()
database.create_table(connection)

while True:
    choice = input(INPUT_PROMPT)
    if choice == "1":
        card_number = bank.generate_card_number()
        pin = bank.generate_pin()
        database.insert_record(connection, card_number, pin)
    elif choice == "2":
        login_card_number = input("\nEnter your card number:\n")
        login_pin = input("Enter your PIN:\n")
        if database.validate_login(connection, login_card_number, login_pin):
            print("\nYou have successfully logged in!")
            bank.login_choices(connection, login_card_number)
        else:
            print("\nWrong card number or PIN!")
        continue
    else:
        print("\nBye!")
        quit()
