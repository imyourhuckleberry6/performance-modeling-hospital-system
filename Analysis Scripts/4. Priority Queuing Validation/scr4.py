import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

file_path = 'ER Wait Time Dataset.csv'
df = pd.read_csv(file_path)

#define the logical order for Urgency Level (Priority levels)
urgency_order = ['Critical', 'High', 'Medium', 'Low']

#group by Urgency Level and calculate mean and standard deviation of Total Wait Time
analysis_data = df.groupby('Urgency Level')['Total Wait Time (min)'].agg(['mean', 'std']).reindex(urgency_order)
analysis_data.columns = ['Mean Total Wait Time (min)', 'Standard Deviation (min)']

#Prepare the text output
output_text = (
    "--- Priority Queuing Validation Results ---\n\n"
    "Mean and Standard Deviation of Total Wait Time by Urgency Level:\n"
    f"{analysis_data.to_string()}\n\n"
)

# Print and Write to text file
print(output_text)
with open('priority_queuing_results.txt', 'w') as f:
    f.write(output_text)

#Generate the plot
# Prepare data for plotting
means = analysis_data['Mean Total Wait Time (min)']
stds = analysis_data['Standard Deviation (min)'].fillna(0) 

plt.figure(figsize=(10, 6))

# Define colors based on urgency
colors = ['firebrick', 'red', 'orange', 'lightcoral']
color_map = {level: color for level, color in zip(urgency_order, colors)}
bar_colors = [color_map.get(level, 'gray') for level in means.index]

# Create bar chart with error bars
bars = plt.bar(means.index, means, yerr=stds, capsize=5, color=bar_colors, edgecolor='black')

# Add values on top of the bars
for i, bar in enumerate(bars):
    yval = bar.get_height()
    # Position text slightly above the bar height + error bar
    plt.text(bar.get_x() + bar.get_width()/2, yval + (stds.iloc[i] + 2 if yval > 0 else 2), 
             f'{yval:.2f}', ha='center', va='bottom', fontsize=10)

plt.title('Priority Queuing Validation: Total Wait Time by Urgency Level')
plt.xlabel('Urgency Level (Priority)')
plt.ylabel('Mean Total Wait Time (minutes)')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.xticks(rotation=0)

#adjust y-limit
plt.ylim(0, means.max() * 1.25)

# ave the plot
plt.savefig('priority_queuing_plot.png')