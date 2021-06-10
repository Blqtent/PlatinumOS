#platinum data START
ver = '1.2.2'
cpu = 40
import time
import math
#platinum data END
print('executing BIOS sequence[exec /BIOS]...')
time.sleep(40/20)
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
  print('Booting PlatinumOS', ver,'...')
  print('cpu speed:', cpu, 'MHz')
  time.sleep(cpu/20)
  print('jumping to kernel...')
  time.sleep(cpu/40)
  print('executing login sequence...')
  time.sleep(cpu/80)
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
  time.sleep(cpu/20)
  print('Platinum shell 1.7')
  print('type "?" for help')
  while True:
    x = input('> ')
    if x == '?':
      print('''
    Platinum Shell 1.7 (c) 2021
    
    Type "menu" to open the app menu.
    
    COMMANDS:
    version --- prints the OS version
    sh version --- prints the shell version
    ? --- to get here
    exit --- exits OS
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
          6: Exit    
        ''')
      if app == '6':
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
      else:
        print('that\'s not a app')
    elif x == 'version':
      print(ver)
    elif x == 'sh version':
      print('1.7')
    elif x == 'cls':
      print('''
    
      ''' * 50)
    elif x == 'files':
      print('''
      boot
      kernel
      ''')
    else:
      print('that is not a command added to the Platinum Shell 1.7\nUpdates will come soon')
while True:
  print('There are 2 systems installed. Which one do you wanna run? Type the number.')
  print('''
  1. Wikipedia search
  2. PlatinumOS
  3. shutdown VM
  ''')
  i = input("OS: ")
  if i == "2":
    PlatinumOS()
  elif i == "1":
    WikipediaSearch()
  elif i == "3":
    print('Shutting down BIOS...')
    time.sleep(3)
    print('done')
    break
  elif i = "4":
    print("Goto https://colab.research.google.com/drive/11Rmkcml9qsNVe1W8alK2Q56AEkVxNyVo?usp=sharing")
  else:
    print("ERROR: THAT IS NOT A OS AVAILIBLE")
