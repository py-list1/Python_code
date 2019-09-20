l1 = [ 1,3,4,7,23,'c','qwerty','c',1,2,4,3, 4.5,9.56]

for i in l1:
    print(i)

range(0,10,1) # > [0,1,2,3,4,5,6,7,8,9]
range(0,10,2) # > [0,2,4,6,8]
range(0,1000,100) # > [0,100,200,300...900]

for i in range(0,10,1):
    print(i)

range(5) #> [0,1,2,3,4]

#accept a number print even numbers till that number
n = int(input("enter number:"))
for i in range(0,n,2):
    print(i)
c= 0
while c < n:
    print(c)
    c = c+2
c1 = 0
while c1<n:
    if c1%2 == 0:
        print(c1)
    c1 = c1+1

