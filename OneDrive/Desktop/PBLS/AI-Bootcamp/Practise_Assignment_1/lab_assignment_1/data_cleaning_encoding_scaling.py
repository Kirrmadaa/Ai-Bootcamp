import pandas as pd

file_path = 'Assignment 1\Assignment 1\Students.csv'  
students_df = pd.read_csv(file_path)


print(students_df.head())


students_df['MathScore'].fillna(students_df['MathScore'].mean(), inplace=True)
students_df['EnglishScore'].fillna(students_df['EnglishScore'].mean(), inplace=True)

from sklearn.preprocessing import LabelEncoder


label_encoder = LabelEncoder()

students_df['Gender'] = label_encoder.fit_transform(students_df['Gender'])



students_df['TotalScore'] = students_df['MathScore'] + students_df['EnglishScore']


from scipy.stats import zscore

students_df[['MathScore', 'EnglishScore', 'TotalScore']] = students_df[['MathScore', 'EnglishScore', 'TotalScore']].apply(zscore)

students_df.to_csv('cleaned_students_data.csv', index=False)
