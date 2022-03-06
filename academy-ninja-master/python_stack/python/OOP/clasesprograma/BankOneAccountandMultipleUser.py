class BankAccount:
    def __init__(self, 
                int_rate = 0, 
                balance = [],  
                added = 0,
                cuentas = []):
        self.interest = int_rate
        self.balance = balance
        self.added_interest = added
        self.cuentas = []
        
    def add_cuenta(self,new_account):
        self.cuentas.append(new_account) 
        return self
    
    def display_accounts_info(self):
        print(f"Sr(a) {self.name}, ud tiene {len(self.cuentas)}, cuentas") 
        for i in range (0, len(self.cuentas)): 
            print(f"Su cuenta No [{i}] es {self.cuentas[i]} y su saldo es {self.account_balance.balance[i]}")
        return self
    
    def make_deposit(self, amount): # aumenta el saldo de la cuenta en la cantidad dada
        index = ''
        self.display_accounts_info()
        index = input("por favor digite el indice de su cuenta donde desea agregar dinero ")
        index = int(index)
        self.account_balance.balance[index] += amount 
        print(f"Su saldo en la cuenta {self.cuentas[index]} es {self.account_balance.balance[index]}")
        return self
    
    # def withdraw(self, amount):# disminuye el saldo de la cuenta en la cantidad dada si hay fondos suficientes; si no hay suficiente dinero,  # imprima un mensaje "Fondos insuficientes: cobrar una tarifa de $ 5" y deduzca $ 5
    #     if self.balance <= 0: 
    #         print(f"la {self.account.account_number}, no tiene fondos.")
    #     else:
    #         amount = amount-5
    #         self.balance -= amount
    #     return self
        
class User:
    def __init__(self, username="anonimo", email_address="prueba@python.com", sexo = "undetermined"):
        self.name = username
        self.email = email_address
        self.sexo = sexo
        
        

            

    

	
    # def yield_interest(self):
    #     if self.account.balance <= 0:
    #         print(f"la {self.account.account_number}, no tiene fondos.")
    #     else:
    #         self.account.added_interest = self.account.balance*self.account.interest
    #         self.account.balance += self.account.added_interest 
    #         print(f"El saldo de la cuenta numero {self.account.account_number}, es {self.account.balance} y el interes ganado es {self.account.added_interest}")
    #     return self


xavi = User(username="Javier",email_address="javi@bank.com", sexo = "M")
xavi.add_cuenta(1001001).add_cuenta(1001002).display_accounts_info().make_deposit(200).display_accounts_info().make_deposit(350).make_deposit(100).make_deposit(50).display_accounts_info()
Joha = User("Johana", "jOHA@bank.com", "F")
Joha.add_cuenta(1001003).add_cuenta(1001004).display_accounts_info().make_deposit(200).display_accounts_info().make_deposit(350).make_deposit(100).make_deposit(50).display_accounts_info()
