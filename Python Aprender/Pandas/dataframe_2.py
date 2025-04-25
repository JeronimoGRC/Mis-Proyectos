import pandas as pd
import numpy as np

#np.random.randn(4,3) con este apartado del código diremos que genere 4 filas y 3 columnas 
df = pd.DataFrame(np.random.randn(4,3),columns=['a','b','c'])
#El valor es generado de manera aleatoria
print(df)