import random

    #Open a file named numbersmake.txt.
outfile = open('a.txt', 'w')
w=50
outfile.write(str(w)+"\n")
    #Produce the numbers
for count in range(1,51):
        #Get a random number
    p=count
    num=random.randint(60,100)
    q=random.randint(160,220)
    r=random.randint(2,6)
    outfile.write(str(p)+" "+str(num)+" "+str(q)+" "+str(r)+"\n")

    #Write 12 random intergers in the range of 1-100 on one line
    #to the file.
    

    #Close the file.
outfile.close()