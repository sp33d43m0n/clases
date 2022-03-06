class User:
    def __init__(self, username="anonimo", email_address="prueba@python.com", sexo = "undetermined"):
        self.name = username
        self.email = email_address
        self.account_balance = 0
        # self.account = BankAccount(int_rate=0.02, balance=0)
        self.sexo = sexo
        
    def make_deposit(self, amount):
        self.account_balance += amount
        return self
    
    # make_withdrawal (self, amount) : haz que este método disminuya el saldo del usuario en la cantidad especificada  
    def make_withdraw(self, amount):
        self.account_balance -= amount
        return self   
    # display_user_balance (self) : haz que este método imprima el nombre del usuario y el saldo de la cuenta en el terminal
    # p.ej. "Usuario: Guido van Rossum, Saldo: $ 150
    def display_user_balance(self):
        if self.sexo == "M":
            print(f"Sr {self.name}, su saldo es ${self.account_balance}")
        elif self.sexo == "F":
            print(f"Sra {self.name}, su saldo es ${self.account_balance}")
        return self
    
    #BONIFICACIÓN: transfer_money (self, other_user, amount) : haz que este método disminuya el saldo del usuario en la cantidad y agrega esa cantidad al saldo de otro other_user
    def tranfer_money(self, other_user, amount): 
        #verificar si tiene saldo, realizar la transferencia
        if amount > self.account_balance:
            print(f"Sr(a) {self.name}, su saldo es insuficiente")
        else:
            other_user.account_balance += amount
            self.account_balance -=amount
            print(f"sr(a) {self.name}, su saldo es {self.account_balance}")
            print(f"sr(a) {other_user.name}, su saldo es {other_user.account_balance}")
        return self
         
        
carlos = User("carlos perez", "carlos@python.com", sexo="M")
maria = User("Maria Garcia", "maria@python.com", sexo="F")
xavi = User("Xavi Melendez", "javier@python.com", sexo="M")

print(carlos.name)
print(carlos.account_balance)
print(maria.name)
print(carlos.email)
maria.make_deposit(100).make_deposit(100).make_deposit(100).make_withdraw(5).display_user_balance()
carlos.make_deposit(100).make_deposit(50).make_withdraw(50).display_user_balance()


carlos.display_user_balance()
print(carlos.account_balance)
print(maria.account_balance)
carlos.display_user_balance()
maria.display_user_balance()
carlos.tranfer_money(maria,50)


