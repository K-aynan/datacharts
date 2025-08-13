
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('ecommerce_preparados.csv')

plt.figure(figsize=(10, 6))
plt.hist(df['Preço'], bins=30, color='green', alpha=0.8)
plt.title('Histogram - Price Distribution')
plt.xlabel('Price (R$)')
plt.ylabel('Frequency')
plt.grid(True)

plt.savefig('histogram.png', dpi=300)
plt.show()
