'''
Random module
it is a buiilt in module in python
it helps to genetate random values
it is best to get OTP generation,Story Generation,Games(Rock Paper Scissiors)
#random  number generation
import random
#random numbet generation -->OTP
a = random.randint(1000,9999)
print(a)
for i in range(5):
    print(random.randint(1000,9999))
#OPT Generation
import random,time
#random number generation -->OTP
#time module helps to use time functions
a = random.randint(1000,9999)
#print(a)
for i in range(5):
    time.sleep(2) #sleep-- it will wait (always give in seconds) helps for a waiting period
    print(random.randint(1000,9999))
    #time.sleep(2)
    
import random,time
#Playing a game(Rock Paper Scissors)
#Two players -->games-->
player1 =input("Enter one of these -->Rock,Paper,Scissors:").lower().strip()
player2=random.choice(['Rock','Paper','Scissors']).lower()
#print(player1)
print(player2)
if player1 =="rock" and player2 =="paper":
    print("Player2 Won...")
elif player1 == "paper" and player2 =="scissors":
    print("Player2 Won...")
elif player1 =="scissors" and player2 =="rock":
    print("Player2 Won...")
elif player1==player2:
    print("Tie!")
else:
    print("player1 won")

#TASK: Get the score for each user and declare the winner
#paly the game for 10 times -->(push in github and share it (tasks  folder in git)
#Task 2 -->Give user a choice -->RPS(1) /NG (number gusseing ) (2)/3 (Study) /any number
#no choice only 1,2,3 -->Function

import random,time
#story telling
when = ['A long back ago','Once upon a time','Few Years ago']
who = ['Devara','King in the france','Barbie Queen']
what =['A magical Sword','Powerful Hammer','Unlimited Arrows']
where = ['Far in the Galaxy','In a Fantasy World','End of  ocean','In India']
how = ['War started','Both fought for 15days','Sad Ending']
# to create a story -->link when to what or who to how....
print(random.choice(when)+" "+random.choice(who)+" "+random.choice(where)" "+random.choice(what)" "+random.choice(how))

#Bussiness Card generation --->name,emailid,mobilenumber,websitelink,address
#segno-->pip install segno
import segno
print(dir(segno))
from segno import helpers
qr = helpers.make_mecard(name="Jahnavi",
                         email="jahnavisaidevi@gmail.com",
                         phone ="+91 8367510733",
                         url="https://www.linkedin.com/in/jahnavi-devi-078999289/",
                         city="Visakapatnam",
                         birthday="2005/04/12") # date of birth (YYYY/MM/DD)
print(qr)
qr.save("mycard.png",scale=10)


#Now its your turn --->explore modules (instaloder package -->instagram)
insatgram,youtube,email automtion....
'''
#Build a Virtual Assistant using Python-->Virtual Environment
#Speak,Respond back,Greet you,Make a Conversation,Open Browser,
#Locate Google Maps,tell a story,Play a game.....
#POP-->Functions,Control Block...
'''




