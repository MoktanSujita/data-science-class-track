# class Color:
#     def __init__(self, name, hex_code):
#         self.name = name
#         self.hex_code = hex_code
#     def display_info(self):
#         print(f"Color Name: {self.name} and hex code is {self.hex_code}")

# color = Color("Red", "#FF0000")
# color.display_info()

class BankAccount:
    def __init__(self, account_holder, account_number, address, balance, pin_code):
        self.account_holder = account_holder
        self.account_number = account_number
        self.address = address
        self.__balance = balance
        self.pin_code = pin_code
    def display_info(self):
        return f"{self.account_holder}'s account number is {self.account_number}"
    
    def deposite_amount(self, amount):
        self.__balance += amount

    def withdraw_amount(self, amount):
        if self.__balance < amount:
            print("Insufficient balance!!!")

        else:
         self.__balance -= amount
         print("Amount withdrawn!!New balance" ,self.__balance)

    def show_balance(self, pin):
        if pin  == self.pin_code:
           print ("Your balance is" ,self.__balance) 

        else:
            print("Incorrect pincode! Cannot show balance")

nimb_bank = BankAccount("Sirjana",200453,"Bhaktapur",2000,1543)
print(nimb_bank)
nimb_bank.deposite_amount(500)
nimb_bank.withdraw_amount(500)

pin = int(input("Enter your pin_code to show balance: "))
nimb_bank.show_balance(pin)

# nimb_bank.display_info()