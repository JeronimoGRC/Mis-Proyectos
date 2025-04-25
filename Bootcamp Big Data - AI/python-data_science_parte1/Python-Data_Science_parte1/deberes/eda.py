import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar los datos
# Asegúrate de cambiar esto por la ruta correcta
archivo_csv = 'C:/Users/Usuario/Desktop/Jero/Mis-Proyectos/Bootcamp Big Data - AI/python-data_science_parte1/Python-Data_Science_parte1/deberes/habitos_sueno_limpios.csv'

df = pd.read_csv(archivo_csv)

# Configuración de estilo
sns.set(style='whitegrid')

# Visualizar la distribución de salarios
plt.figure(figsize=(10, 5))
sns.histplot(df['Salario'], bins=30, kde=True)
plt.title('Distribución de Salarios')
plt.xlabel('Salario')
plt.ylabel('Frecuencia')
plt.show()

# Relación entre salario y nivel de satisfacción
plt.figure(figsize=(10, 5))
sns.scatterplot(x=df['Salario'],
                y=df['Nivel_Satisfaccion'], hue=df['Categoria'])
plt.title('Relación entre Salario y Nivel de Satisfacción')
plt.xlabel('Salario')
plt.ylabel('Nivel de Satisfacción')
plt.legend(title='Categoría')
plt.show()

# Matriz de correlación
plt.figure(figsize=(12, 8))
corr_matrix = df.corr(numeric_only=True)
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Matriz de Correlación entre Variables')
plt.show()

# Relación entre años en la empresa y salario
plt.figure(figsize=(10, 5))
sns.boxplot(x=df['Anios_Trabajo'], y=df['Salario'])
plt.title('Distribución de Salarios según Años de Trabajo')
plt.xlabel('Años de Trabajo')
plt.ylabel('Salario')
plt.xticks(rotation=45)
plt.show()

# Relación entre proyectos completados y nivel de satisfacción
plt.figure(figsize=(10, 5))
sns.regplot(x=df['Proyectos_Completados'],
            y=df['Nivel_Satisfaccion'], scatter_kws={'alpha': 0.5})
plt.title('Relación entre Proyectos Completados y Nivel de Satisfacción')
plt.xlabel('Proyectos Completados')
plt.ylabel('Nivel de Satisfacción')
plt.show()

# Análisis de empleados activos vs inactivos
plt.figure(figsize=(6, 4))
sns.countplot(x=df['Activo'])
plt.title('Distribución de Empleados Activos e Inactivos')
plt.xlabel('Activo (1: Sí, 0: No)')
plt.ylabel('Cantidad')
plt.show()

# Análisis de satisfacción por departamento
plt.figure(figsize=(12, 5))
sns.boxplot(x=df['Departamento'], y=df['Nivel_Satisfaccion'])
plt.xticks(rotation=45)
plt.title('Nivel de Satisfacción por Departamento')
plt.xlabel('Departamento')
plt.ylabel('Nivel de Satisfacción')
plt.show()

# Distribución de salarios por categoría (ordenada)
categoria_ordenada = ['becario', 'junior', 'senior', 'manager', 'director']
df['Categoria'] = pd.Categorical(
    df['Categoria'], categories=categoria_ordenada, ordered=True)

plt.figure(figsize=(12, 5))
sns.boxplot(x=df['Categoria'], y=df['Salario'])
plt.xticks(rotation=45)
plt.title('Distribución de Salarios por Categoría')
plt.xlabel('Categoría')
plt.ylabel('Salario')
plt.show()


print("Análisis completo. Revisa las visualizaciones para obtener insights sobre los datos.")
