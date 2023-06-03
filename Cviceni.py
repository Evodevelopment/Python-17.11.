weight = 93
weight = 8.4

#"Ground Shipping: "
if weight <= 2:
  cost_ground = weight * 1.5 + 20
elif weight <= 6:
  cost_ground = weight * 3 + 20
elif weight <= 10:
  cost_ground = weight * 4 + 20
elif weight > 10:
  cost_ground = weight * 4.75 + 20
print(cost_ground)


#"Ground shipping Premium: "
cost_ground_premium = 125.00
print("Ground Shipping Premium $", cost_ground_premium)

#"Drone Shipping"
weight = 1.5
if weight <= 2:
  drone_ground = weight * 4.5
elif weight <= 6:
  drone_ground = weight * 9
elif weight <= 10:
  drone_ground = weight * 12
elif weight > 10:
  drone_ground = weight * 14.25
print(drone_ground)
