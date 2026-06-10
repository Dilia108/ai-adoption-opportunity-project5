# Implementation Plan — Document Intelligence
**Project:** AI Adoption Opportunity — Document Intelligence
**Client:** CEO Olaf Müller, Hamburg-based logistics and transportation company (500 employees, 16 locations, 8 countries)
**Prepared:** June 2026
**Note on timelines:** All timelines apply a 40% conservative adjustment to published benchmarks to reflect real-world implementation complexity at mid-market scale.

---

## Phase Overview

| Phase | Name | Duration | Key output |
|---|---|---|---|
| 1 | Discovery & Validation | Weeks 1–4 | Go/no-go decision with confirmed assumptions |
| 2 | Data Access & Preparation | Weeks 5–8 | Validated document sample; TMS integration scoped |
| 3 | Proof of Concept | Weeks 9–14 | Extraction accuracy confirmed on real documents |
| 4 | Pilot — Germany–South Africa corridor | Weeks 15–28 | Measured ROI on live corridor |
| 5 | Rollout — full network | Months 8–14 | Full 8-country deployment |
| 6 | Monitoring & improvement loop | Ongoing from Month 4 | Continuous accuracy and ROI tracking |

---

## Phase 1 — Discovery & Validation (Weeks 1–4)

**Objective:** Confirm the assumptions behind the business case before any build commitment.

### Steps

**1.1 Stakeholder confirmation**
- CEO alignment meeting: confirm scope, budget range, and decision timeline
- Operations / Head of Customs: confirm daily document volume per corridor; identify highest-friction document types
- IT / Systems lead: confirm TMS API or export availability; identify integration constraints
- AI Engineer: assess vendor platform options; define model configuration requirements and accuracy thresholds
- Data Engineer: map existing data flows; confirm TMS export formats and field availability for pipeline design
- Legal / Compliance: initiate GDPR and POPIA data flow review for EU–South Africa and EU–Ghana corridors
- Finance: confirm current AP cycle time and cost per invoice from internal data

**1.2 Document volume audit**
- Count invoices, customs declarations, and bills of lading processed per month on the Germany–South Africa corridor
- Identify document receipt method (digital PDF, scanned, fax, email)
- Flag any paper-only document types requiring scanning infrastructure

**1.3 Vendor landscape assessment**
- Shortlist 2–3 Document Intelligence platforms with confirmed logistics and customs experience
- Prioritise vendors with: EU data residency, GDPR-compliant DPA, API integration capability, confidence scoring interface
- Reference check against CSG deployment model

**1.4 Go/no-go criteria**

| Criterion | Minimum threshold |
|---|---|
| Monthly document volume (pilot corridor) | 200+ invoices and declarations combined |
| TMS integration feasibility | API or structured export confirmed by IT |
| Document digitisation rate | 70%+ of documents already in digital format |
| Legal clearance | No blocking issue identified in GDPR/POPIA review |
| Vendor match | At least one vendor meeting all four platform criteria |

---

## Phase 2 — Data Access & Preparation (Weeks 5–8)

**Objective:** Prepare a representative document sample and confirm extraction feasibility.

### Steps

**2.1 Document sample collection**
- Collect 200–500 representative documents from the Germany–South Africa corridor
- Include range of document types: invoices, declarations, bills of lading, proof of delivery
- Include range of document quality: clean PDFs, scanned, fax, mobile photos
- Anonymise any personal data before sharing with vendor (GDPR requirement)

**2.2 TMS integration scoping**
- IT lead and Data Engineer map data fields available via TMS API or export
- Data Engineer confirms field mapping between TMS output and Document Intelligence input
- Integration complexity rated: low (direct API), medium (file-based export), high (custom build required)
- Integration cost estimated and added to project budget

**2.3 Field mapping and extraction rules**
- Define the priority extraction fields: invoice number, date, vendor, line items, HS codes, declared values, country of origin
- Define completeness rules: which fields are mandatory for each document type
- Define value cross-validation rules: which fields must match across invoice, packing list, and declaration

**2.4 Data Processing Agreement**
- Legal review of vendor DPA
- Confirm data residency (EU servers for EU corridor data; confirm South Africa POPIA compliance for SA corridor)
- Sign DPA before any live document processing begins

---

## Phase 3 — Proof of Concept (Weeks 9–14)

**Objective:** Confirm that the selected vendor can extract Müller's actual documents at the required accuracy level before committing to a full pilot.

### Steps

**3.1 Extraction accuracy test**
- AI Engineer configures extraction model on Müller's document sample
- Run 200–500 document sample through the vendor platform
- Measure extraction accuracy per field type (invoice number, HS code, declared value, etc.)
- Measure confidence score distribution: % green / orange / red per document type

**3.2 Acceptance criteria**

| Metric | Minimum threshold for proceeding to pilot |
|---|---|
| Overall field extraction accuracy | 90%+ |
| HS code extraction accuracy | 95%+ (high compliance risk if wrong) |
| Green (auto-approve) rate | 60%+ of documents |
| Processing time per document | Under 60 seconds |
| Degraded document handling | Acceptable accuracy on fax/scan samples |

**3.3 Human review workflow test**
- Configure confidence scoring interface for customs declarants
- Run 2–3 declarants through review workflow with sample documents
- Measure: time to review an orange-flagged document; ease of correction interface; declarant feedback

**3.4 Integration test**
- Test TMS data feed into the Document Intelligence platform
- Confirm pre-population of declaration fields from TMS + extracted document data combined
- Measure: fields pre-populated without manual input (target: 60%+ at PoC stage)

**3.5 Go/no-go for pilot**
If acceptance criteria are met → proceed to Phase 4.
If not met → identify root cause (document quality, vendor limitations, integration gap) and either remediate or reassess vendor selection before proceeding.

---

## Phase 4 — Pilot: Germany–South Africa Corridor (Weeks 15–28)

**Objective:** Measure real ROI on live operations on the highest-complexity corridor before network rollout.

### Why Germany–South Africa first
- Combines EU customs requirements (origin) with POPIA compliance (destination)
- Energy and industrial sector shipments carry complex, multi-line invoices
- African corridor complexity makes the ROI case most visible
- Success here is directly transferable to Ghana, Mozambique, and Namibia lanes

### Steps

**4.1 Go-live preparation**
- Staff training: customs declarants and AP team (half-day session; focus on review interface, not AI concepts)
- Parallel run period: AI system runs alongside manual process for 2 weeks — outputs compared but manual submission used
- Go-live: AI system becomes primary; human review mandatory before submission

**4.2 Success criteria — measured at end of pilot (Week 28)**

| Metric | Baseline | Target (end of pilot) |
|---|---|---|
| Document error rate | 8–15% | Under 7% |
| Cost per invoice | EUR 12–20 | EUR 8–12 |
| Processing time per document | 7+ minutes | Under 3 minutes |
| Fields pre-populated | 0% | 40%+ |
| AP cycle time | 45 days | Under 35 days |
| Customs delay reduction (SA corridor) | Baseline measured in Week 1 | −15% |
| Declarant time on value-added tasks | ~10% | 25%+ |

**4.3 Weekly monitoring during pilot**
- Error rate tracked weekly (target: downward trend from Week 3)
- Confidence score distribution tracked (target: green rate increasing week on week)
- Declarant feedback collected fortnightly
- Any compliance incident logged and reviewed within 24 hours

**4.4 Pilot review meeting (Week 28)**
- Present results against success criteria to CEO and Head of Customs
- Decision: proceed to full rollout / extend pilot / halt and reassess

---

## Phase 5 — Full Network Rollout (Months 8–14)

**Objective:** Extend Document Intelligence to all 8 countries and 16 locations.

### Rollout sequence

| Stage | Corridors | Timeline |
|---|---|---|
| Stage 1 (pilot) | Germany–South Africa | Months 4–7 |
| Stage 2 | Germany–Canada / Germany–USA | Months 8–10 |
| Stage 3 | Germany–France (internal EU flows) | Months 10–11 |
| Stage 4 | Ghana, Namibia, Mozambique lanes | Months 11–14 |

**Why this sequence:**
- Stage 2 adds volume quickly on familiar EU and North American regulatory frameworks
- Stage 3 validates the system on intra-EU flows before adding African complexity
- Stage 4 applies lessons from all previous stages to the highest-risk corridors

### Rollout steps per corridor
1. Document sample audit (1 week)
2. Field mapping and extraction rules configured for local document formats
3. Local legal / compliance review (POPIA for SA already done; Ghana DPA, Namibia requirements)
4. Staff training at local locations (half-day per location)
5. 2-week parallel run
6. Go-live with confidence scoring active

---

## Phase 6 — Monitoring & Improvement Loop (Ongoing from Month 4)

**Objective:** Ensure the system continues to improve and ROI is tracked and reported.

### Monthly KPI dashboard

| Metric | Frequency | Owner |
|---|---|---|
| Document error rate | Monthly | Head of Customs |
| Cost per invoice | Monthly | Finance |
| AP cycle time | Monthly | Finance |
| Fields pre-populated rate | Monthly | Operations |
| Confidence score distribution (green/orange/red) | Monthly | IT / Systems lead |
| Customs delay incidents | Monthly | Head of Customs |
| Declarant time on value-added tasks | Quarterly | Head of Customs |

### Model improvement triggers
- If green rate drops below 55% for two consecutive months → review extraction rules
- If error rate increases above 5% → immediate review of affected document types
- If a new document format is introduced by a client or customs authority → add to extraction model within 2 weeks

### Annual review
- Full accuracy audit across all corridors
- Reassess vendor contract and platform capability
- Assess readiness for Opportunity 2 (Operational Copilot for Planners) based on data quality now available from Document Intelligence outputs
