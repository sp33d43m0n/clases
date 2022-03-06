class BankAccount:
    def __init__(self, account_number, balance, int_rate, added_interest):
        self.account_number = account_number
        self.balance = balance
        self.interest = int_rate
        self.added_interest = added_interest
        
class User:
    def __init__(self, username="anonimo", 
                email_address="prueba@python.com",
                sexo = "undetermined",
                account_number = "undefined",
                balance = 0,
                int_rate = 0,
                added_interest = 0):
        self.name = username
        self.email = email_address
        self.account = BankAccount(account_number, balance, int_rate, added_interest)
        self.sexo = sexo
        
    def make_deposit(self, amount): # aumenta el saldo de la cuenta en la cantidad dada
        self.account.balance += amount
        print(f"Su saldo es {self.account.balance}")
        return self

    def withdraw(self, amount):# disminuye el saldo de la cuenta en la cantidad dada si hay fondos suficientes; si no hay suficiente dinero,  # imprima un mensaje "Fondos insuficientes: cobrar una tarifa de $ 5" y deduzca $ 5
        if self.account.balance <= 0: 
            print(f"la {self.account.account_number}, no tiene fondos.")
        else:
            amount = amount-5
            self.account.balance -= amount
        return self
    
    def display_account_info(self):
        print(f"El saldo de la cuenta numero {self.account.account_number}, es {self.account.balance}")
        return self
	
    def yield_interest(self):
        if self.account.balance <= 0:
            print(f"la {self.account.account_number}, no tiene fondos.")
        else:
            self.account.added_interest = self.account.balance*self.account.interest
            self.account.balance += self.account.added_interest 
            print(f"El saldo de la cuenta numero {self.account.account_number}, es {self.account.balance} y el interes ganado es {self.account.added_interest}")
        return self
    
    def tranfer_money(self, other_user, amount): 
        if amount > self.account.balance:
            print(f"Sr(a) {self.name}, su saldo es insuficiente")
        else:
            other_user.account.balance += amount
            self.account.balance -=amount
            print(f"sr(a) {self.name}, su saldo es {self.account.balance}")
            print(f"sr(a) {other_user.name}, su saldo es {other_user.account.balance}")
        return self


cuenta_ahorros1 = User(username="Javier",email_address="javi@bank.com", sexo = "M", account_number =1001001, balance = 100, int_rate= 0.02)
cuenta_ahorros2 = User("Johana", "jOHA@bank.com", sexo = "F", account_number =1001002, balance = 10, int_rate=0.01)

cuenta_ahorros1.make_deposit(200).make_deposit(200).make_deposit(200).withdraw(100).yield_interest()
cuenta_ahorros2.make_deposit(10).make_deposit(10).withdraw(2).withdraw(3).withdraw(1).withdraw(5).yield_interest()
cuenta_ahorros1.tranfer_money(cuenta_ahorros2,100).display_account_info()
cuenta_ahorros2.display_account_info()