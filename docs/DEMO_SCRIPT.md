# Health360 — End-to-End Demonstration Script

## 1. Introduction
Introduce Health360 as an individual educational Tableau analytics project. State that it explores a synthetic healthcare-related dataset and is not a diagnostic or treatment tool.

## 2. Dataset and preparation
Show the CSV connection. Explain 5,000 records, 16 original fields and 27 prepared Tableau fields. Mention data-quality checks and the constant health_risk_score field, which is excluded from KPI interpretation.

## 3. Worksheets
Show the nine worksheets: disease prevalence, age distribution, disease by age, BMI quartiles, disease by BMI, smoking, alcohol, exercise and clinical indicators.

## 4. Dashboard
Show four KPI metrics and six filters. Demonstrate an age or BMI filter and reset to All. Explain rates are descriptive proportions and disease flags may overlap.

## 5. Story
Navigate the six scenes. State what each chart compares without implying causation or clinical prediction.

## 6. Website and integration
Open the Health360 website. Demonstrate Dashboard and Story embeds and direct Tableau links. If Flask is deployed, show its Python-hosted site and /healthz. Do not describe GitHub Pages as a Flask runtime.

## 7. Limitations
Mention undocumented measurement units and code meanings, the constant risk-score field and the need for source-methodology verification. Conclude that this is exploratory visualization only.