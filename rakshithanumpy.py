# Import NumPy
import numpy as np

# 1. Create a NumPy array from 1 to 20
arr = np.arange(1, 21)
print("Original Array:\n", arr)

# 2. Reshape into 4x5 matrix
matrix = arr.reshape(4, 5)
print("\n4x5 Matrix:\n", matrix)

# 3. Mean, Median, Standard Deviation
mean = np.mean(arr)
median = np.median(arr)
std_dev = np.std(arr)

print("\nMean:", mean)
print("Median:", median)
print("Standard Deviation:", std_dev)

# 4. Extract even numbers
even_numbers = arr[arr % 2 == 0]
print("\nEven Numbers:\n", even_numbers)

# 5. Random 5x5 matrix and transpose
random_matrix = np.random.rand(5, 5)
transpose_matrix = random_matrix.T

print("\nRandom 5x5 Matrix:\n", random_matrix)
print("\nTranspose Matrix:\n", transpose_matrix)

# Import Pandas
import pandas as pd

# 1. Load CSV
df = pd.read_csv("student_data.csv")

# 2. Display first 5 and last 5 records
print("First 5 Records:\n", df.head())
print("\nLast 5 Records:\n", df.tail())

# 3. Check for missing values
print("\nMissing Values:\n", df.isnull().sum())

# Handle missing values (fill with column mean)
df.fillna(df.mean(numeric_only=True), inplace=True)

# 4. Calculate average marks
df["Average"] = df[["Math", "Science", "English"]].mean(axis=1)

# 5. Student with highest average
top_student = df.loc[df["Average"].idxmax()]
print("\nTop Student:\n", top_student)

# 6. Students scoring more than 75 in Math
math_above_75 = df[df["Math"] > 75]
print("\nStudents scoring >75 in Math:\n", math_above_75)

# 7. Add Result column
df["Result"] = df["Average"].apply(lambda x: "Pass" if x >= 40 else "Fail")

print("\nUpdated DataFrame:\n", df.head())
# Import matplotlib
import matplotlib.pyplot as plt

# 1. Bar Chart (Student vs Average)
plt.figure(figsize=(8,5))
plt.bar(df["Name"], df["Average"])
plt.title("Student Average Marks")
plt.xlabel("Student Name")
plt.ylabel("Average Marks")
plt.xticks(rotation=45)
plt.show()


# 2. Pie Chart (Pass vs Fail)
result_counts = df["Result"].value_counts()

plt.figure(figsize=(6,6))
plt.pie(result_counts, labels=result_counts.index, autopct="%1.1f%%")
plt.title("Pass vs Fail Distribution")
plt.show()


# 3. Line Graph (Marks Comparison)
plt.figure(figsize=(8,5))
plt.plot(df["Name"], df["Math"], marker='o', label="Math")
plt.plot(df["Name"], df["Science"], marker='o', label="Science")
plt.plot(df["Name"], df["English"], marker='o', label="English")

plt.title("Marks Comparison")
plt.xlabel("Student Name")
plt.ylabel("Marks")
plt.legend()
plt.xticks(rotation=45)
plt.show()
