import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('ecommerce_preparados.csv')

plt.figure(figsize=(6, 6))
df['Gênero'].value_counts().plot(kind='pie', autopct='%1.1f%%', startangle=90, colors=sns.color_palette('pastel'))
plt.title('Pie Chart - Product Distribution by Gender')
plt.ylabel('')

plt.savefig('pie_chart.png', dpi=300)
plt.show()
