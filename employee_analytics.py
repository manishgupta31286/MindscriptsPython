import numpy as np

employee_data = np.array([
    [101, 25, 35000, 3],
    [102, 30, 45000, 5],
    [103, 28, 55000, 4],
    [104, 35, 65000, 8],
    [105, 40, 75000, 10],
    [106, 32, 48000, 6],
    [107, 29, 52000, 4],
    [108, 45, 85000, 15],
    [109, 38, 70000, 12],
    [110, 26, 40000, 2]
])

emp_ids = employee_data[:, 0]
age = employee_data[:, 1]
salary = employee_data[:, 2]
experience = employee_data[:, 3]

print("Employee IDs:", emp_ids)
print("Ages:", age)
print("Salaries:", salary)
print("Experience:", experience)
print("Total employees:", len(employee_data))
print("Total columns:", employee_data.shape[1])
print("Shape:", employee_data.shape)
print("Dimensions:", employee_data.ndim)
print("Data type:", employee_data.dtype)
print("Size:", employee_data.size)

print("Average age:", np.mean(age))
print("Average salary:", np.mean(salary))
print("Average experience:", np.mean(experience))
print("Maximum salary:", np.max(salary))
print("Minimum salary:", np.min(salary))

print("Employees with salary > 50000:")
print(employee_data[salary > 50000])
print("Employees with salary > 60000:")
print(employee_data[salary > 60000])
print("Employees with age > 30:")
print(employee_data[age > 30])
print("Employees with experience > 5:")
print(employee_data[experience > 5])
print("Employees with age < 30:")
print(employee_data[age < 30])
print("Employees with salary < 50000:")
print(employee_data[salary < 50000])
print("Employees with experience >= 10:")
print(employee_data[experience >= 10])
print("Employees with salary between 50000 and 70000:")
print(employee_data[(salary >= 50000) & (salary <= 70000)])
print("Employees aged between 25 and 35:")
print(employee_data[(age >= 25) & (age <= 35)])
print("Employees with age > 30 and salary > 60000:")
print(employee_data[(age > 30) & (salary > 60000)])

print("Count employees earning more than 50000:", np.sum(salary > 50000))
print("Count employees earning less than 50000:", np.sum(salary < 50000))
print("Count employees with experience > 5:", np.sum(experience > 5))
print("Count employees older than 35:", np.sum(age > 35))
print("Count employees with salary above average salary:", np.sum(salary > np.mean(salary)))

print("Salaries ascending:", np.sort(salary))
print("Salaries descending:", np.sort(salary)[::-1])
print("Ages ascending:", np.sort(age))
print("Experience descending:", np.sort(experience)[::-1])
print("Top 3 highest salaries:", np.sort(salary)[-3:][::-1])

print("Employee with highest salary:", employee_data[np.argmax(salary)])
print("Employee with lowest salary:", employee_data[np.argmin(salary)])
print("Employee with highest experience:", employee_data[np.argmax(experience)])
print("Employee with lowest experience:", employee_data[np.argmin(experience)])
print("Index of employee with salary 75000:", np.where(salary == 75000)[0])

print("Total salary paid:", np.sum(salary))
print("Total years of experience:", np.sum(experience))
print("Median salary:", np.median(salary))
print("Median age:", np.median(age))
print("Standard deviation of salaries:", np.std(salary))

print("Employees eligible for promotion (salary < 70000 and experience > 5):")
print(employee_data[(salary < 70000) & (experience > 5)])
print("Employees eligible for bonus (salary > 50000 and experience > 3):")
print(employee_data[(salary > 50000) & (experience > 3)])

salary_hike_10 = salary.astype(float) * 1.10
salary_hike_20 = salary.astype(float).copy()
salary_hike_20[experience > 10] *= 1.20
print("10% salary hike to all employees:", salary_hike_10)
print("20% salary hike to employees with experience > 10:", salary_hike_20)
print("Annual salary (monthly salary * 12):", salary * 12)
print("Annual bonus (15% of salary):", salary * 0.15)
print("Highest paid experienced employee:", employee_data[np.argmax(salary * (experience > 0))])
print("Youngest employee:", employee_data[np.argmin(age)])
print("Oldest employee:", employee_data[np.argmax(age)])
print("Average salary of employees older than 35:", np.mean(salary[age > 35]))
print("Average salary of employees younger than 30:", np.mean(salary[age < 30]))
print("Salary difference between highest and lowest paid employee:", np.max(salary) - np.min(salary))
print("Employees earning above average salary:", employee_data[salary > np.mean(salary)])
print("Employees earning below average salary:", employee_data[salary < np.mean(salary)])
print("Employees with experience above average experience:", employee_data[experience > np.mean(experience)])

print("Correlation Age and Salary:", np.corrcoef(age, salary)[0, 1])
print("Correlation Experience and Salary:", np.corrcoef(experience, salary)[0, 1])
print("Salary variance:", np.var(salary))
print("Salary percentile 25:", np.percentile(salary, 25))
print("Salary percentile 50:", np.percentile(salary, 50))
print("Salary percentile 75:", np.percentile(salary, 75))
print("Employees above 75th percentile salary:", employee_data[salary > np.percentile(salary, 75)])

salary_min = salary.min()
salary_max = salary.max()
normalized_salary = (salary - salary_min) / (salary_max - salary_min)
print("Normalized salaries:", normalized_salary)

z_scores = (salary - np.mean(salary)) / np.std(salary)
print("Z-score of salaries:", z_scores)

mean_salary = np.mean(salary)
std_salary = np.std(salary)
z_scores = (salary - mean_salary) / std_salary
print("Mean salary:", mean_salary)
print("Salary standard deviation:", std_salary)
print("Z-scores of salaries:", z_scores)

outlier_threshold = 2
outliers = salary[(z_scores > outlier_threshold) | (z_scores < -outlier_threshold)]
print("Salary outliers using Z-score:", outliers)

print("Age and Salary columns:")
print(employee_data[:, [1, 2]])
print("Salary and Experience columns:")
print(employee_data[:, [2, 3]])
print("Reshaped salary array:", salary.reshape(5, 2))
print("Flattened dataset:", employee_data.flatten())
print("Transposed dataset:")
print(employee_data.T)

print("Second highest salary:", np.sort(salary)[-2])
print("Third highest salary:", np.sort(salary)[-3])
print("Second lowest salary:", np.sort(salary)[1])
print("Employee closest to average salary:", employee_data[np.argmin(np.abs(salary - np.mean(salary)))])
print("Employee farthest from average salary:", employee_data[np.argmax(np.abs(salary - np.mean(salary)))])

salary_fixed = salary.copy()
salary_fixed[salary_fixed < 50000] = 50000
print("Salaries below 50000 replaced with 50000:", salary_fixed)

bonus = salary * 0.10
annual_salary = salary * 12
employee_data_bonus = np.column_stack((employee_data, bonus, annual_salary))
print("Dataset with Bonus and Annual Salary columns:")
print(employee_data_bonus)

payroll_share = salary / np.sum(salary) * 100
print("Employee payroll contribution %:", payroll_share)
print("Payroll distribution:", np.sort(salary))
print("Rank employees by salary:", np.argsort(salary))
print("Rank employees by experience:", np.argsort(experience))
print("Top 5 experienced employees:", employee_data[np.argsort(experience)[-5:]])
print("Top 5 highest paid employees:", employee_data[np.argsort(salary)[-5:]])
print("Next year's salary after 8% increment:", salary * 1.08)

print("Payroll cost of company:", np.sum(salary))
print("Average employee age:", np.mean(age))
print("Average employee experience:", np.mean(experience))
print("High-value employees (salary > average):", employee_data[salary > np.mean(salary)])

salary_bands = np.where(salary < 50000, 'Low', np.where(salary < 70000, 'Medium', 'High'))
print("Salary bands:", salary_bands)
print("HR report:")
print({
    "Total employees": len(employee_data),
    "Average salary": np.mean(salary),
    "Average age": np.mean(age),
    "Average experience": np.mean(experience),
    "Highest salary": np.max(salary),
    "Lowest salary": np.min(salary)
})

retention_risk = np.where((age > 35) & (experience < 5), 'High', 'Low')
print("Retention risk:", retention_risk)
print("Workforce age distribution:", np.bincount(age.astype(int)))

print("Complete Employee Analytics Report:")
print("- Total Employees:", len(employee_data))
print("- Average Age:", np.mean(age))
print("- Average Salary:", np.mean(salary))
print("- Average Experience:", np.mean(experience))
print("- Highest Salary:", np.max(salary))
print("- Lowest Salary:", np.min(salary))
print("- Employees above average salary:", np.sum(salary > np.mean(salary)))
print("- Employees with experience > 5:", np.sum(experience > 5))
