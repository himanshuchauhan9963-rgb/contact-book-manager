# Question 1: Iterator & Generator Challenge
from collections import deque

def moving_average(iterable, n):
    it = iter(iterable)
    window = deque(maxlen=n)
    for num in it:
        window.append(num)
        if len(window) == n:
            yield sum(window) / n

# Question 2: Lambda & Functional Programming
students = [
    {'name': 'Alice', 'math': 90, 'science': 85},
    {'name': 'Bob', 'math': 90, 'science': 85},
    {'name': 'Charlie', 'math': 80, 'science': 95}
]

sorted_students = sorted(
    students,
    key=lambda s: (-(s['math'] + s['science']), s['name'])
)

# Question 3: Dictionary & Set Comprehension
import re
from collections import Counter

def word_frequency(paragraph):
    words = re.findall(r'\b\w+\b', paragraph.lower())
    counts = Counter(words)
    return {word: freq for word, freq in counts.items() if freq > 1}

# Question 4: itertools Combinatorics Problem
from itertools import combinations

ingredients = ["egg", "milk", "flour", "sugar", "butter"]

def valid_combinations(ingredients):
    return [
        combo for combo in combinations(ingredients, 3)
        if 'egg' in combo and 'butter' not in combo
    ]

# Question 5: File Handling & Exception Handling
try:
    import pandas as pd
except ImportError:
    print("Pandas is not installed. Please run: pip install pandas")
    exit(1)
import os

class FileMissingError(Exception):
    pass

class MissingColumnError(Exception):
    pass

def merge_csv(file1, file2, output_file):
    if not os.path.exists(file1):
        raise FileMissingError(f"{file1} is missing.")
    if not os.path.exists(file2):
        raise FileMissingError(f"{file2} is missing.")

    df1 = pd.read_csv(file1)
    df2 = pd.read_csv(file2)

    if 'id' not in df1.columns:
        raise MissingColumnError(f"'id' column missing in {file1}")
    if 'id' not in df2.columns:
        raise MissingColumnError(f"'id' column missing in {file2}")

    merged = pd.merge(df1, df2, on='id')
    merged.to_csv(output_file, index=False)

# Sample test calls
if __name__ == "__main__":
    print("Question 1 - Moving Average:")
    print(list(moving_average([1, 2, 3, 4, 5], 3)))

    print("\nQuestion 2 - Sorted Students:")
    print(sorted_students)

    print("\nQuestion 3 - Word Frequency:")
    paragraph = "Hello, hello world! This is a test. Hello again, world."
    print(word_frequency(paragraph))

    print("\nQuestion 4 - Valid Combinations:")
    print(valid_combinations(ingredients))

    print("\nQuestion 5 - Merge CSV:")
    # Uncomment and set your CSV paths to test
    # try:
    #     merge_csv("file1.csv", "file2.csv", "output.csv")
    #     print("CSV files merged successfully.")
    # except Exception as e:
    #     print("Error:", e)
