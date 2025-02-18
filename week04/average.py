
num = 1
list = []
while num != 0:
    num = int(input("Enter Number:"))
    if num != 0:
        list.append(num) 
total = 0
for i in list:
    total = total + int(i)


print("List: ",' '.join(map(str,list)))
print("Total:",total)
print("Average",total/len(list))