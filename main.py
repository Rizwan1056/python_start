#Celsius (°C) scale to its Fahrenheit (°F) formula is given below: °F = (9/5 × °C) + 32.
#The Fahrenheit to Celsius formula is expressed as °C = (°F - 32) × 5/9.

print("=========================")
print("| Temperature Calculator |")
print("=========================")

cels = float(input("Celsius (°C)  to Fahrenheit (°F) : ")) 
fahr = (9/5 * cels) + 32
print("Fahrenheit (°F) : ",fahr)


fahr = float(input("Fahrenheit (°F) to Celsius (°C)  : "))
cels = (fahr -   32) * 5/9
print("Celsius (°C) : ",cels)
