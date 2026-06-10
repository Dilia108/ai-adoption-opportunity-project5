# Technical Solution Draft — Document Intelligence
**Project:** AI Adoption Opportunity — Document Intelligence
**Client:** CEO Olaf Müller, Hamburg-based logistics and transportation company (500 employees, 16 locations, 8 countries)
**Prepared:** June 2026
**Status:** Draft — for internal review before client presentation

---

## 1. Solution Overview

The Document Intelligence system automates the extraction, validation, and pre-population of structured data from incoming logistics documents. It sits between document receipt and the customs declaration / accounts payable workflow — eliminating manual re-keying, reducing error rates, and accelerating processing time across all corridors.

The architecture follows the model deployed by Customs Support Group across 14 European markets in 2025, adapted for Müller's multi-corridor, multi-regulatory environment.

**Core technology stack:**
- Optical Character Recognition (OCR) — converts document images to machine-readable text
- Machine Learning (ML) — classifies document types and learns field extraction patterns over time
- Natural Language Processing (NLP) — interprets unstructured text, resolves context, maps values to structured fields
- Rule-based validation engine — checks completeness and cross-validates values across documents
- Confidence scoring interface — routes extracted fields to human review based on certainty thresholds

---

## 2. System Architecture

### 2.1 High-level data flow

```
[Document sources]
      │
      ▼
[Ingestion layer]        ← email, FTP, API, scanned upload
      │
      ▼
[Document classifier]    ← identifies: invoice / declaration / B/L / POD / packing list
      │
      ▼
[AI extraction engine]   ← OCR + ML + NLP per document type
      │
      ▼
[Validation engine]      ← completeness check + cross-validation rules
      │
      ▼
[Confidence scoring]     ← Green / Orange / Red per field
      │
      ├── Green → auto-pre-populate declaration fields
      ├── Orange → route to declarant review interface
      └── Red → flag for manual entry (AI draft shown as reference)
      │
      ▼
[Human review interface] ← declarant reviews, corrects, approves
      │
      ▼
[TMS / customs system]   ← pre-populated declaration submitted by licensed declarant
      │
      ▼
[Audit log + feedback]   ← corrections feed back to model for continuous improvement
```

### 2.2 Integration points

| System | Integration type | Direction | Purpose |
|---|---|---|---|
| TMS (Transportation Management System) | REST API or structured file export | Bidirectional | Shipment context for pre-population; declaration status back to TMS |
| Customs declaration system | API or direct field injection | Outbound | Pre-populate declaration fields from extracted data |
| Finance / ERP / AP system | API or file-based | Outbound | Pre-populate invoice fields for AP processing |
| Document ingestion channels | Email IMAP, FTP, HTTP upload | Inbound | Receive documents from clients, carriers, and customs authorities |
| Audit log / retention system | Database write | Outbound | HGB 10-year and UCC 3-year retention compliance |
| KPI dashboard | Database read | Outbound | Real-time monitoring of accuracy, throughput, and error rates |

---

## 3. Four Processing Stages

### Stage 1 — Document Ingestion and Classification

The system monitors all incoming document streams continuously:
- Email attachments (PDF, TIFF, JPEG, PNG)
- FTP uploads from carriers and clients
- API feeds from the TMS
- Manual uploads via the review interface

Each document is classified by type before any extraction begins:

| Document type | Extraction model applied |
|---|---|
| Commercial invoice | Invoice extraction model |
| Customs declaration | Declaration pre-population model |
| Bill of lading | B/L extraction model |
| Packing list | Packing list model |
| Certificate of origin | Origin certificate model |
| Proof of delivery | POD extraction model |

**Handling degraded documents:** The system processes handwritten notes, low-resolution scans, fax copies, and mobile phone photos. This capability is confirmed by the CSG deployment, which specifically tested on degraded document quality across European markets.
*(Source: CSG press release May 2025 — https://www.customssupport.com/customs-support-group-deploys-ai-powered-smart-document-processing-across-europe/)*

---

### Stage 2 — AI Extraction

OCR converts the document image to machine-readable text. NLP then interprets context and extracts structured field values.

**Priority extraction fields — commercial invoice:**

| Field | Extraction method | Validation rule |
|---|---|---|
| Invoice number | Pattern recognition (alphanumeric) | Unique per shipment |
| Invoice date | Date extraction + normalisation | Within shipment window |
| Vendor / shipper name | NLP entity recognition | Match against TMS vendor list |
| Consignee | NLP entity recognition | Match against TMS consignee list |
| Line items (description, quantity, unit price) | Table extraction + NLP | Sum matches invoice total |
| Total declared value | Numeric extraction | Matches sum of line items |
| Currency | Entity recognition | Confirmed against shipment record |
| Country of origin | NLP + controlled vocabulary | Valid ISO country code |
| Incoterms | Keyword extraction | Valid Incoterms 2020 code |

**Priority extraction fields — customs declaration:**

| Field | Extraction method | Validation rule |
|---|---|---|
| HS code | NLP classification against HS tariff schedule | Cross-referenced against product description |
| Declared value | Numeric extraction | Matches commercial invoice value |
| Gross / net weight | Numeric extraction | Matches packing list |
| Number of packages | Numeric extraction | Matches packing list |
| Country of origin | NLP + controlled vocabulary | Matches certificate of origin |
| Consignor / consignee | NLP entity recognition | Matches commercial invoice |

**Multi-language support:** Documents in German, English, French, and relevant African corridor languages (where applicable) are processed. NLP models are language-aware — field extraction adapts to document language without separate preprocessing.

---

### Stage 3 — Confidence-Scored Validation

Every extracted field receives a confidence score. The score reflects the model's certainty about the extracted value, based on document quality, field clarity, and consistency with other extracted fields.

**Traffic-light routing:**

| Score | Label | Action | Typical cause |
|---|---|---|---|
| High confidence | Green | Auto-approved; field pre-populated without human review | Clean PDF, unambiguous field, consistent with TMS data |
| Medium confidence | Orange | Flagged for declarant review; suggested value shown | Partially degraded scan, ambiguous text, value inconsistent with TMS |
| Low confidence / missing | Red | Manual entry required; AI draft shown as reference only | Unreadable field, missing data, extraction failed |

**Target distribution (after 3 months of model learning on Müller's documents):**
- Green: 60–70% of fields
- Orange: 20–30% of fields
- Red: 5–10% of fields

This distribution is consistent with the FreightMynd benchmark of 80–90% fields pre-populated after model maturation, and the CSG deployment results.
*(Source: FreightMynd, January 2026 — https://freightmynd.com/blog/customs-declaration-automation-ai/)*

**Cross-validation rules (rule-based, not AI):**

| Rule | Documents checked | Action on failure |
|---|---|---|
| Declared value match | Invoice ↔ Declaration | Flag both fields Orange |
| Weight consistency | Packing list ↔ Declaration | Flag declaration weight Orange |
| HS code consistency | Invoice description ↔ Declaration HS code | Flag HS code Orange for declarant review |
| Document set completeness | Required documents per shipment type | Block submission until set is complete |
| Country of origin consistency | Invoice ↔ Certificate of origin ↔ Declaration | Flag origin field Orange |

**Completeness check:** Before any declaration can be submitted, the system verifies the full document set is present. Missing documents are flagged before the border, not after — eliminating 3–14 day clearance holds caused by incomplete submissions.

---

### Stage 4 — Human Review and Submission

A licensed customs declarant reviews all Orange and Red fields via the review interface. The declarant:
- Sees the AI-suggested value alongside the original document section it was extracted from
- Accepts, corrects, or overrides each flagged field
- Signs off the complete declaration before submission to customs authorities

**Legal responsibility:** The licensed declarant remains the legal submitter under EU Union Customs Code. The AI pre-populates and flags — it never submits. This is a non-negotiable operating procedure and satisfies EU AI Act minimal-risk classification.

**Feedback loop:** Every correction made by a declarant feeds back into the model. The AI Engineer reviews correction patterns weekly in the first 3 months. Fields with persistent Orange or Red rates above threshold trigger model retraining on the affected document type.

---

## 4. Technical Infrastructure Requirements

### 4.1 Deployment options

| Option | Description | Best for |
|---|---|---|
| SaaS (cloud-hosted) | Vendor manages infrastructure; Müller accesses via browser and API | Fastest deployment; lowest internal IT burden; recommended for pilot |
| Private cloud | Vendor platform deployed on Müller's cloud tenant (Azure / AWS / GCP) | Higher data control; required if data residency constraints cannot be met by vendor |
| On-premise | Full deployment on Müller's own servers | Maximum control; highest cost and IT complexity; not recommended for initial deployment |

**Recommendation:** SaaS deployment for pilot and rollout. Confirm EU data residency with selected vendor before contract signature.

### 4.2 TMS integration — technical detail

| Integration method | Complexity | Prerequisites |
|---|---|---|
| REST API (real-time) | Low | TMS exposes REST API with authentication; vendor provides API connector |
| Webhook / event-driven | Low–Medium | TMS supports outbound webhooks on shipment events |
| Structured file export (CSV/XML/JSON) | Medium | TMS scheduled export configured; SFTP or file drop set up |
| Custom middleware | High | Required only if TMS has no standard export; Data Engineer builds connector |

**Fields required from TMS for pre-population:**
- Shipment ID / reference number
- Origin and destination country
- Consignor and consignee details
- Commodity description
- Estimated value and currency
- Carrier and transport mode
- Departure and arrival dates

### 4.3 Security and access control

| Requirement | Implementation |
|---|---|
| Role-based access | Declarants access review interface only; AI Engineer accesses model config; Data Engineer accesses pipeline; Admin accesses all |
| Document encryption | All documents encrypted at rest (AES-256) and in transit (TLS 1.3) |
| Audit trail | Every field extraction, correction, and submission logged with timestamp and user ID |
| Data residency | EU-based servers for EU corridor data; South Africa POPIA compliance confirmed with vendor |
| Retention | HGB §257: 10-year retention for commercial invoices and correspondence; UCC: 3-year customs records |
| NIS2 compliance | AI system covered by Müller's cybersecurity policy; 24-hour incident reporting capability required |

---

## 5. AI Model Specification

### 5.1 Model types used

| Component | Model type | Purpose |
|---|---|---|
| Document classification | CNN / ViT (Vision Transformer) | Identifies document type from layout and visual features |
| Field extraction — structured documents | Fine-tuned transformer (e.g. LayoutLM, Donut) | Extracts fields from tables and structured layouts |
| Field extraction — unstructured / degraded | OCR + sequence-to-sequence NLP | Handles handwritten, fax, low-resolution inputs |
| HS code classification | NLP + tariff schedule lookup | Maps product description to HS code with confidence score |
| Cross-document consistency | Rule engine + embedding similarity | Flags value mismatches across invoice, packing list, declaration |
| Confidence scoring | Calibrated probability output | Assigns Green / Orange / Red per field based on extraction certainty |

### 5.2 Model training and adaptation

**Pre-trained base:** The selected vendor's platform will have a pre-trained base model on logistics document types. The AI Engineer fine-tunes this on Müller's specific document formats during Phase 3 (Proof of Concept).

**Fine-tuning inputs:**
- 200–500 representative documents from the Germany–South Africa corridor (anonymised)
- Field-level ground truth annotations for the first 100 documents (created by Head of Customs team)
- HS code taxonomy relevant to Müller's commodity types (energy equipment, textiles, furniture, hazardous goods)

**Ongoing learning:**
- Declarant corrections feed back to the model weekly
- AI Engineer reviews correction patterns and triggers retraining when error patterns emerge
- Model version controlled — rollback available if a retraining event reduces accuracy

### 5.3 Accuracy targets

| Metric | Minimum acceptable | Target after 3 months |
|---|---|---|
| Overall field extraction accuracy | 90% | 95%+ |
| HS code accuracy | 92% | 97%+ |
| Declared value accuracy | 95% | 99%+ |
| Green (auto-approve) rate | 55% | 65%+ |
| Processing time per document | Under 60 seconds | Under 30 seconds |
| False positive rate (incorrect Green) | Under 3% | Under 1% |

---

## 6. Data Pipeline — Data Engineer Specification

### 6.1 Pipeline architecture

```
[Source systems]          [Pipeline]              [Destination systems]
TMS ──────────────────► Data normalisation ──────► Document Intelligence platform
Email / FTP / API ────► Document ingestion ──────► Review interface
                         │
                         ▼
                     Validation layer
                         │
                         ▼
                     Audit log (PostgreSQL / cloud DB)
                         │
                         ▼
                     KPI dashboard (Tableau / BI tool)
```

### 6.2 Data Engineer responsibilities

| Responsibility | Detail |
|---|---|
| TMS connector | Build and maintain the integration between TMS and Document Intelligence platform |
| Field mapping | Define and maintain the mapping between TMS fields and extraction model input/output fields |
| Data quality monitoring | Alert on pipeline failures, missing fields, or unexpected data formats |
| Audit log design | Schema design for extraction events, correction events, and submission events |
| Retention policy enforcement | Automated archiving and deletion per HGB and UCC requirements |
| KPI data feed | Pipeline from audit log to KPI dashboard for monthly reporting |

### 6.3 Key data quality rules

| Rule | Frequency | Action on failure |
|---|---|---|
| TMS feed received within expected window | Per shipment | Alert to Data Engineer; flag affected documents for manual check |
| Document ingestion rate within normal range | Daily | Alert if daily volume drops below 50% of 30-day average |
| Extraction completion rate | Daily | Alert if more than 5% of documents fail to complete extraction |
| Audit log write success | Per event | Alert on any write failure; no event to be lost |

---

## 7. Compliance and Legal Technical Requirements

| Requirement | Technical implementation |
|---|---|
| EU AI Act — minimal risk | Human review mandatory before submission; no autonomous customs filing; confidence scoring documented |
| GDPR — data minimisation | Only fields required for customs / AP processing extracted and stored; no personal data stored beyond retention requirements |
| GDPR — data processing agreement | Vendor DPA signed before any live document processing; data residency confirmed |
| EU Union Customs Code | Licensed declarant signs off all declarations; AI output is pre-population only, never autonomous submission |
| HGB §257 — 10-year retention | Document archive configured from day one; retention policy enforced by Data Engineer |
| UCC — 3-year customs records | Separate retention tier for customs-specific records |
| South Africa POPIA | Cross-border transfer clauses in vendor agreement; legal basis documented for SA corridor data flows |
| Ghana Data Protection Act | Legal basis documented for Ghana corridor data flows before Stage 4 rollout |
| NIS2 | AI system included in Müller's cybersecurity scope; 24-hour incident reporting capability in place before go-live |

---

## 8. Vendor Selection Criteria

The AI Engineer and IT lead will evaluate shortlisted vendors against the following criteria during Phase 1:

| Criterion | Weight | Notes |
|---|---|---|
| Extraction accuracy on logistics documents | High | Test on Müller's actual document sample in Phase 3 |
| EU data residency | Mandatory | Non-negotiable for GDPR compliance |
| GDPR-compliant DPA | Mandatory | Must be signed before any document processing |
| API integration capability | High | REST API preferred; file-based acceptable |
| Confidence scoring interface | High | Traffic-light model required |
| Logistics and customs domain experience | High | Reference deployments in freight forwarding preferred |
| Multi-language document support | Medium | German, English, French minimum |
| Model fine-tuning capability | Medium | Vendor must allow fine-tuning on Müller's document types |
| Pricing model | Medium | Consumption or SaaS; no per-seat licensing preferred |
| Vendor financial stability | Medium | Mid-market vendor risk — confirm funding and client base |

**Reference deployments to validate against:**
- Customs Support Group (14 European markets, customs declaration automation)
- CR Express (CFS operations, 42% clearance time reduction)
- KlearNow.AI (customs document processing, 85% manual error reduction)

---

## 9. Known Technical Risks and Mitigations

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| TMS has no API or structured export | Medium | High | Confirm in Phase 1 Week 1; if absent, budget for custom connector (EUR 10,000–20,000 additional) |
| Document quality too low for reliable extraction on African corridors | Medium | Medium | Test on sample of Ghana / Mozambique documents in Phase 3 before Stage 4 rollout |
| Vendor model underperforms on Müller's specific HS code taxonomy | Low–Medium | High | Fine-tuning on Müller's commodity types is mandatory in Phase 3; acceptance criteria gate before pilot go-live |
| Data residency non-compliance | Low | High | Confirm vendor server location before DPA signature; walk away if EU residency not available |
| Model accuracy degrades after retraining event | Low | Medium | Version control on all model deployments; rollback procedure documented before go-live |
| Pipeline failure causes documents to be missed | Low | High | Alerting on ingestion rate anomalies; fallback to manual process documented and tested |
| Confidence scoring threshold too aggressive (too many Greens) | Medium | High | AI Engineer sets conservative initial thresholds; tighten gradually as model performance is validated |

---

## 10. Open Questions for Phase 1 Assessment

The following must be confirmed before technical design is finalised:

| Question | Owner | Why it matters |
|---|---|---|
| What TMS is in use and does it have a REST API? | IT lead | Determines integration complexity and cost |
| What is the monthly document volume per corridor? | Operations | Determines platform pricing model and ROI timeline |
| What % of documents are received digitally vs paper? | Operations | Determines whether scanning infrastructure is needed |
| What document languages are common on African corridors? | Head of Customs | Determines NLP language model requirements |
| Are hazardous goods documents (MSDS, DGD) in scope for Phase 1? | Head of Customs + Legal | Hazmat documents have additional regulatory complexity — may be Phase 2+ |
| What is the current customs declaration system? | IT lead | Determines pre-population integration method |
| Is there an existing document archive (DMS)? | IT lead | Determines whether historical documents are available for model fine-tuning |
| What are the Ghana DPA and Namibia data protection requirements? | Legal | Must be confirmed before Stage 4 corridor rollout |
