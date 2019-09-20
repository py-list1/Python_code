#list => collection of objects
l1 = [ 1,3,4,7,23,'c','qwerty','c',1,2,4,3, 4.5,9.56]
#      ^ ^ ^ ^ ^   ^                             ^
#index 0 1 2 3                                   13

try:
    print(l1[4])
    print(l1[14])
except Exception as exp:
    print("index error occured")

print("logic continues...")
