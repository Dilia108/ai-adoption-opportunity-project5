"""
process_datasets.py
===================
Cleans and processes the three Kaggle datasets for the
AI Adoption Opportunity project (Document Intelligence for Logistics).

Inputs  (place in data/raw/):
    - customs_delay.csv
    - logistics_ops.csv
    - shipment_pricing.csv

Outputs (written to data/processed/):
    - customs_delay_clean.csv
    - logistics_ops_clean.csv
    - shipment_pricing_clean.csv

Usage:
    python process_datasets.py

Author:  AI Adoption Opportunity Project
Date:    June 2026

Scripts for running in PowerShell (Windows):
PS: cd C:\Users\dilia\OneDrive\IronHack\Projects\Project5\ai-adoption-opportunity-project
PS: python data\processed\process_datasets.py
"""

import os
import pandas as pd
import numpy as np
from pathlib import Path

# ── Paths ──────────────────────────────────────────────────────────────────
RAW_DIR       = Path("data/raw")
PROCESSED_DIR = Path("data/processed")
PROCESSED_DIR.mkdir(parents=True, exist_ok=True)

# ── Helpers ────────────────────────────────────────────────────────────────

def load_csv(filename: str) -> pd.DataFrame:
    """Load a CSV from data/raw/ with basic feedback.
    Tries UTF-8 first, falls back to latin-1 and cp1252 for non-UTF-8 files."""
    path = RAW_DIR / filename
    if not path.exists():
        raise FileNotFoundError(
            f"\n[ERROR] File not found: {path}"
            f"\nDownload it from Kaggle and place it in data/raw/"
        )
    for encoding in ["utf-8", "latin-1", "cp1252"]:
        try:
            df = pd.read_csv(path, low_memory=False, encoding=encoding)
            if encoding != "utf-8":
                print(f"[INFO]  {filename} — loaded with encoding: {encoding}")
            print(f"[LOAD]  {filename} — {df.shape[0]:,} rows × {df.shape[1]} columns")
            return df
        except UnicodeDecodeError:
            continue
    raise ValueError(f"[ERROR] Could not decode {filename} with utf-8, latin-1, or cp1252")


def report_missing(df: pd.DataFrame, label: str) -> None:
    """Print missing value counts for columns that have any."""
    missing = df.isnull().sum()
    missing = missing[missing > 0]
    if missing.empty:
        print(f"[CHECK] {label} — no missing values")
    else:
        print(f"[CHECK] {label} — missing values:")
        for col, count in missing.items():
            pct = count / len(df) * 100
            print(f"        {col}: {count:,} ({pct:.1f}%)")


def save_csv(df: pd.DataFrame, filename: str) -> None:
    """Save a cleaned DataFrame to data/processed/."""
    path = PROCESSED_DIR / filename
    df.to_csv(path, index=False)
    print(f"[SAVE]  {filename} — {df.shape[0]:,} rows × {df.shape[1]} columns → {path}")


# ═══════════════════════════════════════════════════════════════════════════
# DATASET 1 — Cross-Border Trade & Customs Delay
# Source: https://www.kaggle.com/datasets/ziya07/cross-border-trade-and-customs-delay-dataset
# ═══════════════════════════════════════════════════════════════════════════

def process_customs_delay(filename: str = "customs_delay.csv") -> pd.DataFrame:
    """
    Clean and enrich the customs delay dataset.

    Key columns:
        Customs_Delay_Days  — target for Panel 1 (delay by corridor)
        Risk_Flag           — binary risk classification
        Compliance_Score    — documentation quality proxy
        Inspection_Type     — type of customs inspection
        Trade_Route         — origin–destination pair
        Prior_Offense_Count — repeat error history
    """
    print("\n── Dataset 1: Cross-Border Customs Delay ──────────────────────────")
    df = load_csv(filename)

    # ── 1. Standardise column names ────────────────────────────────────────
    df.columns = (
        df.columns
        .str.strip()
        .str.replace(" ", "_")
        .str.replace(r"[^\w]", "", regex=True)
        .str.lower()
    )

    # ── 2. Report missing values ───────────────────────────────────────────
    report_missing(df, "customs_delay (raw)")

    # ── 3. Drop rows missing the primary target variable ──────────────────
    if "customs_delay_days" in df.columns:
        before = len(df)
        df = df.dropna(subset=["customs_delay_days"])
        dropped = before - len(df)
        if dropped:
            print(f"[DROP]  Removed {dropped:,} rows missing customs_delay_days")

    # ── 4. Remove duplicate rows ──────────────────────────────────────────
    before = len(df)
    df = df.drop_duplicates()
    if len(df) < before:
        print(f"[DEDUP] Removed {before - len(df):,} duplicate rows")

    # ── 5. Clip delay days to plausible range (0–365) ─────────────────────
    if "customs_delay_days" in df.columns:
        df["customs_delay_days"] = df["customs_delay_days"].clip(lower=0, upper=365)

    # ── 6. Ensure compliance score is in [0, 1] ───────────────────────────
    if "compliance_score" in df.columns:
        df["compliance_score"] = pd.to_numeric(df["compliance_score"], errors="coerce")
        # If score is on a 0–100 scale, normalise to 0–1
        if df["compliance_score"].max() > 1.0:
            df["compliance_score"] = df["compliance_score"] / 100
        df["compliance_score"] = df["compliance_score"].clip(0, 1)

    # ── 7. Encode risk flag as integer (0 / 1) ────────────────────────────
    if "risk_flag" in df.columns:
        df["risk_flag"] = df["risk_flag"].astype(str).str.strip().str.lower()
        df["risk_flag"] = df["risk_flag"].map(
            {"1": 1, "true": 1, "yes": 1, "high": 1,
             "0": 0, "false": 0, "no": 0,  "low": 0}
        )

    # ── 8. Derive delay severity bucket (for Tableau colour encoding) ──────
    if "customs_delay_days" in df.columns:
        df["delay_severity"] = pd.cut(
            df["customs_delay_days"],
            bins=[-1, 0, 2, 7, 14, 365],
            labels=["No delay", "1–2 days", "3–7 days", "8–14 days", "15+ days"]
        )

    # ── 9. Derive compliance tier ─────────────────────────────────────────
    if "compliance_score" in df.columns:
        df["compliance_tier"] = pd.cut(
            df["compliance_score"],
            bins=[-0.01, 0.4, 0.7, 0.9, 1.0],
            labels=["Poor (0–40%)", "Moderate (40–70%)", "Good (70–90%)", "Excellent (90–100%)"]
        )

    # ── 10. Flag for Panel 2 join readiness ───────────────────────────────
    df["dataset_source"] = "customs_delay"

    report_missing(df, "customs_delay (clean)")
    save_csv(df, "customs_delay_clean.csv")
    return df


# ═══════════════════════════════════════════════════════════════════════════
# DATASET 2 — Logistics & Supply Chain Operations
# Source: https://www.kaggle.com/datasets/datasetengineer/logistics-and-supply-chain-dataset
# ═══════════════════════════════════════════════════════════════════════════

def process_logistics_ops(filename: str = "logistics_ops.csv") -> pd.DataFrame:
    """
    Clean and enrich the logistics operations dataset.

    Key columns:
        Customs_Clearance_Time  — primary metric (Panel 3)
        Order_Fulfillment_Status — business impact variable
        Shipping_Costs           — cost analysis
        Port_Congestion_Level    — contextual variable
        Route_Risk_Level         — corridor risk
        Timestamp                — time series analysis
    """
    print("\n── Dataset 2: Logistics & Supply Chain Operations ─────────────────")
    df = load_csv(filename)

    # ── 1. Standardise column names ────────────────────────────────────────
    df.columns = (
        df.columns
        .str.strip()
        .str.replace(" ", "_")
        .str.replace(r"[^\w]", "", regex=True)
        .str.lower()
    )

    # ── 2. Parse timestamp ────────────────────────────────────────────────
    if "timestamp" in df.columns:
        df["timestamp"] = pd.to_datetime(df["timestamp"], errors="coerce")
        df["year"]  = df["timestamp"].dt.year
        df["month"] = df["timestamp"].dt.month
        df["month_name"] = df["timestamp"].dt.strftime("%b %Y")
        df["weekday"] = df["timestamp"].dt.day_name()
        invalid_ts = df["timestamp"].isna().sum()
        if invalid_ts:
            print(f"[WARN]  {invalid_ts:,} unparseable timestamps set to NaT")

    # ── 3. Report missing values ───────────────────────────────────────────
    report_missing(df, "logistics_ops (raw)")

    # ── 4. Remove duplicates ──────────────────────────────────────────────
    before = len(df)
    df = df.drop_duplicates()
    if len(df) < before:
        print(f"[DEDUP] Removed {before - len(df):,} duplicate rows")

    # ── 5. Clip numeric columns to plausible ranges ───────────────────────
    numeric_clips = {
        "customs_clearance_time":   (0, 60),     # days
        "shipping_costs":           (0, 500000),  # USD
        "port_congestion_level":    (0, 10),
        "route_risk_level":         (0, 10),
        "supplier_reliability_score": (0, 1),
    }
    for col, (lo, hi) in numeric_clips.items():
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")
            df[col] = df[col].clip(lower=lo, upper=hi)

    # ── 6. Encode fulfillment status ──────────────────────────────────────
    if "order_fulfillment_status" in df.columns:
        df["order_fulfillment_status"] = pd.to_numeric(
            df["order_fulfillment_status"], errors="coerce"
        ).fillna(0).astype(int)
        df["fulfillment_label"] = df["order_fulfillment_status"].map(
            {1: "On time", 0: "Late / failed"}
        )

    # ── 7. Clearance time bucket (for Tableau filters) ────────────────────
    if "customs_clearance_time" in df.columns:
        df["clearance_bucket"] = pd.cut(
            df["customs_clearance_time"],
            bins=[-1, 1, 3, 7, 14, 60],
            labels=["Same day", "1–3 days", "4–7 days", "8–14 days", "15+ days"]
        )

    # ── 8. AI scenario column — apply 42% clearance reduction benchmark ───
    # Reference: CR Express operational reporting (2025)
    if "customs_clearance_time" in df.columns:
        df["clearance_time_with_ai"] = (df["customs_clearance_time"] * 0.58).round(2)

    # ── 9. Source label ───────────────────────────────────────────────────
    df["dataset_source"] = "logistics_ops"

    report_missing(df, "logistics_ops (clean)")
    save_csv(df, "logistics_ops_clean.csv")
    return df


# ═══════════════════════════════════════════════════════════════════════════
# DATASET 3 — Supply Chain Shipment Pricing (USAID)
# Source: https://www.kaggle.com/datasets/apoorvwatsky/supply-chain-shipment-pricing-data
# Official: https://data.usaid.gov/Global-Health-Supply-Chain/Supply-Chain-Shipment-Pricing-Data/a3rc-nmf6
# ═══════════════════════════════════════════════════════════════════════════

def process_shipment_pricing(filename: str = "shipment_pricing.csv") -> pd.DataFrame:
    """
    Clean and enrich the USAID shipment pricing dataset.

    Key columns:
        Freight_Cost_USD         — cost per shipment (Panel 4)
        Shipment_Mode            — air / sea / road / truck
        Country_of_Origin        — maps to Müller's corridors
        Destination_Country      — maps to Müller's corridors
        Line_Item_Value          — invoice complexity proxy
        Weight_Kilograms         — shipment size proxy
    """
    print("\n── Dataset 3: Supply Chain Shipment Pricing (USAID) ───────────────")
    df = load_csv(filename)

    # ── 1. Standardise column names ────────────────────────────────────────
    df.columns = (
        df.columns
        .str.strip()
        .str.replace(" ", "_")
        .str.replace(r"[^\w]", "", regex=True)
        .str.lower()
    )

    # ── 2. Report missing values ───────────────────────────────────────────
    report_missing(df, "shipment_pricing (raw)")

    # ── 3. Remove duplicates ──────────────────────────────────────────────
    before = len(df)
    df = df.drop_duplicates()
    if len(df) < before:
        print(f"[DEDUP] Removed {before - len(df):,} duplicate rows")

    # ── 4. Parse and clean freight cost ──────────────────────────────────
    freight_col = next(
        (c for c in df.columns if "freight" in c and "cost" in c), None
    )
    if freight_col:
        df[freight_col] = (
            df[freight_col]
            .astype(str)
            .str.replace(r"[$,]", "", regex=True)
            .str.strip()
        )
        df[freight_col] = pd.to_numeric(df[freight_col], errors="coerce")
        # Remove negative costs and extreme outliers (> USD 2M)
        df[freight_col] = df[freight_col].clip(lower=0, upper=2_000_000)
        df = df.rename(columns={freight_col: "freight_cost_usd"})

    # ── 5. Parse weight ───────────────────────────────────────────────────
    weight_col = next(
        (c for c in df.columns if "weight" in c or "kg" in c), None
    )
    if weight_col:
        df[weight_col] = pd.to_numeric(df[weight_col], errors="coerce")
        df[weight_col] = df[weight_col].clip(lower=0, upper=500_000)
        df = df.rename(columns={weight_col: "weight_kg"})

    # ── 6. Standardise shipment mode ─────────────────────────────────────
    mode_col = next(
        (c for c in df.columns if "shipment_mode" in c or "mode" in c), None
    )
    if mode_col:
        df[mode_col] = df[mode_col].astype(str).str.strip().str.title()
        df = df.rename(columns={mode_col: "shipment_mode"})

    # ── 7. Standardise country columns ───────────────────────────────────
    # Flag countries relevant to Müller's network
    muller_countries = {
        "Germany", "France", "Ghana", "Mozambique",
        "Namibia", "South Africa", "Canada", "United States"
    }
    for col in df.columns:
        if "country" in col or "origin" in col or "destination" in col:
            df[col] = df[col].astype(str).str.strip().str.title()

    # Add Müller relevance flag if origin or destination column exists
    origin_col = next((c for c in df.columns if "origin" in c), None)
    dest_col   = next((c for c in df.columns if "destination" in c), None)
    if origin_col and dest_col:
        df["muller_corridor"] = (
            df[origin_col].isin(muller_countries) |
            df[dest_col].isin(muller_countries)
        )

    # ── 8. Cost per kg (normalised cost metric) ───────────────────────────
    if "freight_cost_usd" in df.columns and "weight_kg" in df.columns:
        df["cost_per_kg"] = np.where(
            df["weight_kg"] > 0,
            (df["freight_cost_usd"] / df["weight_kg"]).round(4),
            np.nan
        )

    # ── 9. Parse scheduled delivery / actual dates if present ────────────
    for col in df.columns:
        if "date" in col or "scheduled" in col or "delivery" in col:
            df[col] = pd.to_datetime(df[col], errors="coerce")

    # ── 10. Source label ──────────────────────────────────────────────────
    df["dataset_source"] = "usaid_shipment_pricing"

    report_missing(df, "shipment_pricing (clean)")
    save_csv(df, "shipment_pricing_clean.csv")
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

    # Process each dataset — skip gracefully if file not yet downloaded
    for fn, processor in [
        ("customs_delay.csv",    process_customs_delay),
        ("logistics_ops.csv",    process_logistics_ops),
        ("shipment_pricing.csv", process_shipment_pricing),
    ]:
        try:
            results[fn] = processor(fn)
        except FileNotFoundError as e:
            print(str(e))
            print("        Skipping — add the file to data/raw/ and re-run.\n")

    # ── Summary ───────────────────────────────────────────────────────────
    print("\n" + "=" * 60)
    print("  Processing complete")
    print("=" * 60)
    for fn, df in results.items():
        print(f"  ✓  {fn.replace('.csv','')} → {df.shape[0]:,} rows × {df.shape[1]} cols")

    print(f"\n  Cleaned files saved to: {PROCESSED_DIR.resolve()}")
    print("\n  Next steps:")
    print("  1. Open Tableau and connect to data/processed/")
    print("  2. Connect benchmarks.csv and company_cases.csv as separate sources")
    print("  3. Build panels following dashboard_panels.md")


if __name__ == "__main__":
    main()
