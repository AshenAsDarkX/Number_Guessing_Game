import random


#create variables,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
user_name=""
spc=" "
slash="|"
attempt=0
choice="Y"
guess_list=[]

#welcoming message,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
print(spc*30,"WELCOME")


#ask for the choice of user,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
while(choice.upper()=="Y"):
    attempt=0

#ask for the name,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
    while(True):
        user_name= str(input("Please enter your name : "))
        if (len(user_name)>2):
            break
        else:
            print("NAME SHOULD HAVE AT LEAST 3 CHARACTERS!!!")

#game topic and colour mappping,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
    print("\n")
    print(slash*24,"HELLO!",user_name.upper(),"WELCOME TO GAMEINT",slash*24)
    print("Number to guess - XXXX",spc*25,"Colour mapping: ")
    print(spc*52,"1-White ,2-Blue ,3-Red")
    print(spc*52,"4-Yellow ,5-Green ,6-Purple")
    print("\n")

#define the rules,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
    print("RULES!")
    print(spc*2,"1.YOU ONLY HAVE 8 ATTEMPTS")
    print(spc*2,"2.YOU CAN ONLY ENTER 4 NUMBERS\n")

#showing the guidelines to the user,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,    
    print(spc*10,"/////////////GUIDELINES\\\\\\\\\\\\\\\\\\\\\\")
    print("1.If you guessed the correct number in correct position             = 1")
    print("2.If you guessed the correct number but not in the correct position = 0")
    print("3.If you didn't guess the number                                    = -")
    print("4.If you type '0000' the program will terminate")
    print("\n")

#creating the random code,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
    rndm_code=random.sample(range(1,7),4)
    #print("showing the random number for testing",rndm_code)

#the main game loop,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
    for i in range (8) :
        user_win=False
        attempt=attempt+1
        guess_wrong=True
        list.clear(guess_list)
        #print(i)
        #print(rndm_code)

#asking four inputs from user,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,        
        while(guess_wrong):
            guess=str(input("Please enter your four guesses : "))
            print("\n")

#checking weather length of user input is correct or not,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
            if(len(guess)==4):
                for y in range (4):
                    if (int(guess[y])<=6 and y==3):
                        guess_wrong=False
                        
                    elif int(guess[y])>6:
                        print("PLEASE ENTER VALID NUMBER! (-_-)\n")
                        break

            else:
                print("PLEASE ENTER FOUR NUMBERS! [-_-]\n")

#enter the condition of 0000,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
        if (guess=="0000"):
            print("Let's play another time then (*_-) ,,,")
            exit()

#adding the four inputs of user in to the guess_list,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,        
        #print(rndm_code)
        for x in guess:
            guess_list.append(int(x))
        #print(spc*20,guess_list)
        guess_list2=[]
        rndm_code2=[]
        marklist=[]

#mark weather user guesses == 1,0,-,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
        for v in range (len(rndm_code)):
            if guess_list[v] == rndm_code[v]:
                marklist.append("1")
            else:
                guess_list2.append(guess_list[v])
                rndm_code2.append(rndm_code[v])
            #print(guess_list2)
            #print(rndm_code2)
        if(len(rndm_code2)>0):
            guess_list3=[]
            for w in range(len(rndm_code2)):
                if guess_list2[w] in rndm_code2:
                    marklist.append("0")
                else:
                    marklist.append("-")

#showing the resukts to the user,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,                    
        else:
            print("CONGRATS!!!!! YOU HAVE GUESSED THE NUMBER IN", attempt," ATTEMPTS....")
            user_win=True
            break
             
        print("ATTEMPTS",spc*6,"YOUR GUESS",spc*6,"RESULT")
        print("--------",spc*6,"----------",spc*6,"------")

        
        print(spc*1,attempt,spc*11,(" ".join(str(x) for x in guess_list)),spc*9,("  ".join(marklist)),"\n")
        

    if(user_win==False):
        print("Looser!! You didn't guess the number corretly in your attempts")
        print("The random code was",rndm_code,"(^_^)\n")
        

#asking the user is he playing again or not,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,    
    choice=str(input("Do you want to play again(Y/N)(*_-)?   "))
    print("\n")
    if choice.upper() == "Y" :
        i=0
    else:
        print("Let's play another time then (*_*) ,,,\n")
        exit()
#ending the gamme,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,    
else:
    print("Let's play another time then *_* ,,,")
    exit()
