nums=[10,20,30,40,50]
cords=(5,10)
print("numbers are:",nums)
print("coordinates are:",cords)

a=[100,200,300,400,500]
range=a[-3:-1]
print("range is:",range)
print(a[1:4:2])
print(a[-3:-1:2])
a.append(600)
print(a)
a.insert(2,350)
print(a)
a.extend([700,800])
print(a)
a.remove(200)
print(a)
a.pop()
print(a)
a.sort()
print(a)
a.reverse()
print(a)

#task-1
fruits=["apple","banana","carrots","dates"]
print(fruits)
fruits.append("egg")
print(fruits)
fruits.remove("banana")
print(fruits)
fruits.sort()
print(fruits)

#task-2
temperatures = [22, 24, 25, 28, 30, 29, 27, 26, 24, 22]
print("frist reading index is:",temperatures[0])
print("last reading index is:",temperatures[-1])
print("the afternoon peak is:",temperatures[3:6])
print("the lasr 3 hours is:",temperatures[-3:])

#task-3
screen_res = (1920, 1080)
print("Current Resolution: 1920x1080")
#screen_res[0] = 1280
#print(screen_res)
print("Tuples cannot be modified!")


