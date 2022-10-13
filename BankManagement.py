from pandas import *
import pandas as pd
import random
import csv
class Customer_INFO:
    def __init__(self,name,id,password,telnumber,mail):
        self.Name=name
        self.Id=id
        self.Password=password
        self.Telnumber=telnumber
        self.email=mail
class account_INFO:
    def __init__(self,name,password,account_no,type,deposit):
        self.Name=name
        self.Password=password
        self.Account_no=account_no
        self.Type=type
        self.Deposit=deposit

#-------------------------------------------------------------------------------------------------------------
#in this class we just only register or login
class Application:
    @staticmethod
    def register():
        info = []
        while True:
            try:
                Name=input('name:')
                ID = int(input('enter id(number only):'))
                Password=int(input('password(only number):'))
                tell_no=int(input('tellephone number(number only):'))
                email=input('mail:')
                re = Customer_INFO(Name,ID, Password, tell_no, email)
                info.append(re.Name)
                info.append(re.Id)
                info.append(re.Password)
                info.append(re.Telnumber)
                info.append(re.email)
                print('you are registered succesfuly')
                break
            except Exception as e:
                print('please enter in correct format',type(e))
                continue
        return info


#---------------------------------------------------------------------------------------------------------------
#this class is customer pannel
class Customer_pannel:
    @staticmethod
    def show():
        print('NOTE:to transfer money you should first select account info')
        print( '1.create new account\n2.account information\n3.manage account\n4.select stared account\n5.transfer money\n6.pay bills\n7.request loan\n8.close account')
        return Customer_pannel.select_option()
    @staticmethod
    def back_to_menu():
        key = int(input('do you want to continue?to show menu press 1(log out and to register again=2):'))
        if key == 1:
            return Customer_pannel.show()
        elif key==2:
            DataBase.insert_customer_register(data)
        else:
            print('you are logout,thanks')
            exit()

    @staticmethod
    def select_option():
        button=int(input('please enter your choice:'))
        if button==1:
            return Customer_pannel.create_new_account()
        elif button==2:
            return Customer_pannel.show_account_info()
        elif button==3:
            return Customer_pannel.manage_account()
        elif button==4:
            return Customer_pannel.select_stared_account()
        elif button==5:
            return Customer_pannel.transfer_money()
        elif button==6:
            return Customer_pannel.pay_bills()
        elif button==7:
            return Customer_pannel.request_loan()
        elif button==8:
            return Customer_pannel.close_account()

    @staticmethod
    def create_new_account():
        return DataBase.insert_account_info(data)

    @staticmethod
    def show_account_info():
        return DataBase.show_account_info(data)

    @staticmethod
    def manage_account():
        return DataBase.insert_account_info(data)

    @staticmethod
    def select_stared_account():
        acc_pass = int(input('bank_account_password for your account:'))
        return DataBase.stared_account_no(data,acc_pass)

    @staticmethod
    def transfer_money():
        amount=int(input('enter money to transfer:'))
        account_no1 = int(input('enter bank_account number to withdrawal from it:'))
        DataBase.withrawal(data,amount,account_no1)
        account_no2 = int(input('enter bank_account number to deposit to it:'))
        return DataBase.deposit(data,amount,account_no2)

    @staticmethod
    def pay_bills():
        bill_id=int(input('enter bill id:'))
        pay_id=int(input('enter payment id:'))
        return DataBase.pay_bills(data,bill_id,pay_id)

    @staticmethod
    def request_loan():
        amount = int(input('How much do you borrow?:'))
        account_no1 = int(input('enter bank_account number to deposit:'))
        DataBase.deposit(data,amount, account_no1)
        print('The loan was deposited into your account')

    @staticmethod
    def close_account():
        acc_pass=int(input('enter bank_account pass:'))
        return DataBase.close_account(data,acc_pass)




#-----------------------------------SATABASE CLASS----------------------------------------------------------------------------
class DataBase:
    def __init__(self,address):
        self.address=address

    #create a csv file as database
    def create_customer_file(self):
        column=Customer_INFO('name','id','password','telnumber','mail')
        account=account_INFO('fullname','account_pass','account_no','type','deposit')
        col=[]
        col.append(column.Name)
        col.append(column.Id)
        col.append(column.Password)
        col.append(column.Telnumber)
        col.append(column.email)
        col.append(account.Name)
        col.append(account.Password)
        col.append(account.Account_no)
        col.append(account.Type)
        col.append(account.Deposit)
        with open(self.address, 'w') as file:
            writer = csv.writer(file)
            writer.writerow(col)
#---------------------INSERT______________________________________________________________________________________________
    #INSERT......add customer information to csv file
    def insert_customer_register(self):
        print('welcome,you should register first!!!!')
        customer=Application()
        with open(self.address,'a') as f:
            writer=csv.writer(f)
            writer.writerow(customer.register())
        print('you should login to access to your pannel')
        yes = int(input('do you want to register or login now(register=1/login=2):'))
        if yes == 1:
            self.insert_customer_register()
            id = int(input('id(only number):'))
            password = int(input('customer_password(only number):'))
            self.check_custumer_login(id, password)
        elif yes == 2:
            id = int(input('id(only number):'))
            password = int(input('customer_password(only number):'))
            self.check_custumer_login(id, password)
        else:
            print('goodbye')

#-----------------------------------SELECT---------------------------------------------------------------------------------
    #SELECT......for part login_your account,check is there our id and pass exist in csv file
    def check_custumer_login(self,id,password):
        df = read_csv(self.address)
        user_id = df[df['id'] == id]
        user_pass = df[df['password'] == password]
        u = user_id.to_dict()
        v = list(u.values())[1]
        idd = list(v.values())
        p = user_pass.to_dict()
        Pa = list(p.values())[2]
        pas = list(Pa.values())
        if id in idd and password in pas :
            print('you are login,welcome....!!')
            return Customer_pannel.show()
        else:
            yes = int(input('you are not register,do you want to register now(yes=1/login=2):'))
            if yes == 1:
                self.insert_customer_register()
                id = int(input('id(only number):'))
                password = input('password:')
                self.check_custumer_login(id, password)
            elif yes==2:
                id = int(input('id(only number):'))
                password = int(input('password:'))
                self.check_custumer_login(id, password)
            else:
                print('goodbye')

    #show the account information
    def show_account_info(self):
        my_filtered_csv = pd.read_csv(self.address, usecols=['fullname','account_pass','account_no','type','deposit'])
        print('the bank_account info are:\n',my_filtered_csv)
        return Customer_pannel.back_to_menu()

    #in this part ,choose stared account according to customer password
    def stared_account_no(self,acc_pass):
        stared=[]
        df=read_csv(self.address)
        ac_pas=df[df['account_pass']==acc_pass]
        u = ac_pas.to_dict()
        s = list(u.values())[6]
        pas_ac = list(s.values())
        v = list(u.values())[7]
        number_ac = list(v.values())
        if acc_pass in pas_ac:
            stared.append(number_ac)
            print(f'this bank_account_no {stared} are add to stared bank_account_no')
        else:
            print('there is not this account.')
        return Customer_pannel.back_to_menu()



#------------------------------UPDATE------------------------------------------------------------------------------------------
    #CREATE an account
    #UPDATE.......save account information to csv file for each customer,actually we update our csv file
    def insert_account_info(self):
        df = read_csv(self.address)
        n = int(input('how many bank account to open?(enter 2):'))
        for i in range(1, n+1):
            acc_no = random.randint(100, 1000)
            open = account_INFO(input('full_name:'), input('bank_account_password:'), acc_no, input('type:'),
                                int(input('cash:')))
            # updating the column value/data
            if n==2:
                df.loc[i+3, 'fullname'] = open.Name
                df.loc[i+3, 'account_pass'] = open.Password
                df.loc[i+3, 'account_no'] = open.Account_no
                df.loc[i+3, 'type'] = open.Type
                df.loc[i+3, 'deposit'] = open.Deposit
            else:
                df.loc[i, 'fullname'] = open.Name
                df.loc[i, 'account_pass'] = open.Password
                df.loc[i, 'account_no'] = open.Account_no
                df.loc[i, 'type'] = open.Type
                df.loc[i, 'deposit'] = open.Deposit
                # writing into the file
            df.to_csv(self.address, index=False)
        print('your bank_accounts created succesfully...')
        return Customer_pannel.back_to_menu()

    #TRANSFER MONEY
    #in this part we want to transfer money
    def deposit(self, amount,acc_no):
        balance=[]
        df = read_csv(self.address)
        ac_no = df[df['account_no'] == acc_no]
        u = ac_no.to_dict()
        s = list(u.values())[7]
        ac_no = list(s.values())
        v = list(u.values())[9]
        deposit = list(v.values())
        print(deposit)
        if acc_no in ac_no:
            balance.append(amount)
            balance=balance+deposit
            balanc=sum(balance)
            print(f'the {amount} add to your cash :{balanc}')
        else:
            print('there is no such bank_account number,back to menu and try agian.....')
        return Customer_pannel.back_to_menu()

    def withrawal(self, amount,acc_no):
        balance = []
        subtracted=[]
        balance.append(amount)
        df = read_csv(self.address)
        ac_no = df[df['account_no'] == acc_no]
        u = ac_no.to_dict()
        s = list(u.values())[7]
        ac_no = list(s.values())
        v = list(u.values())[9]
        deposit = list(v.values())
        print(deposit)
        if acc_no in ac_no and amount<=deposit[0]:
            for i1,i2 in zip(balance,deposit):
                subtracted.append(i2-i1)
            print(f'the {amount} withdrawal to your cash :{subtracted}')
            return amount
        else:
            print('there is no such bank_account number...try again....')
        return Customer_pannel.back_to_menu()
    #pay bills
    def pay_bills(self,bill_id,pay_id):
        amount = int(input('enter money to transfer:'))
        account_no1 = int(input('enter bank_account number to withdrawal from it:'))
        self.withrawal(amount,account_no1)
        print('your payment successfully.......')
        return Customer_pannel.back_to_menu()
#----------------------DELETE-------------------------------------------------------------------------
    #delete accounts
    def close_account(self,acc_pass):
        df = read_csv(self.address)
        ac_pas = df[df['account_pass'] == acc_pass]
        u = ac_pas.to_dict()
        s = list(u.values())[6]
        pas_ac = list(s.values())
        v = list(u.values())[9]
        deposit = list(v.values())
        print(deposit[0])
        if acc_pass in pas_ac and deposit[0]==0:
            pas_ac.clear()
            print('your account has been cleared........')
        else:
            print('you should withdrawal your money')
            amount = int(input('enter money to transfer:'))
            account_no1 = int(input('enter bank_account number to withdrawal from it:'))
            self.withrawal(amount, account_no1)
            account_no2 = int(input('enter bank_account number to deposit to it:'))
            self.deposit(amount,account_no2)
            print(f'your bank account with {acc_pass} is closed.....')
        return Customer_pannel.back_to_menu()


#-------------------------CONTROLLER------------------------------------------------------------------
file=input('enter file name(enter csv file):')
data=DataBase(file)
data.create_customer_file()
data.insert_customer_register()


#------------------------------------------------------------------------------------------------------------







