import scipy.stats as stats
import scipy.linalg as linalg
import scipy.optimize as optimize
import scipy.spatial as spatial
import scipy.signal as signal
import scipy.fft as fft
import numpy as np

# Métodos más utilizados de la biblioteca SciPy:

# 1. stats.norm.pdf():
# Calcula la función de densidad de probabilidad de una distribución normal.
x = np.linspace(-3, 3, 100)
pdf = stats.norm.pdf(x)
print("\nFunción de densidad de probabilidad calculada.")

# 2. stats.norm.cdf():
# Calcula la función de distribución acumulada de una distribución normal.
cdf = stats.norm.cdf(x)
print("\nFunción de distribución acumulada calculada.")

# 3. stats.ttest_ind():
# Realiza una prueba t para dos muestras independientes.
sample1 = np.random.randn(100)
sample2 = np.random.randn(100)
t_stat, p_value = stats.ttest_ind(sample1, sample2)
print("\nPrueba t realizada, valor p:", p_value)

# 4. stats.pearsonr():
# Calcula el coeficiente de correlación de Pearson.
x = np.random.rand(100)
y = np.random.rand(100)
correlation, _ = stats.pearsonr(x, y)
print("\nCoeficiente de correlación de Pearson:", correlation)

# 5. linalg.inv():
# Calcula la matriz inversa.
A = np.array([[1, 2], [3, 4]])
A_inv = linalg.inv(A)
print("\nMatriz inversa calculada:")
print(A_inv)

# 6. linalg.det():
# Calcula el determinante de una matriz.
det_A = linalg.det(A)
print("\nDeterminante de la matriz:", det_A)

# 7. linalg.eig():
# Calcula los valores y vectores propios de una matriz.
eigvals, eigvecs = linalg.eig(A)
print("\nValores propios calculados:", eigvals)

# 8. optimize.minimize():
# Minimiza una función escalar usando un método específico.


def f(x):
    return x**2 + 3 * x + 2


res = optimize.minimize(f, x0=0)
print("\nResultado de la minimización:")
print(res)

# 9. spatial.distance.euclidean():
# Calcula la distancia euclidiana entre dos puntos.
p1 = np.array([1, 2, 3])
p2 = np.array([4, 5, 6])
distance = spatial.distance.euclidean(p1, p2)
print("\nDistancia euclidiana calculada:", distance)

# 10. spatial.KDTree():
# Crea un árbol KD para búsqueda de vecinos cercanos.
points = np.random.rand(10, 3)
kdtree = spatial.KDTree(points)
print("\nÁrbol KDTree creado.")

# 11. signal.convolve():
# Calcula la convolución de dos señales.
sig1 = np.array([1, 2, 3, 4])
sig2 = np.array([0, 1, 0.5])
convolution = signal.convolve(sig1, sig2, mode='same')
print("\nConvolución de señales calculada.")

# 12. signal.find_peaks():
# Encuentra los picos en una señal.
data = np.sin(np.linspace(0, 10, 100))
peaks, _ = signal.find_peaks(data)
print("\nPicos encontrados en la señal:", peaks)

# 13. fft.fft():
# Calcula la transformada de Fourier rápida.
data = np.random.rand(100)
fft_result = fft.fft(data)
print("\nTransformada de Fourier calculada.")

# 14. fft.ifft():
# Calcula la transformada de Fourier inversa.
ifft_result = fft.ifft(fft_result)
print("\nTransformada de Fourier inversa calculada.")

# 15. stats.kstest():
# Realiza la prueba de Kolmogorov-Smirnov para una muestra.
kstest_res = stats.kstest(sample1, 'norm')
print("\nPrueba KS realizada, valor p:", kstest_res.pvalue)

# 16. stats.iqr():
# Calcula el rango intercuartil de un conjunto de datos.
iqr_value = stats.iqr(sample1)
print("\nRango intercuartil calculado:", iqr_value)

# 17. optimize.curve_fit():
# Ajusta una curva a un conjunto de datos.


def model(x, a, b):
    return a * x + b


x_data = np.linspace(0, 10, 100)
y_data = 3 * x_data + 2 + np.random.randn(100)
popt, _ = optimize.curve_fit(model, x_data, y_data)
print("\nParámetros ajustados del modelo:", popt)

# 18. stats.mode():
# Calcula la moda de un conjunto de datos.
data_mode = stats.mode(sample1)
print("\nModa de los datos:", data_mode.mode)

# 19. stats.shapiro():
# Prueba de normalidad de Shapiro-Wilk.
shapiro_res = stats.shapiro(sample1)
print("\nPrueba de Shapiro-Wilk realizada, valor p:", shapiro_res.pvalue)

# 20. signal.spectrogram():
# Calcula el espectrograma de una señal.
freqs, times, Sxx = signal.spectrogram(data)
print("\nEspectrograma calculado.")
