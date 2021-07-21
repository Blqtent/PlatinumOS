#some game functions
def hangman_hangman():
  import random
  import time

  # Initial Steps to invite in the game:
  print("\nWelcome to Hangman game by DataFlair\n")
  name = input("Enter your name: ")
  print("Hello " + name + "! Best of Luck!")
  time.sleep(2)
  print("The game is about to start!\n Let's play Hangman!")
  time.sleep(3)
  def main():
    global count
    global display
    global word
    global already_guessed
    global length
    global play_game
    words_to_guess = ["january","border","image","film","promise","kids","lungs","doll","rhyme","damage","plants"]
    word = random.choice(words_to_guess)
    length = len(word)
    count = 0
    display = '_' * length
    already_guessed = []
    play_game = ""
    # A loop to re-execute the game when the first round ends:

  def play_loop():
    global play_game
    play_game = input("Do You want to play again? y = yes, n = no \n")
    while play_game not in ["y", "n","Y","N"]:
        play_game = input("Do You want to play again? y = yes, n = no \n")
    if play_game == "y":
        main()
    elif play_game == "n":
        print("Thanks For Playing! We expect you back again!")
        exit()
  # Initializing all the conditions required for the game:
  def hangman():
    global count
    global display
    global word
    global already_guessed
    global play_game
    limit = 5
    guess = input("This is the Hangman Word: " + display + " Enter your guess: \n")
    guess = guess.strip()
    if len(guess.strip()) == 0 or len(guess.strip()) >= 2 or guess <= "9":
        print("Invalid Input, Try a letter\n")
        hangman()
    elif guess in word:
        already_guessed.extend([guess])
        index = word.find(guess)
        word = word[:index] + "_" + word[index + 1:]
        display = display[:index] + guess + display[index + 1:]
        print(display + "\n")

    elif guess in already_guessed:
        print("Try another letter.\n")

    else:
        count += 1

        if count == 1:
            time.sleep(1)
            print("   _____ \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess. " + str(limit - count) + " guesses remaining\n")

        elif count == 2:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess. " + str(limit - count) + " guesses remaining\n")

        elif count == 3:
           time.sleep(1)
           print("   _____ \n"
                 "  |     | \n"
                 "  |     |\n"
                 "  |     | \n"
                 "  |      \n"
                 "  |      \n"
                 "  |      \n"
                 "__|__\n")
           print("Wrong guess. " + str(limit - count) + " guesses remaining\n")

        elif count == 4:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess. " + str(limit - count) + " last guess remaining\n")

        elif count == 5:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |    /|\ \n"
                  "  |    / \ \n"
                  "__|__\n")
            print("Wrong guess. You are hanged!!!\n")
            print("The word was:",already_guessed,word)
            play_loop()

    if word == '_' * length:
        print("Congrats! You have guessed the word correctly!")
        play_loop()

    elif count != limit:
        hangman()


  main()

  hangman()

def guessing_game():
  import random
  number = random.randint(0,100)
  tries = 1
  done = False
  print("this is the number guessing game. enter a guess and see if you're right!")
  while True:
    guess = int(input("enter a guess"))
    if guess == number:
      done == True
      print("you won!")
      break
    else:
      tries += 1
      if guess > number:
        print("too large")
      else: 
        print("too small")
      if done == True:
        break
  print(f"you needed {tries} tries!")
#start of the os :)
ver = '3.1.0'
cpu = 40
import time
import math
print("SimpleVM Box")
time.sleep(3)
print('PlatinumBIOS (c) July 2021')
time.sleep(2)
print('locating bootloader...')
time.sleep(3)
print('done')
def WikipediaSearch():
  print("Booting search...")
  time.sleep(cpu/10)
  print('welcome, type "exit" to shutdown the system.\ntype your search term:')
  while True:
    y = input('')
    if y == "exit":
      print('going back to boot menu')
      break
    else:
      print("goto https://en.wikipedia.org/wiki/"+y)
def PlatinumOS():
  G = False
  H = True
  apps = ["MicroText.app","Time.app","Browse.app","Calc.app", "APL.app", "SPL.app", "Calender.app"]
  print('')
  print('Booting PlatinumOS', ver,'...')
  print("CPU: SimpleVM Box")
  print('cpu speed:', cpu, 'MHz')
  time.sleep(cpu/40)
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
  print('Platinum shell 1.9')
  print('type "?" for help')
  while True:
    x = input('>')
    if x == '?':
      print('''
    Platinum Shell 2.0 (c) 2021
    
    Type the name of the app to open the app.
    
    COMMANDS:
    version --- prints the OS version
    sh version --- prints the shell version
    ? --- to get here
    exit --- exits OS
    ls --- lists directories
    open --- opens files
    apps --- lists all the apps
    about --- info about the OS
    pip install --- install an app
    pip --- list the apps available for download
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
    
    elif x == 'MicroText.app':
          print('welcome to Micro Text, a simple text editor \n type "sys.exit" to exit this app \n (c)2021')
          while True:
            y = input()
            if y == 'sys.exit':
              print('thanks for using Micro Text.')
              break
    elif x == 'Browse.app':
            print('welcome to Platinum Browser, a simple browser\n type "sys.exit" to exit this app \n (c)2021')
            while True:
              a = input('search:')
              if a == 'sys.exit':
                print('thanks for using Platinum Browser!\n see you next time')
                break
              else:
                print('goto: https://google.com/search?q='+a)
    elif x == 'Calc.app':
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
    elif x == 'APL.app':
          print('goto: https://colab.research.google.com/drive/14JMxZbH0reUuJBRCBCMjrntDvHkKN4US?usp=sharing')
    elif x == 'SPL.app':
          print('goto: https://colab.research.google.com/drive/1WD60jEsfEcyGL9zmS6EqTWhlnfeGW48Z?usp=sharing')
    elif x == 'Time.app':
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
    elif x == 'version':
      print(ver)
    elif x == 'sh version':
      print('1.9')
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
      DiamondCoder1000 - creator
      GDOS creator... I forgot his/her name. sorry - inspiration for boot screen
      DiamondCoder1000 - tester
      Linus Torvalds - inspiration for most commands
      Bill Gates and Paul Allen - For getting me into computer science and coding :)
      My python teacher - I wouldn't even be doing this lol
      Github creator - I wouldn't be here without him/her
      ''')
    elif x == 'open license' or x == 'open license.txt':
      print('GNU General Public License v3.0')
    elif x == 'open help' or x == 'open help.txt':
      print('''
    
    Platinum Shell 2.0 (c) 2021
    
    Type the name of the app to open the app.
    
    COMMANDS:
    version --- prints the OS version
    sh version --- prints the shell version
    ? --- to get here
    exit --- exits OS
    ls --- lists directories
    open --- opens files
    apps --- lists all the apps
    about --- info about the OS
    pip install --- install an app
    pip --- list the apps available for download
    ''')
    
       
    elif x == 'pip install GuessingGame':
      print('getting packages...')
      print('000%')
      ti.sleep(1)
      print('025%')
      ti.sleep(1)
      print('075%')
      ti.sleep(3)
      print('100%: DONE: GUESSING_GAME IS INSTALLED. TYPE "GuessingGame.app" TO OPEN.')
      G = True

    elif x == 'pip install Hangman':
      print('getting packages...')
      print('000%')
      ti.sleep(1)
      print('025%')
      ti.sleep(1)
      print('075%')
      ti.sleep(3)
      print('100%: DONE: HANMAN IS INSTALLED. TYPE "Hangman.app" TO OPEN.')
      H = True
    elif x == 'Hangman.app':
      if H == True:
        hangman_hangman()
      else: 
        print('ERROR<hangman is not installed>')
    
    elif x == 'GuessingGame.app':
      if G == True:
        guessing_game()
      else:
        print('ERROR<guessing game is not installed>')
    elif x == 'about':
      print("""
      version: 3.1.0
      (c) 2021 all rights reserved
      Diamondcoder1000
      July 21, 2021
      """)
    elif x == 'apps':
      for i in apps:
        print(i)
      if H == True:
        print("Hangman.app")
      elif G == True:
        print("GuessingGame.app")
    elif x == 'Calender.app':
      import calendar 

      print("Your Calender\n \n ")

      y = int(input("Enter the Year : "))
      m = int(input("Enter the month : "))
      try:
          mycalender = calendar.month(y , m)
          print("\n", mycalender)
      except IndexError:
          print("Its out of range")
    elif x == "pip":
      print("""
      DOWNLOADABLE APPS
      =================
      Hangman
      GuessingGame
      """)
    else:
      print('that is not a command added to the Platinum Shell 1.9\nUpdates will come soon\n')
while True:
  print('There are 3 operating systems installed to your SimpleVM Box. Which one do you want to run? Type the number.')
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
