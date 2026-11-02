# Health360 — Clinical & Healthcare Risk Analysis

## Abstract
Health360 is an educational data-visualization project that uses Tableau to explore demographic, lifestyle and clinical-indicator patterns in a supplied synthetic healthcare dataset. It presents nine worksheets, an interactive dashboard with six filters and a six-scene story.

## Problem statement
Healthcare-related records are difficult to compare when reviewed only as rows in a table. This project organizes supplied indicators into charts and filters so users can inspect groups and outcome flags.

## Dataset
The source file contains 5,000 records and 16 original columns. The prepared Tableau export has 27 fields after adding derived grouping/display fields. The audit reports no missing cells and no exact duplicate rows. health_risk_score is constant at 100.0 and is not used as a differentiating KPI.

## Methodology
The workflow connects the CSV to Tableau, validates fields, creates seven calculated fields, builds nine worksheets, assembles a dashboard, creates a six-scene story and embeds published views in a responsive website. Flask source is included for deployment on a Python-capable host.

## Tableau views
The nine views cover disease prevalence, age distribution, disease by age group, BMI quartiles, disease by BMI, smoking, alcohol, exercise and blood-pressure/cholesterol indicators. The dashboard includes filters for age group, gender, BMI quartile, smoking, alcohol and exercise level.

## Published links
Dashboard: https://public.tableau.com/views/Health360_Clinical_Healthcare_Risk_Analysis/Health360_Dashboard_Final_

Story: https://public.tableau.com/views/Health360_Clinical_Healthcare_Risk_Analysis/Health360_Patient_Risk_Lifestyle_Insights

## Limitations
Some units and category-code meanings are undocumented. Group differences do not demonstrate causation. health_risk_score is constant. This project is not clinically validated and must not be used for diagnosis, prognosis or treatment.

## Future work
Verify data provenance and licence, complete measured performance tests, test public access, capture the final demo video and deploy Flask separately if a live server is required.