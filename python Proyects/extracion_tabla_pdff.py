#En principio lo primero que hay que instalar es la biblioteca camelot-py
import camelot

#En este caso la operación debe necesitar un .pdf que se ubique en la misma carpeta que el script además 
# de que tenga que incluir una tabla dentro del propio pdf
tabla = camelot.read_pdf('tabla.pdf',pages='1')

tabla.export('tabla.csv',f='csv',compress=True)

tabla[0].to_csv('tabla.csv')