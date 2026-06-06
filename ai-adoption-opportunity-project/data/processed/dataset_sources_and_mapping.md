# Datasets sources and Dashboard Panels mapping for providing evidence

## Data Sources per Panel

| Panel | Dataset | What it shows |
|---|---|---|
| 1. Current state: delay by corridor | Customs Delay | Where time is being lost today |
| 2. Root cause: compliance score vs. clearance time | Customs Delay + Ops | Documentation quality drives delay |
| 3. Business impact: clearance time vs. fulfillment | Ops dataset | Delays translate into missed deliveries |
| 4. Cost map: freight cost by corridor | USAID Shipment Pricing | Where financial exposure is highest |
| 5. The fix: AI accuracy benchmark overlay | Published stats (CSG, CR Express) | What Document Intelligence changes |
| 6. ROI card: cost per invoice manual vs. AI | Published benchmarks | The financial case in one number |

Panels 1–4 use Kaggle data. Panels 5–6 use published benchmark figures from the research (CSG's 99% accuracy, 42% clearance time reduction from CR Express, USD 2.78 vs USD 12.88 invoice cost from Parseur) as reference lines overlaid on the charts — making the gap between today and the AI scenario visible in one view.

---

## Panel Datasets

---

**Files overview processed:**

* `benchmarks.csv`         → Panel 5 and 6 (AI vs manual comparison)
* `company_cases.csv`      → Panel 5 peer evidence
* `customs_delay_clean.csv`      → Panel 1 and 2 (Kaggle dataset 1)
* `logistics_ops_clean.csv`      → Panel 3 (Kaggle dataset 2)
* `shipment_pricing_clean.csv`   → Panel 4 (USAID / Kaggle dataset 3)

---

### Panels 1–2: Cross-Border Trade & Customs Delay Dataset

- **Source:** Kaggle — ziya07
- **URL:** https://www.kaggle.com/datasets/ziya07/cross-border-trade-and-customs-delay-dataset
- **Size:** 10,000+ shipment records
- **Key columns:**
  - `Customs_Delay_Days` — average delay per route, translatable to cost
  - `Risk_Flag` — proportion of shipments flagged as high-risk
  - `Compliance_Score` — relationship between documentation quality and clearance speed
  - `Inspection_Type` — whether delays are document-driven or physical
  - `Prior_Offense_Count` — how repeat errors compound over time
  - `Trade_Route` — segmentation by corridor

### Panel 3: Logistics & Supply Chain Operations Dataset

- **Source:** Kaggle — datasetengineer
- **URL:** https://www.kaggle.com/datasets/datasetengineer/logistics-and-supply-chain-dataset
- **Size:** Hourly records, January 2021 – January 2024
- **Key columns:**
  - `Customs_Clearance_Time` — primary metric linking documentation to speed
  - `Order_Fulfillment_Status` — links customs delay to missed deliveries
  - `Shipping_Costs` — cost variance across routes and conditions
  - `Port_Congestion_Level` — contextualises delays (port-driven vs. document-driven)
  - `Route_Risk_Level` — segments high-risk corridors
  - `Supplier_Reliability_Score` — upstream data quality issues cascading into document errors

### Panel 4: Supply Chain Shipment Pricing Data (USAID)

- **Source:** USAID / Kaggle
- **Kaggle URL:** https://www.kaggle.com/datasets/apoorvwatsky/supply-chain-shipment-pricing-data
- **Official government source:** https://data.usaid.gov/Global-Health-Supply-Chain/Supply-Chain-Shipment-Pricing-Data/a3rc-nmf6
- **Nature:** Real government procurement data — strongest credibility signal for executive audience
- **Key columns:**
  - `Freight_Cost_USD` — cost per shipment and variance across carriers and routes
  - `Line_Item_Value` — invoice complexity (more line items = higher manual processing risk)
  - `Shipment_Mode` — air vs. sea vs. road (different document requirements)
  - `Country_of_Origin` / `Destination_Country` — maps onto Müller's 8-country footprint
  - `Vendor_and_Carrier` — multi-party document flows
  - `Weight_Kilograms` — proxy for shipment complexity

---

## Panel Benchmarks

### Panel 5: The Fix — AI Accuracy Benchmark Overlay

Reference lines overlaid on Kaggle charts. Hardcoded values with source citations.

| Metric | Manual | AI | Source | URL |
|---|---|---|---|---|
| Document accuracy rate | 85–92% | 99–99.5% | DocStreams.ai / CR Express | https://www.crexpressinc.com/blog/ai/ai-customs-clearance-cfs |
| Processing time per document | 7+ minutes | Under 30 seconds | Docsumo IDP Market Report 2025 | https://www.docsumo.com/blogs/intelligent-document-processing/intelligent-document-processing-market-report-2025 |
| Customs clearance time reduction | Baseline | −42% | CR Express CFS operations | https://www.crexpressinc.com/blog/ai/ai-customs-clearance-cfs |
| Documentation efficiency — simple tasks | Baseline | +99% | Customs Support Group rollout 2025 | https://www.customssupport.com/customs-support-group-deploys-ai-powered-smart-document-processing-across-europe/ |
| Documentation efficiency — complex tasks | Baseline | +36% | Customs Support Group / Intelligent CIO Europe | https://www.intelligentcio.com/eu/2025/04/11/customs-support-group-carries-industry-from-burden-to-business-opportunity-through-ai-innovation/ |
| Customs delay reduction | Baseline | −30% | FreightAmigo / VirtualWorkforce.ai | https://virtualworkforce.ai/ai-for-customs-documentation-emails/ |

### Panel 6: ROI Card — Cost per Invoice Manual vs. AI

KPI card layout — four numbers showing before/after on cost, time, error rate, and payback period.

| Metric | Manual | AI | Source | URL |
|---|---|---|---|---|
| Cost per invoice | USD 12.88–19.83 | USD 2.36–2.78 | Parseur / APQC / Ascend | https://parseur.com/blog/ai-invoice-processing-benchmarks |
| Processing time | 5–17.4 days | 6–12 hours | Parseur best-in-class benchmarks 2025 | https://parseur.com/blog/ai-invoice-processing-benchmarks |
| Error rate | 8–15% | Under 1% | Fluxity.ai 2025 | https://www.fluxity.ai/blog/ai-invoice-processing-cost-savings-2025 |
| Payback period | — | 60–90 days | Multiple sources | https://www.docsumo.com/blogs/intelligent-document-processing/intelligent-document-processing-market-report-2025 |
| First-year ROI | — | 30–200% | Docsumo / IDC | https://www.docsumo.com/blogs/intelligent-document-processing/intelligent-document-processing-market-report-2025 |
| Cost reduction | — | Up to 80% | Parseur / Vroozi 2025 | https://parseur.com/blog/ai-invoice-processing-benchmarks |

---

## Source Notes

### CSG results
- **Primary (press release):** Customs Support Group, *Customs Support Group Deploys AI-Powered Smart Document Processing Across Europe*, 20 May 2025 — https://www.customssupport.com/customs-support-group-deploys-ai-powered-smart-document-processing-across-europe/
- **Verification:** Intelligent CIO Europe, *Customs Support Group carries industry from burden to business opportunity through AI innovation*, 11 April 2025 — https://www.intelligentcio.com/eu/2025/04/11/customs-support-group-carries-industry-from-burden-to-business-opportunity-through-ai-innovation/
- **Italy rollout detail:** Customs Support Group, *Artificial Intelligence (AI) Meets Customs*, March 2026 — https://www.customssupport.com/artificial-intelligence-ai-meets-customs/

### Parseur invoice benchmarks
- **Article:** Parseur, *AI Invoice Processing Benchmarks 2026 — Accuracy, Speed, and Cost Comparison*, November 2025 — https://parseur.com/blog/ai-invoice-processing-benchmarks
- **Underlying sources cited within:** APQC Open Standards Benchmarking (Accounts Payable); Deloitte partnership with Basware (89% touchless processing figure); Ascend (USD 2.36 per invoice figure)

### CR Express figures
- **Article:** CR Express, *AI for Customs Clearance in CFS*, December 2025 — https://www.crexpressinc.com/blog/ai/ai-customs-clearance-cfs
- **Note:** CR Express is a Chicago-based logistics operator (founded 1999, 280,000 sq ft facility near O'Hare International Airport). The 42% clearance time reduction and 99.5% accuracy figures are reported from their own CFS operations.

### Docsumo — Gartner and IDC analyst data
- **Primary statistics article:** Docsumo, *50 Key Statistics and Trends in Intelligent Document Processing (IDP) for 2025* — https://www.docsumo.com/blogs/intelligent-document-processing/intelligent-document-processing-market-report-2025
- **Analyst references cited within:**
  - Gartner Magic Quadrant for Intelligent Document Processing Solutions (2025)
  - IDC MarketScape: Worldwide Intelligent Document Processing Software 2025–2026
- **Additional Docsumo article referencing both:** https://www.docsumo.com/blog/what-is-agentic-document-processing