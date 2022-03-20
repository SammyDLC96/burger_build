#Burger_Builder
#This code is for practice purpose only

#Assigning price to Buns
def Bun_Price(Buns):

    B_Price = float()
    if Buns == "Plain" or "Sesame":
        B_Price = float(3.75)
        #if Buns == "Ciabatta" or "Pretzel":
            #B_Price = float(5.25)
        #elif Buns == "Ciabatta":
            #B_Price = float(4.50)
        #elif Buns == "Pretzel":
            #B_Price = float(5.00) 

        return B_Price
    print(float(B_Price))

#Prompting user to select Bun
print("Hi, welcome to BurgerKingdom. Pleaase build your Burger.")
Buns = input("What bun would you like: Plain, Sesame, Ciabatta or Pretzel?")

Bun_Price(Buns)
print("This bun costs: $", Bun_Price(Buns)) #Printing bun price

#Prompting user to select Patty
Pattys = input("Please select a patty type: Turkey, Chicken, Beef or Veggie?")

#Assigning price to Pattys
def Patty_Price(Pattys):

    P_Price = float()
    if Pattys == "Turkey" or "Chicken":
        P_Price = float(2.75)
    #if Pattys == "Chicken":
        #P_Price = float(3.25)
    #if Pattys == "Beef":
        #P_Price = float(4.00)
    #if Pattys == "Veggie":
        #P_Price = float(1.50)
        return P_Price

Patty_Price(Pattys)
print("This patty costs: $", Patty_Price(Pattys)) #Printing patty price

#Prompting user to select Cheese
Cheese = input("Now select the cheese: Provalone, American or Pepper Jack?")

#Assigning price to Cheese
def Cheese_Price(Cheese):

    Ch_Price = float()
    if Cheese == "Provalone" or "American" or "American":
        Ch_Price = float(1.20)
        return Ch_Price

Cheese_Price(Cheese)    
print("This cheese cost: $", Cheese_Price(Cheese)) #Printing cheese price

#Prompting user to select Vegs
Vegs = input("Finally select your veg: Lettuce, Tomatoes or Onions?")

#Assigning price to Vegs
def Veg_Price(Vegs):
    
    V_Price = float
    if Vegs == "Lettuce" or "Tomatoes":
        V_Price = float(0.75)
        #if Vegs == "Onions":
            #V_Price = float(1.25)
            
        return V_Price

Veg_Price(Vegs)
print("This veg cost: $", Veg_Price(Vegs))

Tax = float(12.2)
Bill = Bun_Price(Buns) + Patty_Price(Pattys) + Cheese_Price(Cheese) + Veg_Price(Vegs)

#Get Tax
Tax_Amt = (Bill * Tax) / 100

#Get total Bill
Total_Bill = Bill + Tax_Amt
Total_Bill = round(Total_Bill, 2) #Rounding total to 2 decimal points

#Print total bill
print("Your total is: $", Total_Bill)
print("Thank you for shopping with us!")


