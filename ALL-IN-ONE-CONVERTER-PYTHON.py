def length_unit_converter():
    print("\n--- LENGTH UNIT CONVERTER ---")
    print("1. Meters to Kilometers")
    print("2. Kilometers to Meters")
    user_selection = int(input("Select your conversion type: "))

    if user_selection == 1:
        meters_val = float(input("Input length in meters: "))
        print("Equivalent Kilometers =", meters_val / 1000)
    elif user_selection == 2:
        kms_val = float(input("Input length in kilometers: "))
        print("Equivalent Meters =", kms_val * 1000)
    else:
        print("That's not a valid option for length conversion.")

def temp_scale_converter():
    print("\n--- TEMPERATURE SCALE CONVERTER ---")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    user_selection = int(input("Pick a temperature conversion: "))

    if user_selection == 1:
        celsius_val = float(input("Enter temperature in Celsius: "))
        print("Fahrenheit equivalent =", (celsius_val * 9/5) + 32)
    elif user_selection == 2:
        fahrenheit_val = float(input("Enter temperature in Fahrenheit: "))
        print("Celsius equivalent =", (fahrenheit_val - 32) * 5/9)
    else:
        print("Invalid temperature conversion choice.")

def mass_unit_converter():
    print("\n--- MASS UNIT CONVERTER ---")
    print("1. Kilograms to Grams")
    print("2. Grams to Kilograms")
    user_selection = int(input("Choose a weight conversion: "))

    if user_selection == 1:
        kg_val = float(input("Provide weight in kilograms: "))
        print("Grams =", kg_val * 1000)
    elif user_selection == 2:
        g_val = float(input("Provide weight in grams: "))
        print("Kilograms =", g_val / 1000)
    else:
        print("Incorrect option for mass conversion.")

def duration_converter():
    print("\n--- DURATION CONVERTER ---")
    print("1. Hours to Minutes")
    print("2. Minutes to Hours")
    user_selection = int(input("Select a time conversion: "))

    if user_selection == 1:
        hours_val = float(input("Enter duration in hours: "))
        print("Minutes =", hours_val * 60)
    elif user_selection == 2:
        minutes_val = float(input("Enter duration in minutes: "))
        print("Hours =", minutes_val / 60)
    else:
        print("Invalid choice for time conversion.")

def foreign_exchange_converter():
    print("\n--- FOREIGN EXCHANGE CONVERTER (Illustrative Rates) ---")
    print("1. INR to USD")
    print("2. USD to INR")
    user_selection = int(input("Choose a currency exchange: "))

    # These rates are illustrative and would need real-time updates for accuracy.
    INR_TO_USD_RATE = 0.0125 # Slightly adjusted rate
    USD_TO_INR_RATE = 82.5   # Slightly adjusted rate

    if user_selection == 1:
        inr_amount = float(input("Input amount in INR: "))
        print("USD =", inr_amount * INR_TO_USD_RATE)
    elif user_selection == 2:
        usd_amount = float(input("Input amount in USD: "))
        print("INR =", usd_amount * USD_TO_INR_RATE)
    else:
        print("Unrecognized currency conversion option.")

def numerical_base_converter():
    print("\n--- NUMERICAL BASE CONVERTER ---")
    print("1. Decimal to Binary")
    print("2. Decimal to Octal")
    print("3. Decimal to Hexadecimal")
    print("4. Binary to Decimal")
    user_selection = int(input("Pick a number system conversion: "))

    if user_selection == 1:
        dec_num = int(input("Enter a decimal number: "))
        print("Binary representation =", bin(dec_num))
    elif user_selection == 2:
        dec_num = int(input("Enter a decimal number: "))
        print("Octal representation =", oct(dec_num))
    elif user_selection == 3:
        dec_num = int(input("Enter a decimal number: "))
        print("Hexadecimal representation =", hex(dec_num))
    elif user_selection == 4:
        binary_str = input("Enter a binary string: ")
        print("Decimal equivalent =", int(binary_str, 2))
    else:
        print("That's not a valid number system conversion.")




while True:
    print("\n\n===== THE ULTIMATE CONVERSION HUB =====")
    print("1. Length Unit Converter")
    print("2. Temperature Scale Converter")
    print("3. Mass Unit Converter")
    print("4. Duration Converter")
    print("5. Foreign Exchange Converter")
    print("6. Numerical Base Converter")
    print("7. Exit Application")

    main_choice = int(input("Your choice from the main menu: "))

    if main_choice == 1:
        length_unit_converter()
    elif main_choice == 2:
        temp_scale_converter()
    elif main_choice == 3:
        mass_unit_converter()
    elif main_choice == 4:
        duration_converter()
    elif main_choice == 5:
        foreign_exchange_converter()
    elif main_choice == 6:
        numerical_base_converter()
    elif main_choice == 7:
        print("Exiting the converter. Farewell!")
        break
    else:
        print("Invalid main menu selection! Please try again with a number from 1 to 7.")