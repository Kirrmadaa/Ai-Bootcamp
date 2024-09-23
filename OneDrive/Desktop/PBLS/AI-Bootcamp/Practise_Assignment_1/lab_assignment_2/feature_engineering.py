import pandas as pd

file_path = 'Assignment_1_question_file\Sales.csv'  
sales_df = pd.read_csv(file_path)


print(sales_df.head())

sales_df['Revenue'] = sales_df['Price'] * sales_df['QuantitySold']


from scipy.stats import zscore

sales_df['Price_zscore'] = zscore(sales_df['Price'])


sales_df = sales_df[(sales_df['Price_zscore'].abs() <= 3)]


sales_df.drop(columns=['Price_zscore'], inplace=True)


from sklearn.preprocessing import MinMaxScaler


scaler = MinMaxScaler()

sales_df[['Price', 'Revenue']] = scaler.fit_transform(sales_df[['Price', 'Revenue']])

sales_df.to_csv('cleaned_sales_data.csv', index=False)
