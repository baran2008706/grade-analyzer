courses = {}
num = int(input("enter the number of courses:"))

total = 0
for i in range(1, num + 1):
    course = input("enter course name:")
#we use float here because the scores can be any number in the range of real numbers
    scores = float(input("enter your score:"))
    courses[course] = scores
    total += scores

print("your average is:", total/num)
print(courses)
