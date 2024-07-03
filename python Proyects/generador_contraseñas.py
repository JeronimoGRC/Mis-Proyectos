import random

contraseña = ""
contraseña_mas_mayus = ""
letras = ['a','b','c','d','f','g','h','i','j','k','l','m','n',
          'ñ','o','p','q','r','s','t','u','v','w','x','y','z']

caracteres_especiales = ['!','¡','¿','?','%','$','#','&','_']

for i in range(6):
    aletorio = random.randint(0,25)
    contraseña += letras[aletorio]
    contraseña_mas_mayus = contraseña.capitalize()

for i in range(2):
    num = random.randint(0,9)
    num_str = str(num)
    contraseña_mas_mayus += num_str


especial = caracteres_especiales[random.randint(0,8)]
contraseña_mas_mayus += especial

lista_contraseña = list(contraseña_mas_mayus)
random.shuffle(lista_contraseña)
contraseña_final = ''.join(lista_contraseña)
print(contraseña_final)