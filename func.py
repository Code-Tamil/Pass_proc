##########################################################
# >> Version : pass_proc_1.0.1 
# >> Created by : Tharun
# >> Description : Open source password manager
# >> Docs : https://github.com/Tharunkumarmuthu/Pass_proc
##########################################################

# IMPORTING
import hashlib 
import random
import pyfiglet
import os
import func
from sys import exit

# Creating Lists
for_which_arr = []
the_pass_arr = []

# Declaring Functions

# MODULES INSTALLING FUNC
def install ():
    if os.name == 'posix':
        os.system('pip3 install hashlib\npip3 install pyfiglet')
    else:
	    os.system('pip install hashlib\npip install pyfiglet')

# NULL CHECKER
def is_null(input):
    if input == '':
        return True
    else:
        return False

# RETURN YES
def return_yes(input):
    if input == 'y' or input == 'Y':
        return True
    else:
        return False
# RANDOM PASSWORD GENERATOR

def random_gen():

    uppercase = 'QWERTYUIOPASDFGHJKLZXCVBNM'
    lowercase = uppercase.lower()
    digits = '1234567890'
    symbols = '~!@#$%^&*()_+`-=[]\\;\',./{}|:"<>?'
    #ups, lws, nums, syms = True, True, True, True
    screen_clear()
    print('RANDOM PASSWORD GENERATOR')
    ups = return_yes(input('Do you want Uppercase [ABCD] (y/n) : '))
    lws = return_yes(input('Do you want Lowercase [abcd] (y/n) : '))
    nums = return_yes(input('Do you want Numbers   [1234] (y/n) : '))
    syms = return_yes(input('Do you want Symbols   [!@#$] (y/n) : '))
    every = ''
    if ups:
        every += uppercase
    if lws:
        every += lowercase
    if nums:
        every += digits
    if syms:
        every += symbols
    if every == '':
        every = uppercase + lowercase + digits + symbols
    length = input('Length of the pass : ')
    try:
        int(length)
    except ValueError:
        length = 8
    if int(length) == 0 or int(length) > 20:
        length = 8
    ran_pass =  ''.join(random.choice(every) for i in range(int(length))) 
    print (f'Your password is generated and saved {ran_pass}')
    return ran_pass

# THE DECODER
def decode_func(todecode, userpass):
    uppercase = 'QWERTYUIOPASDFGHJKLZXCVBNM'
    lowercase = uppercase.lower()
    digits = '1234567890'
    symbols = '~!@#$%^&*()_+`-=[]\\;\',./{}|:"<>?'
    space = ' '
    every = uppercase + lowercase + digits + symbols + space
    for temp_let in every:
        let = temp_let + userpass
        result = hashlib.md5(let.encode())
        fin = result.hexdigest() + '\n'
        if (todecode == fin):
            return let[0:1]
        else:
            continue
    return "wrong_password"

# CHECK WRONG PASSWORD
def pass_check(name_of_the_file,userpass):
    result_m = ''
    with open(name_of_the_file, "r") as file: 
        data = file.readlines() 
        for line in data: 
            if line == 'sofwa\n':
                continue
            elif line == 'sotpa\n':
                continue
            else:
                temp_result = str(decode_func(line, userpass))
                if temp_result == 'wrong_password':
                    result_m = False
                else:
                    result_m = True
    return result_m

# PASS PRINTER
def view_the_pass(the_file, userpass):
    result_m = ''
    with open(the_file, "r") as file: 
        data = file.readlines() 
        screen_clear()
        i = 1
        for line in data: 
            if line == 'sofwa\n':
                result_m += f'\n\n{i})\tFor which >> '
                i += 1
            elif line == 'sotpa\n':
                result_m += '\n  \tThe pass  >> '
            else:
                result_m += str(decode_func(line, userpass)) 
    print(result_m + '\n')
    press_exit(the_file,userpass)

# PASS WRITER
def write_the_pass(name_of_the_file, userpass):
    screen_clear()
    for_which = input('Title for you password (eg. email) >>')
    the_pass = input('What\'s the password [type \'pg\' to generate pass]>>')
    if is_null(for_which) or is_null(the_pass):
        write_the_pass(name_of_the_file,userpass)
    if the_pass == 'pg':
        the_pass = random_gen()
    for temp_let in for_which:
        let = temp_let + userpass
        result = hashlib.md5(let.encode())
        for_which_arr.append(result.hexdigest())
    for temp_let in the_pass:
        let = temp_let + userpass
        result = hashlib.md5(let.encode())
        the_pass_arr.append(result.hexdigest())

    with open(name_of_the_file, "a") as f:
        f.write('sofwa\n')
        for elem in for_which_arr:
            f.write(f'{elem}\n')
        f.write('sotpa\n')
        for elem in the_pass_arr:
            f.write(f'{elem}\n')
    print('Successfully appended')    
    for_which_arr.clear()
    the_pass_arr.clear()
    press_exit(name_of_the_file,userpass)

# PASS DELETER
def pass_del(the_file,userpass):
    how_many = 0
    result_m = ''
    with open(the_file, "r") as file: 
        data = file.readlines() 
        screen_clear()
        i = 1
        for line in data: 
            if line == 'sofwa\n':
                result_m += f'\n\n{i})\tFor which >> '
                i += 1
            elif line == 'sotpa\n':
                result_m += '\n  \tThe pass  >> '
            else:
                result_m += str(decode_func(line, userpass)) 
        how_many = i - 1
    print(result_m + '\n')
    no_of_pass = input('Enter the no. of pass to delete: ')
    try:
        int(no_of_pass)
    except ValueError:
        input('Select a correct option [ENTER]')
        pass_del(the_file,userpass)
    if no_of_pass == '' or int(no_of_pass) == 0 or int(no_of_pass)> how_many:
        input('Select a correct option [ENTER]')
        pass_del(the_file,userpass)
    result = []
    with open(the_file, "r") as file: 
        data = file.readlines() 
        i = 0
        o = int(no_of_pass)
        can_print = True
        for line in data:
            if line == 'sofwa\n':
                i += 1
                if i == o:
                    can_print = False
                else:
                    can_print = True
                    result.append(line)
            else:   
                if can_print:
                    result.append(line)
                    continue
    with open(the_file, "w") as file:
        for line in result:
            file.write(line)

# CREATE FILE
def create_file():
    screen_clear()
    temp_file_name = input('Enter a name for the file : ')
    userpass = input('Enter a password to encrypt : ')
    if is_null(temp_file_name) or is_null(userpass):
        create_file()
    if temp_file_name[-7:] == '.thpass':
        file_name = temp_file_name
    else:
        file_name = temp_file_name + '.thpass'
    write_the_pass(file_name, userpass)
    press_exit(file_name,userpass)

# CLEAR SRCEEN
def screen_clear():
    if os.name == 'posix':
      _ = os.system('clear')
    else:
      _ = os.system('cls')
    banner()

# BANNER
def banner():
    ascii_banner = pyfiglet.figlet_format("Pass || Proc") 
    print(ascii_banner)
    print('-' * 55)
    print('>> Version : pass_proc_1.0.1 \n>> Created by : Tharun\n>> Description : Open source password manager\n>> Docs : https://github.com/Tharunkumarmuthu/Pass_proc\n>> Support : bc1qcxpjnznn7zmq3xyxnafqjn39j46e5j33seu3dz')
    print('-' * 55)    

# OPTION SELECTING
def option_selector(file_name,userpass):
    # Selecting options
    screen_clear()
    print('Select from the options \n1)view the pass\n2)write a pass\n3)delete a pass')
    option = input()
    try:
        int(option)
    except ValueError:
        input('Select a correct option [ENTER]')
        option_selector(file_name,userpass)
    if int(option) == 1:
        view_the_pass(file_name, userpass)
        press_exit(file_name,userpass)
    elif int(option) == 2:
        write_the_pass(file_name, userpass)
        press_exit(file_name,userpass)
    elif int(option) == 3:
        pass_del(file_name, userpass)
        press_exit(file_name,userpass)
    else:
        input('Select a correct option [ENTER]')
        option_selector(file_name,userpass)

# press_exit
def press_exit(settable_file_name,settable_userpass):
    input('PRESS [ENTER] ')
    my_main(settable_file_name,settable_userpass)

# the main func
def my_main(settable_file_name,settable_userpass):
    #gets into the program
    if settable_file_name == '' and settable_userpass == '':
        # BANNER AND STUFFS
        screen_clear()
        #Getting the path of the file
        print(settable_file_name,settable_userpass)
        temp_file_name = str(input('Enter the encrypted file path [press (Enter) to create]: '))
        if temp_file_name == '':
            create_file()
        elif temp_file_name[-7:] == '.thpass':
            file_name = temp_file_name
        else:
            file_name = temp_file_name + '.thpass'

        #error catching
        try:
            with open(file_name, "r") as file:
                file.readlines
        except FileNotFoundError:
            ans = input('Not any file found \nDo you want to create a file[y\\n] : ')
            if ans == 'y'  or ans == 'Y':
                create_file()
            else:
                my_main('','')
        #user pass
        userpass = input('Enter your password to encrypt : ')
        # Check pass
        if pass_check(file_name,userpass) == False:
            print('!!! WRONG_PASSWORD !!!')
            press_exit('','')
        option_selector(file_name,userpass)
    else:
        screen_clear()
        option_selector(settable_file_name,settable_userpass)
