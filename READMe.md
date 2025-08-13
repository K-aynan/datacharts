# Exploratory Data Analysis - E-commerce

This project performs an **exploratory analysis** of the dataset `ecommerce_preparados.csv`, generating different types of charts to highlight patterns, distributions, and relationships between variables.

## 📌 Objective

The main goal is to explore customer behavior, identify trends, and visually present the most relevant information using Python with the `pandas`, `matplotlib`, and `seaborn` libraries.

---

## 📂 Data Structure

The `ecommerce_preparados.csv` file contains information such as:

- **Age** – Customers’ ages
- **AmountSpent** – Amount spent per purchase
- **ProductCategory** – Category of the purchased product
- Other numerical variables that can be used in the analysis

---

## 📊 Types of Charts Generated

### 1️⃣ Histogram

Shows the distribution of **Amount Spent** by customers, helping identify the most common spending ranges.

### 2️⃣ Scatter Plot

Shows the relationship between **Age** and **Amount Spent**, helping to determine if older or younger customers tend to spend more.

### 3️⃣ Heatmap

Displays the correlation between numerical variables, identifying positive or negative relationships between them.

### 4️⃣ Bar Chart

Shows the purchase count per **Product Category**, helping identify the best-selling categories.

### 5️⃣ Pie Chart

Displays the proportion of sales by **Product Category**, showing each category’s market share.

### 6️⃣ Density Plot

Shows the smooth distribution of **Amount Spent**, useful for understanding concentration and variation in values.

### 7️⃣ Regression Plot

Shows the relationship between **Age** and **Amount Spent** with a trend line, useful for identifying behavioral patterns.

---

## 📦 Libraries Used

- **pandas** → Data manipulation and reading
- **matplotlib** → Chart creation
- **seaborn** → More sophisticated charts and heatmaps

Install the required libraries with:

```bash
pip install pandas matplotlib seaborn
```
