# simple amount caluulate how many remain amount 

print("\n\t=== WellCome To Currency Sort ===\n")
rupee = int(input("Plz Enter a Amount: "))

fiveThousand =rupee // 5000 
thousand = (rupee % 5000) // 1000
fiveHundred = (rupee % 1000) //500
hundred = (rupee % 500) // 100
fifty = (rupee % 100) // 50
ten = (rupee % 50) // 10
ones = (rupee % 10) // 1


print("\n\t5000: ",fiveThousand)
print("\t1000 :",thousand)
print("\t500  :",fiveHundred)
print("\t100  :",hundred)
print("\t50   :",fifty)
print("\t10   :",ten)
print("\t1    :",ones)


