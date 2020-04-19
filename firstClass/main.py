import random
import sys

# print ("hello world")
# print ('what is your name')
#myName = input()
#if myName:
#    print ('hello you')
#else:
#    print('what are you')


#print ('It is good to meet you, ' + myName)
#print ('The length of your name is: ' + str(len(myName)))
#print ('What is your age?')

#myAge = input()
#print('You will be ' + str(int(myAge) + 1) + ' in a year') 

#
# # spam = ''
# while spam == '':
#     print ('please type your name')
#     spam = input()
#

# spam = 0
# while spam < 5:
#     spam += 1
#     if spam == 4:
#         continue
#     print (spam)

#arr = range(5)
#inputNum = input()
#total = 0
#for i in range(int(inputNum)):
#    total += i + 1
#    print('rolling total: ' + str(total))
#print('total: ' + str(total))


# for i in range(0, 10, -1):
#     print (str(i))

#####################
#Starting section 3 #
#####################

#print(random.randint(1, 10))




# def hello(text):

#     print(testText2)
#     testText2 = "asdfasdf"
#     #hello() RECURSION HAR HAR HAR fails at 999 loops


# testText2 = "test222"
# testText = "test"


# hello(testText)
# print(testText)
# print(testText2)


# def spam():
#     print(eggs)


# eggs = 42
# spam()


# def div42by(divideBy) :
#     try:
#         return 42 / divideBy
#     except:
#         print('Error  here bruh')


# print(div42by(2))
# print(div42by(4))
# print(div42by(0))


# print('How many cats do you have?')
# numCats = input()
# try:
#     if int(numCats) >= 4 :
#         print('That is a lot of cats.')
#     else:
#         print('That is not that many cats')
# except:
#     print('error, error')



print("Hello. What is your name?")
nameText = input()
print("well, " + nameText + ", I am thinking of a number between 1 and 20")
randValue = random.randint(1, 20)
isGuessRight = False
NumGuesses = 0
while(isGuessRight == False):
    print("take a guess")
    try:
        guessedNum = int(input())
    except:
        print("please input a real number")
        continue

    NumGuesses += 1
    if(guessedNum == randValue):
        print("good job, " + nameText + ", You guessed my number in " + str(NumGuesses) + " guesses!")
        break
    elif(NumGuesses == 7):
        print("Nope. The number I was thinking of was " + str(NumGuesses) + ".")
    elif(guessedNum < randValue):
        print("your guessed number is too low")
    elif(guessedNum > randValue):
        print("your guessed number is too high")
    else:
        print("this shouldn't happen")



