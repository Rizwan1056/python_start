#Celsius (°C) scale to its Fahrenheit (°F) formula is given below: °F = (9/5 × °C) + 32.
#The Fahrenheit to Celsius formula is expressed as °C = (°F - 32) × 5/9.
while True:
    print("\t=========================")
    print("\t|Temperature Calculator |")
    print("\t=========================\n")
    print("\t1.Celsius to Fahrenheit  (°C) ")
    print("\t2.Fahrenheit to Celsius (°F)")
    print("\t3.Kelvin to Celsius(°K) \n")
    selection = int(input("Enter Selection => : "))

    if(selection==1):

        cels = float(input("Please Enter Celsius (°C)  : ")) 
        fahr = (9/5 * cels) + 32
        print("Fahrenheit is (°F) : ",fahr)

    elif(selection==2):
        fahr = float(input("Please Enter Fahrenheit (°F)  : "))
        cels = (fahr -   32) * 5/9
        print("Celsius is (°C) : ",cels)

    elif(selection==3):
        kelvin = float(input("Please Enter Kelvin (°K)  : "))
        cels = (kelvin - 273.15)
        print("Celsius is (°C) : ",cels)
    else:
        print("Invalid Selection")
        break
    