fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print("would you like to have {}".format(fruit))


for number in range(1,11):
    if number == 5:
        print("skipping 5")
        continue
    print("the number is {}".format(number))


temp=30
while temp>20:
    print("the temp {}".format(temp))
    temp=temp-1
    if temp==25:
        break

for num in range(1,11):
    if num == 2:
        pass
    else:
        print("the number is {}".format(num))