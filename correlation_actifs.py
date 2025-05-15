print ("Projet correlation lancé")
import yfinance as yf
import pandas as pd 
# Liste des tickers (symboles boursiers)
tickers = ["GLD","USO","^GSPC","^NDX"]
# Télécharger les données de prix (prix de clôture)
data = yf.download(tickers, start= "2025-01-01", end="2025-05-01")
close_prices=data["Close"]
print(data.head())
alias= {"GLD": "Or", "USO": "Pétrole", "^GSPC": "S&P500", "^NDX": "Nasdaq 100"}
close_prices.rename(columns=alias, inplace=True)
# Calculer la matrice de corrélation
correlation_matrix = close_prices.corr()
# Afficher la matrice de corrélation
print ("\nMatrice de corrélation:")
print(correlation_matrix)
import seaborn as sns
import matplotlib.pyplot as plt
# Création de la heatmap
plt.figure(figsize=(10,8))
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5, annot_kws={"size":8})
plt.tight_layout
# Titre et affichage
plt.title ("Matrice de corrélation entre actifs")
plt.show()