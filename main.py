from PasswordGenerator import passwordgenerator
from UsernameGenerator import usernamegenerator
def menu():
  while 1 == 1
    cmd = input("type 1 to make a password, type 2 to make a username and a password, EXIT to exit")
    if cmd == '1':
      passwordgenerator()
    elif cmd == '2':
      usernamegenerator()
    elif cmd == 'EXIT':
      break
    else:
      print('Sry, I didn\'understand what do you meant. please try again')