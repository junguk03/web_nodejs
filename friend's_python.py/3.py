math_score = [40, 65, 23, 77, 84, 11, 9, 100, 94, 35, 34, 29, 78, 86, 90, 95, 44, 48, 51, 30]
math_score.sort()
math_score.reverse()
first = int(input("i = "))
second = int(input("j = "))
first -= 1
sum = 0
for x in range(first,second):
    sum += math_score[x]
count = second - first
average = round(sum/count)
print(average)