
# Exercise 1
count = 10
while count >= 1:
    print(count)
    count -= 1

# Exercise 2
count = 1
while count <= 20:
    if count % 2 == 0:
        print(count)
    count += 1

# Exercise 3
for count in range(1, 11):
    if count == 5:
        continue
    print(count)

# Exercise 4
for count in range(1, 11):
    if count == 7:
        break
    print(count)

# Bonus
total = 0
num = 1
while num <= 100:
    total += num
    num += 1

print(total)
