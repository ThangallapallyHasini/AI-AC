def calc_average(marks):
    total = 0
    for m in marks:
        total += m
    average = total / len(marks)
    return average  # Typo fixed

marks = [85, 90, 78, 92]
print("Average Score is ", calc_average(marks))
