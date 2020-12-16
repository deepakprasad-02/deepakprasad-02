import sqlite3

# SQL Queries for managing the credit card, pin and balance data 

CREATE_TABLE_QUERY = 'CREATE TABLE IF NOT EXISTS card(id INTEGER PRIMARY KEY, number TEXT, pin TEXT, balance INTEGER DEFAULT 0)'
INSERT_RECORD = 'INSERT INTO card (number, pin) VALUES (?, ?)'
FETCH_CARD_NUMBER_PIN = 'SELECT number FROM card where number = ? and pin =?'
FETCH_BALANCE_QUERY = 'SELECT balance FROM card where number = ?'
UPDATE_BALANCE = 'UPDATE card set balance = balance + ? where number = ?'
FETCH_CARD_NUMBER = 'SELECT number FROM card where number = ?'
DEDUCT_BALANCE = 'UPDATE card set balance = balance - ? where number =?'
DELETE_ACCOUNT = 'DELETE FROM card WHERE number = ?'




def db_connection():
    return sqlite3.connect('card.s3db') # Returns the database connection


def create_table(connection):
    with connection:
        connection.execute(CREATE_TABLE_QUERY)  # Creates the card table


def insert_record(connection, card_number, pin):
    with connection:
        connection.execute(INSERT_RECORD, (card_number, pin))  # Insert a single record into card database


def validate_login(connection, card_number, pin):
    with connection:
        record = connection.execute(FETCH_CARD_NUMBER_PIN, (card_number, pin)).fetchone()  # Retrieves card number and pin from the card table
        if record:
            return True
        return False


def get_balance(connection, card_number):
    with connection:
        return connection.execute(FETCH_BALANCE_QUERY, (card_number,)).fetchone()[0]  # retrieves balance for the respective card number


def update_income_in_db(connection, income, login_card_number):
    with connection:
        connection.execute(UPDATE_BALANCE, (income, login_card_number))  # updates the balance for the respective card number


def validate_card(connection, card_number):
    with connection:
        record = connection.execute(FETCH_CARD_NUMBER, (card_number,)).fetchone()  # Retrieves only the card number from card table
        if record:
            return True
        return False


def transfer_balance(connection, card_number, source_card_number, amount):
    with connection:
        connection.execute(DEDUCT_BALANCE, (amount, source_card_number))  # updates the balance in senders account by deducting the respective amount 
        connection.execute(UPDATE_BALANCE, (amount, card_number))  # updates the balance in reciever's account by adding the respective amount 


def delete_account(connection, card_number):
    with connection:
        connection.execute(DELETE_ACCOUNT, (card_number, ))  # Deletes the card number, pin and the balance for the card number provided
