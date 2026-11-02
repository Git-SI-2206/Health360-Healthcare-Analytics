# Health360 — Project Status

**Owner:** Git-SI-2206  
**Repository:** https://github.com/Git-SI-2206/Health360-Healthcare-Analytics

## Owner-confirmed deliverables
- Source data connected in Tableau Desktop (5,000 rows, 27 prepared fields).
- Seven calculated fields created and validated.
- Nine Tableau analytical worksheets and a dashboard assembled.
- Six dashboard filters added.
- Six-scene Tableau Story created.
- Workbook published to Tableau Public.
- Responsive website and Tableau Embedding API v3 source prepared.
- Flask app, deployment configuration, project documentation and demo script prepared.

## Published views
- Dashboard: https://public.tableau.com/views/Health360_Clinical_Healthcare_Risk_Analysis/Health360_Dashboard_Final_
- Story: https://public.tableau.com/views/Health360_Clinical_Healthcare_Risk_Analysis/Health360_Patient_Risk_Lifestyle_Insights

## Still to verify
- Test both Tableau links in a signed-out browser.
- Enable GitHub Pages and verify the live website.
- Deploy Flask on a Python-capable host if required; GitHub Pages does not execute Python.
- Test all filters/actions and record measured load times.
- Record the end-to-end demonstration video.
- Add the final .twbx only after checking its contents and size.

## Data limitations
The source CSV contains 16 original columns; a reference PDF says 17. The prepared Tableau export contains 27 fields. health_risk_score is constant at 100.0. Several units and category-code meanings are undocumented. The owner describes the dataset as synthetic; row-level data is omitted pending provenance/licence confirmation.

This is educational descriptive analytics, not a clinically validated diagnostic, prognostic or treatment system.