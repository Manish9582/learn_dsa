import random as r
import csv
class Bank:
    balence=0;
    accountNumber=None;
    def __init__(self ,name ,phone,age ,nominee ,accountNumber ,password ):
        self.name=name;
        self.phone=phone;
        self.age=age;
        self.nominee=nominee;
        self.__accountNumber=accountNumber;
        self.__balance=0;
        self.password=password
        
    def GetAccountNumber(self):
        return self.__accountNumber;
    
    def getBalance(self):
        return self.__balance;
    def addBalance(self ,amount):
        self.__balance+=amount
        return "Add Amount successfully"
    def Credit(self,amount):
        self.__balance-=amount
        return "credit Amount successfully"

class BankFunctionLity:
    def __init__(self ,name ,phone,age ,nominee,password ):
        self.name=name;
        self.phone=phone;
        self.age=age;
        self.nominee=nominee;
        self.password=password
    
    def CreatAccount(self):
        AcountNumber=r.randrange(100000000,999999999);
        self.account=Bank(self.name ,self.phone ,self.age ,self.nominee,AcountNumber ,self.password);
        with open('bank.csv',"a" ,newline= "") as file:
            write=csv.writer(file);
            write.writerow([
                self.account.name ,
                self.account.phone ,
                self.account.age ,
                self.account.nominee,
                AcountNumber,
                self.account.password
            ])
            
        print('create account successfuly');
        print('Its your acount number',AcountNumber)
    def LoginAccount(self,acountNumber ,password):
        with open('bank.csv','r') as file:
            getFile=csv.reader(file);
            next(getFile)
            for row in getFile:
                if(int(row[4])==int(acountNumber)):
                    if(str(row[5])==str(password)):
                        print('Account is login successfuly');
                        return "Done";
                    else:
                        print('Enter the correct password')
                        return "Fail";
                print('Please Enter the correct Acount Number');
                return "Fail";
      
    def DebitAmount(self ,value):
       result=self.account.addBalance(value);
       print(result);
       totalBalance=self.account.getBalance();
       print('Total Balance',totalBalance);
     
    def CreditAmount(self ,value):
       result=self.account.Credit(value);
       print(result);
       totalBalance=self.account.getBalance();
       print('Total Balance',totalBalance); 
    
    def DeleteAccount(self ,accountNumber,password):
        found=False;
        with open('bank.csv','r') as file:
            read=csv.reader(file)
            rows=[];
            for row in read:
                if(int(row[4])==int(accountNumber)):
                    found=True;
                    if(str(row[5])==str(password)):
                        print('Account is Delete successfuly');
                        continue;
                    else:
                        print('Enter the correct password')
                        return "Fail";
                rows.append(row)
        if not found:
            print('Please enter the correct account number');
            return "Fail";
            
        with open('bank.csv','w',newline="") as file:
            write=csv.writer(file);
            write.writerows(rows)
            
        return "Done";
                
                     
        
 
print('*****  Welcome to apna bank  *****');
print('Choose the option') 
print('Your want to create acount if as so press 1');
print('Your want to check balance if as so press 2');
print('Your want to debit amount if as so press 3');
print('Your want to credit amount if as so press 4');
print('Your want to delete account if as so press 5'); 


choose=input('Chooose your option : ')
if(type(int(choose))!=int):
    print('Enter only number')
  
  
 
if choose==1:
    print('Thank for give you interst in apne bank');
    name=input('Enter the name');
    age=input('Enter the age');
    phone=input('Enter the phone');  
    if phone.len()!=10:
        print('Please enter the correct phone number')
    nominee=input('Enter the nominee name');
    password=input('Enter the password');