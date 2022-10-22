#ASSIGNMENT 1
#Create a program that will print your nickname using only asterisk character(*). 
#Your program should be uploaded to github before 11:59 PM.

#First indicate the number of lines(height) and width of the pattern.
height = 8
width = (2 * height) - 1

#Introduction
print("Hello, my nickname is...\n")

#make a pattern JEL from Jelen
def printJ() :
     
    for i in range(0,height) :
        for j in range(0,height) :
            if ( i == height - 1 and (j > 0 and j < height - 1) ):
                print("*",end="")
            elif ( (j == height - 1 and i != height - 1) or (i > (height // 2) - 1 and j == 0 and i != height - 1) ) :
                print("*",end="")
            else :
                print(end=" ")
        print()

printJ()
