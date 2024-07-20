#Celsius (°C) scale to its Fahrenheit (°F) formula is given below: °F = (9/5 × °C) + 32.
#The Fahrenheit to Celsius formula is expressed as °C = (°F - 32) × 5/9.

print("\t=========================")
print("\t|Temperature Calculator |")
print("\t=========================\n")
print("\t1.Celsius (°C) ")
print("\t2.Fahrenheit (°F) \n")
selection = int(input("Enter Selection => : "))

if(selection==1):

    cels = float(input("Please Enter Celsius (°C)  : ")) 
    fahr = (9/5 * cels) + 32
    print("Fahrenheit is (°F) : ",fahr)

elif(selection==2):
    fahr = float(input("Please Enter Fahrenheit (°F)  : "))
    cels = (fahr -   32) * 5/9
    print("Celsius is (°C) : ",cels)

else:
    print("Invalid Selection")