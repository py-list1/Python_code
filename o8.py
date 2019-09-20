def function_one(m,n=6):
    print(m)
    print(n)
    for i in range(m):
        print(n)
    l1 =[2,4]
    function_one(100)
    #return (True,1,l1)


print(function_one(10,5))

print(function_one(10))

result,result1,result2 = function_one(10)
print(result)
print(result1)
print(result2)

tup_result = function_one(10)
print(tup_result[0])
print(tup_result[1])
print(tup_result[2])

