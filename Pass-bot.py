#!/usr/bin/env python3

from random import shuffle,randint,sample
import string
from zipfile import ZipFile
from os import path,remove
from time import sleep


def satisfier(a):
    fl1,fl2,fl3,fl4=0,0,0,0
    for i in a:
        if i.isalnum()==False:
            fl1+=1
        if i.isdigit()==True:
            fl2+=1
        if i.isupper()==True:
            fl3+=1
        if i.islower()==True:
            fl4+=1
    if fl1>0 and fl2>0 and fl3>0 and fl4>0:
        return True
    else:
        return False    

L2 = list(string.ascii_uppercase)+list(string.ascii_lowercase)+list(string.digits)+list(string.punctuation)

L2.remove("\\")
L2.remove('"')
L2.remove("'")
L2.remove(".")
L1 = L2[:]


resp = input('''1) Get password
2) Get random 6 digit key code
3) Create a new password database

#If you are running this script for the first time, go with option 3 
#If you are going for option 1 please make sure you copied your keyfile in this directory

Response(1,2,3): ''')

print()

if resp=="1":
    if path.exists("key.txt")==False:
        print("The key file does not exist. Please copy the key from your SECURE location to this directory")
        sleep(10)
        exit()
    D2 = {}
    file_enc = open("key.txt")
    L3 = list(file_enc.read().strip())
    for i in range(len(L1)):
        D2[L3[i]]=L1[i]
    file_enc.close()

    file_code = input("File code: ")
    code = int(input("Password code: "))
    
    file = open("passlist"+file_code+".txt")
    L = file.readlines()
    file.close()
    enc_pass = L[code-1].strip()
    unenc_pass=''
    for i in enc_pass:
        if i not in D2:
            unenc_pass+=i
        else:
            unenc_pass+=D2[i]
    
    print("Your password is: ")
    print()
    print(unenc_pass)
    print()
    
    resp4 = input('''Would you like to delete the key copy present in this folder?
Please do make sure you have a copy already present in the secure location as 
once the key is deleted, you will NOT be able to retrieve your passwords.
Type "yes" in all capital letters to delete the key. [YES/n]: ''')
    if (resp4=='YES'):
        remove("key.txt")
        print("Key deleted (hope you kept a copy.)")
        
    else:
        print("Key not deleted.")


elif resp=="2":
    x = randint(100000,999999)

    print("Your randomly generated code is:")
    print(x)
    print("Since this key is just a random 6 digit code, you are free to think of one yourself")



elif resp=="3":
    while True:
        resp3 = input("Are you sure you want to generate a new database and key? [y/n]: ")
        if resp3 == 'y' or resp3 == 'Y':
            shuffle(L2)
            enc_file = open("key.txt",'w')
            for i in L2:
                enc_file.write(i)
            enc_file.close()    
            
            D1 = {}
            
            for i in range(len(L1)):
                D1[L1[i]]=L2[i]

            print("New key created ")
            print()
            for i in L2:
                print(i,end='')
            print()
            print()
             
            sets=input("Number of character sets [Default => 4] (minimum = 1): ")
            if sets == '':
                sets = 4
            else:
                sets = int(sets)

            chars=input("Number of characters per set: [Default => 10] (minimum = 4): ")
            if chars == '':
                chars = 10
            else:
                chars = int(chars)


            print("Generating password database:\nCharacter sets:",str(sets),"\nCharacters per set:",str(chars))
            print()

            for z in range(1,101):
                z=str(z)
                z="0"*(2-len(z))+z
                name ="passlist"+z+".txt"
                file = open(name,'w')
                file_len = []

                while len(file_len) < 10**4:
                    s=''
                    while len(s)<(chars*sets)+sets-1:
                        x = sample(L1,chars)
                        for i in x:
                            s+=i
                        s+=' '
                    s=s[:-1]
                    if satisfier(s):
                        s2=''
                        for j in s:
                            if j not in D1:
                                s2+=j
                            else:
                                s2+=D1[j]
                        file.write(s2)
                        file.write('\n')
                    else:
                        continue

                    file.close()

                    with open(name) as file: 
                        file_len = file.readlines()

                    file = open(name,'a')
                    
                print("Passlist"+str(z)+" created, "+str(100-int(z))+" remaining.")
            print()
            print("Database created.")
            while True:    
                compy=input('''Do you want to save a compressed copy (zip) of this database?
This may decrease security as someone could get a copy of your unique database.
Proceed? [y/n] ''')
                if compy == 'y' or compy=='Y':
                    zippy = ZipFile("Database.zip",'w')
                    for i in range(1,101):
                        i=str(i)
                        i="0"*(2-len(i))+i
                        zippy.write("passlist"+str(i)+".txt")
                    zippy.write("key.txt")
                    zippy.close()
                    print()
                    print('''Database backup has been stored as a compressed zip file in this directory.

Please copy/move this file to a SECURE location.''')
                    break
                elif compy == 'n' or compy == 'N':
                    print()
                    print("No backup of database created.")
                    break
                else:
                    print()
                    print("Invalid input")
                    continue
            print("Please move your key to a SECURE location for security purposes:)")    
            break


        elif resp3=='n' or resp3=='N':
            print("Cancelling process.")
            break
        
        else:
            print("Invalid input")

else:
    print("Please choose valid option!")

print("This window will automatically close in 100 seconds.")
sleep(100)
