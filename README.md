# Health360 — Clinical & Healthcare Risk Analysis

This individual educational project uses Tableau to explore demographic, lifestyle, symptom and clinical-indicator patterns in a supplied synthetic healthcare dataset.

## Live project
- **Website:** https://git-si-2206.github.io/Health360-Healthcare-Analytics/
- **GitHub repository:** https://github.com/Git-SI-2206/Health360-Healthcare-Analytics
- **Tableau Dashboard:** https://public.tableau.com/views/Health360_Clinical_Healthcare_Risk_Analysis/Health360_Dashboard_Final_
- **Tableau Story:** https://public.tableau.com/views/Health360_Clinical_Healthcare_Risk_Analysis/Health360_Patient_Risk_Lifestyle_Insights

## Dataset
The repository contains `smart_healthcare_dataset.csv` at the root. It has 5,000 records and 16 original columns. The Tableau-ready export contains 27 fields after adding derived grouping/display fields. The supplied quality audit reports zero missing cells and zero exact duplicate rows. The `health_risk_score` field is constant at 100.0 and is not used as a differentiating KPI.

The project owner identifies the source dataset as synthetic. The source publisher/licence is not documented in the supplied material. Treat the CSV as educational sample data and do not infer real patient attributes or clinical outcomes from it.

## Tableau deliverables
The published workbook includes nine analytical worksheets, a dashboard with six filters and a six-scene story. This is descriptive educational analysis, not a clinically validated diagnostic, prognostic or treatment system.

## Repository structure
- `index.html`, `assets/` — responsive website and Tableau Embedding API v3.
- `app.py`, `requirements.txt`, `render.yaml` — Flask app/deployment configuration.
- `prepare_data.py`, `smart_healthcare_dataset.csv`, `data/` — source CSV, reproducible preparation script, field dictionary and quality reports.
- `Tableau/` — three original assessment reference PDFs.
- `tableau/` — Tableau build guide and performance-test template.
- `docs/` — project documentation and demo script.

## Run locally
Static site: open `index.html` in a modern browser.

Flask:
```bash
python -m pip install -r requirements.txt
python app.py
```
Open http://127.0.0.1:5000. The `/healthz` route returns basic service health.

## Hosting note
GitHub Pages serves static files only; it does not execute Python/Flask. Deploy the Flask application separately to a Python-capable host if required by the assessment.

## Responsible interpretation
Some measurement units and categorical code meanings are undocumented. Associations do not establish causation or an individual's medical risk. This project must not be used for clinical decisions.
