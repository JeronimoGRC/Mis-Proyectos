from sklearn.model_selection import train_test_split, cross_val_score, GridSearchCV
from sklearn.preprocessing import StandardScaler, MinMaxScaler, LabelEncoder, OneHotEncoder
from sklearn.linear_model import LinearRegression, LogisticRegression, Ridge, Lasso
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier, AdaBoostClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, mean_squared_error, classification_report, confusion_matrix, roc_auc_score
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
import numpy as np
import pandas as pd

# Métodos más utilizados de la biblioteca scikit-learn:

# 1. train_test_split():
# Divide un dataset en conjuntos de entrenamiento y prueba.
data = np.random.rand(100, 5)
labels = np.random.randint(2, size=100)
X_train, X_test, y_train, y_test = train_test_split(data, labels, test_size=0.2, random_state=42)
print("Conjunto de entrenamiento y prueba divididos.")

# 2. StandardScaler():
# Escala los datos para que tengan media 0 y desviación estándar 1.
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
print("Datos escalados con StandardScaler.")

# 3. MinMaxScaler():
# Escala los datos a un rango específico (0 a 1 por defecto).
minmax_scaler = MinMaxScaler()
X_train_minmax = minmax_scaler.fit_transform(X_train)
X_test_minmax = minmax_scaler.transform(X_test)
print("Datos escalados con MinMaxScaler.")

# 4. LabelEncoder():
# Convierte etiquetas categóricas en valores numéricos.
le = LabelEncoder()
categorias = ['rojo', 'verde', 'azul', 'rojo', 'azul']
categorias_encoded = le.fit_transform(categorias)
print("Etiquetas categóricas codificadas:", categorias_encoded)

# 5. OneHotEncoder():
# Convierte variables categóricas en representación de variables dummy.
ohe = OneHotEncoder()
categorias_ohe = ohe.fit_transform(np.array(categorias).reshape(-1, 1)).toarray()
print("Representación OneHot de categorías:", categorias_ohe)

# 6. LinearRegression():
# Modelo de regresión lineal.
lin_reg = LinearRegression()
lin_reg.fit(X_train, y_train)
y_pred_lin = lin_reg.predict(X_test)
print("Regresión lineal entrenada.")

# 7. Ridge():
# Modelo de regresión Ridge con regularización L2.
ridge = Ridge(alpha=1.0)
ridge.fit(X_train, y_train)
print("Regresión Ridge entrenada.")

# 8. Lasso():
# Modelo de regresión Lasso con regularización L1.
lasso = Lasso(alpha=0.1)
lasso.fit(X_train, y_train)
print("Regresión Lasso entrenada.")

# 9. LogisticRegression():
# Modelo de regresión logística.
log_reg = LogisticRegression()
log_reg.fit(X_train, y_train)
y_pred_log = log_reg.predict(X_test)
print("Regresión logística entrenada.")

# 10. RandomForestClassifier():
# Clasificador de bosque aleatorio.
rf = RandomForestClassifier(n_estimators=100)
rf.fit(X_train, y_train)
y_pred_rf = rf.predict(X_test)
print("Clasificador RandomForest entrenado.")

# 11. GradientBoostingClassifier():
# Clasificador de Gradient Boosting.
gb = GradientBoostingClassifier()
gb.fit(X_train, y_train)
y_pred_gb = gb.predict(X_test)
print("Clasificador Gradient Boosting entrenado.")

# 12. AdaBoostClassifier():
# Clasificador de AdaBoost.
ab = AdaBoostClassifier()
ab.fit(X_train, y_train)
y_pred_ab = ab.predict(X_test)
print("Clasificador AdaBoost entrenado.")

# 13. SVC():
# Clasificador basado en máquinas de soporte vectorial.
svc = SVC()
svc.fit(X_train, y_train)
y_pred_svc = svc.predict(X_test)
print("Clasificador SVC entrenado.")

# 14. accuracy_score():
# Calcula la precisión de un modelo.
acc_rf = accuracy_score(y_test, y_pred_rf)
print("Precisión de RandomForest:", acc_rf)

# 15. mean_squared_error():
# Calcula el error cuadrático medio de un modelo de regresión.
mse_lin = mean_squared_error(y_test, y_pred_lin)
print("Error cuadrático medio de regresión lineal:", mse_lin)

# 16. classification_report():
# Muestra un informe de métricas de clasificación.
print("Reporte de clasificación de RandomForest:")
print(classification_report(y_test, y_pred_rf))

# 17. confusion_matrix():
# Calcula la matriz de confusión.
print("Matriz de confusión de RandomForest:")
print(confusion_matrix(y_test, y_pred_rf))

# 18. roc_auc_score():
# Calcula el área bajo la curva ROC.
roc_auc = roc_auc_score(y_test, y_pred_rf)
print("Área bajo la curva ROC:", roc_auc)

# 19. PCA():
# Reducción de dimensionalidad con Análisis de Componentes Principales.
pca = PCA(n_components=2)
X_train_pca = pca.fit_transform(X_train)
X_test_pca = pca.transform(X_test)
print("Datos transformados con PCA.")

# 20. KMeans():
# Algoritmo de clustering K-Means.
kmeans = KMeans(n_clusters=3)
kmeans.fit(X_train)
print("Modelo K-Means entrenado.")

# 21. cross_val_score():
# Realiza validación cruzada.
scores = cross_val_score(rf, X_train, y_train, cv=5)
print("Puntajes de validación cruzada:", scores)

# 22. GridSearchCV():
# Búsqueda de hiperparámetros con validación cruzada.
param_grid = {'n_estimators': [50, 100, 200]}
grid_search = GridSearchCV(RandomForestClassifier(), param_grid, cv=5)
grid_search.fit(X_train, y_train)
print("Mejores hiperparámetros de RandomForest:", grid_search.best_params_)
