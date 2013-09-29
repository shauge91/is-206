#Assigns variable cars value 100
cars = 100 
#Assigns variable space_in_a_car, a underscore character value 4.0
space_in_a_car = 4.0
#Assigns variable drivers value 30 
drivers = 30
#Assigns variable passengers value 90 
passengers = 90
#Assigns variable cars_not_driven value cars minus value drivers
cars_not_driven = cars - drivers
#assigns variable cars_driven value drivers
cars_driven = drivers
#assigns variable carpool_capacity value cars_driven times apce_in_a_car
carpool_capacity = cars_driven * space_in_a_car
#assigns average_passengers_per_car value passengers divided by cars_driven
average_passengers_per_car = passengers / cars_driven

print "There are", cars, "cars available."
print "There are only", drivers, "drivers avaiable."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."

