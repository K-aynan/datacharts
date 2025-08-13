import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('ecommerce_preparados.csv')

plt.figure(figsize=(6, 4))
corr = df.corr(numeric_only=True)
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title('Heatmap - Correlation Between Numeric Variables')

plt.savefig('heatmap.png', dpi=300)
plt.show()
