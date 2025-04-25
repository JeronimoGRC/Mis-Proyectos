from sklearn.feature_selection import SelectKBest, f_classif, RFE
from sklearn.pipeline import Pipeline
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.impute import SimpleImputer
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.manifold import TSNE
from sklearn.gaussian_process import GaussianProcessClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import f1_score, precision_score, recall_score, silhouette_score
from sklearn.calibration import CalibratedClassifierCV
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.multioutput import MultiOutputClassifier
from sklearn.semi_supervised import LabelPropagation
import numpy as np
import pandas as pd

# Métodos avanzados de la biblioteca scikit-learn:

# 1. SelectKBest():
# Selecciona las K mejores características según una función de puntuación.
X = np.random.rand(100, 10)
y = np.random.randint(2, size=100)
kbest = SelectKBest(score_func=f_classif, k=5)
X_selected = kbest.fit_transform(X, y)
print("Características seleccionadas con SelectKBest.")

# 2. RFE():
# Eliminación recursiva de características para seleccionar las más importantes.
clf = DecisionTreeClassifier()
rfe = RFE(estimator=clf, n_features_to_select=5)
X_rfe = rfe.fit_transform(X, y)
print("Características seleccionadas con RFE.")

# 3. Pipeline():
# Crea un pipeline que encadena múltiples transformaciones y un modelo.
pipeline = Pipeline([
    ('scaler', SimpleImputer(strategy='mean')),
    ('classifier', KNeighborsClassifier())
])
pipeline.fit(X, y)
print("Pipeline entrenado con imputación y KNN.")

# 4. GaussianNB():
# Clasificador Naive Bayes Gaussiano.
nb = GaussianNB()
nb.fit(X, y)
print("Modelo GaussianNB entrenado.")

# 5. DecisionTreeClassifier():
# Árbol de decisión para clasificación.
dt = DecisionTreeClassifier()
dt.fit(X, y)
print("Modelo DecisionTreeClassifier entrenado.")

# 6. LinearDiscriminantAnalysis():
# Análisis discriminante lineal para reducción de dimensionalidad.
lda = LinearDiscriminantAnalysis()
X_lda = lda.fit_transform(X, y)
print("Reducción de dimensionalidad con LDA aplicada.")

# 7. TSNE():
# Reducción de dimensionalidad no lineal.
tsne = TSNE(n_components=2)
X_tsne = tsne.fit_transform(X)
print("Datos transformados con TSNE.")

# 8. GaussianProcessClassifier():
# Clasificador basado en procesos gaussianos.
gpc = GaussianProcessClassifier()
gpc.fit(X, y)
print("Modelo GaussianProcessClassifier entrenado.")

# 9. MLPClassifier():
# Clasificador basado en redes neuronales multicapa.
mlp = MLPClassifier(max_iter=1000)
mlp.fit(X, y)
print("Modelo MLPClassifier entrenado.")

# 10. f1_score():
# Calcula la métrica F1 para evaluación de clasificación.
y_pred = dt.predict(X)
f1 = f1_score(y, y_pred)
print("F1 Score:", f1)

# 11. precision_score():
# Calcula la precisión de un modelo de clasificación.
precision = precision_score(y, y_pred)
print("Precision Score:", precision)

# 12. recall_score():
# Calcula la sensibilidad (recall) de un modelo de clasificación.
recall = recall_score(y, y_pred)
print("Recall Score:", recall)

# 13. silhouette_score():
# Evalúa la calidad de agrupamiento de un modelo de clustering.
km = KNeighborsClassifier(n_neighbors=3)
km.fit(X, y)
sil_score = silhouette_score(X, km.predict(X))
print("Silhouette Score:", sil_score)

# 14. CalibratedClassifierCV():
# Calibración de probabilidades para modelos de clasificación.
calibrated_clf = CalibratedClassifierCV(base_estimator=dt, cv=5)
calibrated_clf.fit(X, y)
print("Clasificador calibrado con CalibratedClassifierCV.")

# 15. CountVectorizer():
# Convierte texto en una matriz de frecuencia de palabras.
text_data = ["hola mundo", "aprendiendo scikit-learn",
             "procesamiento de texto"]
vectorizer = CountVectorizer()
X_text = vectorizer.fit_transform(text_data)
print("Texto vectorizado con CountVectorizer.")

# 16. TfidfVectorizer():
# Convierte texto en una matriz TF-IDF.
tfidf_vectorizer = TfidfVectorizer()
X_tfidf = tfidf_vectorizer.fit_transform(text_data)
print("Texto transformado con TfidfVectorizer.")

# 17. MultiOutputClassifier():
# Clasificación de múltiples salidas.
multi_target_clf = MultiOutputClassifier(KNeighborsClassifier())
multi_target_clf.fit(X, np.random.randint(2, size=(100, 3)))
print("Modelo MultiOutputClassifier entrenado.")

# 18. LabelPropagation():
# Algoritmo de aprendizaje semisupervisado basado en la propagación de etiquetas.
lp = LabelPropagation()
lp.fit(X, y)
print("Modelo LabelPropagation entrenado.")
