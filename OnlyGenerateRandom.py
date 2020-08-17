import os, sys
import random
from random import choice

path = 'Outputfile.txt'
list = 'abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()/?":;.>,<{][}+=-_`|\~'
trys = 10000000
length = 32
new = open(path, 'w')
print(new)
for i in range (0 , trys)  :
            #Remember to add random.choice() to A in order to set the correct amount of random
            #variable searches based on your grep search
            #New instances must be based on the length of the password searched for
  A = random.choice(list), random.choice(list), random.choice(list), random.choice(list), random.choice(list), random.choice(list), random.choice(list), random.choice(list), random.choice(list), random.choice(list), random.choice(list) ,random.choice(list),random.choice(list), random.choice(list), random.choice(list), random.choice(list), random.choice(list), random.choice(list), random.choice(list), random.choice(list), random.choice(list), random.choice(list), random.choice(list), random.choice(list), random.choice(list), random.choice(list),random.choice(list), random.choice(list), random.choice(list), random.choice(list), random.choice(list), random.choice(list)
  B = "".join(A)
      # ^ Joining all segments -- DEPENDS ON LENGTH for 256 = 32 random.choice()
  f = open("Outputfile.txt", "a")
  print("Try:",i, "Out of:", trys, B, file=f)
  # ^ Printing the output & writing to Outputfile
  i += 1
