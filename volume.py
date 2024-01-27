#program to calculate volume of a sphere
import math

def calculate_sphere_volume(radius):
    volume = (4/3) * math.pi * radius**3
    return volume

def main():
    # Prompt the user for the radius of the sphere
    try:
        radius = float(input("Enter the radius of the sphere: "))
        
        if radius <= 0:
            print("Radius must be a positive number.")
        else:
            # Calculate the volume
            volume = calculate_sphere_volume(radius)

            # Display the result
            print(f"The volume of the sphere with radius {radius} is: {volume:.2f}")
    
    except ValueError:
        print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()
