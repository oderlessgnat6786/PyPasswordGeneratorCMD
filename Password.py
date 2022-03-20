import random
import time
import os
import string
exampleFile = "SUSSYBAKAAMOGUS.txt"
from RandomStringGenPGEN import *

p_dir = "C:\\PyPassGenPasswords"


if not os.path.exists(p_dir):
    os.makedirs(p_dir)


os.chdir(p_dir)


#os.chdir(os.path.dirname(os.path.abspath("C:\\Users\\NITHIN\\Documents\\PyPassGenPasswords\\")))
print("Passwords saved at :- ",os.getcwd())

#print('Say "Exit" to Exit (Any Progress will not be Saved)')

Saves = []

def shuffle_string(s: str) -> str: 
    L = list(s) 
    random.shuffle(L)  # shuffles in place, None output 
    return "".join(L)

Exit = False
Limit = 250

Password = generateString(15)
LocalSeed = "nil"

Alphabet = ABCabcABCabc(generateString(26))
Numerals = "1234567890"
Symbols = "_@._@..@__@._@..@__@._@..@_"

UnicodeChar = [Alphabet,Numerals,Symbols]

Seeds = []

Seed = ""

Passwords = []

def GenerateSeeds():   
    for x in range(5):
        LocalSeed = shuffle_string(Password)
        Seeds.append(LocalSeed)
    print("Code.s+5")

def ChooseSeed():
    for z in range(2):
        Seed = random.choice(Seeds)
    print("Code.sDone")
    

def charFind(c,s):
    for pos,char in enumerate(s):
        if(char == c):
            return pos

def file_format(string):
   sussybaka = charFind(".",string)
   antecedent = sussybaka
   consequent = len(string)
   
   formattedText = string[antecedent:consequent]
   return formattedText

def searchPassword(listt, platform):
    for i in range(len(listt)):
        if listt[i] == platform:
            return True
    return False


#List


    

        
GenerateSeeds()
ChooseSeed()
while Exit == False:
    
     files = [f for f in os.listdir('.') if os.path.isfile(f)]
     for i in files:
         if files == 0:
             intro = open("Introduction.txt","w")
             intro.write("PyPasswordGenerator v1.0 Line - Version")
             intro.close()
         else:

             fileFormat = file_format(i)
             
             if fileFormat == ".txt":
                cutlength = len(i) - 4
                FileText = i[0:cutlength]
                Passwords.append(FileText)
        
     def CreationMode(Password,Limit):

        #Limit

        print("Enter Your Maximum Password Limit")
        Text = int(input("0 - Default | Maximum Limit - 250 :::: -->> "))
        
        if Text == 0:
            Limit = 250
            
        elif Text < 250:
            Limit = Text
            
        elif Text > 250:
            Limit = 250
            
        print("Limit = ",Limit)


        #Symbol

        #Number

        print(" ")

        print("Continue...")
   
        Unicode = input("0 - Agree | Other Keys - Decline ")
        if Unicode == "0":
            for i in range(1):
                Result = Password
           
                
                randChar = random.choice(UnicodeChar)
               # print(randChar)
                randType = random.randint(1,10)
              #  print(randType)
              #  randSamp = Seed.join()

                
                Password = Result.join(random.sample(randChar, randType))
            #    print(Password, " | No. Of Characters = ", len(Password))

            PassLen = len(Password)
            
            
            
            if PassLen > Limit:
                print("Code.>Max")
                xa = Limit + 1
                Password = Password[1:xa]
                time.sleep(2)
                print("Finished Passcode")



            
            print(Password, " = ", len(Password))
            print("")

            print("----- INFO -----")
            
            Name = "Untitled"
            askName = input("Enter Password Name --> ")
            Name = askName
            print("v1.0")

            tableofFormat = [Name,".txt"]
            text = "".join(tableofFormat)

            #passomat = [Name," = ",Password]
            passomat = [Password]

            passText = "".join(passomat)
            
            nt = open(text, "w")
            nt.write(passText)
            nt.close()

            print("")
            print("Password saved Successfully")
            print("")

            
        else:
            quit()

     def ViewingMode():
         print("Type a Password Name to Continue (Capitals Must be Equal As well) :--")
         askNamePass = input("")
         if searchPassword(Passwords,askNamePass):
             FileNameTwo = [askNamePass,".txt"]
             FileName = "".join(FileNameTwo)
             xp = open(FileName)
             ReadInfo(askNamePass,xp)
             xp.close()
         else:
             print("Couldn't find a Password like that / No Passwords Exist.")

     def DeletePass():
         print("Type a Password Name to Continue (Capitals Must be Equal As well) :--")
         askNamePass = input("")
         if searchPassword(Passwords,askNamePass):
              FileNameTwo = [askNamePass,".txt"]
              FileName = "".join(FileNameTwo)
              xp = open(FileName)
              print("Do you really want to Delete This Password?")
              askS = input("0 =  Yes, Im sure | Other Keys = No, i'll keep this password -->> ")
              if askS == "0":
                  
                  ReadInfo(askNamePass,xp)
                  xp.close()
                  os.remove(FileName)
                  print("Successfully removed password :(")
              else:
                  print(" ")
                  close()
         elif askNamePass == "Introduction.txt":
            print("Error: Couldn't Delete File Introduction.")
         else:
             print("Couldn't find a Password like that / No Passwords Exist.")

     print("Choose a option to continue")
     ask0 = input("1 = View Passwords | 2 = Create a Password | 3 = Delete Password | 4 = Close Application -->> ")
     if ask0 == "1":
        print(Passwords," :- Passwords")
        ViewingMode()
     elif ask0 == "2":
        CreationMode(Password,Limit)
     elif ask0 == "3":
        print(Passwords," :- Passwords")
        DeletePass() 
     elif ask0 == "4":
        break
        
     for zinc in Passwords:
         Passwords.clear()
quit()
