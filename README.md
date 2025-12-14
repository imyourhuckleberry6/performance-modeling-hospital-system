Comprehensive Hospital Resource Allocation System Analysis

1.	System Description
The selected system is a Hospital Emergency Treatment center for patients that represents the process of patients coming into the center for treatment and their experience while there. This synthetic dataset recorded the visit time and day of patients, their urgency level of needing treatment and how the emergency treatment center handles them in a systematic way.

2.	Dataset Description
This system is supported by a dataset which contained the information of multiple hospital emergency treatment centers around urban and rural country areas. For the sake of this analysis, the dataset is cleaned and organized by the proceedings of only a single emergency treatment unit and its activities. This allows the user to closely analyze the goings in this selected center and analyze its bottlenecks and optimization of activities. 1023 individual unique entries are given for this analysis of the center.
Dataset used can be found at:
https://github.com/imyourhuckleberry6/performance-modeling-hospital-system

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
