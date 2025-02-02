#!/usr/bin/env python3


while True:
    try:
        print("\nEnter 99 at any time to exit")
        input_string = input("Enter a string here: ")

        if input_string == "99":
            print("\nExiting!")
            break

        else:
            reversed_string = ''

            for char in input_string:
                reversed_string = char + reversed_string

            print(f"\nReversed string: {reversed_string}")

    except ValueError:
        print("\nInvalid input")

