#-------------------------------------------------------------------------#
#Exercises with lists
#-------------------------------------------------------------------------#
#Part 1
print("======== Part 1 ==========")

l = [1, 4, 9, 10, 23]
print(l)

print(l[1:3])
print(l[-2:])

l.append(90)
print(l)

avg = sum(l) / len(l)
print(l)

del l[1:3]
print(l)

#Part 2
print("\n\n======== Part 2 ==========")

def listSort(wordList):
    wordList.sort(key=lambda s:s.lower())


print("Please input some words to sort:")
test2 = input().split(" ")
listSort(test2)
print("Sorted as: ", test2)

#Part 3
print("\n\n======== Part 3 ==========")

capitalizedInput = []

print("Please provide 3 lines of input:")
for i in range(0, 3):
    capitalizedInput.append(input().upper())

for i in range(0, 3):
    print(capitalizedInput[i])



#-------------------------------------------------------------------------#
#Exercises with dictionaries
#-------------------------------------------------------------------------#

print("\n\n======== Dictionaries ==========")

ages = {
"Peter": 10,
"Isabel": 11,
"Anna": 9,
"Thomas": 10,
"Bob": 10,
"Joseph": 11,
"Maria": 12,
"Gabriel": 10,
}

print("Dictionary length: ", len(ages))

def averageAge(dict):
    sum = 0
    for person in dict.items():
        sum += person[1]
    return sum / len(dict)

print("Average age: ", averageAge(ages))

def oldest(dict):
    x = ("", 0)
    for i in dict.items():
        if i[1] > x[1]:
            x = i

    return x

print("Oldest person is: ", oldest(ages))

def ageProgression(dict, n):
    for key,value in dict.items():
         dict[key] = value + n

ageProgression(ages, 10)
print(ages)