# Project suggested by CodeAcademy introduction to Python
# Sal runs the biggest shipping company in the tri-county area, Sal’s Shippers.
# Sal wants to make sure that every single one of his customers has the best, and most affordable experience shipping their packages.
# In this project, you’ll build a program that will take the weight of a package and determine the cheapest way to ship that package using Sal’s Shippers.
# Sal’s Shippers has several different options for a customer to ship their package:
# Ground Shipping, which is a small flat charge plus a rate based on the weight of your package.
# Ground Shipping Premium, which is a much higher flat charge, but you aren’t charged for weight.
# Drone Shipping (new), which has no flat charge, but the rate based on weight is triple the rate of ground shipping.

weight = 1

# Ground shipping
flat_charge_ground = 20
if weight <= 2 : 
  cost_ground = weight * 1.5 + flat_charge_ground
elif weight > 2 and weight <= 6 : 
  cost_ground = weight * 3 + flat_charge_ground
elif weight > 6 and weight <= 10 : 
  cost_ground = weight * 4 + flat_charge_ground
elif weight > 10 : 
  cost_ground = weight * 4.75 + flat_charge_ground
else : 
  print("Error")
print("Ground shipping costs you: ", cost_ground)

# Ground Shipping Premium
cost_premium = 125
print("Ground shipping Premium costs you: ", cost_premium)

# Drone Shipping
if weight <= 2 : 
  cost_drone = weight * 4.5
elif weight > 2 and weight <= 6 : 
  cost_drone = weight * 9
elif weight > 6 and weight <= 10 : 
  cost_drone = weight * 12
elif weight > 10 : 
  cost_drone = weight * 14.25
else : 
  print("Error")
print("Drone shipping costs you: ", cost_drone)

if cost_ground < cost_premium and cost_ground < cost_drone : 
  print("With a cost of ", cost_ground, "ground shipping is your most affordable option.")

if cost_premium < cost_ground and cost_premium < cost_drone : 
    print("With a cost of ", cost_premium, "ground shipping premium is your most affordable option.")

if cost_drone < cost_ground and cost_drone < cost_premium : 
    print("With a cost of ", cost_drone, "drone shipping is your most affordable option.")
