import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import os

# Load the dataset
college = pd.read_csv('college_dataset.csv')

# Set the style for plots
plt.style.use('seaborn-v0_8-whitegrid')
sns.set(font_scale=1.2)

# Create a figure for the boxplot
plt.figure(figsize=(12, 8))
ax = sns.boxplot(x='major_category', y='median', data=college, hue='major_category', legend=False)
ax.set_title('Median Income by College Major Category', fontsize=16)
ax.set_xlabel('Major Category', fontsize=14)
ax.set_ylabel('Median Income ($)', fontsize=14)
plt.xticks(rotation=90)
plt.tight_layout()
plt.savefig('income_by_major_category_boxplot.png', dpi=300)
plt.close()

# Perform one-way ANOVA to test for significant differences between categories
categories = college['major_category'].unique()
income_by_category = [college[college['major_category'] == category]['median'] for category in categories]

# Perform ANOVA
f_stat, p_value = stats.f_oneway(*income_by_category)

# Print ANOVA results
print("One-way ANOVA Results:")
print(f"F-statistic: {f_stat:.4f}")
print(f"p-value: {p_value:.8f}")
print(f"Significant at alpha=0.05: {p_value < 0.05}")

# Calculate effect size (Eta-squared)
# Sum of squares between groups
ss_between = sum(len(group) * ((group.mean() - college['median'].mean()) ** 2) for group in income_by_category)
# Sum of squares total
ss_total = sum((college['median'] - college['median'].mean()) ** 2)
# Calculate eta-squared
eta_squared = ss_between / ss_total

print(f"\nEffect size (Eta-squared): {eta_squared:.4f}")
print("Interpretation of effect size:")
if eta_squared < 0.01:
    effect_size_interp = "Small effect"
    print("Small effect")
elif eta_squared < 0.06:
    effect_size_interp = "Medium effect"
    print("Medium effect")
else:
    effect_size_interp = "Large effect"
    print("Large effect")

# Save results to a text file
with open('statistical_analysis_results.txt', 'w') as f:
    f.write("Statistical Analysis of Association between College Major Category and Income\n")
    f.write("=" * 70 + "\n\n")
    f.write("One-way ANOVA Results:\n")
    f.write(f"F-statistic: {f_stat:.4f}\n")
    f.write(f"p-value: {p_value:.8f}\n")
    f.write(f"Significant at alpha=0.05: {p_value < 0.05}\n\n")
    f.write(f"Effect size (Eta-squared): {eta_squared:.4f}\n")
    f.write(f"Interpretation: {effect_size_interp}\n\n")
    
    f.write("Summary of Income by Major Category:\n")
    f.write(college.groupby('major_category')['median'].agg(['mean', 'median', 'std', 'min', 'max']).sort_values('mean', ascending=False).to_string())
    
print("\nResults saved to 'statistical_analysis_results.txt'")
