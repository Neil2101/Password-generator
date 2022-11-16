def passwordgenerator():
  try:
    from random import shuffle,randint
    password = []
    letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",
                "A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","T","V","W","X","Y","Z"]

    numbers = [range(0,9)]

    numletters = input("how much letters do you want? Answer: ")

    numnumbers = input("how much numbers do you want? Answer: ")

    for j in range(0,int(numnumbers)):
      shuffle(letters)
      a = numbers[randint(0,len(numbers)-1)]
      password.append(a)
    for k in range(0,int(numletters)):
      shuffle(numbers)
      b = letters[randint(0,len(letters)-1)]
      password.append(b)

    shuffle(password)
    Password = ''.join(password)
    with open('Pythonstorage.txt', "a") as myfile:
        myfile.write(str(Password)+', ')
    print(Password)
  except Exception as E:
    print("sorry, something went wrong: " + str(E))
  finally:
      myfile.close()
