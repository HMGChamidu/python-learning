count =10
while count >=1:
    print(count)
    count -=1   

count = 1
while count <=20:
    if count % 2 ==0:
        print(count)
        
count += 1


for count in range (1,11):
    if count == 5:
        continue
    print(count)

for count in range(1,11):
    if count == 7:
        break
    print(count)

#sum of numbers

total= 0
num = 1
while num <= 100:
    total += num
    num += 1
print(total)