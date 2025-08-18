import pandas as pd

data = {
    'EmpID': [101, 102, 103, 104, 105, 106],
    'Dept': ['HR', 'IT', 'HR', 'IT', 'Sales', 'Sales'],
    'Salary': [50000, 60000, 55000, 65000, 45000, 47000]
}

df = pd.DataFrame(data)

# Find max salary per dept
max_salaries = df.groupby('Dept')['Salary'].transform('max')

# Filter employees with max salary in their dept
top_earners = df[df['Salary'] == max_salaries]

# Rename columns
top_earners = top_earners.rename(columns={'EmpID': 'MaxSalaryEmpID', 'Salary': 'MaxSalary'})

# Select only relevant columns
result_df = top_earners[['Dept', 'MaxSalaryEmpID', 'MaxSalary']]

print(result_df)
