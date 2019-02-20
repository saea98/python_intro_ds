#incializa la variable types _of_people
types_of_people=10
#Asigna a la variable x un texto con formato usando la variable {types_of_people}
x=f"There are {types_of_people} types of peoples"

#Asigna a la variable binary el texto binary
binary="binary"
#asigna a la variable do_not el texto don't 
do_not="don`t"
#Asigna a la variable y el texto con formato usando en el las variable binary y do_not
y=f"Those who know {binary} and those who {do_not}"
# muestra en consola los valores de las variable x y y en renglon separado
print(x)
print(y)

#imprime un texto con formato usando el valor d ela variable x
print(f"I said: {x}")
#imprime un texto con formato usando el valor d ela variable y
print(f"I also said: {y}")


#asigma el valor booleano False a la variable hilarius
hilarius=False

#Asigna el texto Isn't  that joke so funny? a la variable joke_evaluation
joke_evaluation="Isn't  that joke so funny?"
#imprime el valor de la variable joke_evaluation y da formato a la variable booleana hilarius para desplegaral como texto
print(joke_evaluation,format(hilarius))

#asgina el texto This is the left side of... a la variable w
w="This is the left side of..."
#asginna el texto a string with a right side. a la variable e
e="a string with a right side."
#concatena las variable w y e e imprime su valor 
print(w + e)