# Health360 Tableau Build Guide

## Data source
Connect health360_tableau_ready.csv as a Text File. The prepared export has 5,000 records and 27 fields (16 original fields plus derived grouping/display fields).

## Seven calculated fields
- Disease Count: INT([Heart Disease]) + INT([Diabetes]) + INT([Stroke])
- Any Disease Flag: IIF([Disease Count] > 0, 1, 0)
- Heart Disease Rate: SUM([Heart Disease]) / COUNT([Age])
- Diabetes Rate: SUM([Diabetes]) / COUNT([Age])
- Stroke Rate: SUM([Stroke]) / COUNT([Age])
- Any Disease Rate: SUM([Any Disease Flag]) / COUNT([Age])
- Patient Records: COUNT([Age])

Format the four rates as percentages with one decimal place.

## Nine worksheets
1. 01_Disease_Prevalence — Measure Names / Measure Values, three disease rates.
2. 02_Age_Distribution — Age Group by Patient Records.
3. 03_Disease_By_Age_Group — Age Group with three disease-rate measures.
4. 04_BMI_Quartile_Profile — BMI Quartile by Patient Records.
5. 05_Disease_By_BMI_Quartile — heatmap: BMI Quartile by Measure Names, color by Measure Values.
6. 06_Smoking_Disease — Smoking Label by three disease rates.
7. 07_Alcohol_Disease — Alcohol Label by three disease rates.
8. 08_Exercise_Disease — Exercise Level Label by three disease rates.
9. 09_Clinical_Indicators — Blood Pressure vs Cholesterol, color by Heart Disease Label; add Age, Bmi, Glucose, Heart Disease, Diabetes and Stroke to Tooltip.

For grouped bars, filter Measure Names to the three disease-rate fields and set Analysis → Stack Marks → Off. Format rate axes as percentages.

## Dashboard
Create KPI_Summary with Diabetes Rate, Heart Disease Rate, Patient Records and Stroke Rate. Build Health360_Dashboard_Final with a KPI row, paired chart rows, six filters (Age Group, Gender, BMI Quartile, Smoking Label, Alcohol Label, Exercise Level Label) and a full-width clinical-indicators scatter plot. Test each filter on all relevant sheets.

## Story
Create Health360_Patient_Risk_Lifestyle_Insights with six story points: disease prevalence, age distribution, disease by age, BMI distribution, disease by BMI, exercise vs disease.

## Interpretation
The health_risk_score field is constant at 100.0 and is not a useful differentiating KPI. Some units and code meanings are undocumented; do not infer clinical thresholds. Rates are descriptive dataset proportions, not validated individual risk estimates.