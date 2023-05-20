hall_of_fame = []
name_sum = []
while(1):
    name = input("Enter the name: ")
    if name != "X":
        sum = 0
        math_score = int(input("Enter " + name + "'s Math score: "))
        english_score = int(input("Enter" + name + "'s English score: "))
        sum = math_score + english_score
        if math_score >= 90 and english_score >= 90:
            name_sum.append(name)
            name_sum.append(sum)
            hall_of_fame.append(list(name_sum))
            name_sum = []
        else:
            continue
    else:
        break

print(hall_of_fame)
