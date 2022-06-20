name=input("What is your name?: ")
weight= float(input("What is the weight of your package in pounds?: "))
print("Your package's weight is " + str(weight) + "lb")
ground_shipping=""
premium_ground_shipping= 125
drone_shipping=""

#Cost of Ground Shipping
if weight<=2:
  ground_shipping=20+1.50*weight
elif weight <=6:
  ground_shipping=20+3.00*weight
elif weight <=10:
  ground_shipping=20+4.00*weight
else:
  ground_shipping=20+4.75*weight
print("Cost using ground shipping: " + "$" + str(ground_shipping))

#Cost of Premium Ground Shipping

print("Cost using premium ground shipping: " + 
"$" + str(premium_ground_shipping))

#Cost of Drone Shipping
if weight<=2:
  drone_shipping=4.50*weight
elif weight <=6:
  drone_shipping=9.00*weight
elif weight <=10:
  drone_shipping=12.00*weight
else:
  drone_shipping=14.25*weight
print("Cost using drone shipping: " + "$" + str(drone_shipping))

cheapest=""
minimum=min(ground_shipping, premium_ground_shipping, drone_shipping)
if minimum==ground_shipping:
  cheapest= "ground shipping"
elif minimum==premium_ground_shipping:
  cheapest= "premium ground shipping"
else:
  cheapest= "drone shipping"  

print(name + "," + " the cheapest shipping option for your package is " + cheapest 
+ ".")
