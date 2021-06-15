#Jack Savini
#CS 174
#I only commented #5, since commenting #3&4 would be superfluous.


#1) Do an example. A = [0, 5, 2, 11, 7, 9, 3].

#A=[0,5,2,11,7,9,3]
#B=[0,0,0,0,0,0,0,0,0,0,0,0]
#B=[1,0,1,1,0,1,0,1,0,1,0,1]
#A=[0,2,3,5,7,9,11]

#2) Give an Big-O analysis of this algorithm. That is, count how many steps
#(assuming A contains n elements), and give the Big-O version.

#Because the code is made up of for loops, none of which are contained within
#another for loop, the big O notation is O(n). 



'''
#3) Code it. 

A = [0,5,2,11,7,9,3]
B = []
final_A = []

size = len(A)

maxx = A[0]

for i in range(1, size):
    if A[i]>maxx:
        maxx = A[i]

for j in range(0,maxx + 1):
    B.append(0)

for k in A:
    B[k] = 1

print(B)

for l in A:
    final_A.append(B.index(1))
    B[B.index(1)]=0

print(final_A)
'''
'''
#4) Modify it to handle arrays A whose smallest element is not 0.

A = [-6,-8,-1,0,5,2,11, -120000,7,9,3]
B = []
final_A = []

size = len(A)

maxx = A[0]
minn = A[0]

for i in range(1, size):
    if A[i]>maxx:
        maxx = A[i]

for p in range(1, size):
    if A[p]<minn:
        minn = A[p]

for j in range(maxx + 1 - minn):
    B.append(0)

for k in A:
    B[k-minn] = 1

print(B)

for l in A:
    final_A.append(B.index(1)+minn)
    B[B.index(1)]=0

print(final_A)
'''
#5) Modify it to handle sets that have duplicates.

#here's the setup for my lists, feel free to modify A to your hearts content
A = [-1200,5,5,-30,-66,7,8,17,-2,-666,33,135,222,8,0,0,12,14,14,14,14,-1201]
B = []
final_A = []

#just making a variable for easy access to the size of A
size = len(A)

#These set up variables maxx and minn, which contain the maximum value
#and minimum value within A respectively
maxx = A[0]
minn = A[0]

#This loop finds the max # in A
for i in range(1, size):
    if A[i]>maxx:
        maxx = A[i]

#This loop finds the min # in A
for p in range(1, size):
    if A[p]<minn:
        minn = A[p]

#This loop adds all the 0s to list B
for j in range(maxx - minn + 1):
    B.append(0)

#This loop adds numbers in the B list whose position corresponds to their value
#in A, and whose value correponds to the number of times it is in the list.


for k in A:
    B[k-minn] += 1

#Setting up some more variables for esy access, as you do
sizeB = len(B)

#Uncomment this if you wish to gaze upon the brilliance of list B.
#print(B)

#This loop adds elements to the final list, the number of times added
#corresponding to the value in B, and value determined by position in B
for l in range(sizeB):
    while B[l] > 0:
        final_A.append(B.index(B[l])+minn)
        B[l]-=1

#Print is self explanatory
print(final_A)

#Tadaaaaaa *bow* *bow* *curtain closes*
