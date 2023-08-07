import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the student data from CSV
data = pd.read_csv('student_data.csv')

# Explore the dataset and understand its structure
print(data.head())  # Display the first few rows of the dataset

# Calculate the correlation between study time and exam scores
correlation = data['StudyTime'].corr(data['ExamScore'])

# Print the correlation value
print(f"Correlation between Study Time and Exam Scores: {correlation:.2f}")

# Scatter plot to visualize the relationship between study time and exam scores
plt.figure(figsize=(8, 6))
plt.scatter(data['StudyTime'], data['ExamScore'])
plt.xlabel('Study Time (hours)')
plt.ylabel('Exam Score')
plt.title('Study Time vs. Exam Scores')
plt.show()

# Use seaborn's regplot to visualize the relationship with a regression line
plt.figure(figsize=(8, 6))
sns.regplot(x='StudyTime', y='ExamScore', data=data)
plt.xlabel('Study Time (hours)')
plt.ylabel('Exam Score')
plt.title('Study Time vs. Exam Scores with Regression Line')
plt.show()

# Box plot to visualize the distribution of exam scores at different study time levels
plt.figure(figsize=(8, 6))
sns.boxplot(x='StudyTime', y='ExamScore', data=data)
plt.xlabel('Study Time (hours)')
plt.ylabel('Exam Score')
plt.title('Distribution of Exam Scores at Different Study Time Levels')
plt.show()
