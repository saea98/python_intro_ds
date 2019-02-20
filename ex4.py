cars=100 #asigna el valor 100 a la variable cars
space_in_car=4 #asigna el valor 4.0 a la variable space_in_car
drivers=30 #asgina el valor 30 a la variable drivers 
passengers=90 # asgina el valor 90 a la variable passengers
cars_not_driven = cars - drivers # calcula los autos sin conductor restando a la variable cars la variable drivers
cars_driven=cars # inicia la variable cars_driven con el valor cars 
carpool_capacity=cars_driven*space_in_car # la variable carpool_capacity es igual a cars_driven multiplicado por space_in_car
average_passengers_per_car=passengers/cars_driven# la variable average_passengers_per_car es igual al disión de passengers/cars_driven
# oo hasta este punto no se ha desplegado ningun dato 
print("There are ",cars," cars available") #despliega el total de autos tidponibles 
print("There are only ", drivers," drivers avaliable")#despliega el total de conductores disponibles
print("There will be ", cars_not_driven," empty cars to day")# muestra el numero de autos vacios el día de hoy 
print("We cant transport ",carpool_capacity," people today")# despliega la capacidad de transporte de personas el día d ehoy
print("We  have " ,passengers,"to carpool today")#total de pasajeros para transportar
print("We need to put about ", average_passengers_per_car," in each car.")#DESPLIEGA EL PASAJEROS POR AUTO 