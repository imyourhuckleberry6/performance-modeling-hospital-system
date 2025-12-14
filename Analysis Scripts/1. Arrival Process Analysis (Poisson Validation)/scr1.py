import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import expon

def analyze_arrival_process(file_path):
    df = pd.read_csv(file_path)
    print("Dataset loaded successfully.")

    #1. preprocess Data
    #convert 'visit date' to datetime objects
    df['Visit Date'] = pd.to_datetime(df['Visit Date'], errors='coerce')
    
    #to drop rows with invalid dates
    df = df.dropna(subset=['Visit Date'])

    #sort by arrival time (for inter-arrival calculation)
    df = df.sort_values('Visit Date')

    #2. CAlculate Statistics
    # Calculate difference between current and previous rows time
    df['Inter-Arrival Time (min)'] = df['Visit Date'].diff().dt.total_seconds() / 60

    #remove the first row
    inter_arrival_times = df['Inter-Arrival Time (min)'].dropna()

    # Calculate Mean inter-arriival Time (1/lambda)
    mean_inter_arrival = inter_arrival_times.mean()
    
    # Calculate Arrival Rate lambda (patients per minute)
    arrival_rate_lambda = 1 / mean_inter_arrival 

    # 3. Generate Text Report
    output_text = (
        "--- Arrival Process Analysis Results ---\n"
        f"Total Observations: {len(inter_arrival_times)}\n"
        f"Mean Inter-Arrival Time: {mean_inter_arrival:.2f} minutes\n"
        f"Arrival Rate (lambda): {arrival_rate_lambda:.5f} patients/minute\n"
        f"Arrival Rate (hourly): {arrival_rate_lambda * 60:.2f} patients/hour\n"
    )

    print(output_text)

    # Save to txt file
    with open('arrival_analysis_results.txt', 'w') as f:
        f.write(output_text)
    print("Results saved to 'arrival_analysis_results.txt'")

    # 4. Generate and Save Graph
    plt.figure(figsize=(10, 6))

    # Histogram of data
    plt.hist(inter_arrival_times, bins=20, density=True, alpha=0.6, color='skyblue', edgecolor='black', label='Actual Data')

    #Theoretical Exponential Distribution Curve
    #this generate x-values for the curve
    x = np.linspace(0, inter_arrival_times.max(), 100)
    #callculate PDF: lambda * exp(-lambda * x)
    pdf = expon.pdf(x, scale=1/arrival_rate_lambda) 

    plt.plot(x, pdf, 'r-', lw=2, label=f'Theoretical Exponential (λ={arrival_rate_lambda:.4f})')

    plt.title('Arrival Process Analysis: Inter-Arrival Times')
    plt.xlabel('Inter-Arrival Time (minutes)')
    plt.ylabel('Probability Density')
    plt.legend()
    plt.grid(True, alpha=0.3)

    # Save Plot
    plt.savefig('arrival_distribution_plot.png')
    print("Graph saved to 'arrival_distribution_plot.png'")

if __name__ == "__main__":
    analyze_arrival_process('ER Wait Time Dataset.csv')