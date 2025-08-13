import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('ecommerce_preparados.csv')

plt.figure(figsize=(8, 5))
df['Marca'].value_counts().head(10).plot(kind='bar', color='skyblue')
plt.title('Bar Chart - Top 10 Brands by Count')
plt.xlabel('Brand')
plt.ylabel('Number of Products')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.savefig('bar_chart.png', dpi=300)
plt.show()