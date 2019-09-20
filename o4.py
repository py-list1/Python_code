d1 = {'a':100,'b':120,'c':100,'d':220,'e':500}
print(d1['a'])

#list => collection of objects
l1 = [ 1,3,4,7,23,'c','qwerty','c',1,2,4,3, 4.5,9.56]
#      ^ ^ ^ ^ ^   ^                             ^
#index 0 1 2 3                                   13

try:
    print(d1['x'])
    print(l1[4])
    print(l1[14])
except IndexError as ex:
    print("Index error occured")
except KeyError as ex:
    print("key error occured")

print("logic continues....")
