import random

list = ["Guu","Choki","paa"]

print ("Janken...")
print ("type Guu or Choki or Paa")

user = input ('>>>')

pc = random.choice(list)

win = 'You win!! (T_T)'
lose = 'You lose!! (^o^)'
draw = 'Draw (-_-)'

try:
   if user == pc:
       judge = draw
        
   else:
       if user == "Guu":
           if pc == "Choki":
               judge = win
           else:
               judge = lose

       elif user == "Choki":
           if pc == "Paa":
               judge = win
           else:
                judge = lose

       elif user == "Paa":
           if pc == "Guu":
               judge = win
           else:
               judge = lose
             
   print("You chose %s" % user)
   print("I chose %s" % pc)
   print("Result: %s" % judge)

except:
   print("type Guu or Choki or Paa")