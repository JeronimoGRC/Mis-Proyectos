import pandas as pd

df = pd.DataFrame([
    ['Jeronimo',21],
    ['David',34],
    ['Ana',18]],
    columns=['NOMBRE','EDAD'])

# El significado de columns es el título de la columna
# El primer corchete es la información que tendrá la tabla

print(df)