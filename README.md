# Aadhaar Demographic Update Analysis  
UIDAI Data Hackathon 2026

## Overview
This repository contains the Python-based data analysis performed as part of the UIDAI Data Hackathon 2026. The project focuses on unlocking societal and behavioral trends from Aadhaar Demographic Update data and translating them into meaningful insights that can support informed administrative decision-making and system improvements.

Aadhaar demographic updates such as changes in personal and contact details reflect life events, mobility, and digital behavior of citizens. By analyzing these updates across time and geography, this study aims to understand how residents interact with the Aadhaar ecosystem beyond initial enrolment.

---

## Dataset
- Dataset Name: Aadhaar Demographic Update Dataset  
- Source: UIDAI via Data.gov.in  
- Dataset Type: High Value Dataset (HVD)  
- Granularity:
  - Time: Date / Monthly
  - Geography: State, District, Pincode
  - Age Groups: 5–17 years and 17 years & above

The dataset provides aggregated counts of demographic updates performed by Aadhaar holders. The dataset itself is not included in this repository due to size and data-sharing constraints.

---

## Analysis Performed
The following analyses were carried out in this project:

- Data cleaning and preprocessing  
- Age-wise demographic update analysis  
- Time-series trend analysis with moving averages  
- Month-on-month growth rate analysis  
- District-wise demographic update distribution  
- Pincode-level hotspot detection  
- Custom metric calculation: Update Dominance Ratio (UDR)  
- Outlier detection using distribution-based methods  
- Correlation analysis between age-wise update groups  

### Update Dominance Ratio (UDR)
A custom metric introduced in this analysis:

UDR = Updates (Age 17+) / Total Updates

This metric helps identify whether demographic updates in a region are primarily adult-driven or child-driven, providing insight into societal behavior and administrative demand patterns.

---

## Tools & Technologies
- Python  
- Pandas  
- NumPy  
- Matplotlib  
- Seaborn  

All tools used are open-source, ensuring transparency and reproducibility of results.

---

## How to Run the Code
1. Place the Aadhaar demographic update CSV file in the same directory as the Python script  
2. Ensure Python 3.x is installed  
3. Install required libraries if not already available:
   pip install pandas numpy matplotlib seaborn
4. Run the analysis script:
   python aadhar.py

The script generates multiple visualizations that illustrate trends, distributions, and key analytical insights.

---

## Key Outcomes
- Identification of temporal trends in Aadhaar demographic updates  
- Detection of geographic inequality in update activity across districts  
- Recognition of high-intensity update hotspots at pincode level  
- Insights into adult versus child update dominance  
- Actionable indicators for administrative planning and system optimization  

---

## Relevance and Impact
The findings from this analysis can assist UIDAI and policymakers in:
- Understanding citizen interaction patterns with Aadhaar  
- Anticipating system load and service demand  
- Allocating resources more effectively  
- Improving accessibility and planning demographic update infrastructure  

---

## Author
Keerthishree  
Participant, UIDAI Data Hackathon 2026
