#list => collection of objects
l1 = [ 1,3,4,7,23,'c','qwerty','c',1,2,4,3, 4.5,9.56]
#      ^ ^ ^ ^ ^   ^                             ^
#index 0 1 2 3                                   13

print(l1[4])
print(l1[13])

l1[5] = "Tuesday"
l1[10] = 555
print(l1)
#tuple
t1 = (23,45,56,78)
print(t1[0])
#t1[2] = 200
#dictionary = > collection of key value pairs
d1 = {'a':100,'b':120,'c':100,'d':220,'e':500,'f':l1}
print(d1['a'])
#print(d1['x'])
#set
s1= set(l1)
print(s1)
l2=[45,67,23]
s2=set(l2)
print(s2)
print(s1.intersection(s2))
print(s1.union(s2))
















