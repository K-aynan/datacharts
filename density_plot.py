import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('ecommerce_preparados.csv')

plt.figure(figsize=(8, 5))
sns.kdeplot(df['Preço'], shade=True, color='purple')
plt.title('Density Plot - Price Distribution')
plt.xlabel('Price (R$)')
plt.ylabel('Density')
plt.grid(True)

plt.savefig('density_plot.png', dpi=300)
plt.show()