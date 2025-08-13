import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('ecommerce_preparados.csv')

plt.figure(figsize=(8, 5))
sns.regplot(x='Nota', y='Preço', data=df, scatter_kws={'alpha':0.5})
plt.title('Regression Plot - Rating vs. Price')
plt.xlabel('Rating')
plt.ylabel('Price (R$)')
plt.grid(True)

plt.savefig('regression_plot.png', dpi=300)
plt.show()
