class BankAccount:
    def __init__(self, int_rate = 0, balance = 0, account_number = "undefined", added = 0):
        self.account_number = account_number
        self.balance = balance
        self.interest = int_rate
        self.added_interest = added
        
    def make_deposit(self, amount): # aumenta el saldo de la cuenta en la cantidad dada
        self.balance += amount
        return self

    def withdraw(self, amount):# disminuye el saldo de la cuenta en la cantidad dada si hay fondos suficientes; si no hay suficiente dinero,  # imprima un mensaje "Fondos insuficientes: cobrar una tarifa de $ 5" y deduzca $ 5
        if self.balance <= 0: 
            print(f"la {self.account_number}, no tiene fondos.")
        else:
            amount = amount-5
            self.balance -= amount
        return self
    
    def display_account_info(self):
        print(f"El saldo de la cuenta numero {self.account_number}, es {self.balance}")
        return self
	
    def yield_interest(self):
        if self.balance <= 0:
            print(f"la {self.account_number}, no tiene fondos.")
        else:
            self.added_interest = self.balance*self.interest
            self.balance += self.added_interest 
            print(f"El saldo de la cuenta numero {self.account_number}, es {self.balance} y el interes ganado es {self.added_interest}")
        return self


cuenta_ahorros1 = BankAccount(0.05,500,"1001001")
cuenta_ahorros2 = BankAccount(0.03,135,"1001002")

cuenta_ahorros1.make_deposit(200).make_deposit(200).make_deposit(200).withdraw(100).yield_interest()
cuenta_ahorros2.make_deposit(10).make_deposit(10).withdraw(2).withdraw(3).withdraw(1).withdraw(5).yield_interest()