import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

file_path = 'ER Wait Time Dataset.csv'
df = pd.read_csv(file_path)

#1. Calculate W (Average Wait Time in the System)
W = df['Total Wait Time (min)'].mean()

# 2. Calculate Lambda (Average Arrival Rate)
# Convert 'visit date' to datetime objects
df['Visit Date'] = pd.to_datetime(df['Visit Date'])
df = df.sort_values('Visit Date')

# Calculate inter-arrival times in minutes
df['Inter-Arrival Time (min)'] = df['Visit Date'].diff().dt.total_seconds() / 60
inter_arrival_times = df['Inter-Arrival Time (min)'].dropna()

# Calculate Mean Inter-Arrival Time
mean_inter_arrival = inter_arrival_times.mean()

# Calculate Arrival Rate lambda (patients per minute)
if mean_inter_arrival > 0:
    lambda_rate = 1 / mean_inter_arrival
else:
    lambda_rate = 0
    
# 3. Calculate L (Theoretical Average Number of Patients in the System)
L_theoretical = lambda_rate * W

# prepare text output
output_text = (
    "-Little's Law Verification Results (L = \lambda W)-\n\n"
    "1. Average System Time (W):\n"
    f"   W = {W:.2f} minutes (Average Total Wait Time)\n\n"
    "2. Average Arrival Rate (lambda):\n"
    f"   Mean Inter-Arrival Time = {mean_inter_arrival:.2f} minutes\n"
    f"   lambda = {lambda_rate:.5e} patients/minute\n"
    f"   lambda (hourly) = {lambda_rate * 60:.4f} patients/hour\n\n"
    "3. Theoretical Average Patients in System (L):\n"
    f"   L_theoretical = lambda * W = {L_theoretical:.2f} patients\n"
)

# Print and Write to txt file
print(output_text)
with open('little_law_results.txt', 'w') as f:
    f.write(output_text)

# 5. Generate the plot
plt.figure(figsize=(8, 5))
plt.bar(['Average Total Wait Time (W)'], [W], color='darkred', edgecolor='black')

# Add data label
plt.text(0, W + 2, f'{W:.2f} min', ha='center', va='bottom', fontsize=12, fontweight='bold')

plt.title("Little's Law Component: Average System Time (W)")
plt.ylabel('Mean Total Wait Time (minutes)')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.ylim(0, W * 1.2)

#Save the plot
plt.savefig('little_law_plot.png')