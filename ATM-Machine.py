

print('-' * 50)
print('     |_______________________________________|')
print('     |______________ATM-MACHINE______________|')
print('     |_______________________________________|')
print('-' * 50)

Options=['(1).Check Balance', '(2).Withdraw', '(3).Register', '(4).Buy Data' ]
DataList =['(1).1GB : $200  ', '(2).2GB : $500', '(3).9GB : $200', '(4).12Gb : $3500', '(5).Check Data Balance', '(0).Back ' ]
Data = 0
Balance = 3000


def DataPrice():
    for DataPrices in DataList:
        print(DataPrices)
def selectionOPtion():
    for List in Options:
        print(List)
selectionOPtion()

while True:
    choice = int(input('Select Options: '))
    if choice == 1:
        print(f"Your Account Balance is : {Balance}")
        selectionOPtion()
        continue
    if choice == 2:
        choice = int(input('How Much  you Want WithDraw: '))
        Balance -= choice
        print(f"Your Balance Remain : {Balance} \n  You WithDraw: {choice}")
        print(f"successful:  $ {choice}")
        break
    if choice == 3:
        while choice:
            name = input('Enter your name :')
            age = (input('Enter your Age :'))
            Email = input('Enter your Email :')
            PhoneNumber = (input('Enter your PhoneNumber :'))
            Password = (input('Enter your Password :'))
            print(f"\n Successful SignUp \n: Your informations  is Here  \n Name: {name} \n Age: {age} \n Email: {Email} \n PhoneNumber: {PhoneNumber}")
            break
    if choice == 4:
        while choice: 
            print('****************** Buy Data ******************')
            DataPrice()
            choice = int(input('Choice DataPlan  : '))
            print(f'Option {choice} Selected')
            if choice == 1:
                Balance -= 200
                if choice == 1:
                    Data += 1
                print(f"You successful buy Data from your Bank account  \n 1GB at : ${200} \n Your Account Balance is :{Balance}")
            

            if choice == 2:
                Balance -= 500
                if choice == 2:
                    Data += 2
                print(f"You successful buy Data from your Bank account  \n 2GB at : ${500} \n Your Account Balance is :{Balance}")
            if choice == 3:
                Balance -= 2000
                if choice == 3:
                    Data += 9
                print(f"You successful buy Data from your Bank account  \n 9GB at : ${2000} \n Your Account Balance is :{Balance}")

            if choice == 4:
                Balance -= 3500
                if choice == 4:
                    Data += 12
                while choice:
                    if Balance < 0:
                        print('invalid')
                    else:
                        print(f"You successful buy Data from your Bank account  \n 12GB at : ${3500} \n Your Account Balance is :{Balance}")
                    break
            if choice == 5:
                print(f"Your Data Balance is : {Data}GB")
            if choice == 0:
                break
    selectionOPtion()
    continue



