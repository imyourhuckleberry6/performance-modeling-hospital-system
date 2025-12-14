Comprehensive Hospital Resource Allocation System Analysis

1.	System Description
The selected system is a Hospital Emergency Treatment center for patients that represents the process of patients coming into the center for treatment and their experience while there. This synthetic dataset recorded the visit time and day of patients, their urgency level of needing treatment and how the emergency treatment center handles them in a systematic way.

2.	Dataset Description
This system is supported by a dataset which contained the information of multiple hospital emergency treatment centers around urban and rural country areas. For the sake of this analysis, the dataset is cleaned and organized by the proceedings of only a single emergency treatment unit and its activities. This allows the user to closely analyze the goings in this selected center and analyze its bottlenecks and optimization of activities. 1023 individual unique entries are given for this analysis of the center.

2.1 ER Wait Time Dataset (ER Wait Time Dataset.csv)
Include entries on patient data, their level of urgency as well has going on’s in the emergency unit for each day.
Key attributes:
Visit day: date of the patient’s arrival to the unit
Time of day: when the patients arrived
Urgency level: how critical the patient is in need of treatment
Nurse-to-Patient Ratio: how many nurses are available to take care of patient
Specialist Availability: how many specialists are available
Facility Size (Beds): how many beds are available
Time to Registration (min), Triage, Medical professional: how much time the patient took in each stage of the care process
Patient outcome: were the patient discharged or admitted
Satisfaction: how satisfied the patient were with their treatment in the unit
2.2	ER Wait Time Dataset Original (ER Wait Time Dataset – unaltered original.csv)
This is the original dataset gotten for the analysis before it was cleaned and organized. It is included only for completion purposes and does not serve any standing value for the tests.

6.	Methodology
   
The analysis is done in a phased, data driven approach by using Python as the standard language for data analysis and its libraries (Pandas, Numpy, SciPy, mathplotlib) to do five analysis tests with goals in mind.

6.1	Arrival Process analysis
Determine if the patient arrival follow a Poisson process with exponential inter-arrival times.
Method: convert ‘visit date’ column to timestamps and calculate the time difference between consecutive patients (inter-arrival times). Plot the findings to a histogram and try to overlay the theoretical exponential curve which shows perfect Poisson process over the actual data.
Estimations:


6.2	Load Variation Analysis
Using ‘day of week’ and ‘time of day’ entries, Identify periods of peak load (non-stationary) across different time categories. This helps us understand the arrival rate lambda changes over time in the unit.
Method: use descriptive analytics with a categorical frequency distribution methodology. Group data by ‘time of day’ and ‘day of week’ values and calculate the number of arrivals per time and day. Do frequency count on day of week values and time of day. Summarize on graph by count.

6.3	Stage Wise Delay Decomposition
Analyze each waiting stages contribution to the overall wait time of the patients.
Method: calculate the mean and variance for ‘time to registration’, ‘time to triage’, ‘time to medical professional’. Identify the key bottleneck area in the process. See which area needs more servers. For each stage calculate the mean delay, standard deviation. Identify bottlenecks using highest mean delay and high standard deviation which suggest wait time varying widely.

6.4	Priority Queuing Validation
Analyze the effectiveness of the emergency unit’s priority queuing servicing to the patients.  The system need to prioritize critical patients first than lesser urgent patients.
Method: group by ‘urgency level’ and compare the mean ‘total wait time and ‘time to medical professional’ values. Get standard deviation to see spread of wait times within each level.
6.5	Impact of Server Capacity
Examine the empirical connection between resource levels and patient waiting time. This will be used to evaluate how staff levels affect wait times in the unit.
Method: use queuing theory where servers are nurses and specialists. use ‘nurse to patient ratio’, ‘specialist availability’ and mean ‘total wait time’ and create a correlation between them. Nurse to patient ratio is sorted by ascending order of ratio and specialists are grouped by 0-10 scale and sorted in ascending order the same way. Graph based on total wait time to ratio on a 0 to 10 scale.

6.6	Little’s Law
This helps us verify if the system is in a stable state.
Method: calculate average arrival rates (patients/hour) and average wait time W using ‘total wait time’. Do computation L = lambda x W to estimate the average number of patients in the system.
