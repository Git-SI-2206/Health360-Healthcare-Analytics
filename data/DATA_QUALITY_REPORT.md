# Health360 data-quality and preparation report

**Source shape:** 5,000 rows × 16 columns  
**Tableau-ready shape:** 5,000 rows × 27 columns

## Verification
- Missing values: 0
- Exact duplicate rows: 0
- Invalid values in checked binary columns: 0 fields
- health_risk_score: one unique value; min/max = 100.0/100.0

## Descriptive summaries
- Mean age: 48.81; median: 49; range: 18–79 (unit not documented).
- Mean BMI-like value: 24.97; range: 15.0–42.6 (unit not documented).
- Disease flag rates: heart disease 29.98%, diabetes 34.92%, stroke 24.86%.
- Disease prevalence varies sharply by age band in this file. This is a descriptive data pattern, not a causal or clinical conclusion.

## Cleaning decisions
No source rows were removed and no missing values were imputed. Source columns remain unchanged. Eleven grouping/display fields were added for Tableau. BMI quartiles are calculated from this dataset and are not medical BMI classifications.

## Items requiring confirmation
1. Dataset provenance, licence and permission to publish patient-level rows.
2. Units and operational definitions for BMI, blood pressure, cholesterol and glucose.
3. Meanings of exercise codes 0, 1 and 2.
4. 0/1 encoding for smoking, alcohol, symptoms and disease outcome fields.
5. The sharp concentration of outcome flags in older ages; confirm source methodology and outcome-generation logic.
6. Formula and intended meaning of health_risk_score; it is constant and excluded from KPI analysis.

## Reproducibility
The prepare_data.py script validates the expected 16-column source schema, preserves rows and raw columns, and generates the Tableau-ready export, field dictionary and JSON summary.