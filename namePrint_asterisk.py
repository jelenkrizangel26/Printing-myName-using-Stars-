#ASSIGNMENT 1
#Create a program that will print your nickname using only asterisk character(*). 
#Your program should be uploaded to github before 11:59 PM.



#Introduction
print("Hello, my nickname is...\n")


#make a pattern JEL from Jelen
str1 = "JEL"
letter_J = [[" " for i in range(6)] for j in range(6)]
letter_E = [[" " for i in range(6)] for j in range(6)]
letter_L = [[" " for i in range(6)] for j in range(6)]

#code for N
for row in range(6):
    for col in range(6):
        if col==0 or col==6 or row==col:
            letter_J[row][col]= "*"

#code for E
for row in range(6):
    for col in range(6):
        if col==0 or ((row==0 or row==3 or row==6) and (col>0)):
            letter_E[row][col]="*"

#code for L
for row in range(6):
    for col in range(6):
        if col==0 or row==6 and col>0:
            letter_L[row][col]="*"

for row in range(6):
    for col in range(6):
        print(letter_J[row][col],end="")
    for col in range(6):
        print(letter_E[row][col],end="")
    for col in range(6):
        print(letter_L[row][col],end="")
print()