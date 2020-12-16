# Simple Banking System
This project was developed as part of JetBrains Academy's python Developer program.

## Description
Everything goes digital these days, and so does money. Today, most people have credit cards, which save us time, energy and nerves. 
From not having to carry a wallet full of cash to consumer protection, cards make our lives easier in many ways. 
In this project, a simple banking system with database is developed.

## Learning outcomes:
* Implement banking operations in python.
* Integrate SQL for persistent data storage.
* Implement Luhn's algorithm for credit card validation.

# Options overview
Login menu options:
1. Create an account
2. Log into account
0. Exit

After successful log in, the options would be:
1. Balance
2. Add income
3. Do transfer
4. Close account
5. Log out
0. Exit

Balance retrieves the balance from data base associated with logged in card number

Add income is used to deposit money to the account.

Do transfer item will allow transferring money to another account and handles the following errors:

If the user tries to transfer more money than he/she has, output: "Not enough money!"
If the user tries to transfer money to the same account, output the following message: “You can't transfer money to the same account!”
If the receiver's card number doesn’t pass the Luhn algorithm, you should output: “Probably you made a mistake in the card number. Please try again!”
If the receiver's card number doesn’t exist, you should output: “Such a card does not exist.”
If there is no error, ask the user how much money they want to transfer and make the transaction.
If the user chooses the Close account item, you should delete that account from the database.


## Sample scenarios

The symbol > represents the user input.

Example 1:

1. Create an account
2. Log into account
0. Exit
>1

Your card has been created
Your card number:
4000009455296122
Your card PIN:
1961

1. Create an account
2. Log into account
0. Exit
>1

Your card has been created
Your card number:
4000003305160034
Your card PIN:
5639

1. Create an account
2. Log into account
0. Exit
>2

Enter your card number:
>4000009455296122
Enter your PIN:
>1961

You have successfully logged in!

1. Balance
2. Add income
3. Do transfer
4. Close account
5. Log out
0. Exit
>2

Enter income:
>10000
Income was added!

1. Balance
2. Add income
3. Do transfer
4. Close account
5. Log out
0. Exit
>1

Balance: 10000

1. Balance
2. Add income
3. Do transfer
4. Close account
5. Log out
0. Exit
>3

Transfer
Enter card number:
>4000003305160035
Probably you made a mistake in the card number. Please try again!

1. Balance
2. Add income
3. Do transfer
4. Close account
5. Log out
0. Exit
>3

Transfer
Enter card number:
>4000003305061034
Such a card does not exist.

1. Balance
2. Add income
3. Do transfer
4. Close account
5. Log out
0. Exit
>3

Transfer
Enter card number:
>4000003305160034
Enter how much money you want to transfer:
>15000
Not enough money!

1. Balance
2. Add income
3. Do transfer
4. Close account
5. Log out
0. Exit
>3

Transfer
Enter card number:
>4000003305160034
Enter how much money you want to transfer:
>5000
Success!

1. Balance
2. Add income
3. Do transfer
4. Close account
5. Log out
0. Exit
>1

Balance: 5000

1. Balance
2. Add income
3. Do transfer
4. Close account
5. Log out
0. Exit

>0
Bye!
Example 2:

1. Create an account
2. Log into account
0. Exit
>1

Your card has been created
Your card number:
4000007916053702
Your card PIN:
6263

1. Create an account
2. Log into account
0. Exit
>2

Enter your card number:
>4000007916053702
Enter your PIN:
>6263

You have successfully logged in!

1. Balance
2. Add income
3. Do transfer
4. Close account
5. Log out
0. Exit
>4

The account has been closed!

1. Create an account
2. Log into account
0. Exit
>2

Enter your card number:
>4000007916053702
Enter your PIN:
>6263

Wrong card number or PIN!

1. Create an account
2. Log into account
0. Exit
>0

Bye!
