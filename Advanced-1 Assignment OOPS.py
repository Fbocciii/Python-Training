# 1. Create a checking account class and derive it from Account class
#     -deposit() : Any amount can be deposited
#     -withdraw() : Maximum 6 withdrawals allowed per month. Withdrawal capped at 700
# 2. Create a Savings Account Class and derive it from Account class
#     -deposit() : Any amount can be deposited
#     -withdraw() : Maximum 6 withdrawals allowed. Withdrawal capped at 700
# 3. Modify the account class to accept the properties of Account holder like the firstname, lastname, and address from a different class named AccountHolder
#
# Create at least 3 instances of Account. Each of the instances will have both Checking and Savings account Maintain
# all the transactions done by each AccountHolder for both Checking and Savings Account. Let the transactions include
# the date and time, kind of transaction, amount, status

import datetime


class Transaction:
    def __init__(self, tran_type, value, status, date):
        self.tran_type = tran_type
        self.amount = value
        self.status = status
        self.date = date


class AccountHolder:
    def __init__(self, first_name, last_name, address):
        self._first_name = first_name
        self._last_name = last_name
        self._address = address

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, name):
        self._first_name = name

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, name):
        self._last_name = name

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value

    def __str__(self):
        return self._first_name + " " + self._last_name

    def to_line(self):
        return self._first_name + "," + self._last_name + "," + self._address


class Account:
    def __init__(self, first_name, last_name, address):
        self.balance = 0
        self.transactions = []
        self.holder = AccountHolder(first_name, last_name, address)

    def set_all(self, first_name, last_name, address, balance, transaction_list):
        self.balance = int(balance)
        self.holder.first_name = first_name
        self.holder.last_name = last_name
        self.holder.address = address
        for x in range(0, len(transaction_list), 4):
            tran = Transaction(transaction_list[x], transaction_list[x+1], transaction_list[x+2], datetime.datetime.strptime(transaction_list[x+3].strip(), "%Y-%m-%d %H:%S:%M.%f"))
            self.transactions.append(tran)

    def set_transactions(self, transaction_list):
        for x in range(0, len(transaction_list), 4):
            tran = Transaction(transaction_list[x], transaction_list[x+1], transaction_list[x+2], datetime.datetime.strptime(transaction_list[x+3].strip(), "%Y-%m-%d %H:%S:%M.%f"))
            self.transactions.append(tran)

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(Transaction("Deposit", amount, " ", datetime.datetime.now()))

    def withdrawal(self, amount):
        if amount > 700:
            print("Too large of an amount, please try again")
            return False
        elif self.balance - amount < 0:
            print("Insufficient funds, please try again")
            return False
        else:
            self.balance -= amount
            self.transactions.append(Transaction("Withdrawal", amount, " ", datetime.datetime.now()))
            return True

    def __str__(self):
        return str(self.holder) + " Balance: " + str(self.balance)

    def balance_to_line(self):
        return str(self.balance)

    def transactions_to_line(self):
        line = self.holder.to_line()
        if len(self.transactions) > 0:
            line += ","
        for i in range(0, len(self.transactions)):
            line = line + self.transactions[i].tran_type + "," + str(self.transactions[i].amount) + "," + self.transactions[i].status + "," + str(self.transactions[i].date)
            if i < len(self.transactions) - 1:
                line += ","
        line += "\n"
        return line

class SavingsAccount(Account):
    # def __str__(self):
    #     return str(self.holder) + " Balance: " + str(self.balance)

    def __init__(self, first_name, last_name, address):
        super().__init__(first_name, last_name, address)
        # self.balance = balance
        # self.transactions = transactions
        # self.holder = AccountHolder(first_name, last_name, address)


class CheckingAccount(Account):

    def __init__(self, first_name, last_name, address):
        super().__init__(first_name, last_name, address)
        # self.balance = balance
        # self.transactions = transactions
        # self.holder = AccountHolder(first_name, last_name, address)

    def withdrawal(self, amount):
        if super().withdrawal(amount):
            counter = 0
            for tran in self.transactions[-7:-1]:
                if datetime.datetime.now().month == tran.date.month:
                    counter += 1
                if (datetime.datetime.now() - tran.date).days > 30:
                    break
            if counter >= 6:
                self.transactions.pop(len(self.transactions) - 1)
                self.balance += amount
                print("Exceeded maximum allowed withdrawals in past month, please select another option")
                return False
            else:
                return True
        else:
            return False

    # def __str__(self):
    #     return str(self.holder) + " Balance: " + str(self.balance)


class BankAccount:
    def __init__(self):
        self.savings = SavingsAccount()
        self.checking = CheckingAccount()

    def __init__(self, first_name, last_name, address):
        self.savings = SavingsAccount(first_name, last_name, address)
        self.checking = CheckingAccount(first_name, last_name, address)

    def get_account(self, acc_type):
        if acc_type == "c":
            return self.checking
        elif acc_type == "s":
            return self.savings
        else:
            return None

import os

acc1 = BankAccount("John", "Smith", "123 drive")
acc2 = BankAccount("Jane", "Doe", "456 lane")
acc3 = BankAccount("Spider", "Man", "789 ave")

acc_list = [acc1, acc2, acc3]
with os.scandir(".") as mydir:
    accounts_found = False
    transactions_found = False
    for e in mydir:
        if e.name == "AccountList.csv":
            accounts_found = True
        elif e.name == "TransactionsList.csv":
            transactions_found = True

    if accounts_found:
        account_file = open("AccountList.csv", "r+")
    else:
        account_file = open("AccountList.csv", "w+")

    if transactions_found:
        transactions_file = open("TransactionsList.csv", "r+")
    else:
        transactions_file = open("TransactionsList.csv", "w+")


line_counter = 0
while account_file.readline() != "":
    line_counter += 1
    print(line_counter)

if line_counter == 3:
    account_file.seek(0)
    for acc in acc_list:
        line_list = account_file.readline().split(',')
        acc.checking.holder.first_name = line_list[0]
        acc.checking.holder.last_name = line_list[1]
        acc.checking.holder.address = line_list[2]
        acc.checking.balance = int(line_list[3])
        #acc.checking.set_all(line_list[0], line_list[1], line_list[2], int(line_list[3]), line_list[4:])

        #line_list = account_file.readline().split(',')
        acc.savings.holder.first_name = line_list[0]
        acc.savings.holder.last_name = line_list[1]
        acc.savings.holder.address = line_list[2]
        acc.savings.balance = int(line_list[4])
        #acc.savings.set_all(line_list[0], line_list[1], line_list[2], int(line_list[3]), line_list[4:])

line_counter = 0
while transactions_file.readline() != "":
    line_counter += 1
    print(line_counter)

if line_counter == 6:
    transactions_file.seek(0)
    for acc in acc_list:
        line_list = transactions_file.readline().split(',')
        if len(line_list) > 3:
            acc.checking.set_transactions(line_list[3:])

        line_list = transactions_file.readline().split(',')
        if len(line_list) > 3:
            acc.savings.set_transactions(line_list[3:])

account_selection = 1
try:
    while 1 <= int(account_selection) <= 3:
        print("Enter any value besides 1-3 to exit")
        print("Please select the account you wish to access (1-3):")
        account_selection = int(input())

        print("Would you like to view the checking or savings account? (C/S)")
        account_type = input().lower()
        while not (account_type == 'c' or 's'):
            print("Invalid selection, please select Checking(C) or Savings(S)")
            account_type = input().lower()

        if account_type == 'c':
            print(acc_list[account_selection-1].checking)
        elif account_type == 's':
            print(acc_list[account_selection-1].savings)

        print("Would you like to withdraw or deposit? (W/D) \nPress Enter to exit")
        transaction_choice = input().lower()

        if transaction_choice != "w" and not "d":
            continue

        print("How much would you like to ", "withdraw" if (transaction_choice == "w") else "deposit", "?")
        amount = -1
        while amount < 0:
            try:
                amount = int(input())
            except Exception:
                print("Invalid input, please try another value: ")
                amount = -1

        if transaction_choice == 'w':
            acc_list[account_selection-1].get_account(account_type).withdrawal(amount)
        else:
            acc_list[account_selection-1].get_account(account_type).deposit(amount)

except Exception:
    print("Exiting program...")

account_file.truncate(0)
transactions_file.truncate(0)
for acc in acc_list:
    account_file.writelines(acc.checking.holder.to_line() + "," + acc.checking.balance_to_line() + "," + acc.savings.balance_to_line() + '\n')
    #account_file.writelines(acc.checking.to_line())
    #account_file.writelines(acc.savings.to_line())
    transactions_file.writelines(acc.checking.transactions_to_line())
    transactions_file.writelines(acc.savings.transactions_to_line())

account_file.close()
transactions_file.close()
