"""
process_datasets.py
===================
Cleans and processes source datasets for the
AI Adoption Opportunity project (Document Intelligence for Logistics).

Inputs  (place in data/raw/):
    LPI raw files (from https://databank.worldbank.org/data/download/LPI_CSV.zip):
        LPICSV.csv          LPI data — all countries, all indicators, all years
        LPICountry.csv      Country metadata — region, income group, etc.
        LPISeries.csv       Indicator metadata — definitions, licence, etc.

    Pre-curated project files:
        benchmarks.csv      AI vs manual performance benchmarks
        company_cases.csv   Operator case study results

Outputs (written to data/processed/):
    LPI_data.csv            Long-format data: one row per country × indicator × year
    LPI_countries.csv       Country metadata with clean column names
    LPI_indicators.csv      Indicator metadata with clean column names
    benchmarks.csv          Validated and copied as-is
    company_cases.csv       Validated and copied as-is

Tableau connection:
    Connect each file as a separate data source.
    Join LPI_data ↔ LPI_countries  on  country_code = country_code
    Join LPI_data ↔ LPI_indicators on  indicator_code = indicator_code

Source:
    World Bank Logistics Performance Index
    License: Creative Commons Attribution 4.0 (CC BY 4.0)

Usage:
    python data/processed/process_datasets.py

Author:  AI Adoption Opportunity Project
Date:    June 2026

PowerShell (Windows):
    cd C:\\Users\\dilia\\OneDrive\\IronHack\\Projects\\Project5\\ai-adoption-opportunity-project
    python data\\processed\\process_datasets.py
"""

import pandas as pd
from pathlib import Path

# ── Paths ──────────────────────────────────────────────────────────────────
# Resolved relative to this script so it works regardless of where it is run.
# Expected layout:
#   <project_root>/
#       data/
#           raw/                      ← source files here
#           processed/
#               process_datasets.py   ← this script
#               LPI_data.csv          ← outputs written here
#               LPI_countries.csv
#               LPI_indicators.csv

_SCRIPT_DIR   = Path(__file__).resolve().parent   # data/processed/
_PROJECT_ROOT = _SCRIPT_DIR.parent.parent          # <project_root>/

RAW_DIR       = _PROJECT_ROOT / "data" / "raw"
PROCESSED_DIR = _PROJECT_ROOT / "data" / "processed"
PROCESSED_DIR.mkdir(parents=True, exist_ok=True)


# ── Helpers ────────────────────────────────────────────────────────────────

def load_csv(filename: str) -> pd.DataFrame:
    """Load a CSV from data/raw/, trying utf-8 then latin-1 then cp1252."""
    path = RAW_DIR / filename
    if not path.exists():
        raise FileNotFoundError(
            f"\n[ERROR] File not found: {path}"
            f"\n        Place it in data/raw/ and re-run."
        )
    for encoding in ["utf-8", "latin-1", "cp1252"]:
        try:
            df = pd.read_csv(path, low_memory=False, encoding=encoding)
            if encoding != "utf-8":
                print(f"[INFO]  {filename} — loaded with {encoding} encoding")
            print(f"[LOAD]  {filename} — {df.shape[0]:,} rows × {df.shape[1]} columns")
            return df
        except UnicodeDecodeError:
            continue
    raise ValueError(f"[ERROR] Could not decode {filename}")


def report_missing(df: pd.DataFrame, label: str) -> None:
    """Print missing value report for any columns that have nulls."""
    missing = df.isnull().sum()
    missing = missing[missing > 0]
    if missing.empty:
        print(f"[CHECK] {label} — no missing values")
    else:
        print(f"[CHECK] {label} — columns with missing values:")
        for col, n in missing.items():
            print(f"        {col}: {n:,} ({100 * n / len(df):.1f}%)")


def save_csv(df: pd.DataFrame, filename: str) -> None:
    """Save a cleaned DataFrame to data/processed/."""
    path = PROCESSED_DIR / filename
    df.to_csv(path, index=False)
    print(f"[SAVE]  {filename} — {df.shape[0]:,} rows × {df.shape[1]} columns → {path}")


# ═══════════════════════════════════════════════════════════════════════════
# FILE 1 — LPI_data.csv
# Source: LPICSV.csv
# Wide → long transformation. One row per country × indicator × year.
# ═══════════════════════════════════════════════════════════════════════════

def process_lpi_data(filename: str = "LPICSV.csv") -> pd.DataFrame:
    """
    Clean LPICSV.csv and reshape from wide to long format.

    Input (wide format):
        Columns: Country Name, Country Code, Indicator Name, Indicator Code,
                 2007, 2010, 2012, 2014, 2016, 2018, 2023

    Output (long format) — LPI_data.csv:
        country_code        ISO3 code — join key to LPI_countries.csv
        country_name        e.g. "Germany"
        indicator_code      World Bank code — join key to LPI_indicators.csv
        indicator_name      Full indicator name
        indicator_label     Short snake_case label  e.g. "customs_score"
        indicator_type      "score" (1–5 scale) or "rank" (1 = best performer)
        year                Survey year (integer)
        value               Score or rank value
        dataset_source      "World Bank LPI"
    """
    print("\n── LPICSV.csv → LPI_data.csv ───────────────────────────────────────")
    df = load_csv(filename)

    # Validate expected columns
    required = {"Country Name", "Country Code", "Indicator Name", "Indicator Code"}
    missing = required - set(df.columns)
    if missing:
        raise ValueError(f"[ERROR] Missing columns in {filename}: {missing}")

    # Detect year columns (4-digit numeric column names)
    year_cols = sorted(
        [c for c in df.columns if str(c).strip().isdigit() and len(str(c).strip()) == 4],
        key=int
    )
    print(f"[INFO]  Survey years detected: {year_cols}")

    # Melt wide → long
    df_long = df.melt(
        id_vars    = ["Country Name", "Country Code", "Indicator Name", "Indicator Code"],
        value_vars = year_cols,
        var_name   = "year",
        value_name = "value",
    )

    # Cast types
    df_long["year"]  = df_long["year"].astype(int)
    df_long["value"] = pd.to_numeric(df_long["value"], errors="coerce")

    # Drop rows where value is null (country not surveyed in that year)
    before = len(df_long)
    df_long = df_long.dropna(subset=["value"])
    print(f"[DROP]  {before - len(df_long):,} null rows removed "
          f"(countries not surveyed in a given year)")

    # Classify indicator type: score (.XQ) or rank (.RK)
    df_long["indicator_type"] = df_long["Indicator Code"].apply(
        lambda c: "score" if str(c).endswith(".XQ") else "rank"
    )

    # Round rank values to integers
    mask = df_long["indicator_type"] == "rank"
    df_long.loc[mask, "value"] = (
        df_long.loc[mask, "value"].round(0).astype("Int64")
    )

    # Add short human-readable label per indicator code
    label_map = {
        "LP.LPI.OVRL.XQ": "lpi_overall_score",
        "LP.LPI.OVRL.RK": "lpi_overall_rank",
        "LP.LPI.CUST.XQ": "customs_score",
        "LP.LPI.CUST.RK": "customs_rank",
        "LP.LPI.INFR.XQ": "infrastructure_score",
        "LP.LPI.INFR.RK": "infrastructure_rank",
        "LP.LPI.ITRN.XQ": "intl_shipments_score",
        "LP.LPI.ITRN.RK": "intl_shipments_rank",
        "LP.LPI.LOGS.XQ": "logistics_competence_score",
        "LP.LPI.LOGS.RK": "logistics_competence_rank",
        "LP.LPI.TRAC.XQ": "tracking_tracing_score",
        "LP.LPI.TRAC.RK": "tracking_tracing_rank",
        "LP.LPI.TIME.XQ": "timeliness_score",
        "LP.LPI.TIME.RK": "timeliness_rank",
    }
    df_long["indicator_label"] = (
        df_long["Indicator Code"].map(label_map)
        .fillna(df_long["Indicator Code"])
    )

    # Add source label
    df_long["dataset_source"] = "World Bank LPI"

    # Rename and order columns
    df_long = df_long.rename(columns={
        "Country Name":   "country_name",
        "Country Code":   "country_code",
        "Indicator Name": "indicator_name",
        "Indicator Code": "indicator_code",
    })

    df_long = df_long[[
        "country_code", "country_name",
        "indicator_code", "indicator_name", "indicator_label", "indicator_type",
        "year", "value", "dataset_source",
    ]].sort_values(["country_name", "indicator_label", "year"]).reset_index(drop=True)

    report_missing(df_long, "LPI_data")
    print(f"[INFO]  {df_long['country_code'].nunique()} countries · "
          f"{df_long['indicator_label'].nunique()} indicators · "
          f"{sorted(df_long['year'].unique())} years")
    save_csv(df_long, "LPI_data.csv")
    return df_long


# ═══════════════════════════════════════════════════════════════════════════
# FILE 2 — LPI_countries.csv
# Source: LPICountry.csv
# Select useful columns, clean names. Join key: country_code.
# ═══════════════════════════════════════════════════════════════════════════

def process_lpi_countries(filename: str = "LPICountry.csv") -> pd.DataFrame:
    """
    Clean LPICountry.csv — keep the columns useful for Tableau analysis.

    Output — LPI_countries.csv:
        country_code        ISO3 code — join key to LPI_data.csv
        country_short_name  e.g. "Germany"
        country_long_name   e.g. "Federal Republic of Germany"
        alpha2_code         2-letter ISO code e.g. "DE"
        region              e.g. "Europe & Central Asia"
        income_group        e.g. "High income"
        currency            e.g. "Euro"
    """
    print("\n── LPICountry.csv → LPI_countries.csv ─────────────────────────────")
    df = load_csv(filename)

    # Map source columns to clean output names — only keep what's useful
    col_map = {
        "Country Code": "country_code",
        "Short Name":   "country_short_name",
        "Long Name":    "country_long_name",
        "2-alpha code": "alpha2_code",
        "Region":       "region",
        "Income Group": "income_group",
        "Currency Unit":"currency",
    }

    # Keep only columns that exist in the file
    available = {k: v for k, v in col_map.items() if k in df.columns}
    df_out = df[list(available.keys())].rename(columns=available).copy()

    # Remove duplicate country codes if any
    before = len(df_out)
    df_out = df_out.drop_duplicates(subset=["country_code"])
    if len(df_out) < before:
        print(f"[DEDUP] Removed {before - len(df_out):,} duplicate country rows")

    df_out = df_out.sort_values("country_short_name").reset_index(drop=True)

    report_missing(df_out, "LPI_countries")
    print(f"[INFO]  {len(df_out)} countries")
    save_csv(df_out, "LPI_countries.csv")
    return df_out


# ═══════════════════════════════════════════════════════════════════════════
# FILE 3 — LPI_indicators.csv
# Source: LPISeries.csv
# Select useful columns, clean names. Join key: indicator_code.
# ═══════════════════════════════════════════════════════════════════════════

def process_lpi_indicators(filename: str = "LPISeries.csv") -> pd.DataFrame:
    """
    Clean LPISeries.csv — keep the columns useful for Tableau tooltips
    and indicator filtering.

    Output — LPI_indicators.csv:
        indicator_code      World Bank code — join key to LPI_data.csv
        indicator_name      Full name e.g. "Efficiency of the clearance process..."
        long_definition     Methodology and survey description
        licence_type        e.g. "CC BY-4.0"
    """
    print("\n── LPISeries.csv → LPI_indicators.csv ─────────────────────────────")
    df = load_csv(filename)

    col_map = {
        "Series Code":     "indicator_code",
        "Indicator Name":  "indicator_name",
        "Long definition": "long_definition",
        "License Type":    "licence_type",
    }

    available = {k: v for k, v in col_map.items() if k in df.columns}
    df_out = df[list(available.keys())].rename(columns=available).copy()

    # Add short label (same map as LPI_data for easy cross-reference)
    label_map = {
        "LP.LPI.OVRL.XQ": "lpi_overall_score",
        "LP.LPI.OVRL.RK": "lpi_overall_rank",
        "LP.LPI.CUST.XQ": "customs_score",
        "LP.LPI.CUST.RK": "customs_rank",
        "LP.LPI.INFR.XQ": "infrastructure_score",
        "LP.LPI.INFR.RK": "infrastructure_rank",
        "LP.LPI.ITRN.XQ": "intl_shipments_score",
        "LP.LPI.ITRN.RK": "intl_shipments_rank",
        "LP.LPI.LOGS.XQ": "logistics_competence_score",
        "LP.LPI.LOGS.RK": "logistics_competence_rank",
        "LP.LPI.TRAC.XQ": "tracking_tracing_score",
        "LP.LPI.TRAC.RK": "tracking_tracing_rank",
        "LP.LPI.TIME.XQ": "timeliness_score",
        "LP.LPI.TIME.RK": "timeliness_rank",
    }
    df_out["indicator_label"] = (
        df_out["indicator_code"].map(label_map)
        .fillna(df_out["indicator_code"])
    )

    # Reorder columns
    col_order = ["indicator_code", "indicator_label", "indicator_name",
                 "long_definition", "licence_type"]
    col_order = [c for c in col_order if c in df_out.columns]
    df_out = df_out[col_order].sort_values("indicator_label").reset_index(drop=True)

    report_missing(df_out, "LPI_indicators")
    print(f"[INFO]  {len(df_out)} indicators")
    save_csv(df_out, "LPI_indicators.csv")
    return df_out


# ═══════════════════════════════════════════════════════════════════════════
# FILES 4 & 5 — benchmarks.csv and company_cases.csv
# Pre-curated files — validate and copy only, no transformations.
# ═══════════════════════════════════════════════════════════════════════════

def validate_and_copy(filename: str) -> pd.DataFrame:
    """Validate a pre-curated CSV and copy it to data/processed/."""
    print(f"\n── {filename} (pre-curated) ─────────────────────────────────────")
    df = load_csv(filename)
    report_missing(df, filename)
    before = len(df)
    df = df.drop_duplicates()
    if len(df) < before:
        print(f"[DEDUP] Removed {before - len(df):,} duplicate rows")
    save_csv(df, filename)
    return df


# ═══════════════════════════════════════════════════════════════════════════
# MAIN
# ═══════════════════════════════════════════════════════════════════════════

def main():
    print("=" * 60)
    print("  AI Adoption Opportunity — Dataset Processing")
    print("  Document Intelligence for Logistics")
    print("=" * 60)

    results = {}

    # ── LPI files ─────────────────────────────────────────────────────────
    lpi_processors = [
        ("LPICSV.csv",      process_lpi_data),
        ("LPICountry.csv",  process_lpi_countries),
        ("LPISeries.csv",   process_lpi_indicators),
    ]
    for raw_file, processor in lpi_processors:
        try:
            key = processor.__name__.replace("process_lpi_", "LPI_") + ".csv"
            results[raw_file] = processor(raw_file)
        except FileNotFoundError as e:
            print(str(e))
        except ValueError as e:
            print(str(e))

    # ── Pre-curated project files ─────────────────────────────────────────
    for filename in ["benchmarks.csv", "company_cases.csv"]:
        try:
            results[filename] = validate_and_copy(filename)
        except FileNotFoundError as e:
            print(str(e))

    # ── Summary ───────────────────────────────────────────────────────────
    print("\n" + "=" * 60)
    print("  Processing complete")
    print("=" * 60)
    for fname, df in results.items():
        print(f"  ✓  {fname:30} → {df.shape[0]:,} rows × {df.shape[1]} cols")

    print(f"\n  Files saved to: {PROCESSED_DIR.resolve()}")
    print("\n  Tableau connection guide:")
    print("  1. Connect LPI_data.csv as primary data source")
    print("  2. Join LPI_countries.csv  on  country_code  =  country_code")
    print("  3. Join LPI_indicators.csv on  indicator_code = indicator_code")
    print("  4. Connect benchmarks.csv as separate data source")
    print("  5. Connect company_cases.csv as separate data source")
    print("\n  Useful filters in Tableau:")
    print("  indicator_type  = 'score'         → 1–5 scale values only")
    print("  indicator_label = 'customs_score' → Panel 1 chart")
    print("  year            = 2023            → latest survey round")


if __name__ == "__main__":
    main()
