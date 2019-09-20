fo = open("new_file.txt",'w+')
lines=fo.readlines()
print(lines)

for line in lines:
    print(line)

fo.close()
