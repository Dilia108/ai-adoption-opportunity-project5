# Datasets Sources and Dashboard Panels Mapping

---

## Story Structure

The dashboard tells a single argument across five panels in two acts.

**Act 1 — The problem (Panels 1–3)**
No mention of AI. Olaf reads three panels that describe his current reality and arrives at Panel 4 already feeling the problem.

**Act 2 — The solution (Panels 4–5)**
AI is introduced as the answer to a problem already established — not as a product pitch.

---

## Data Sources per Panel

| Panel | Title | Dataset(s) | What it shows |
|---|---|---|---|
| 1 | 1 in 8 documents contains an error | `benchmarks.xlsx` (Manual scenario) | Manual error rate, cost per invoice, processing time, staff throughput — the daily reality before any technology |
| 2 | Three error types — three consequences | `benchmarks.xlsx` (Manual scenario) | Wrong HS code → fine + hold; missing document → clearance hold 3–14 days; value mismatch → physical inspection |
| 3 | Each error compounds into a chain of business cost | `benchmarks.xlsx` (Supply Chain Impact + ROI categories) | Cost chain: error → hold → mode switch → margin hit; AP cycle time before/after; logistics cost, margin, and service level impact |
| 4 | AI eliminates each error type at source | `benchmarks.xlsx` (AI scenario) + `company_cases.xlsx` | Same three error types from Panel 2, resolved; before/after on error rate, time, accuracy; CSG, CR Express, KlearNow proof |
| 5 | The financial return — and why the timing matters | `benchmarks.xlsx` (ROI & Financial + Market & Adoption) | Cost per invoice, processing time, AP cycle time, payback, first-year ROI, margin impact; competitive adoption gap |

---

## Processed Files Overview

| Processed file | Source | Used in panels | Notes |
|---|---|---|---|
| `LPI_data.xlsx` | `LPICSV.csv` (World Bank) | Panel 1 (supporting context) | LPI corridor scores embedded as supporting context inside Panel 1, not as a standalone chart |
| `LPI_countries.xlsx` | `LPICountry.csv` (World Bank) | Panel 1 (supporting context) | Joined to LPI_data in Tableau for region and income group |
| `LPI_indicators.xlsx` | `LPISeries.csv` (World Bank) | Panel 1 (supporting context) | Joined to LPI_data in Tableau for indicator definitions |
| `benchmarks.xlsx` | Pre-curated | Panels 1–5 | Primary data source across all panels; filter by scenario and category |
| `company_cases.xlsx` | Pre-curated | Panel 4 | Filter `relevance_to_muller` = "Direct" for the proof section |

---

## Panel Detail

---

### Panel 1 — 1 in 8 documents contains an error
**Act:** Problem
**Hook:** The error rate as an immediate, operational number Olaf can translate to his own volume.

**Primary dataset:** `benchmarks.xlsx` — filter `scenario = 'Manual'`

| Metric shown | Column | Value |
|---|---|---|
| Manual document error rate | `metric` = Error rate | 8–15% |
| Cost per invoice — manual | `metric` = Cost per invoice | USD 12–20 |
| Processing time — manual | `metric` = Processing time | 5–17 days |
| Staff throughput | `metric` = Documents per hour | 5 docs/hr |
| Time per declaration | `metric` = Time per document | 7+ minutes |
| AP cycle time | `metric` = AP cycle time | 45 days |
| Document accuracy | `metric` = Document accuracy rate | 88% |

**Supporting context (inside panel, not lead):**
World Bank LPI 2023 corridor scores for Müller's 8 countries. Filter `LPI_data.xlsx` on `indicator_label = 'customs_score'` and `year = 2023`. Used to explain that errors cost more in low-LPI corridors (Ghana rank 97, Mozambique rank 115, Namibia rank 66) — not as a standalone chart.

**AP (accounts payable) cycle time definition (display as footnote):**
*AP cycle time = days from receiving an invoice to completing processing, validation, and approval for payment.*

---

### Panel 2 — Three error types — three consequences
**Act:** Problem
**Structure:** Three mirrored cards — same layout reused in Panel 4 so Olaf reads Panel 4 as "problem resolved."

**Primary dataset:** `benchmarks.xlsx` — filter `scenario = 'Manual'`, `category = 'Document Processing'`

| Card | Error type | Label | Consequence shown |
|---|---|---|---|
| 1 | Submission error | Wrong HS code | USD 10K fine + container held |
| 2 | Completeness error | Missing document | Clearance hold 3–14 days |
| 3 | Consistency error | Value mismatch | Physical inspection triggered |

**Card colour coding (for Tableau):**
- Card 1 (Wrong HS code): red bottom — highest financial consequence
- Card 2 (Missing document): amber bottom — high time consequence
- Card 3 (Value mismatch): amber bottom — high operational consequence

**Callout text (hardcoded):**
*All three errors are manual data entry problems. They occur because staff re-key data across documents, work from different source files, and have no automated cross-validation before submission.*

---

### Panel 3 — Each error compounds into a chain of business cost
**Act:** Problem — bridge between Panel 2 errors and Panel 5 ROI

**Primary dataset:** `benchmarks.xlsx` — filter `category IN ('Supply Chain Impact', 'ROI & Financial')`

**Cost chain (left to right — hardcoded labels, values from benchmarks):**

| Step | Label | Value | Metric |
|---|---|---|---|
| 1 | Document error | 8–15% | of submitted documents contain errors |
| 2 | Customs hold | 3–14 days | shipment detained pending correction |
| 3 | Missed window | 2× freight cost | air replaces ocean when deadline is lost |
| 4 | Margin erosion | 4–7% | net margin — any cost spike hits profit directly |

**Charts:**

*Left — AP cycle time (bar chart, manual vs AI for context):*
- Manual: 45 days
- With AI: 12 days
- Source: `benchmarks.xlsx`, `metric` = AP cycle time

*Right — Business impact (bar chart, amber — shows cost of NOT acting):*
- Logistics cost reduction potential: 15%
- Margin improvement for mid-market 3PLs: 52.5%
- Service level improvement: 65%
- Source: `benchmarks.xlsx`, `category = 'Supply Chain Impact'`

**Callout text (hardcoded):**
*At 4–7% net margins, a 2–3% cost increase from document-driven delays is not a rounding error. For energy and industrial clients with zero tolerance for delivery failures, the reputational cost compounds the financial one.*

---

### Panel 4 — AI eliminates each error type at source
**Act:** Solution
**Structure:** Three mirrored cards matching Panel 2 exactly — same error type labels, same card order. Green bottoms replace red/amber to signal resolution.

**Primary dataset 1:** `benchmarks.xlsx` — filter `scenario = 'AI'`

| Before/after metric | Manual value | AI value | Column |
|---|---|---|---|
| Error rate | 8–15% | <1% | `metric` = Error rate |
| Time per document | 7 min (420s) | 30 seconds | `metric` = Time per document |
| Fields pre-populated | — | 80–90% | `metric` = Fields pre-populated |
| Clearance time reduction | baseline | −42% | `metric` = Customs clearance time reduction |
| Simple tasks efficiency | baseline | +99% | `metric` = Documentation efficiency simple |
| Complex declarations | baseline | +36% | `metric` = Documentation efficiency complex |

**Primary dataset 2:** `company_cases.xlsx` — filter `relevance_to_muller = 'Direct'`, `result_type = 'Quantitative'`

| Company | Metric shown | Value | Highlight |
|---|---|---|---|
| Customs Support Group | Efficiency gain simple / complex | 99% / 36% | ✓ Closest structural match — highlighted card |
| CR Express | Clearance time reduction | −42% | — |
| KlearNow.AI | Manual error reduction | −85% | — |

**Callout text (hardcoded):**
*The improvement is largest precisely where it matters most — Mozambique, Ghana, Namibia — where manual errors have the highest clearance cost and the lowest tolerance for re-submission.*

---

### Panel 5 — The financial return — and why the timing matters
**Act:** Solution

**Primary dataset:** `benchmarks.xlsx` — filter `category = 'ROI & Financial'`

| ROI card | Manual | AI | Metric column |
|---|---|---|---|
| Cost per invoice | USD 12–20 | USD 2–3 | Cost per invoice |
| Processing time | 5–17 days | 6–12 hours | Processing time |
| AP cycle time | 45 days | 12 days | AP cycle time |
| Payback period | — | 60–90 days | Payback period |
| First-year ROI | — | 30–200% | First-year ROI |
| Margin improvement | Net 4–7% | +30–75% | Margin improvement |

**Competitive gap chart:** `benchmarks.xlsx` — filter `category = 'Market & Adoption'`
- Large enterprises AI adoption: 70%
- Mid-sized providers (Müller): 28%

**Callout text (hardcoded):**
*70% of large logistics operators have already adopted AI. Only 28% of mid-sized providers have. Early movers are building the clean data track record, the AEO compliance profile, and the client confidence that late movers will have to buy back at a higher cost.*

---

## Benchmark Data Reference

### benchmarks.xlsx — scenario = 'Manual' (Panels 1–3)

| Category | Metric | Value | Source |
|---|---|---|---|
| Document Processing | Error rate | 8–15% | Fluxity.ai 2025 |
| Document Processing | Cost per invoice | USD 12–20 | Parseur / APQC 2025 |
| Document Processing | Processing time | 5–17 days | Parseur 2025 |
| Document Processing | Documents per hour | 5 | DocStreams.ai 2025 |
| Document Processing | Time per document | 7+ minutes | Docsumo IDP 2025 |
| Document Processing | AP cycle time | 45 days | Docsumo 2025 |
| Document Processing | Document accuracy rate | 88% | DocStreams.ai / CR Express |
| Supply Chain Impact | Logistics cost reduction | 15% | McKinsey / StartUs Insights 2025 |
| Supply Chain Impact | Margin improvement | 52.5% | European Logistics Association 2025 |
| Supply Chain Impact | Service level improvement | 65% | StartUs Insights 2025 |

### benchmarks.xlsx — scenario = 'AI' (Panel 4)

| Category | Metric | Value | Source |
|---|---|---|---|
| Document Processing | Error rate | <1% | Fluxity.ai 2025 |
| Document Processing | Cost per invoice | USD 2–3 | Parseur / APQC 2025 |
| Document Processing | Time per document | 30 seconds | Docsumo IDP 2025 |
| Document Processing | AP cycle time | 12 days | Docsumo 2025 |
| Customs Clearance | Fields pre-populated | 80–90% | FreightMynd 2026 |
| Customs Clearance | Customs clearance time reduction | −42% | CR Express 2025 |
| Customs Clearance | Documentation efficiency simple | +99% | Customs Support Group 2025 |
| Customs Clearance | Documentation efficiency complex | +36% | Customs Support Group 2025 |
| Customs Clearance | Document accuracy rate | 99.5% | CR Express 2025 |

### benchmarks.xlsx — category = 'ROI & Financial' (Panel 5)

| Metric | Value | Source |
|---|---|---|
| Payback period | 60–90 days | Docsumo / IDC 2025 |
| First-year ROI | 30–200% | Docsumo / IDC 2025 |
| Margin improvement — 3PL | +30–75% | European Logistics Association 2025 |
| Cost reduction | Up to 80% | Parseur / Vroozi 2025 |
| Staff productivity gain | +50% | Docsumo 2025 |
| 3-year median ROI | 3.5× investment | McKinsey via DocShipper 2025 |

### benchmarks.xlsx — category = 'Market & Adoption' (Panel 5)

| Metric | Value | Source |
|---|---|---|
| Large enterprise AI adoption | 70% | Penske Transportation Leaders Survey 2025 |
| Mid-sized provider AI adoption | 28% | DocShipper 2025 |

---

## company_cases.xlsx — Panel 4 Reference

Filter: `relevance_to_muller = 'Direct'`, `result_type = 'Quantitative'`

| Company | Use case | Metric | Value | Source |
|---|---|---|---|---|
| Customs Support Group | Document Intelligence | Efficiency — simple tasks | +99% | CSG press release + Intelligent CIO Europe, May 2025 |
| Customs Support Group | Document Intelligence | Efficiency — complex declarations | +36% | CSG press release + Intelligent CIO Europe, May 2025 |
| Customs Support Group | Document Intelligence | Declarations processed digitally/year | 4 million | Intelligent CIO Europe, April 2025 |
| CR Express | Customs clearance | Clearance time reduction | −42% | CR Express CFS operations, December 2025 |
| CR Express | Customs clearance | Document accuracy | 99.5% | CR Express CFS operations, December 2025 |
| KlearNow.AI | Document processing | Manual error reduction | −85% | KlearNow.AI 2025 |
| FreightMynd | Declaration automation | Fields pre-populated | 80–90% | FreightMynd, January 2026 |

---

## World Bank LPI — Tableau Join Guide

**Files:** `LPI_data.xlsx`, `LPI_countries.xlsx`, `LPI_indicators.xlsx`
**Used in:** Panel 1 supporting context only

**In Tableau Data Source tab:**
1. Connect `LPI_data.xlsx` as primary source
2. Add `LPI_countries.xlsx` — join on `country_code = country_code`
3. Add `LPI_indicators.xlsx` — join on `indicator_code = indicator_code`

**Filters for Panel 1 context:**
- `indicator_label = 'customs_score'`
- `year = 2023`
- `country_code IN ('DEU','FRA','GHA','MOZ','NAM','ZAF','CAN','USA')`

**Key scores (2023 — or most recent available):**

| Country | Customs score | Global rank | Data year | Note |
|---|---|---|---|---|
| Canada | 4.0 | 7 | 2023 | — |
| Germany | 3.9 | 3 | 2023 | — |
| France | 3.7 | 13 | 2023 | — |
| United States | 3.7 | 17 | 2023 | — |
| South Africa | 3.3 | 19 | 2023 | — |
| Namibia | 2.8 | 66 | 2023 | — |
| Ghana | 2.7 | 97 | 2023 | — |
| Mozambique | 2.5 | 115 | 2016 | No 2023 survey data available |

---

## Source Notes

### Customs Support Group (CSG)
- **Primary:** CSG, *Customs Support Group Deploys AI-Powered Smart Document Processing Across Europe*, May 2025 — https://www.customssupport.com/customs-support-group-deploys-ai-powered-smart-document-processing-across-europe/
- **Verification:** Intelligent CIO Europe, *CSG carries industry from burden to business opportunity through AI innovation*, April 2025 — https://www.intelligentcio.com/eu/2025/04/11/customs-support-group-carries-industry-from-burden-to-business-opportunity-through-ai-innovation/
- **Detail:** CSG, *Artificial Intelligence (AI) Meets Customs*, March 2026 — https://www.customssupport.com/artificial-intelligence-ai-meets-customs/
- **Why it matters:** Closest structural match to Müller — multi-country European operator, same customs workflows, 14 markets

### CR Express
- **Article:** CR Express, *AI for Customs Clearance in CFS*, December 2025 — https://www.crexpressinc.com/blog/ai/ai-customs-clearance-cfs
- **Note:** Chicago-based logistics operator (founded 1999, 280,000 sq ft near O'Hare). The 42% clearance time reduction and 99.5% accuracy are reported from their own CFS operations.

### Parseur invoice benchmarks
- **Article:** Parseur, *AI Invoice Processing Benchmarks 2026*, November 2025 — https://parseur.com/blog/ai-invoice-processing-benchmarks
- **Underlying sources:** APQC Open Standards Benchmarking (Accounts Payable); Deloitte / Basware; Ascend (USD 2.36 per invoice)

### Docsumo / IDC / Gartner
- **Primary:** Docsumo, *50 Key Statistics in IDP for 2025* — https://www.docsumo.com/blogs/intelligent-document-processing/intelligent-document-processing-market-report-2025
- **Analyst sources cited within:** Gartner Magic Quadrant for IDP 2025; IDC MarketScape IDP 2025–2026

### World Bank LPI
- **Download:** https://databank.worldbank.org/data/download/LPI_xlsx.zip
- **License:** Creative Commons Attribution 4.0 (CC BY 4.0)
- **Survey:** 652 logistics professionals, 139 countries, 2023
- **Note on Mozambique:** No 2023 survey data available; 2016 score (2.5) used as most recent available

### Fluxity.ai
- **Article:** https://www.fluxity.ai/blog/ai-invoice-processing-cost-savings-2025

### FreightMynd
- **Article:** https://freightmynd.com/blog/customs-declaration-automation-ai/ — January 2026

### KlearNow.AI
- **Source:** KlearNow.AI operational reporting, 2025
