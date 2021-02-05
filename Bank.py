import pygame
import random
import json
import turtle
from turtle import Screen
from pygame.locals import *
import requests
from lazyme.string import color_print

url = 'http://176.9.164.222:2211'


# Home Page
def start():
    h = 500
    w = 500
    running = True
    screen = pygame.display.set_mode((h, w))
    img = pygame.image.load('Home.jpg')
    img.convert()
    rect = img.get_rect()
    rect.center = h // 2, w // 2
    while running:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_RETURN:
                    running = False
        screen.blit(img, rect)
        pygame.display.update()
    pygame.quit()
    login(url)


# Log in form
def login(url):
    tests = 0
    while tests < 5:
        color_print('--------------', color='red')
        color_print('**Login Form**', color='black', highlight='white', bold=True)
        color_print('--------------', color='red')
        information = {'username': input('Username: '), 'password': input('Password: ')}
        response = requests.post(url + '/api/Login', information)
        if response.status_code == 200:
            # TOKEN
            token = json.loads(response.text)['token']
            jwttoken = {'Authorization': 'JWT ' + token}
            color_print('Log in Successful.', color='black', highlight='green')
            return options(jwttoken)
        else:
            color_print('Username or Password is incorrect!', color='white', highlight='red')
            tests += 1
            if tests == 5:
                break
            else:
                ans = input('Do you want to try again?(yes/no)\n')
                while ans.lower() != 'yes' and ans.lower() != 'no':
                    ans = input('Do you want to try again?(yes/no)\n')
                if ans.lower() == 'no':
                    break


# List of options
def options(jwttoken):
    h2 = 590
    w2 = 615
    running2 = True
    screen = pygame.display.set_mode((h2, w2))
    img2 = pygame.image.load('options.png')
    img2.convert()
    rect2 = img2.get_rect()
    rect2.center = h2 // 2, w2 // 2
    screen.blit(img2, rect2)
    pygame.display.update()
    while running2:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_1:
                    key1(jwttoken)
                    running2 = False
                elif event.key == K_2:
                    key2(jwttoken)
                    running2 = False
                elif event.key == K_3:
                    key3(jwttoken)
                    running2 = False
                elif event.key == K_4:
                    key4(jwttoken)
                    running2 = False
                elif event.key == K_5:
                    key5(jwttoken)
                    running2 = False
                elif event.key == K_6:
                    key6(jwttoken)
                    running2 = False
                elif event.key == K_7:
                    key7(jwttoken)
                    running2 = False
                elif event.key == K_8:
                    key8(jwttoken)
                    running2 = False
                elif event.key == K_9:
                    key9(jwttoken)
                    running2 = False
                elif event.key == K_F10:
                    keyf10(jwttoken)
                    running2 = False
                elif event.key == K_F7:
                    keyf7(jwttoken)
                    running2 = False
                elif event.key == K_ESCAPE:
                    pygame.quit()
                    return 0
                    running2 = False
    input('For showing Options Enter something.\n')
    options(jwttoken)


# *** If options selected ***

# key1 --> Creating a Bank Account
def key1(jwttoken):
    pygame.quit()
    creating = True
    while creating:
        color_print('--------------', color='red')
        color_print('**Please Fill This Form**', color='black', highlight='white', bold=True)
        color_print('--------------', color='red')
        fname = input('firstName: ')
        lname = input('lastName: ')
        phone = input('phoneNumber: ')
        national = input('nationalCode: ')
        if not phone.isdigit():
            color_print('PhoneNumber is invalid!', color='white', highlight='red')
            ask = True
            while ask:
                again = input('Do you want to try again?(yes/no)\n')
                if again.lower() == 'yes':
                    creating = True
                    ask = False
                elif again.lower() == 'no':
                    creating = False
                    ask = False
                else:
                    ask = True

        else:
            if not national.isdigit():
                print('NationalCode is invalid!', color='white', highlight='red')
                ask = True
                while ask:
                    again = input('Do you want to try again?(yes/no)\n')
                    if again.lower() == 'yes':
                        creating = True
                        ask = False
                    elif again.lower() == 'no':
                        creating = False
                        ask = False
                    else:
                        ask = True
            else:
                key1info = {'accountOwner': {'firstName': fname, 'lastName': lname, 'phoneNumber': phone,
                                             'nationalCode': national}}
                response = requests.post(url + '/api/accounts/BankAccountListCreate', headers=jwttoken, json=key1info)
                if response.status_code == 201:
                    acc = json.loads(response.text)
                    color_print('Here is your account details : ', color='black', highlight='green')
                    print('accountNumber:', acc['accountNumber'])
                    print('accountOwner:')
                    print('-->firstName:', acc['accountOwner']['firstName'])
                    print('-->lastName:', acc['accountOwner']['lastName'])
                    print('-->phoneNumber:', acc['accountOwner']['phoneNumber'])
                    print('-->nationalCode:', acc['accountOwner']['nationalCode'])
                    if 'accounts' in acc['accountOwner'].keys():
                        print('accounts:')
                        for i in range(len(acc['accountOwner']['accounts'])):
                            print('-->''accountNumber:', acc['accountOwner']['accounts'][i]['accountNumber'])
                            print('-->status:', acc['accountOwner']['accounts'][i]['status'])
                    print('credit:', acc['credit'])
                    print('status:', acc['status'])
                    color_print('--------------------', color='red')
                    creating = False
                else:
                    color_print('PhoneNumber or NationalCode is invalid!', color='white', highlight='red')
                    ask = True
                    while ask:
                        again = input('Do you want to try again?(yes/no)\n')
                        if again.lower() == 'yes':
                            creating = True
                            ask = False
                        elif again.lower() == 'no':
                            creating = False
                            ask = False
                        else:
                            ask = True


# key2 --> Getting List of Accounts
def key2(jwttoken):
    pygame.quit()
    response = requests.get(url + '/api/accounts/BankAccountListCreate', headers=jwttoken)
    acclist = json.loads(response.text)
    for i in range(len(acclist)):
        print('accountNumber:', acclist[i]['accountNumber'])
        print('accountOwner:')
        print('-->firstName:', acclist[i]['accountOwner']['firstName'])
        print('-->lastName:', acclist[i]['accountOwner']['lastName'])
        print('-->phoneNumber:', acclist[i]['accountOwner']['phoneNumber'])
        print('-->nationalCode:', acclist[i]['accountOwner']['nationalCode'])
        if 'accounts' in acclist[i]['accountOwner'].keys():
            print('accounts: ')
            print('-->accountNumber:', acclist[i]['accountOwner']['accounts'][0]['accountNumber'])
            print('-->status:', acclist[i]['accountOwner']['accounts'][0]['status'])
        print('credit:', acclist[i]['credit'])
        print('status:', acclist[i]['status'])
        color_print('-------------------', color='red')


# key3 --> User Sign Up
def key3(jwttoken):
    pygame.quit()
    signing = True
    while signing:
        key3info = {'username': input('Username: '), 'password': input('Password: ')}
        response = requests.post(url + '/api/accounts/User/SignUp', headers=jwttoken, json=key3info)
        if response.status_code == 201:
            newclient = json.loads(response.text)
            color_print('Done!', color='black', highlight='green')
            print('-->username:', newclient['username'])
            color_print('-----------------------', color='red')
            signing = False
        else:
            color_print('Username already exists.', color='white', highlight='red')
            asking = True
            while asking:
                again = input('Do you want to try again?(yes/no)\n')
                if again.lower() == 'yes':
                    signing = True
                    asking = False
                elif again.lower() == 'no':
                    signing = False
                    asking = False
                else:
                    signing = True
                    asking = True


# key4 --> Getting Logs
def key4(jwttoken):
    pygame.quit()
    h4 = 570
    w4 = 480
    running4 = True
    screen = pygame.display.set_mode((h4, w4))
    img4 = pygame.image.load('logs.png')
    img4.convert()
    rect4 = img4.get_rect()
    rect4.center = h4 // 2, w4 // 2
    screen.blit(img4, rect4)
    pygame.display.update()
    while running4:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_1:
                    graph(jwttoken)
                    running4 = False
                elif event.key == K_2:
                    text(jwttoken)
                    running4 = False
                elif event.key == K_3:
                    options(jwttoken)
                    running4 = False


# Getting logs in text form
def text(jwttoken):
    pygame.quit()
    getting = True
    while getting:
        accountnum = input('AccountNumber: ')
        if not accountnum.isdigit():
            color_print('AccountNumber is invalid!', color='white', highlight='red')
            ask = True
            while ask:
                again = input('Do you want to try again?(yes/no)\n')
                if again.lower() == 'yes':
                    getting = True
                    ask = False
                elif again.lower() == 'no':
                    getting = False
                    ask = False
                else:
                    ask = True
        else:
            key4info = {'accountNumber': accountnum}
            response = requests.post(url + '/api/accounts/GetBankAccountLogs', headers=jwttoken, json=key4info)
            if response.status_code == 200:
                logs = json.loads(response.text)
                print('currentCredit:', logs['currentCredit'])
                for i in range(len(logs['logs'])):
                    print('id:', logs['logs'][i]['id'])
                    print('amount:', logs['logs'][i]['amount'])
                    print('definition:', logs['logs'][i]['definition'])
                    print('logType:', logs['logs'][i]['logType'])
                    print('date:', logs['logs'][i]['date'])
                    color_print('-----------------------', color='red')
                getting = False
            else:
                color_print('AccountNumber is invalid or dosent exist!', color='white', highlight='red')
                ask = True
                while ask:
                    again = input('Do you want to try again?(yes/no)\n')
                    if again.lower() == 'yes':
                        getting = True
                        ask = False
                    elif again.lower() == 'no':
                        getting = False
                        ask = False
                    else:
                        ask = True


# Getting logs in graph form
def graph(jwttoken):
    pygame.quit()
    trying = True
    try:
        while trying:
            accountnum = input('AccountNumber: ')
            key4info = {'accountNumber': accountnum}
            fixed = 5
            response = requests.post(url + '/api/accounts/GetBankAccountLogs', headers=jwttoken, json=key4info)
            if not accountnum.isdigit():
                color_print('AccountNumber is invalid!', color='white', highlight='red')
                ask2 = True
                while ask2:
                    again = input('Do you want to try again?(yes/no)\n')
                    if again.lower() == 'yes':
                        trying = True
                        ask2 = False
                    elif again.lower() == 'no':
                        trying = False
                        ask2 = False
                    else:
                        ask = True
            else:
                if response.status_code == 200:
                    logs = json.loads(response.text)
                    current = int(logs['currentCredit'])
                    final = int(logs['currentCredit'])
                    log = []
                    logtypes = []
                    colors = ['blue', 'red', 'green', 'yellow', 'pink', 'purple', 'orange', 'brown', 'black']
                    trying = False
                    for k in range(len(logs['logs'])):
                        log += [logs['logs'][k]['amount']]
                        logtypes += [logs['logs'][k]['logType']]
                    for j in range(len(log)):
                        if logtypes[j] == '+':
                            current = current - log[j]
                        else:
                            current = current + log[j]
                    for i in range(len(logs['logs'])):
                        length = len(logs['logs'])
                        amount = int(logs['logs'][i]['amount'])
                        logtype = str(logs['logs'][i]['logType'])
                        idd = logs['logs'][i]['id']
                        if i == 0:
                            date = str(logs['logs'][i]['date'])
                            hour = int(date[14:16])
                            screen = Screen()
                            screen.setup(width=1.0, height=1.0)
                            turtle.screensize(length * 1000, length * 1000)
                            turtle.penup()
                            turtle.goto(-320, -250)
                            turtle.pendown()
                            turtle.fd(1000)
                            turtle.stamp()
                            turtle.write('id')
                            turtle.setpos(-320, -250)
                            turtle.left(90)
                            turtle.fd(1000)
                            turtle.stamp()
                            turtle.write('Credit')
                            turtle.penup()
                            turtle.setpos(-320 + hour, -250 + current)
                            turtle.color(random.choice(colors))
                            turtle.dot()
                            turtle.color('black')
                            turtle.write((0, current))
                            turtle.pendown()
                        if i > 0:
                            hour += fixed * (i + 7)
                        if logtype == '+':
                            current += amount
                            turtle.goto(-320 + hour, -250 + current)
                            turtle.color(random.choice(colors))
                            turtle.dot()
                            turtle.color('black')
                            turtle.write((idd, current))
                        else:
                            current -= amount
                            turtle.goto(-320 + hour, -250 + current)
                            turtle.color(random.choice(colors))
                            turtle.dot()
                            turtle.color('black')
                            turtle.write((idd, current))
                    turtle.hideturtle()
                    turtle.exitonclick()

                else:
                    color_print('Account Number doesnt exist!', color='white', highlight='red')
                    ask = True
                    while ask:
                        again = input('Do you want to try again?(yes/no)\n')
                        if again.lower() == 'yes':
                            trying = True
                            ask = False
                        elif again.lower() == 'no':
                            trying = False
                            ask = False
                        else:
                            ask = True

    except Exception:
        pass
    color_print('-----------------------', color='red')


# key5 --> Adding an Account To Account Owner
def key5(jwttoken):
    pygame.quit()
    adding = True
    while adding:
        ncode = input('NationalCode: ')
        if not ncode.isdigit():
            color_print('NationalCode is invalid!', color='white', highlight='red')
            ask = True
            while ask:
                again = input('Do you want to try again?(yes/no)\n')
                if again.lower() == 'yes':
                    adding = True
                    ask = False
                elif again.lower() == 'no':
                    adding = False
                    ask = False
                else:
                    ask = True
        else:
            key5info = {'nationalCode': ncode}
            response = requests.post(url + '/api/accounts/AddAccountToAccountOwner', headers=jwttoken, json=key5info)
            if response.status_code == 200:
                addacc = json.loads(response.text)
                print('accountNumber:', addacc['accountNumber'])
                print('accountOwner:')
                print('-->firstName:', addacc['accountOwner']['firstName'])
                print('-->lastName:', addacc['accountOwner']['lastName'])
                print('-->phoneNumber:', addacc['accountOwner']['phoneNumber'])
                print('-->nationalCode:', addacc['accountOwner']['nationalCode'])
                if 'accounts' in addacc['accountOwner'].keys():
                    print('accounts:')
                    for i in range(len(addacc['accountOwner']['accounts'])):
                        print('-->accountNumber:', addacc['accountOwner']['accounts'][i]['accountNumber'])
                        print('-->status:', addacc['accountOwner']['accounts'][i]['status'])
                        color_print('-------------------', color='red')
                print('credit:', addacc['credit'])
                print('status:', addacc['status'])
                color_print('-------------------', color='red')
                adding = False
            else:
                color_print('NationalCode is invalid!', color='white', highlight='red')
                ask = True
                while ask:
                    again = input('Do you want to try again?(yes/no)\n')
                    if again.lower() == 'yes':
                        adding = True
                        ask = False
                    elif again.lower() == 'no':
                        adding = False
                        ask = False
                    else:
                        ask = True


# key6 --> Close an Account
def key6(jwttoken):
    pygame.quit()
    closing = True
    while closing:
        accnum = input('AccountNumber: ')
        if not accnum.isdigit():
            color_print('AccountNumber is invalid!', color='white', highlight='red')
            ask = True
            while ask:
                again = input('Do you want to try again?(yes/no)\n')
                if again.lower() == 'yes':
                    closing = True
                    ask = False
                elif again.lower() == 'no':
                    closing = False
                    ask = False
                else:
                    ask = True
        else:
            key6info = {'accountNumber': accnum}
            response = requests.post(url + '/api/accounts/CloseAccount', headers=jwttoken, json=key6info)
            if response.status_code == 200:
                close = json.loads(response.text)
                color_print(close, color='black', highlight='white')
                color_print('-------------------', color='red')
                closing = False
            else:
                color_print('AccountNumber is invalid.', color='white', highlight='red')
                ask = True
                while ask:
                    again = input('Do you want to try again?(yes/no)\n')
                    if again.lower() == 'yes':
                        closing = True
                        ask = False
                    elif again.lower() == 'no':
                        closing = False
                        ask = False
                    else:
                        ask = True


# key7 --> Block an Account
def key7(jwttoken):
    pygame.quit()
    blocking = True
    while blocking:
        accnumber = input('AccountNumber: ')
        if not accnumber.isdigit():
            color_print('AccountNumber is invalid!', color='white', highlight='red')
            ask = True
            while ask:
                again = input('Do you want to try again?(yes/no)\n')
                if again.lower() == 'yes':
                    blocking = True
                    ask = False
                elif again.lower() == 'no':
                    blocking = False
                    ask = False
                else:
                    ask = True
        else:
            key7info = {'accountNumber': accnumber}
            response = requests.post(url + '/api/accounts/CloseAccount', headers=jwttoken, json=key7info)
            if response.status_code == 200:
                block = json.loads(response.text)
                color_print(block, color='black', highlight='white', bold=True)
                color_print('-------------------', color='red')
                blocking = False
            else:
                color_print('AccountNumber is invalid.', color='white', highlight='red')
                ask = True
                while ask:
                    again = input('Do you want to try again?(yes/no)\n')
                    if again.lower() == 'yes':
                        blocking = True
                        ask = False
                    elif again.lower() == 'no':
                        blocking = False
                        ask = False
                    else:
                        ask = True


# key8 --> Retrieve a Bank Account
def key8(jwttoken):
    pygame.quit()
    retrieving = True
    while retrieving:
        acc = input('AccountNumber: ')
        if not acc.isdigit():
            color_print('AccountNumber is invalid!', color='white', highlight='red')
            ask = True
            while ask:
                again = input('Do you want to try again?(yes/no)\n')
                if again.lower() == 'yes':
                    retrieving = True
                    ask = False
                elif again.lower() == 'no':
                    retrieving = False
                    ask = False
                else:
                    ask = True
        else:
            response = requests.get(url + '/api/accounts/BankAccountRetrieve/' + acc, headers=jwttoken)
            retacc = json.loads(response.text)
            if response.status_code == 200:
                color_print('-----------------------', color='red')
                print('accountNumber:', retacc['accountNumber'])
                print('accountOwner:')
                print('-->firstName:', retacc['accountOwner']['firstName'])
                print('-->lastName:', retacc['accountOwner']['lastName'])
                print('-->phoneNumber:', retacc['accountOwner']['phoneNumber'])
                print('-->nationalCode:', retacc['accountOwner']['nationalCode'])
                if 'accounts' in retacc['accountOwner'].keys():
                    print('accounts:')
                    for i in range(len(retacc['accountOwner']['accounts'])):
                        print('-->accountNumber:', retacc['accountOwner']['accounts'][i]['accountNumber'])
                        print('-->status:', retacc['accountOwner']['accounts'][i]['status'])
                print('credit:', retacc['credit'])
                print('status:', retacc['status'])
                color_print('-----------------------', color='red')
                retrieving = False
            else:
                color_print('AccountNumber is invalid.', color='white', highlight='red')
                ask = True
                while ask:
                    again = input('Do you want to try again?(yes/no)\n')
                    if again.lower() == 'yes':
                        retrieving = True
                        ask = False
                    elif again.lower() == 'no':
                        retrieving = False
                        ask = False
                    else:
                        ask = True


# key9 --> Retrieve Account Owner
def key9(jwttoken):
    pygame.quit()
    retrieving = True
    while retrieving:
        natcode = input('nationalCode: ')
        if not natcode.isdigit():
            color_print('NationalCode is invalid!', color='white', highlight='red')
            ask = True
            while ask:
                again = input('Do you want to try again?(yes/no)\n')
                if again.lower() == 'yes':
                    retrieving = True
                    ask = False
                elif again.lower() == 'no':
                    retrieving = False
                    ask = False
                else:
                    ask = True
        else:
            response = requests.get(url + '/api/accounts/AccountOwnerRetrieve/' + natcode, headers=jwttoken)
            retowner = json.loads(response.text)
            if response.status_code == 200:
                print('firstName:', retowner['firstName'])
                print('lastName:', retowner['lastName'])
                print('phoneNumber:', retowner['phoneNumber'])
                print('nationalCode:', retowner['nationalCode'])
                if 'accounts' in retowner.keys():
                    print('accounts:')
                    for i in range(len(retowner['accounts'])):
                        print('-->accountNumber:', retowner['accounts'][i]['accountNumber'])
                        print('-->status:', retowner['accounts'][i]['status'])
                        color_print('------------------', color='red')
                retrieving = False
            else:
                color_print('NationalCode is invalid.', color='white', highlight='red')
                ask = True
                while ask:
                    again = input('Do you want to try again?(yes/no)\n')
                    if again.lower() == 'yes':
                        retrieving = True
                        ask = False
                    elif again.lower() == 'no':
                        retrieving = False
                        ask = False
                    else:
                        ask = True


# keyf7 --> Make a Transaction
def keyf7(jwttoken):
    pygame.quit()
    h3 = 600
    w3 = 554
    running3 = True
    screen = pygame.display.set_mode((h3, w3))
    img3 = pygame.image.load('transaction.png')
    img3.convert()
    rect3 = img3.get_rect()
    rect3.center = h3 // 2, w3 // 2
    screen.blit(img3, rect3)
    pygame.display.update()
    while running3:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_1:
                    withdraw(jwttoken)
                    running3 = False
                elif event.key == K_2:
                    add(jwttoken)
                    running3 = False
                elif event.key == K_3:
                    transfer(jwttoken)
                    running3 = False
                elif event.key == K_4:
                    options(jwttoken)
                    running3 = False


def withdraw(jwttoken):
    pygame.quit()
    withdrawing = True
    while withdrawing:
        fromacc = input('FromAccount: ')
        amount = input('Amount: ')
        define = input('Definition: ')
        if not fromacc.isdigit():
            color_print('FromAccountNumber is invalid!', color='white', highlight='red')
            ask = True
            while ask:
                again = input('Do you want to try again?(yes/no)\n')
                if again.lower() == 'yes':
                    retrieving = True
                    ask = False
                elif again.lower() == 'no':
                    retrieving = False
                    ask = False
                else:
                    ask = True
        else:
            if not amount.isdigit():
                color_print('Amount is invalid!', color='white', highlight='red')
                ask = True
                while ask:
                    again = input('Do you want to try again?(yes/no)\n')
                    if again.lower() == 'yes':
                        withdrawing = True
                        ask = False
                    elif again.lower() == 'no':
                        withdrawing = False
                        ask = False
                    else:
                        ask = True
        withdrawinfo = {'fromAccount': fromacc, 'amount': amount, 'definition': define, 'cash': 'true'}
        response = requests.post(url + '/api/transaction/TransactionListCreate', headers=jwttoken, json=withdrawinfo)
        withdraw = json.loads(response.text)
        if response.status_code == 201:
            color_print('-----------------------', color='red')
            print('id:', withdraw['id'])
            print('fromAccountNumber:', withdraw['fromAccountNumber'])
            print('toAccountNumber:', withdraw['toAccountNumber'])
            print('amount:', withdraw['amount'])
            print('definition:', withdraw['definition'])
            print('cash:', withdraw['cash'])
            color_print('-----------------------', color='red')
            withdrawing = False
        else:
            if list(withdraw.values())[0][0] == 'not enough credit':
                color_print('This Account has not enough credit!', color='white', highlight='red')
                ask = True
                while ask:
                    again = input('Do you want to try again?(yes/no)\n')
                    if again.lower() == 'yes':
                        withdrawing = True
                        ask = False
                    elif again.lower() == 'no':
                        withdrawing = False
                        ask = False
                    else:
                        ask = True
            else:
                color_print('Invalid Input!', color='white', highlite='red')
                ask = True
                while ask:
                    again = input('Do you want to try again?(yes/no)\n')
                    if again.lower() == 'yes':
                        withdrawing = True
                        ask = False
                    elif again.lower() == 'no':
                        withdrawing = False
                        ask = False
                    else:
                        ask = True


def add(jwttoken):
    pygame.quit()
    adding = True
    while adding:
        toacc = input('ToAccount: ')
        amount = input('Amount: ')
        define = input('Definition: ')
        if not toacc.isdigit():
            color_print('ToAccountNumber is invalid!', color='white', highlight='red')
            ask = True
            while ask:
                again = input('Do you want to try again?(yes/no)\n')
                if again.lower() == 'yes':
                    adding = True
                    ask = False
                elif again.lower() == 'no':
                    adding = False
                    ask = False
                else:
                    ask = True
        else:
            if not amount.isdigit():
                color_print('Amount is invalid!', color='white', highlight='red')
                ask = True
                while ask:
                    again = input('Do you want to try again?(yes/no)\n')
                    if again.lower() == 'yes':
                        adding = True
                        ask = False
                    elif again.lower() == 'no':
                        adding = False
                        ask = False
                    else:
                        ask = True
        addinfo = {'toAccount': toacc, 'amount': amount, 'definition': define, 'cash': 'true'}
        response = requests.post(url + '/api/transaction/TransactionListCreate', headers=jwttoken, json=addinfo)
        print(response.status_code)
        if response.status_code == 201:
            add = json.loads(response.text)
            color_print('-----------------------', color='red')
            print('id:', add['id'])
            print('fromAccountNumber:', add['fromAccountNumber'])
            print('toAccountNumber:', add['toAccountNumber'])
            print('amount:', add['amount'])
            print('definition:', add['definition'])
            print('cash:', add['cash'])
            color_print('-----------------------', color='red')
            adding = False
        else:
            color_print('Invalid Input!', color='white', highlight='red')
            ask = True
            while ask:
                again = input('Do you want to try again?(yes/no)\n')
                if again.lower() == 'yes':
                    adding = True
                    ask = False
                elif again.lower() == 'no':
                    adding = False
                    ask = False
                else:
                    ask = True


def transfer(jwttoken):
    pygame.quit()
    transfering = True
    while transfering:
        fromacc = input('FromAccount: ')
        toacc = input('ToAccount: ')
        amount = input('Amount: ')
        define = input('Definition: ')
        if not fromacc.isdigit():
            color_print('FromAccountNumber is invalid!', color='white', highlight='red')
            ask = True
            while ask:
                again = input('Do you want to try again?(yes/no)\n')
                if again.lower() == 'yes':
                    transfering = True
                    ask = False
                elif again.lower() == 'no':
                    transfering = False
                    ask = False
                else:
                    ask = True
        else:
            if not toacc.isdigit():
                color_print('ToAccountNumber is invalid!', color='white', highlight='red')
                ask = True
                while ask:
                    again = input('Do you want to try again?(yes/no)\n')
                    if again.lower() == 'yes':
                        transfering = True
                        ask = False
                    elif again.lower() == 'no':
                        transfering = False
                        ask = False
                    else:
                        ask = True
            else:
                if not amount.isdigit():
                    color_print('Amount is invalid!', color='white', highlight='red')
                    ask = True
                    while ask:
                        again = input('Do you want to try again?(yes/no)\n')
                        if again.lower() == 'yes':
                            transfering = True
                            ask = False
                        elif again.lower() == 'no':
                            transfering = False
                            ask = False
                        else:
                            ask = True
        transinfo = {'fromAccount': fromacc, 'toAccount': toacc, 'amount': amount, 'definition': define,
                     'cash': 'false'}
        response = requests.post(url + '/api/transaction/TransactionListCreate', headers=jwttoken, json=transinfo)
        transfer = json.loads(response.text)
        if response.status_code == 201:
            color_print('-----------------------', color='red')
            print('id:', transfer['id'])
            print('fromAccountNumber:', transfer['fromAccountNumber'])
            print('toAccountNumber:', transfer['toAccountNumber'])
            print('amount:', transfer['amount'])
            print('definition:', transfer['definition'])
            print('cash:', transfer['cash'])
            color_print('Transaction done.', color='black', highlight='green')
            color_print('-----------------------', color='red')
            transfering = False
        else:
            if list(transfer.values())[0][0] == 'not enough credit':
                color_print('This Account has not enough credit!', color='white', highlight='red')
                ask = True
                while ask:
                    again = input('Do you want to try again?(yes/no)\n')
                    if again.lower() == 'yes':
                        transfering = True
                        ask = False
                    elif again.lower() == 'no':
                        transfering = False
                        ask = False
                    else:
                        ask = True
            else:
                color_print('Invalid Input!', color='white', highlite='red')
                ask = True
                while ask:
                    again = input('Do you want to try again?(yes/no)\n')
                    if again.lower() == 'yes':
                        transfering = True
                        ask = False
                    elif again.lower() == 'no':
                        transfering = False
                        ask = False
                    else:
                        ask = True


# keyf10 --> Getting All Transactions
def keyf10(jwttoken):
    pygame.quit()
    response = requests.get(url + '/api/transaction/TransactionListCreate', headers=jwttoken)
    alltrans = json.loads(response.text)
    for i in range(len(alltrans)):
        print('id:', alltrans[i]['id'])
        print('fromAccountNumber:', alltrans[i]['fromAccountNumber'])
        print('toAccountNumber:', alltrans[i]['toAccountNumber'])
        print('amount:', alltrans[i]['amount'])
        print('definition:', alltrans[i]['definition'])
        print('cash:', alltrans[i]['cash'])
        color_print('--------------------', color='red')
        repeating = False


# Start Application
start()