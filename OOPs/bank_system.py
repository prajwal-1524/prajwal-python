class customer:
    bank_name='Nabil Bank'

    def __init__(self, name,balance=0.0):
        self.name = name
        self.balance = balance

    def deposite(self,amt):
        self.balance= self.balance + amt
        print('balance after the deposition', self.balance)

    def withdrawl(self,amt):
        if amt > self.balance:
            print('insufficient balance please deposite  first')

        else:
            self.balance = self.balance - amt
            print('the balance after withdrawl is :', self.balance)

print()
print('welcome to nabil bikash bank')

name= input('enter your name')
c=customer(name)
while True:
    print('d-deposite \n w-withdrawl \n e-exit')
    option = input('enter your option:')
    if option == 'd' or option=='D':

        amt =  float(input('please enter the amount you want to deposite '))
        c.deposite(amt)

    elif option=='w' or option=='W':
        amt = float(input('enter the amount you want to withdraw'))
        c.withdrawl(amt)

    else:
        print(' invalid option, please select the valid option')        
    
    