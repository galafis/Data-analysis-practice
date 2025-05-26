import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import os

# Create a dataset equivalent to the "college" dataset
# Based on the codebook provided in the assignment

# Set random seed for reproducibility
np.random.seed(42)

# Define major categories
major_categories = [
    "Engineering", 
    "Business", 
    "Health", 
    "Education", 
    "Humanities & Liberal Arts",
    "Social Science", 
    "Biology & Life Science", 
    "Physical Sciences", 
    "Computers & Mathematics",
    "Agriculture & Natural Resources",
    "Industrial Arts & Consumer Services",
    "Law & Public Policy",
    "Communications & Journalism",
    "Arts",
    "Psychology & Social Work",
    "Interdisciplinary"
]

# Number of majors to generate
n_majors = 173

# Generate data
data = {
    'rank': list(range(1, n_majors + 1)),
    'major_code': list(range(1001, 1001 + n_majors)),
    'major': [f"Major {i}" for i in range(1, n_majors + 1)],
    'major_category': np.random.choice(major_categories, size=n_majors),
    'total': np.random.randint(1000, 50000, size=n_majors),
    'sample_size': np.random.randint(100, 5000, size=n_majors),
}

# Create DataFrame
college = pd.DataFrame(data)

# Generate income data with intentional differences between categories
# Engineering and Business will have higher incomes
# Education and Humanities will have lower incomes
median_income_by_category = {
    "Engineering": (65000, 10000),  # (mean, std)
    "Business": (60000, 12000),
    "Health": (55000, 9000),
    "Computers & Mathematics": (62000, 11000),
    "Physical Sciences": (50000, 8000),
    "Biology & Life Science": (45000, 7000),
    "Social Science": (48000, 9000),
    "Law & Public Policy": (52000, 10000),
    "Agriculture & Natural Resources": (42000, 8000),
    "Industrial Arts & Consumer Services": (40000, 7000),
    "Education": (36000, 6000),
    "Humanities & Liberal Arts": (38000, 7000),
    "Psychology & Social Work": (40000, 6000),
    "Communications & Journalism": (42000, 8000),
    "Arts": (35000, 9000),
    "Interdisciplinary": (44000, 10000)
}

# Generate income data
college['median'] = college['major_category'].apply(
    lambda cat: np.random.normal(
        median_income_by_category[cat][0], 
        median_income_by_category[cat][1]
    )
)
college['median'] = college['median'].round().astype(int)

# Generate 25th and 75th percentiles
college['p25th'] = (college['median'] * 0.8).round().astype(int)
college['p75th'] = (college['median'] * 1.2).round().astype(int)

# Generate gender percentages
college['perc_men'] = np.random.uniform(0.1, 0.9, size=n_majors).round(3)
college['perc_women'] = (1 - college['perc_men']).round(3)

# Generate employment statistics
college['perc_employed'] = np.random.uniform(0.7, 0.95, size=n_majors).round(3)
college['perc_unemployed'] = (1 - college['perc_employed']).round(3)
college['perc_employed_fulltime'] = np.random.uniform(0.6, 0.9, size=n_majors).round(3)
college['perc_employed_parttime'] = (1 - college['perc_employed_fulltime']).round(3)
college['perc_employed_fulltime_yearround'] = np.random.uniform(0.7, 0.95, size=n_majors).round(3)

# Generate job requirement statistics
college['perc_college_jobs'] = np.random.uniform(0.5, 0.9, size=n_majors).round(3)
college['perc_non_college_jobs'] = (1 - college['perc_college_jobs']).round(3)
college['perc_low_wage_jobs'] = np.random.uniform(0.05, 0.3, size=n_majors).round(3)

# Save the dataset
college.to_csv('college_dataset.csv', index=False)

print("College dataset created and saved to 'college_dataset.csv'")
print(f"Number of records: {len(college)}")
print(f"Number of major categories: {len(college['major_category'].unique())}")
print("Major categories:", sorted(college['major_category'].unique()))
