def calculate_fine(return_date, due_date):
    days_late = return_date - due_date
    fine_rate = 0

    if days_late > 0:
        if days_late <= 7:
            fine_rate = 20
        elif days_late <= 14:
            fine_rate = 50
        else:
            fine_rate = 100

    return days_late, fine_rate

bookID = input("Enter the book ID: ")
due_date = int(input("Enter the due date (number of days since borrowing): "))
return_date = int(input("Enter the return date (number of days since borrowing): "))

days_late, fine_rate = calculate_fine(return_date, due_date)

if fine_rate > 0:
    fine_amount = fine_rate
else:
    fine_amount = 0

print(f"Book ID: {bookID}")
print(f"Due Date: {due_date} days since borrowing")
print(f"Return Date: {return_date} days since borrowing")
print(f"Days Overdue: {days_late}")
print(f"Fine Rate: KSH {fine_rate}")
print(f"Fine Amount: KSH {fine_amount}")