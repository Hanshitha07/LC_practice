radius_input = input("Enter the radius of the circle: ")

if radius_input == "True" or radius_input == "False":
    print("Invalid input: boolean is not accepted as a radius.")

elif radius_input.isalpha():
    print("Invalid input: string is not accepted as a radius.")

elif 'j' in radius_input:
    radius = complex(radius_input)
    if radius.imag != 0:
        print("Invalid input: complex number is not accepted.")
    elif radius.real > 0:
        area = 3.14 * radius.real ** 2
        print("The area of the circle is:", area)
    else:
        print("Invalid input: radius must be greater than 0.")

elif radius_input.replace('.', '', 1).lstrip('-').isdigit():
    radius = float(radius_input)
    if radius > 0:
        area = 3.14 * radius ** 2
        print("The area of the circle is:", area)
    else:
        print("Invalid input: radius must be greater than 0.")

else:
    print("Invalid input.")