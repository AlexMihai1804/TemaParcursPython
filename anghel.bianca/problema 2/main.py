# importarea bibliotecilor
import pandas as pd  # importarea bibliotecii pandas folosita pentru citirea fisierelor csv
import matplotlib.pyplot as plt  # importarea bibliotecii matplotlib.pyplot folosita pentru realizarea graficelor

date = pd.read_csv('data.csv')  # citirea fisierului csv
date.plot()  # realizarea graficului
plt.show()  # afisarea graficului
X = 6  # X conform cerintei
primeleX = date.head(X)  # selectarea primelor X linii
primeleX.plot()  # realizarea graficului
plt.show()  # afisarea graficului
Y = 15  # Y conform cerintei
ultimeleY = date.tail(Y)  # selectarea ultimelor Y linii
coloane_selectate = ultimeleY[['Durata', 'Puls']]  # selectarea coloanelor Durata si Puls
coloane_selectate.plot()  # realizarea graficului
plt.show()  # afisarea graficului
