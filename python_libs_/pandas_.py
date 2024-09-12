import pandas as pd

#1. Data Cleaning
# DataFrame with missing values
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [25, None, 30, 22],
        'City': ['New York', 'Los Angeles', None, 'Chicago']}
df = pd.DataFrame(data)

# a. Fill missing values in 'Age' with the mean age
df['Age'].fillna(df['Age'].mean(), inplace=True)

# b. Drop rows with any missing values
df.dropna(inplace=True)

print(df)

# 2. Data exploration
data ={'Product':['A', 'B', 'C', 'A', 'B', 'C'],
       'Sales':[100,150, 200, 130,  120, 180]}
df = pd.DataFrame(data)

print(df['Sales'].describe())

# 3 data transformation
data = {'Product': ['A', 'B', 'C','D'],
        'Quantity':[10, 20, 30, 40],
        'Price':[100, 200, 300, 400]}
df = pd.DataFrame(data)

filtered_df = df[df['Quantity']>20][['Product', 'Price']]
print(filtered_df)

# 4 analysis
# Sample time series DataFrame
date_range = pd.date_range(start='2024-01-01', periods=10, freq='D')
data = {'Date': date_range, 'Sales': [100, 120, 130, 150, 140, 160, 170, 180, 190, 200]}
df = pd.DataFrame(data)

# Set 'Date' as the index
df.set_index('Date', inplace=True)

# Resample data to monthly frequency and calculate the mean sales
monthly_sales = df.resample('M').mean()

# Print the resulting DataFrame
print(monthly_sales)

# 5 Data exporting
data = {'Name':['Alice', 'Bob', 'Charlie'],
        'Score':[85, 90,78]}
df.to_csv('panda_process.csv', index=False)
print("Data saved to 'panda_processd.csv'")





# more data Transformation
import numpy as np

# Sample DataFrame
np.random.seed(42)  # For reproducibility
data = {
    'Date': pd.date_range(start='2024-01-01', periods=100, freq='D'),
    'Product': np.random.choice(['Product_A', 'Product_B', 'Product_C'], size=100),
    'Category': np.random.choice(['Electronics', 'Clothing', 'Groceries'], size=100),
    'Price': np.random.uniform(10, 100, size=100),
    'Quantity': np.random.randint(1, 20, size=100)
}
data['Revenue'] = data['Price'] * data['Quantity']
df = pd.DataFrame(data)

# 1. Renaming Columns and Indexes
df.rename(columns={'Product': 'Item', 'Quantity': 'Qty'}, inplace=True)
df.columns = [col.lower() for col in df.columns]

# 2. Changing Data Types
df['date'] = pd.to_datetime(df['date'])
df['price'] = df['price'].astype('float')
df['category'] = df['category'].astype('category')

# 3. Handling Missing Data
df.loc[5:10, 'revenue'] = np.nan
df['revenue'].fillna(df['revenue'].mean(), inplace=True)

# 4. Mapping and Replacing Values
df['category'] = df['category'].map({'Electronics': 'Elec', 'Clothing': 'Cloth', 'Groceries': 'Groc'})
df['item'] = df['item'].str.replace('_', ' ')

# 5. Applying Functions to Data
df['price_with_tax'] = df['price'].apply(lambda x: x * 1.08)
df['revenue_squared'] = df['revenue'].transform(np.square)

# 6. Binning and Discretization
df['price_bin'] = pd.cut(df['price'], bins=[0, 30, 60, 100], labels=['Low', 'Medium', 'High'])

# 7. Scaling and Normalization
df['price_scaled'] = (df['price'] - df['price'].min()) / (df['price'].max() - df['price'].min())

# 8. Adding or Removing Columns
df['profit'] = df['revenue'] - (df['qty'] * df['price'])
df.drop('revenue_squared', axis=1, inplace=True)

# 9. Pivoting and Melting
melted_df = df.melt(id_vars=['date', 'item'], value_vars=['price', 'qty'])
pivot_df = melted_df.pivot(index='date', columns='variable', values='value')

# 10. Stacking and Unstacking
stacked_df = df.set_index(['date', 'item']).stack()
unstacked_df = stacked_df.unstack()

# 11. Sorting Data
sorted_df = df.sort_values(by='price', ascending=False)
sorted_index_df = df.sort_index()

# 12. Merging and Joining Data
df2 = pd.DataFrame({
    'item': ['Product A', 'Product B', 'Product D'],
    'supplier': ['Supplier_X', 'Supplier_Y', 'Supplier_Z']
})
merged_df = pd.merge(df.reset_index(), df2, on='item', how='left')

# 13. Aggregation and Grouping
grouped_df = df.groupby('category').agg({'revenue': 'sum', 'qty': 'mean'})

# 14. Resampling Time Series Data
df.set_index('date', inplace=True)
monthly_revenue = df.resample('M').sum()['revenue']

# 15. Window Functions
df['rolling_mean'] = df['revenue'].rolling(window=7).mean()
df['expanding_sum'] = df['revenue'].expanding().sum()

# 16. String Manipulation
df['item'] = df['item'].str.upper()
df['is_elec'] = df['category'].str.contains('Elec')

# 17. Removing Duplicates
df.drop_duplicates(inplace=True)

# 18. Working with Categorical Data
df['category'] = df['category'].astype('category')
df['category_codes'] = df['category'].cat.codes

# 19. Handling Outliers
df = df[(df['price'] >= 10) & (df['price'] <= 90)]
df['price_clipped'] = df['price'].clip(lower=15, upper=85)

# 20. Combining and Concatenating DataFrames
df_concat = pd.concat([df.reset_index(drop=True), df2], axis=1)

# 21. Flattening MultiIndex
df_reset = df_reset = pivot_df.reset_index()
df_reset.columns = ['_'.join(col).strip() if isinstance(col, tuple) else col for col in df_reset.columns]

# Display the final transformed DataFrame
print(df.head())
