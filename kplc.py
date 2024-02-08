
#Bill calculator
def kplc(customer_ID, customer_name, units):
    if units <=199:
        charge = 1.2 * units
    elif units >= 200 and units < 400:
        charge = units * 1.5
    elif units >= 400 and units < 600:
        charge = unite * 1.8
    elif units >= 600:
        charge = units * 2
    return charge
customer_ID = int(input("Enter your ID: "))
customer_name = input("Enter your Name: ")
units_consumed = int(input("Enter units: "))
print(kplc(customer_ID, customer_name, units_consumed))