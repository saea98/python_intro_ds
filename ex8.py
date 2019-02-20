formatter = "{} {} {} {}" #variable formatter con 4 llaves
print(formatter.format(1, 2, 3, 4))#usa la variable formatter para desplegar el arreglo 1,2,3,4 con el formato de dicha variable
print(formatter.format("one", "two", "three", "four"))#usa la variable formatter para desplegar el arreglo "one", "two", "three", "four"  con el formato de dicha variable
print(formatter.format(True, False, False, True))#mismo caso pero susando valores booleanos
print(formatter.format(formatter, formatter, formatter, formatter))#imprime 4 veces el texto de la variable formatter sin dar formato 
print(formatter.format(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear"
))#imprime cada uno de los 4 textos usando la variable formatter y la función format
