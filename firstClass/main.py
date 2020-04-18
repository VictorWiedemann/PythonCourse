import random
import sys

print ("hello world")
print ('what is your name')
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




def hello(text):
    print("test", end='')
    print('howdy! ' + text)
    print ('world')
    #hello() RECURSION HAR HAR HAR

hello("test")
