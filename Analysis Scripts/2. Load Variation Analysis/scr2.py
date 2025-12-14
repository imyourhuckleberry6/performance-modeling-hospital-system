import pandas as pd
import matplotlib.pyplot as plt

file_path = 'ER Wait Time Dataset.csv'
df = pd.read_csv(file_path)

# 1. LOad Variation by Day of Week
#define order to ensure days are plotted correctly
day_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
day_counts = df['Day of Week'].value_counts().reindex(day_order, fill_value=0)

# 2. Load Variation by Time of Day
# define logical time order
time_order = ['Early Morning','Late Morning', 'Afternoon', 'Evening','Night']
time_counts = df['Time of Day'].value_counts().reindex(time_order, fill_value=0)

# prepare output to text
output_text = (
    "---Load Variation Analysis Results---\n\n"
    "A. Patients by Day of Week:\n"
    f"{day_counts.to_string()}\n\n"
    "B. Patients by Time of Day:\n"
    f"{time_counts.to_string()}\n"
)

#print and Write to text file
print(output_text)
with open('load_variation_results.txt', 'w') as f:
    f.write(output_text)

#Generate the combined plot
# Creates a single figure with two subplots side by side
fig, axes = plt.subplots(1, 2, figsize=(15, 6))
fig.suptitle('Patient Arrival Load Variation', fontsize=16)

# Plot 1: Day of Week
day_counts.plot(kind='bar', ax=axes[0], color='skyblue', edgecolor='black')
axes[0].set_title('A. Total Patients by Day of Week')
axes[0].set_xlabel('Day of Week')
axes[0].set_ylabel('Number of Patients (Count)')
axes[0].tick_params(axis='x', rotation=45)
axes[0].grid(axis='y', linestyle='--', alpha=0.7)

# Plot 2: Time of Day
time_counts.plot(kind='bar', ax=axes[1], color='salmon', edgecolor='black')
axes[1].set_title('B. Total Patients by Time of Day')
axes[1].set_xlabel('Time of Day')
axes[1].set_ylabel('Number of Patients (Count)')
axes[1].tick_params(axis='x', rotation=45)
axes[1].grid(axis='y', linestyle='--', alpha=0.7)

plt.tight_layout(rect=[0, 0.03, 1, 0.95]) # To adjust lsyout
plt.savefig('load_variation_plot.png')