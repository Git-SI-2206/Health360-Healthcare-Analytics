"""Prepare the source CSV for the Health360 Tableau workbook.

Usage:
    python prepare_data.py smart_healthcare_dataset.csv

The script preserves the 16 source columns and adds 11 display/grouping fields.
"""
from __future__ import annotations
import argparse
from pathlib import Path
import json
import pandas as pd

EXPECTED = [
    "age", "gender", "bmi", "exercise_level", "smoking", "alcohol",
    "blood_pressure", "cholesterol", "glucose", "fatigue", "chest_pain",
    "dizziness", "heart_disease", "diabetes", "stroke", "health_risk_score",
]
BINARY = ["smoking", "alcohol", "fatigue", "chest_pain", "dizziness",
          "heart_disease", "diabetes", "stroke"]

def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("source_csv", type=Path)
    parser.add_argument("--output-dir", type=Path, default=Path("data"))
    args = parser.parse_args()

    df = pd.read_csv(args.source_csv)
    if list(df.columns) != EXPECTED:
        raise ValueError(f"Expected the 16 source columns in order: {EXPECTED}; got {list(df.columns)}")
    if len(df) != 5000:
        print(f"WARNING: expected 5,000 rows; found {len(df)}")
    if df.isna().any().any():
        raise ValueError("Missing values found. Review the source; this script does not impute.")
    if df.duplicated().any():
        raise ValueError("Duplicate rows found. Review the source; this script does not delete rows.")
    for col in BINARY:
        invalid = sorted(set(df[col].dropna().unique()) - {0, 1})
        if invalid:
            raise ValueError(f"Unexpected binary codes in {col}: {invalid}")

    out = df.copy()
    out["age_group"] = pd.cut(
        out["age"], bins=[17, 29, 44, 59, 79],
        labels=["18-29", "30-44", "45-59", "60-79"], include_lowest=True
    ).astype(str)
    q1, q2, q3 = [float(out["bmi"].quantile(q)) for q in (0.25, 0.50, 0.75)]
    out["bmi_quartile"] = pd.cut(
        out["bmi"], bins=[-float("inf"), q1, q2, q3, float("inf")],
        labels=["Q1 - lower", "Q2 - lower-middle", "Q3 - upper-middle", "Q4 - upper"],
        include_lowest=True
    ).astype(str)
    out["exercise_level_label"] = out["exercise_level"].map(lambda x: f"Code {int(x)}")
    for col in BINARY:
        label = f"{col}_label"
        out[label] = out[col].map({0: "No (0)", 1: "Yes (1)"})

    args.output_dir.mkdir(parents=True, exist_ok=True)
    output = args.output_dir / "health360_tableau_ready.csv"
    out.to_csv(output, index=False)
    summary = {
        "source_rows": int(len(df)), "source_columns": int(len(df.columns)),
        "tableau_ready_rows": int(len(out)), "tableau_ready_columns": int(len(out.columns)),
        "missing_values_total": int(df.isna().sum().sum()),
        "duplicate_rows": int(df.duplicated().sum()),
        "health_risk_score_unique_values": int(df["health_risk_score"].nunique()),
        "bmi_quartile_cutpoints": {"q1": q1, "q2": q2, "q3": q3},
        "disease_prevalence_percent": {
            c: round(float(df[c].mean() * 100), 2)
            for c in ["heart_disease", "diabetes", "stroke"]
        }
    }
    (args.output_dir / "data_quality_summary.json").write_text(
        json.dumps(summary, indent=2), encoding="utf-8"
    )
    print(f"Wrote {output} ({len(out)} rows x {len(out.columns)} fields)")

if __name__ == "__main__":
    main()
