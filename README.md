# AI Adoption Opportunity — Document Intelligence
**Project type:** AI Use Case Discovery, Business Case, and Dashboard Prototype
**Client:** CEO Olaf Müller, Hamburg-based logistics and transportation company (500 employees, 16 locations, 8 countries)
**Prepared:** June 2026
**Author:** Dilia Navarro

---

## Project Summary

This project identifies, justifies, and presents the strongest AI adoption opportunity for a mid-size third-party logistics provider (3PL) operating across Europe, North America, and Sub-Saharan Africa. The recommended use case is **Document Intelligence** — AI-powered extraction, validation, and pre-population of customs and invoice data.

The deliverables include a Tableau dashboard built as an executive presentation, a full implementation plan, a technical solution draft, and supporting business case documentation.


**Process note:**

This project went through two phases before reaching its current form.

The initial research phase explored publicly available datasets — including Kaggle logistics and customs datasets and Hugging Face document processing datasets. This was very usefull to understand public data available. Nevertheless, after assessment, none provided the field-level specificity needed for a credible CEO-level business case. The decision was made to build the data foundation from pre-curated benchmark files sourced from named industry publications, operator case studies from public press releases and annual reports, and the World Bank LPI dataset for geographic context. Every number in the dashboard has a named source and a URL.

The dashboard also evolved during construction. Several visualisations were simplified from their original design — combined charts replaced with small multiples, some panels split in two to avoid overcrowding. These decisions prioritised readability over technical complexity, reflecting what communicates most effectively in a one-to-one executive presentation.

---

## 1. Use Case Discovery and Description

### Business context and problem statement

Müller's company processes thousands of logistics documents per month across 8 countries and 16 locations — commercial invoices, customs declarations, bills of lading, and proof-of-delivery documents. All of these are processed manually: staff re-key data from one document into another, cross-check values by hand, and assign HS codes from product descriptions without automated support.

The result is a documented industry-wide problem that applies directly to this operating environment:

- **8–15% of submitted documents contain errors** — wrong HS codes, missing documents, or value mismatches across invoice and declaration
- **Each error costs EUR 12–20 to process** and triggers a cascade: customs hold (3–14 days), missed delivery window, air freight at 4–6x cost, and direct margin erosion
- **AP cycle time is 45 days** — working capital tied up in slow invoice processing
- **At 4–7% net margins**, a 2–3% cost increase from document errors is the difference between a profitable and unprofitable shipment

The problem is amplified by geography. Four of Müller's eight corridors score below 3.0 on the World Bank Logistics Performance Index customs efficiency scale (Ghana: 2.5, Namibia: 2.7, Mozambique: 2.5) — meaning errors on African corridors are harder to correct and slower to resolve than on European or North American lanes.

### Stakeholder identification

| Stakeholder | Role in decision |
|---|---|
| CEO Olaf Müller | Primary decision-maker — sole authority on adoption |
| Head of Customs / Operations | Process owner — daily impact of errors and delays |
| Customs declarants | Primary end users of the solution |
| Finance / AP team | Secondary users — invoice processing workflow |
| IT / Systems lead | TMS integration assessment |
| AI Engineer | Model configuration and performance monitoring |
| Data Engineer | Pipeline design and data quality |
| Legal / Compliance | GDPR, POPIA, EU AI Act assessment |

### Discovery process and assumptions

Three AI opportunities were evaluated and compared on six criteria: data dependency, time to ROI, implementation cost, regulatory upside, risk level, and competitive precedent. The three candidates were:

1. **Document Intelligence** — reads and extracts data from logistics documents
2. **Operational Copilot for Planners** — demand forecasting and load optimisation
3. **Shipment Visibility and Risk Prediction** — predictive ETA and disruption alerting

Document Intelligence was selected as the first move because it requires no historical data preparation (existing documents are the input), has the fastest documented ROI in logistics AI (3–4 months, conservatively adjusted to 3–4 months), and directly addresses the confirmed operational problem.

Full comparison and justification: `research/opportunities_risks.md`

### Why this use case matters

Three reasons specific to this client:

1. **No data dependency.** Unlike demand forecasting or route optimisation, Document Intelligence works on documents that already exist. There is no waiting period, no data preparation phase, and no dependency on historical data quality.

2. **Geographic amplifier.** Errors on Müller's African corridors — Ghana, Mozambique, Namibia — cost significantly more to correct than on European or North American lanes. The World Bank LPI data (Panel 1b of the dashboard) quantifies this risk by corridor. Document Intelligence reduces the error rate that drives this elevated cost.

3. **Competitive window.** 70% of large logistics operators have already adopted AI. Only 28% of mid-sized providers have. Early movers are building the clean data track record, the AEO compliance profile, and the client confidence that late movers will have to buy back at a higher cost.

### Expected outcomes and value

| Metric | Baseline | Conservative target (pilot) | Stretch (12 months) |
|---|---|---|---|
| Document error rate | 8–15% | Under 7% | Under 2% |
| Cost per invoice | EUR 12–20 | EUR 8–12 | EUR 2–3 |
| Processing time per document | 7+ minutes | Under 3 minutes | Under 45 seconds |
| AP cycle time | 45 days | Under 35 days | 12 days |
| Fields pre-populated | 0% | 40% | 80–90% |
| Customs delay reduction | Baseline | −15% | −30% |
| First-year ROI | — | 20–140% (conservative) | — |
| Payback period | — | 3–4 months | — |

---

## 2. Dataset Justification

### Dataset 1 — benchmarks.xlsx

**Source:** Pre-curated from named industry publications
**Location:** `data/processed/benchmarks.xlsx` · Raw: `data/raw/benchmarks.csv`

**Description:** 45 rows, one per metric per scenario. Covers document processing benchmarks (Manual and AI scenarios), customs clearance metrics, ROI and financial metrics, and market adoption rates. Key columns: `metric`, `scenario`, `kpi_value`, `unit`, `category`, `source`, `source_year`, `notes`.

**Why appropriate:** Every metric in the dashboard is sourced from a named publication with a year and URL. The benchmark data directly measures the operational problem (error rate, processing time, cost) and the AI solution outcome (accuracy rate, clearance time reduction, payback period) — making the before/after comparison credible and auditable.

**Data quality:** All values are midpoints or explicitly labelled bounds (lower/upper). Where ranges exist (e.g. cost per invoice EUR 12–20), both bounds are stored as separate rows and formatted as a range in Tableau calculated fields. No imputed values. Payback period and ROI figures have been conservatively adjusted by +40% from published benchmarks to reflect mid-market implementation complexity.

**Preprocessing:** CSV source (`benchmarks.csv`) processed to Excel via `data/processed/process_datasets.py`. Column `kpi_value` renamed from `value` in v1 to avoid Tableau field naming conflicts. Three rows updated with +40% conservative adjustment: payback period (75 → 105 days), first-year ROI upper (200% → 140%), first-year ROI lower (30% → 20%).

---

### Dataset 2 — company_cases.xlsx

**Source:** Pre-curated from named operator press releases, annual reports, and trade media
**Location:** `data/processed/company_cases.xlsx` · Raw: `data/raw/company_cases.csv`

**Description:** 30 rows covering AI deployment results at Customs Support Group, Kuehne+Nagel, Maersk, DB Schenker, CR Express, FreightMynd, KlearNow.AI, XPO Logistics, DHL, and unnamed operators. Key columns: `company`, `use_case`, `metric`, `result_value`, `result_type`, `relevance_to_muller`, `source`, `notes`.

**Why appropriate:** Provides named operator evidence that the benchmarks are achievable in production deployments — not projections. The `relevance_to_muller` field filters to Direct and Indirect relevance, allowing the dashboard to surface only the most comparable cases (Customs Support Group, CR Express, KlearNow.AI, FreightMynd).

**Data quality:** Quantitative results only are used in the dashboard (filtered on `result_type = 'Quantitative'`). All results are sourced from primary publications (press releases, annual reports, company operational reporting). Qualitative entries are retained in the dataset for research reference but excluded from visualisations.

**Preprocessing:** No transformation beyond CSV-to-Excel conversion.

---

### Dataset 3 — LPI_data.xlsx + LPI_countries.xlsx

**Source:** World Bank Logistics Performance Index 2023
**Download:** https://databank.worldbank.org/data/download/LPI_xlsx.zip
**Licence:** Creative Commons Attribution 4.0 (CC BY 4.0)
**Location:** `data/processed/LPI_data.xlsx`, `data/processed/LPI_countries.xlsx`
**Raw files:** `data/raw/LPICSV.csv`, `data/raw/LPICountry.csv`, `data/raw/LPISeries.csv`

**Description:** LPI_data contains one row per country × indicator × year (2007–2023). 19 indicator types covering overall LPI score/rank, customs efficiency, infrastructure, international shipments, logistics competence, timeliness, and tracking. LPI_countries contains country metadata: region, income group, currency.

**Why appropriate:** The World Bank LPI is the authoritative global benchmark for logistics and customs performance. The customs efficiency score directly quantifies why errors cost more in some corridors than others — providing the geographic evidence layer that makes the business case specific to Müller's network rather than generic.

**Data quality:** Official World Bank survey data, 652 logistics professionals, 139 countries, 2023. Mozambique has no 2023 survey entry — 2016 data (score 2.5) is used as the most recent available. This is disclosed in Panel 1b of the dashboard. All other Müller corridors have 2023 data.

**Preprocessing:** Long-format CSV processed to Excel. Filtered in Tableau to `indicator_label = 'customs_score'`, `year = 2023` (2016 for Mozambique), and `country_code IN (DEU, FRA, GHA, MOZ, NAM, ZAF, CAN, USA)`. Joined to `LPI_countries.xlsx` on `country_code` in Tableau for income group color-coding.

---

## 3. Dashboard Design Rationale

### Key metrics selection

Metrics were selected on one criterion: does this number appear in Olaf Müller's operational reality or his financial statements? Abstract industry averages were excluded. Every metric shown is either directly measurable at Müller's company or sourced from a structurally comparable operator.

The metric set covers three layers deliberately:

- **Operational inputs** (error rate, processing time, document accuracy) — Panel 1 and 4b — establish the problem and the solution in operational terms
- **Financial consequences** (cost per invoice, AP cycle time, margin impact) — Panels 3 and 5 — translate the operational problem into margin language
- **Strategic context** (corridor LPI scores, competitive adoption gap) — Panels 1b and 5 — make the case specific to Müller's geography and timing

### Visualization choices

| Chart type | Used for | Why |
|---|---|---|
| KPI text cards | Error rate, cost, processing time, AP cycle time (Panel 1) | Large headline numbers land faster than charts for a CEO audience |
| Gauge chart | Document accuracy rate (Panel 1) | Makes 89% accuracy visceral — the red arc is the problem |
| Horizontal bar chart | LPI corridor scores (Panel 1b), real companies results (Panel 4b), competitive gap (Panel 5) | Horizontal layout accommodates long labels; natural ranking from top to bottom |
| Small multiples — vertical bars | Before/after metrics (Panel 4b) | Each metric gets its own axis scale — prevents the 420-second processing time from compressing all other metrics |
| Text table | Financial return (Panel 5) | ROI metrics are ranges, not single values — a table communicates this honestly; bars would require averaging |
| Static PNG cards | Error types (Panel 2), cost chain (Panel 3a), AI resolution cards (Panel 4a) | Full typographic control for narrative cards with colored borders; Tableau text objects cannot replicate this layout |

### Layout and organisation decisions

**Two-act structure:** Panels 1–3 contain no mention of AI. The problem is established on its own terms before the solution appears. This prevents the dashboard from reading as a product pitch and ensures Olaf arrives at Panel 4 already feeling the problem.

**Panel 2 ↔ Panel 4 mirror:** The three error type cards use identical layout in both panels. Red and amber borders in Panel 2 become green in Panel 4a. The visual continuity signals resolution without requiring text explanation.

**Color system:** A four-color system is used consistently throughout — navy for primary/neutral, amber for warning/manual, red for highest risk, green for AI/improvement. Color carries meaning, not decoration.

**Separation of narrative and data:** Static image panels (3a, 4a) carry the narrative argument. Live Tableau sheets carry the data evidence. This separation keeps each element doing what it does best.

### How the dashboard supports the investment decision

The dashboard is structured to answer the four questions a CEO asks before committing to an AI investment:

| Question | Panel that answers it |
|---|---|
| What is the actual problem? | Panel 1 — error rate, cost, time |
| Is this problem specific to my business? | Panel 1b — corridor LPI scores for my 8 countries |
| What exactly goes wrong, and what does it cost? | Panels 2, 3a, 3b |
| Does AI actually fix it? | Panels 4a, 4b |
| What is the financial return, and why act now? | Panel 5 |

---

## 4. Implementation Plan Reference

### Where to find the implementation documents

| Document | Location | Contents |
|---|---|---|
| Solution proposal | `implementation/solution_proposal.md` | Use case summary, investment recommendation, solution description, roles |
| Implementation plan | `implementation/implementation_plan.md` | 6 phases, step-by-step activities, owners, milestones, success criteria |
| Technical solution draft | `implementation/technical_solution_draft.md` | System architecture, AI model specification, data pipeline, compliance, vendor criteria |
| Timeline estimate | `implementation/timeline_estimate.md` | Phase-by-phase timeline with 40% conservative adjustment; PoC validation period |
| Cost analysis | `cost_estimation/cost_analysis.md` | Three budget scenarios (EUR 82K–226K), ROI model, staff time costs |

### How the implementation connects to the dashboard prototype

The dashboard is the presentation layer of a complete project. Each implementation phase has a direct connection to what the dashboard demonstrates:

**Phase 1 (Discovery & Validation)** validates the assumptions behind Panel 1 — the error rate, document volume, and corridor risk data shown are the starting point for the business case that Phase 1 confirms or adjusts.

**Phase 2 (Data Access & Preparation)** produces the document sample and field mapping that the AI model in Panel 4b is benchmarked against. The extraction fields shown (HS code, declared value, fields pre-populated) are exactly the fields the Data Engineer maps in Phase 2.

**Phase 3 (Proof of Concept + Validation)** tests whether the Panel 4b metrics (99% accuracy, 30-second processing, 85% fields pre-populated) are achievable on Müller's actual documents. The acceptance criteria in the implementation plan mirror the Panel 4b chart targets.

**Phase 4 (Pilot)** produces the real data that would replace the benchmark data in Panel 4b — if the dashboard is updated post-pilot, the small multiple charts would show Müller's own before/after results rather than industry benchmarks.

**Phase 5 (Rollout)** expands the solution to all 8 corridors shown on Panel 1b. The corridor order in the implementation plan (Germany–South Africa first, African corridors last) maps directly to the risk ranking shown on the LPI corridor chart.

**Phase 6 (Monitoring)** generates the KPI data that would feed a live version of Panel 5 — cost per invoice, AP cycle time, and error rate tracked monthly against the baseline shown in the dashboard.

---

## 5. Project File Index

| File | Folder | Purpose |
|---|---|---|
| `README.md` | root | This file — project overview and documentation index |
| `requirements.txt` | root | Python dependencies for `process_datasets.py` |
| `Dashboard_ai_opportunity_v2.twbx` | `presentation/` | Tableau workbook — 9-panel executive presentation |
| `dashboard_documentation.md` | `dashboard/` | Full dashboard technical documentation |
| `benchmarks.xlsx` | `data/processed/` | Primary data source — all panels |
| `company_cases.xlsx` | `data/processed/` | Operator case studies — Panel 4b |
| `LPI_data.xlsx` | `data/processed/` | World Bank LPI scores — Panel 1b |
| `LPI_countries.xlsx` | `data/processed/` | Country metadata — Panel 1b |
| `LPI_indicators.xlsx` | `data/processed/` | LPI indicator definitions — reference |
| `dataset_sources_and_mapping.md` | `data/processed/` | Data lineage and panel-by-panel mapping |
| `process_datasets.py` | `data/processed/` | Script to regenerate processed files from raw CSVs |
| `solution_proposal.md` | `implementation/` | Investment recommendation and solution design |
| `implementation_plan.md` | `implementation/` | 6-phase implementation plan |
| `technical_solution_draft.md` | `implementation/` | Technical architecture and AI specification |
| `timeline_estimate.md` | `implementation/` | Timeline with conservative adjustments |
| `cost_analysis.md` | `cost_estimation/` | Budget scenarios and ROI model |
| `use_case_discovery.md` | `research/` | Full use case justification and stakeholder analysis |
| `market_research.md` | `research/` | Industry overview and AI adoption signals |
| `opportunities_risks.md` | `research/` | Opportunity comparison and risk register |
| `sources.md` | `research/` | Consolidated source list with URLs |

---

## 6. Sources

| Category | Sources |
|---|---|
| Document processing benchmarks | Fluxity.ai 2025 · Parseur / APQC 2025 · Docsumo IDP 2025 · DocStreams.ai 2025 · Quadient 2025 |
| Corridor risk | World Bank LPI 2023 (CC BY 4.0) · lpi.worldbank.org |
| Cost chain and business impact | McKinsey / StartUs Insights 2025 · European Logistics Association 2025 |
| AI solution evidence | CSG May 2025 · Intelligent CIO Europe April 2025 · CR Express Dec 2025 · FreightMynd Jan 2026 · KlearNow.AI 2025 |
| Financial return | Docsumo / IDC 2025 · Parseur / Vroozi 2025 · European Logistics Association 2025 |
| Market adoption | Penske Transportation Leaders Survey 2025 · DocShipper 2025 |
| Regulatory | European Commission EU Customs Reform · Deloitte EU AI Act November 2025 |
