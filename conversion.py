import time

def time_stop():
    time.sleep(0.53)

print("*"*90)
print("\n\t\t\t\tUNIT CONVERSION\n")
print("*"*90)

print("1 - TEMPERATURE CONVERSION\n2 - DISTANCE  CONVERSION\n3 - TIME CONVERSION\n")


while True:
    try:
        choice=int(input("Enter your Choice for Unit Conversion: "))
        if choice in range(1,4):
            break
        else:
            print("\nEnter your Choice within the range")
    except ValueError:
        print("\nEnter only number")

if choice == 1:
    print("\n\t\t\t\t TEMPERATURE CONVERSION")

    print("1. Celsius    ---→   Fahrenheit")
    print("2. Fahrenheit ---→   Celsius")
    print("3. Celsius    ---→   Kelvin")
    print("4. Kelvin     ---→   Celsius")
    print("5. Fahrenheit ---→   Kelvin")
    print("6. Kelvin     ---→   Fahrenheit\n")

    while True:
        try:
            temp_conversion_choice=int(input("Enter your choice which Temperature you have to convert: "))
            if temp_conversion_choice in range(1,7):
                break
            else:
                print("\nYour choice within the range")
        except ValueError:
            print("\nEnter only number")


    if temp_conversion_choice == 1:
        print("╭────────────────────────────────────────────────────────────╮")
        print("│               Celsius ------>  Fahrenheit                  │")
        print("╰────────────────────────────────────────────────────────────╯")
        c=float(input("\nEnter The Celsius Temperature: "))
        f=((9/5)*c)+32
        time_stop()
        print(f"\n{c} degree Celsius is equal to {f:.3f} degree Fahrenheit")
        print(f"{c}°C = {f:.3f}°F")

    elif temp_conversion_choice == 2:
        print("╭────────────────────────────────────────────────────────────╮")
        print("│              Fahrenheit ------>   Celsius                  │")
        print("╰────────────────────────────────────────────────────────────╯")
        f=float(input("\nEnter The Fahrenheit Temperature: "))
        c=(f-32)*(5/9)
        print(f"\n{f} degree Fahrenheit is equal to {c:.3f} degree celsius")
        print(f"{f}°F = {c:.3f}°C")

    elif temp_conversion_choice == 3:
        print("╭────────────────────────────────────────────────────────────╮")
        print("│              Celsius   ------>   Kelvin                    │")
        print("╰────────────────────────────────────────────────────────────╯")
        c=float(input("\nEnter The Celsius Temperature: "))
        k=c+273.15
        print(f"\n{c} degree Celsius is equal to {k:.3f} degree Kelvin")
        print(f"{c}°C = {k:.3f} K")

    elif temp_conversion_choice == 4:
        print("╭────────────────────────────────────────────────────────────╮")
        print("│              Kelvin ----→ Celsius                          │")
        print("╰────────────────────────────────────────────────────────────╯")
        k=float(input("Enter The Kelvin Temperature: "))
        c=k-273.15
        print(f"\n{k} degree Kelvin is equal to {c:.3f} degree Celsius")
        print(f"{k} K  = {c:.3f}°C")

    elif temp_conversion_choice == 5:
        print("╭────────────────────────────────────────────────────────────╮")
        print("│              Fahrenheit ----→ Kelvin                       │")
        print("╰────────────────────────────────────────────────────────────╯")
        f=float(input("Enter the Fahrenheit Temperature: "))
        k=((f-32)*(5/9))+273.15
        print(f"n{f} degree Fahrenheit is equal to {k:.3f} degree Kelvin")
        print(f"{f}°F = {k:.3f} K")

    elif temp_conversion_choice == 6:
        print("\n\t\t\tKelvin --→ Fahrenheit")
        print("╭────────────────────────────────────────────────────────────╮")
        print("│              Kelvin ----→ Fahrenheit                       │")
        print("╰────────────────────────────────────────────────────────────╯")
        k=float(input("Enter the Kelvin Temperature: "))
        f=((k-273.15)*(9/5))+32
        print(f"\n{k} degree Kelvin is equal to {f:.3f} degree Fahrenheit")
        print(f"{k} K = {f:.3f}°F")

elif choice == 2:

    print("\n\t\t\t\t DISTANCE CONVERSION")
    print("1.Kilometer   ---→  Meter")
    print("2.Meter       ---→  Centimeter")
    print("3.Centimeter  ---→  Millimeter") 
    print("4.Meter       ---→  Kilometer")
    print("5.Inch        ---→  Centimeter")
    print("6.Mile        ---→  Kilometer")

    while True:
            try:
                distance_conversion_choice=int(input("Enter your choice which distance you have to convert: "))
                if distance_conversion_choice in range(1,7):
                    break
                else:
                    print("\nYour choice within the range")
            except ValueError:
                print("\nEnter only number")

    if distance_conversion_choice == 1:
        print("╭────────────────────────────────────────────────────────────╮")
        print("│              Kilometer   ----→  Meter                      │")
        print("╰────────────────────────────────────────────────────────────╯")
        km=int(input("Enter how many kilometers : "))
        m=km*1000
        print(f"{km} kilometers to {m} meters")

    elif distance_conversion_choice == 2:
        print("╭────────────────────────────────────────────────────────────╮")
        print("│              Meter   ----→  Centimeter                     │")
        print("╰────────────────────────────────────────────────────────────╯")
        m=int(input("Enter how many meters : "))
        cm=m*100
        print(f"{m} meters to {cm} centimeters")

    elif distance_conversion_choice == 3:
        print("╭────────────────────────────────────────────────────────────╮")
        print("│              Centimeter  ---→  Millimeter                  │")
        print("╰────────────────────────────────────────────────────────────╯")
        cm=int(input("Enter how many centimeters : "))
        mm=cm*10
        print(f"{cm} meters to {mm} millimeters")

    elif distance_conversion_choice == 4:
        print("╭────────────────────────────────────────────────────────────╮")
        print("│              Meter   ----→  kilometer                      │")
        print("╰────────────────────────────────────────────────────────────╯")
        m=int(input("Enter how many meters : "))
        km=m/1000
        print(f"{m} meters to {km} kilometers")

    elif distance_conversion_choice == 5:
        print("╭────────────────────────────────────────────────────────────╮")
        print("│              INCH   ----→  Centimeter                      │")
        print("╰────────────────────────────────────────────────────────────╯")
        i=int(input("Enter how many inches : "))
        cm=i*2.54
        print(f"{i} Inch to {cm} centimeters")

    elif distance_conversion_choice == 6:
        print("╭────────────────────────────────────────────────────────────╮")
        print("│              Mile   ----→  kilometer                       │")
        print("╰────────────────────────────────────────────────────────────╯")
        M=int(input("Enter how many miles : "))
        km=M * 1.609
        print(f"{M} miles to {km} kilometers")

elif choice == 3:
    print("\n\t\t\t\t TIME CONVERSION")
    print("1.Hour   ----→  Minute")
    print("2.Minute ----→  Second")
    print("3.Day    ----→  Hour") 
    print("4.Week   ----→  Day")
    print("5.Month  ----→  Days") 
    print("6.Year   ----→  Days")


    while True:
                try:
                    time_conversion_choice=int(input("Enter your choice which Time you have to convert: "))
                    if time_conversion_choice in range(1,7):
                        break
                    else:
                        print("\nYour choice within the range")
                except ValueError:
                    print("\nEnter only number")

    if time_conversion_choice == 1:
        print("╭────────────────────────────────────────────────────────────╮")
        print("│              Hour   ----→  Minute                          │")
        print("╰────────────────────────────────────────────────────────────╯")
        H=int(input("Enter how many hours: "))
        M=H*60
        print(f"{H}Hours to {M}Minutes")

    elif time_conversion_choice == 2:
        print("╭────────────────────────────────────────────────────────────╮")
        print("│              Minute ----→  Second                          │")
        print("╰────────────────────────────────────────────────────────────╯")

        print("╭────────────────────────────────────────────────────────────╮")
        print("│              Day    ----→  Hour                            │")
        print("╰────────────────────────────────────────────────────────────╯")

        print("╭────────────────────────────────────────────────────────────╮")
        print("│              Week   ----→  Day                             │")
        print("╰────────────────────────────────────────────────────────────╯")

        print("╭────────────────────────────────────────────────────────────╮")
        print("│              Month  ----→  Days                            │")
        print("╰────────────────────────────────────────────────────────────╯")

        print("╭────────────────────────────────────────────────────────────╮")
        print("│              Year   ----→  Days                            │")
        print("╰────────────────────────────────────────────────────────────╯")
    





    
    
    



        

        

    

    

