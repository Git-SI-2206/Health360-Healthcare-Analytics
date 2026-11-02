# Health360 — Clinical & Healthcare Risk Analysis

An individual educational data-analytics project using Tableau to explore demographic, lifestyle, symptom and clinical-indicator patterns in a supplied synthetic healthcare dataset.

## Live project
- **GitHub Pages website (after Pages is enabled):** https://git-si-2206.github.io/Health360-Healthcare-Analytics/
- **GitHub repository:** https://github.com/Git-SI-2206/Health360-Healthcare-Analytics
- **Tableau Dashboard:** https://public.tableau.com/views/Health360_Clinical_Healthcare_Risk_Analysis/Health360_Dashboard_Final_
- **Tableau Story:** https://public.tableau.com/views/Health360_Clinical_Healthcare_Risk_Analysis/Health360_Patient_Risk_Lifestyle_Insights

## Dataset
The source CSV contains 5,000 records and 16 original columns. The Tableau-ready export contains 27 fields after adding documented grouping/display fields. The data-quality audit reported zero missing cells and zero exact duplicate rows. The `health_risk_score` is constant at 100.0 and is not used as a differentiating KPI.

The project owner describes the dataset as synthetic. The row-level CSV is intentionally not included in this public repository pending confirmation of source/licence and redistribution terms.

## Tableau deliverables
The published workbook includes nine analytical worksheets, a dashboard with six filters and a six-scene story. This project is descriptive and educational; it is not a clinically validated diagnostic, prognostic or treatment system.

## Repository structure
- `index.html`, `assets/` — responsive website and Tableau Embedding API v3.
- `app.py`, `requirements.txt`, `render.yaml` — Flask app/deployment configuration.
- `prepare_data.py`, `data/` — preparation script, dictionary and quality reports (no row-level CSV).
- `tableau/` — build guide and performance-test template.
- `docs/` — project documentation and demo script.
- `PROJECT_STATUS.md`, `PUBLISHING_CHECKLIST.md` — handoff notes.

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
