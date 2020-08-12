# STILL A WORK IN PROGRESS - Austin K 
import os, sys
import subprocess
import random
from Crypto.Cipher import AES
from random import choice
 # Brute Force AES Key Cracker File
 # Encryption:
Data = open('Data.txt','r')
key = b'WmZq4t7w!z%C*F-J@NcRfUjXn2r5u8x/'
cipher = AES.new(key,AES.MODE_EAX)
nonce = cipher.nonce
ciphertext, tag = cipher.encrypt_and_digest(Data)
    # Decryption:
    # Brute Force Cycle Attempt Function
path = 'Outputfile.txt'
list = 'abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()/?":;.>,<{][}+=-_`|\~'
trys = 1000000000
length = 32
new = open(path, 'w')
print(new)
for i in range (0 , trys)   :
  seg1 = "b'"
  seg2 = "'"
            #Remember to add random.choice() to A in order to set the correct amount of random
            #variable searches based on your grep search
            #New instances must be based on the length of the password searched for
  A = random.choice(list), random.choice(list), random.choice(list), random.choice(list), random.choice(list), random.choice(list), random.choice(list), random.choice(list), random.choice(list), random.choice(list), random.choice(list) ,random.choice(list),random.choice(list), random.choice(list), random.choice(list), random.choice(list), random.choice(list), random.choice(list), random.choice(list), random.choice(list), random.choice(list), random.choice(list), random.choice(list), random.choice(list), random.choice(list), random.choice(list),random.choice(list), random.choice(list), random.choice(list), random.choice(list), random.choice(list), random.choice(list)
  B = "".join(A)
  key = B
  key = B[:0] + seg1
  key = B[:33] + seg2
            # ^ Joining all segments -- DEPENDS ON LENGTH for 256 = 32 random.choice()
  f = open("Outputfile.txt", "a")
  print("Try:",i, "Out of:", trys, B, file=f)
  # ^ Printing the output & writing to Outputfile

  cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
  plaintext = cipher.decrypt(ciphertext)

  try:
    cipher.verify(tag)
    print("The message is authentic", plaintext)

  except ValueError:
    print("Key incorrect or message corrupted")
    f.close()
    i += 1
