import sys

def main():
    # Prompt user to enter their birth year
    birth_year_input = input("Enter your birth year: ")
    
    # Calculate age based on the entered birth year
    current_year = 2024  # You can update this to the current year
    try:
        birth_year = int(birth_year_input)
        age = current_year - birth_year
        print(f"Your age is: {age} years")
    except ValueError:
        print("Invalid input. Please enter a valid year.")

    # Ask user to provide their height in meters
    height_input = input("Enter your height in meters: ")

    #  Display the data type of each input and display it
    print(f"\nData types:")
    print(f"Birth year input is of type: {type(birth_year_input)}")
    print(f"Height input is of type: {type(height_input)}")

    # Display the size of each input and display it
    print(f"\nSize (in bytes):")
    print(f"Size of birth year input: {sys.getsizeof(birth_year_input)} bytes")
    print(f"Size of height input: {sys.getsizeof(height_input)} bytes")

if __name__ == "__main__":
    main()
