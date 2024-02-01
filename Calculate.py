subject_1 = int(input("Enter the marks for the first subject: "))
subject_2 = int(input("Enter the marks for the second subject: "))
subject_3 = int(input("Enter the marks for the third subject: "))

# Calculate the average
average_score = (subject_1 + subject_2 + subject_3) / 3

# Tabulate the average
if 70 <= average_score <= 100:
    grade = "A"
elif 60 <= average_score <= 69:
    grade = "B"
elif 50 <= average_score <= 59:
    grade = "C"
elif 40 <= average_score <= 49:
    grade = "D"
elif 0 <= average_score <= 39:
    grade = "Fail"
else:
    grade = "Invalid Input"

print(f"Average Score: {average_score:.2f}")
print(f"Grade: {grade}")
