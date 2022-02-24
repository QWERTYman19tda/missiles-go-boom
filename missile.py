#importing
import time
import random
import datetime
#from saved_names import saved <-- FIX MEEEEEEEEEEEEEEEEEEEEEE

#setting variables
command = ''
yesno = ''
name = ''
username = ''
passwd = ''
name = ""
name_helper = ""
name_formatted = ''
name_num = 0
determine_launch = True
safety_class = random.randint(1111, 9999)
time_wait = random.randint(1, 10)
exit_code = random.randint(0, 9)

def time_random():
    time_wait = random.randint(1, 10)

def random_launch():
    
    determine_launch_number = random.randint(1, 2)
    
    if determine_launch_number == 1:
        determine_launch = True
    else:  
        determine_launch = False
'''
def name_saver():
    
    name_num = 0
    
    while name_saved == True:
        name_saver =+ 1
        last_key = [*saved.keys()][-1]
'''
#create class
def timer():
    #variables
    h = 0
    m = 0
    s = 14
        # Create class that acts as a countdown
    def countdown(h, m, s):
 
        # Calculate the total number of seconds
        total_seconds = h * 3600 + m * 60 + s
 
        # While loop that checks if total_seconds reaches zero
        # If not zero, decrement total time by one second
        while total_seconds >= 1:
    
            # Timer represents time left on countdown
            timer = datetime.timedelta(seconds = total_seconds)
            
            # Prints the time left on the timer
            print(timer, end="\r")
     
            # Delays the program one second
            time.sleep(1)
 
            # Reduces total time by one second
            total_seconds -= 1
            
        else:
            print('')
        
    countdown(int(h), int(m), int(s))
    
def name(name, name_helper):
    name = ""
    name_helper = ""
    name_formatted = name + name_helper    

#variables
command = ''
#beginning input
command = input("root-user:~$")
if command == "sudo access network":
    print('ERROR 756 \nThis server is protected \n What is the password and username?')
    username = input('Username:\n')
    passwd = input('Password:\n')
    if username == 'KingBonzo' and passwd == 'MeLoveTacos':
        print('Access Granted with SUDO mode activated')
    else:
        print('Error 457 \nPassword ('+str(passwd)+') and username ('+str(username)+') entered did not match the ones we we have on file. \nPlease try again.')
        quit()
    command = ''
    command = input('   >')
    if command == 'trigger launch missiletype == SATURN 5':
        print("Who would like to launch MISSILE SATURN 5? ")
        command = ''
        name = input('   >')
        if name != '':
            print('Now accessing...')
            time.sleep(time_wait)
            time_random()
            print('...')
            time.sleep(time_wait)
            time_random()
            print('...')
            time.sleep(time_wait)
            time_random()
            print('...')
            time.sleep(time_wait)
            '''
            saved[name_num] = name
            name(name, name_helper)
            name_formatted = open("saved_names", "a")
            '''
            yesno = input('Are you sure? ')
            if yesno == 'yes' or 'YES' or 'Yes':
                random_launch()
                if determine_launch == True:
                    print('Contact will Occour Shortly')
                    timer()
                    print('Contact Confirmed')
                    time.sleep(random.randint(0, 5))
                    print('Logoff Successful with exit code '+str(exit_code)+'.')
                    quit()
                elif yesno == 'no' or 'No' or 'NO':
                    print('This script has been canceled.')
                    quit()
                else:
                    print('ERROR 398 \nThe IP adress trying to preform a Safety Class '+str(safety_class)+'\n action is not verified by the owner.')
                    quit()
            else:
                print('SCRIPT END')
        else:
            print('SCRIPT END')
    else:
        print('SCRIPT END')
else:
    print('SCRIPT END')
