#program to output gross pay--
#prompt the user to enter hours worked and rate per hour
hours_worked=float(input("Enter hours worked:"))
rate_per_hour=float(input("Enter rate per hour:"))
#calculate gross pay
gross_pay= hours_worked*rate_per_hour
#display the result
print(f"\nGross pay: ${gross_pay:.2f}")