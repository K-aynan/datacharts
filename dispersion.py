import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('ecommerce_preparados.csv')

plt.figure(figsize=(8, 5))
plt.scatter(df['Nota'], df['Preço'], color='#5883a8', alpha=0.6)
plt.title('Scatter Plot - Rating vs. Price')
plt.xlabel('Rating')
plt.ylabel('Price (R$)')
plt.grid(True)

plt.savefig('scatter.png', dpi=300)
plt.show()