# Shodan Port 104 Analysis

Small cybersecurity project using Shodan data to look at hosts with port 104 exposed. Port 104 is commonly associated with DICOM, which is used in medical imaging systems.

## What I did

- Used the Shodan API to search port 104
- Collected country, organization, port, and timestamp data
- Removed IP addresses from the public dataset
- Used Python and pandas to analyze the results
- Used matplotlib to visualize the data

## Results

The results show which countries and organizations appeared most often in the dataset.

<img width="713" height="457" alt="port104_results_by_country" src="https://github.com/user-attachments/assets/731d4267-f564-4287-823e-65425ab436a3" />

<img width="787" height="462" alt="port104_top_organizations" src="https://github.com/user-attachments/assets/bef16c67-00f6-4fcf-9d32-645cac227ce0" />


## Files

- `dicom_search.py` - Shodan search script
- `shodan_visualizations.ipynb` - data analysis and visualizations
- `data/port104_sanitized.csv` - dataset with IP addresses removed

## Tools

Python, Shodan API, pandas, matplotlib, Jupyter
