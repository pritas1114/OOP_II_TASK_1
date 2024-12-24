#Titas Sarker
#a_Let_Me_Handle_It

"""
Create a custom Exception and handle it in the following way:
"""

class InvalidVoterException(Exception):
    pass

# a) Take an input named age
try:
    age = int(input("Enter age: "))

    # b) if age < 18, it will raise InvalidVoterException
    if age < 18:
        raise InvalidVoterException("Age is less than 18. Not eligible to vote.")
    else:
        print("Eligible to vote.")
except InvalidVoterException as e:
    print(e)
except ValueError:
    print("Invalid input. Please enter a valid integer.")
    
    
    
#b_Salary_Exception    
    
"""
Create a custom exception named SalaryNotInRange if salary is less than 10,000 and greater than 50,000

"""

class SalaryNotInRange(Exception):
    def __init__(self, salary):
        super().__init__(f"Salary {salary} is not in the range of 10,000 to 50,000")


class Rectangle:
    def __init__(self, name, salary):
        self.name = name
        if not (10000 <= salary <= 50000):
            raise SalaryNotInRange(salary)
        self.salary = salary

    def displaySalary(self):
        print(f"Name: {self.name}, Salary: {self.salary}")


try:
    emp = Rectangle("John", 60000)  # Will raise exception
    emp.displaySalary()
except SalaryNotInRange as e:
    print(e)
    
#c_More_Exceptions

"""
Given an array, a = [10, 5, 15, 20]
divisor => take input of int type
"""

a = [10, 5, 15, 20]

try:
    divisor = int(input("Enter divisor: "))

    # a) Perform division
    result = [x / divisor for x in a]
    print("Division results:", result)

    # b) Handle exceptions
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except ValueError:
    print("Error: Invalid value entered.")
except NameError:
    print("Error: Variable name not found.")
except TypeError:
    print("Error: Type mismatch.")
except IndexError:
    print("Error: Index out of range.")
except AttributeError:
    print("Error: Invalid attribute access.")
except FileNotFoundError:
    print("Error: File not found.")

# c) Use try, except, else, finally
finally:
    print("Execution completed.")    



#d_Bank_Account_Exception

"""
Create a custom exception "insufficientFund" if balance is not greater than withdraw amount

"""

class InsufficientFund(Exception):
    def __init__(self, balance, withdraw_amount):
        super().__init__(f"Insufficient funds: Balance {balance}, Withdraw Amount {withdraw_amount}")


class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFund(self.balance, amount)
        self.balance -= amount
        print(f"Withdrawal successful. Current balance: {self.balance}")


account = BankAccount(5000)

try:
    account.withdraw(6000)
except InsufficientFund as e:
    print(e)

try:
    account.withdraw(3000)
except InsufficientFund as e:
    print(e)
    