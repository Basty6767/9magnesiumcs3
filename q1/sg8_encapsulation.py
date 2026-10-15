class Bankaccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number
        self.__balance = balance
        
    def set_account_number(self, account_number):
        self.__account_number = account_number
        
    def set_balance(self, balance):
        if balance < 0:
            print("The balance cannot be negative.")
        else:
            self.__balance = balance
    
    @property
    def get_account_number(self):
        return self.__account_number
    
    @property
    def get_balance(self):
        return self.__balance
    
    
acc1 = Bankaccount("123456789", 1000)

print("Account 1")
print(f"Account Number: {acc1.get_account_number}")
print(f"Balance: {acc1.get_balance}")

print("Set balance to -6767")
acc1.set_balance(-6767)
print(f"Account Number: {acc1.get_account_number}")
print(f"Balance: {acc1.get_balance}")