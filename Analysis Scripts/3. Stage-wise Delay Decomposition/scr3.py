import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

file_path = 'ER Wait Time Dataset.csv'
df = pd.read_csv(file_path)

#define the delay columns for analysis
delay_cols = [
    'Time to Registration (min)',
    'Time to Triage (min)',
    'Time to Medical Professional (min)'
]

# Calculate descriptive statistics (mean and standard deviation)
analysis_data = df[delay_cols].agg(['mean', 'std']).T
analysis_data.columns = ['Mean Delay (min)', 'Standard Deviation (min)']

# Rename index for cleaner output, plotting
analysis_data.index = [
    'Registration', 
    'Triage', 
    'Medical Professional'
]

#Prepare the text output
output_text = (
    "--Stage-wise Delay Decomposition Results--\n\n"
    "Mean and Standard Deviation of Delay at each Stage:\n"
    f"{analysis_data.to_string()}\n\n"
)

# Print and Write to text file
print(output_text)
with open('delay_decomposition_results.txt', 'w') as f:
    f.write(output_text)

#Generate the plot
# Prepare data for plotting
means = analysis_data['Mean Delay (min)']
stds = analysis_data['Standard Deviation (min)']
stages = analysis_data.index

plt.figure(figsize=(10, 6))

# Create bar chart with error bars
bars = plt.bar(stages, means, yerr=stds, capsize=5, color=['skyblue', 'salmon', 'lightgreen'], edgecolor='black')

# Add values on top of the bars
for bar in bars:
    yval = bar.get_height()
    # Position text slightly above the bar height + error bar
    plt.text(bar.get_x() + bar.get_width()/2, yval + (stds.iloc[bars.index(bar)] * 0.1), 
             f'{yval:.2f}', ha='center', va='bottom', fontsize=10)

plt.title('Stage-wise Delay Decomposition (Mean Wait Times)')
plt.xlabel('ER Process Stage')
plt.ylabel('Delay in Stage (minutes)')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.ylim(0, means.max() * 1.2) # Set y-limit higher to accommodate text
plt.xticks(rotation=0) 

# Save the plot
plt.savefig('delay_decomposition_plot.png')