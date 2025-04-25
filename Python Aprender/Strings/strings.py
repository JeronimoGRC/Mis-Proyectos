primer_string = "Comillas dobles"
segundo_string = 'Comillas simples'

#Concatenar strings
print(primer_string,segundo_string)
print('esto es un texto de una variable ' + primer_string + ' ' + segundo_string) # Muy pesado
print(f'esto es un texto de una variable {primer_string}, {segundo_string}') #Forma correcta

#Separar el String
otro = 'hola'
a,b,c,d = otro

print(a)
print(b)
print(c)
print(d)