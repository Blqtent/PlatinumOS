#start of the os :)
ver = '2.1.1 pre-1'
cpu = 40
import time
import math
print('PlatinumBIOS (c) June 2021')
print('executing BIOS sequence...')
time.sleep(2)
print('locating bootloader...')
time.sleep(3)
print('(DONE)')
def WikipediaSearch():
  print("Booting search...")
  time.sleep(cpu/10)
  print('welcome, type "exit" to shutdown the system.\ntype your search term:')
  while True:
    y = input('')
    if y == "exit":
      print('Bye!')
      print('going back to boot menu')
      break
    else:
      print("goto https://en.wikipedia.org/wiki/"+y)
def PlatinumOS():
  G = False
  H = True
  print('')
  print('Booting PlatinumOS', ver,'...')
  print('cpu speed:', cpu, 'MHz')
  print('locating kernel...')
  print('')
  print('')
  time.sleep(cpu/20)
  print('jumping to kernel...')
  time.sleep(cpu/40)
  print('executing login sequence...')
  time.sleep(cpu/20)
  print('Platinum login:\n')
  # login sequence {
  class Login:
    error = None
    def __init__(self, uid, passw):
        self.uid = "admin"
        self.passw = "password"

    def authenticate(self):
        if (self.uid == logid and self.passw == logpass):
            print('authenticating...')
            time.sleep(3)
        else:
            while True:
              print('login unsucessful')
  log = Login("", "")
  logid = input("Enter your user ID: ")
  logpass = input("Enter your password: ")


  log.authenticate()
  # }

  print('login sucessful')
  print('Welcome to PlatinumOS', ver)
  print('Exiting...')
  time.sleep(2)
  print('Platinum shell 1.7')
  print('type "?" for help')
  while True:
    x = input('>')
    if x == '?':
      print('''
    Platinum Shell 1.8 (c) 2021
    
    Type "menu" to open the app menu.
    
    COMMANDS:
    version --- prints the OS version
    sh version --- prints the shell version
    ? --- to get here
    exit --- exits OS
    ls --- lists directories
    open --- opens files
    reboot --- reboots the system(WIP)
      ''')
    elif x == 'exit':
      print('shutting down Shell...')
      time.sleep(cpu/20)
      print('shutting down kernel...')
      time.sleep(cpu/20)
      print('logging out...')
      time.sleep(cpu/20)
      print('going back to boot screen...')
      print('done')
      break
    elif x == 'menu':
      while True: 
        app = input('''
          APP MENU
          -------------------------------------------------------
          1: microText
          2: Platinum Browser
          3: Calculator
          4: Arithmetic Programming Language(APL)
          5: Simple Programming Language(SPL)
          6: Timer
          7: Exit    
        ''')
        if app == '7':
          break
        elif app == '1':
          print('''
    
          ''' * 50)
          print('welcome to Micro Text, a simple text editor \n type "sys.exit" to exit this app \n (c)2021')
          while True:
            y = input()
            if y == 'sys.exit':
              print('thanks for using Micro Text\n see you next time!')
              break
        elif app == '2':
            print('''
            ''' * 50)
            print('welcome to Platinum Browser, a simple browser\n type "sys.exit" to exit this app \n (c)2021')
            while True:
              a = input('search:')
              if a == 'sys.exit':
                print('thanks for using Platinum Browser!\n see you next time')
                break
              else:
                print('goto: https://google.com/search?q='+a)
        elif app == '3':
            print('''
      
            ''' * 50)
            print('welcome to Calculator, a simple calculator\n type "sys.exit" to exit this app \n (c)2021')
            # Program make a simple calculator

            # This function adds two numbers
            def add(x, y):
              return x + y

          # This function subtracts two numbers
            def subtract(x, y):
              return x - y

          # This function multiplies two numbers
            def multiply(x, y):
              return x * y

          # This function divides two numbers
            def divide(x, y):
              return x / y


            print("Select operation.")
            print("1.Add")
            print("2.Subtract")
            print("3.Multiply")
            print("4.Divide")
            print("5.Exit")
            while True:
              # Take input from the user
              choice = input("Enter choice(1/2/3/4/5): ")

              # Check if choice is one of the four options
              if choice in ('1', '2', '3', '4','5'):
                if choice == '5':
                  break
                else: 
                  num1 = float(input("Enter first number: "))
                  num2 = float(input("Enter second number: "))

                if choice == '1':
                  print(num1, "+", num2, "=", add(num1, num2))

                elif choice == '2':
                  print(num1, "-", num2, "=", subtract(num1, num2))

                elif choice == '3':
                  print(num1, "*", num2, "=", multiply(num1, num2))

                elif choice == '4':
                  print(num1, "/", num2, "=", divide(num1, num2))
                elif choice == '6':
                  break
                else:
                  print("Invalid Input")
        elif app == '4':
          print('goto: https://colab.research.google.com/drive/14JMxZbH0reUuJBRCBCMjrntDvHkKN4US')
        elif app == '5':
          print('goto: https://colab.research.google.com/drive/1WD60jEsfEcyGL9zmS6EqTWhlnfeGW48Z')
        elif app == '6':
          from time import sleep
          m = 0
          print("""**************************
          Welcome To FASTIMER®
          **************************""")
          while True:
            try:
              countdown = int(input("How many seconds:  "))
              break
            except ValueError:
              print("ERROR, TRY AGAIN")
          original = countdown
          while countdown >= 60:
            countdown -= 60
            m += 1
          for i in range (original,0,-1):
            if m < 0:
              break
            for i in range(countdown,-2,-1):
              if i % 60 == 0:
                m-=1
              if i == 0:
                break
              print(m," minutes and ",i," seconds")
              sleep(1)
            if m < 0:
              break
            for j in range(59,-1,-1):
              if j % 60 == 0:
                m-=1          
              print(m," minutes and ",j," seconds")
              sleep(1)
          print("TIMER FINISHED")
      else:
        print('that\'s not a app')
    elif x == 'version':
      print(ver)
    elif x == 'sh version':
      print('1.8')
    elif x == 'cls':
      print('''
    
      ''' * 50)
    elif x == 'ls':
      print('''
      credits.txt
      liscense.txt
      help.txt
      ''')
    elif x == 'open credits' or x == 'open credits.txt':
      print('''
      DiamondCoder1000 - creator and tester
      ''')
    elif x == 'open license' or x == 'open license.txt':
      print('GNU General Public License v3.0')
    elif x == 'open help' or x == 'open help.txt':
      print('''
    Platinum Shell 1.8 (c) 2021
    
    Type "menu" to open the app menu.
    
    COMMANDS:
    version --- prints the OS version
    sh version --- prints the shell version
    ? --- to get here
    exit --- exits OS
    ls --- lists directories
    open --- opens files
    ''')
    
       
     elif x == 'pip install Guessing_Game':
      print('getting packages...')
      print('000%')
      ti.sleep(1)
      print('025%')
      ti.sleep(1)
      print('075%')
      ti.sleep(3)
      print('100%: DONE: GUESSING_GAME IS INSTALLED. TYPE "open guessing game" TO OPEN.')
      G = True

    elif x == 'pip install Hangman':
      print('getting packages...')
      print('000%')
      ti.sleep(1)
      print('025%')
      ti.sleep(1)
      print('075%')
      ti.sleep(3)
      print('100%: DONE: HANMAN IS INSTALLED. TYPE "open hangman" TO OPEN.')
      H = True
    elif x == 'hangman':
      if H == True:
        hangman_hangman()
      else: 
        print('ERROR<hangman is not installed>')
    
    elif x == 'guessing game':
      if G == True:
        guessing_game()
      else:
        print('ERROR<guessing game is not installed>')
    elif x == 'about':
      print("""
      version: 2.1.0
      (c) 2021 all rights reserved
      Diamondcoder1000
      May 26, 2021
      """)
    else:
      print('that is not a command added to the Platinum Shell 1.8\nUpdates will come soon\n')
while True:
  print('There are 3 systems installed. Which one do you wanna run? Type the number.')
  print('''
  1. Wikipedia search
  2. PlatinumOS
  3. BPL programming
  4. shutdown
  ''')
  i = input("OS: ")
  if i == "2":
    PlatinumOS()
  elif i == "1":
    WikipediaSearch()
  elif i == "4":
    print('Shutting down BIOS...')
    time.sleep(3)
    print('done')
    break
  elif i == "3":
    print("Goto https://colab.research.google.com/drive/11Rmkcml9qsNVe1W8alK2Q56AEkVxNyVo?usp=sharing")
  else:
    print("ERROR: THAT IS NOT A OS AVAILIBLE")
