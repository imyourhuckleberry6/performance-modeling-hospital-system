import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

file_path = 'ER Wait Time Dataset.csv'
df = pd.read_csv(file_path)

# 1. Analysis for Nurse-to-Patient Ratio
nurse_analysis = df.groupby('Nurse-to-Patient Ratio')['Total Wait Time (min)'].mean().reset_index()
nurse_analysis.rename(columns={'Total Wait Time (min)': 'Mean Wait Time (min)'}, inplace=True)
nurse_analysis = nurse_analysis.sort_values('Nurse-to-Patient Ratio')

# 2. Analysis for Specialist Availability
specialist_analysis = df.groupby('Specialist Availability')['Total Wait Time (min)'].mean().reset_index()
specialist_analysis.rename(columns={'Total Wait Time (min)': 'Mean Wait Time (min)'}, inplace=True)
specialist_analysis = specialist_analysis.sort_values('Specialist Availability')

#prepare text output
output_text = (
    "-Impact of Server Capacity Analysis Results--\n\n"
    "A. Mean Total Wait Time vs. Nurse-to-Patient Ratio:\n"
    f"{nurse_analysis.to_string(index=False)}\n\n"
    "B. Mean Total Wait Time vs. Specialist Availability (0-10 Scale):\n"
    f"{specialist_analysis.to_string(index=False)}\n\n"
)

# Print and Write to text file
print(output_text)
with open('server_capacity_results.txt', 'w') as f:
    f.write(output_text)

#Generate the plot
fig, axes = plt.subplots(1, 2, figsize=(16, 6))
fig.suptitle('Impact of Server Capacity on Mean Total Wait Time', fontsize=16)

# Plot 1: Nurse-to-Patient Ratio
bars1 = axes[0].bar(nurse_analysis['Nurse-to-Patient Ratio'].astype(str), nurse_analysis['Mean Wait Time (min)'], color='teal', edgecolor='black')
axes[0].set_title('A. Mean Wait Time by Nurse-to-Patient Ratio')
axes[0].set_xlabel('Nurse-to-Patient Ratio (Lower is Better Staffing)')
axes[0].set_ylabel('Mean Total Wait Time (minutes)')
axes[0].grid(axis='y', linestyle='--', alpha=0.7)
# Add data labels
for bar in bars1:
    yval = bar.get_height()
    axes[0].text(bar.get_x() + bar.get_width()/2, yval + 2, f'{yval:.1f}', ha='center', va='bottom', fontsize=10)


# Plot 2: Specialist Availability
bars2 = axes[1].bar(specialist_analysis['Specialist Availability'].astype(str), specialist_analysis['Mean Wait Time (min)'], color='purple', edgecolor='black')
axes[1].set_title('B. Mean Wait Time by Specialist Availability')
axes[1].set_xlabel('Specialist Availability (0-10 Scale, Higher is Better)')
axes[1].set_ylabel('Mean Total Wait Time (minutes)')
axes[1].grid(axis='y', linestyle='--', alpha=0.7)
# Add data labels
for bar in bars2:
    yval = bar.get_height()
    axes[1].text(bar.get_x() + bar.get_width()/2, yval + 2, f'{yval:.1f}', ha='center', va='bottom', fontsize=10)

# Set common y axis limit for easy comparison
max_wait = max(nurse_analysis['Mean Wait Time (min)'].max(), specialist_analysis['Mean Wait Time (min)'].max())
axes[0].set_ylim(0, max_wait * 1.15)
axes[1].set_ylim(0, max_wait * 1.15)


plt.tight_layout(rect=[0, 0.03, 1, 0.95]) 
plt.savefig('server_capacity_plot.png')