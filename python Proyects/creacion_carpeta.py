#Importamos los modulos necesarios para las operaciones de automatización
import calendar
from pathlib import Path

# Nos creamos una variable para enlistar todos los meses existentes
meses_anio = list(calendar.month_name[1:])
# Nos creamos una variable para enlistar todos los días existentes
dia_semana = list(calendar.day_name[:])

#Dois bucles uno para los meses del año y otro para los días de la semana
for i, mes in enumerate(meses_anio):
    for dia in dia_semana:
       Path(f'python Proyects/2024/{i+1}.{mes}/{dia}').mkdir(parents=True,exist_ok=True)

print("¡Carpetas creadas!")