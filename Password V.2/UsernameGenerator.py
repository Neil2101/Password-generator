def passwordgenerator():
  try:
    from random import shuffle,randint
    password = []
    letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",
                "A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","T","V","W","X","Y","Z"]

    numbers = ['1','2','3','4','5','6','7','8','9','0']

    numletters = input("how much letters do you want? Answer: ")

    numnumbers = input("how much numbers do you want? Answer: ")

    for j in range(0,int(numnumbers)):
      a = numbers[randint(0,9)]
      password.append(a)
    for k in range(0,int(numletters)):
      b = letters[randint(0,len(letters)-1)]
      password.append(b)

    shuffle(password)
    Password = ''.join(password)
    with open('Pythonstorage1.txt', "a") as myfile:
        myfile.write(str(Password)+', ')
    print(Password)
  except Exception as E:
    print("sorry, something went wrong: " + str(E))
  finally:
      myfile.close()

def usernamegenerator():
  try:
    from random import randint,shuffle
    from nltk.corpus import words
    username = []
    word_list = words.words()
    numbers = ['1','2','3','4','5','6','7','8','9','0']
    shuffle(word_list)
    hmuch = int(input("Hi, how much numbers do you want? Answer: ").strip())
    for i in range(0,hmuch):
      username.append(numbers[randint(0,len(numbers)-1)])
    for j in range(0,randint(1,2)):
      username.append(word_list[randint(0,len(word_list)-1)])
    Username = ''.join(username)

    with open('Usernamepassword.txt', "a") as myfile1:
      myfile.write(str(Username)+', ')
    print(Username)
    passwordgenerator()
  except Exception as E:
    print("sorry, something went wrong: " + str(E))
  finally:
    myfile1.close()