# Health360 — Project Status

**Owner:** Git-SI-2206  
**Repository:** https://github.com/Git-SI-2206/Health360-Healthcare-Analytics  
**Website:** https://git-si-2206.github.io/Health360-Healthcare-Analytics/

## Completed
- Source dataset committed at repository root as `smart_healthcare_dataset.csv` (5,000 records, 16 original columns).
- Three original Tableau assessment PDFs added to `Tableau/`.
- Tableau-ready export preparation script and data dictionary/quality report committed.
- Seven calculated Tableau fields created and validated.
- Nine Tableau analytical worksheets created and assembled into a dashboard.
- Six dashboard filters added.
- Six-scene Tableau Story created.
- Workbook published to Tableau Public.
- Responsive website with Tableau Dashboard and Story embed configured.
- Flask app and Python-host deployment configuration prepared.
- Project documentation, build guide and demo script committed.
- GitHub Pages deployment completed successfully.

## Published views
- Dashboard: https://public.tableau.com/views/Health360_Clinical_Healthcare_Risk_Analysis/Health360_Dashboard_Final_
- Story: https://public.tableau.com/views/Health360_Clinical_Healthcare_Risk_Analysis/Health360_Patient_Risk_Lifestyle_Insights

## Remaining
- Test both Tableau embeds in a signed-out browser and check the rendered website.
- Deploy Flask on a Python-capable host if required; GitHub Pages does not execute Python.
- Test all filters/actions and record measured load times.
- Record the end-to-end demonstration video.
- Add the final .twbx if required and suitable for sharing.

## Data limitations
The owner describes the source as synthetic; its original publisher/licence is not documented. The source CSV has 16 original columns; a separate reference document elsewhere stated 17, which does not match the CSV header. The Tableau-ready export has 27 fields. `health_risk_score` is constant at 100.0. Several units and category-code meanings are undocumented.

This is educational descriptive analytics, not a clinically validated diagnostic, prognostic or treatment system.
