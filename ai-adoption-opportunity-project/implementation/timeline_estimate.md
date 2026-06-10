# Timeline Estimate — Document Intelligence
**Project:** AI Adoption Opportunity — Document Intelligence
**Client:** CEO Olaf Müller, Hamburg-based logistics and transportation company (500 employees, 16 locations, 8 countries)
**Prepared:** June 2026
**Note on timeline methodology:** All timelines apply a 40% conservative adjustment to published industry benchmarks. Original benchmark timelines are shown for reference. Adjusted timelines are the working targets for this engagement.

---

## Timeline Overview

| Phase | Original benchmark | Adjusted (+40%) | Weeks |
|---|---|---|---|
| 1 — Discovery & Validation | 2–3 weeks | 3–4 weeks | Weeks 1–4 |
| 2 — Data Access & Preparation | 2–3 weeks | 3–4 weeks | Weeks 5–8 |
| 3a — Proof of Concept | 4–6 weeks | 6 weeks | Weeks 9–14 |
| 3b — PoC Validation Period | Not in benchmark | 4 weeks | Weeks 15–18 |
| 4 — Pilot (Germany–South Africa) | 8–10 weeks | 11–14 weeks | Weeks 19–34 |
| 5 — Rollout (full network) | 4–6 months | 6–8 months | Months 10–16 |
| **Total to first ROI** | **3–4 months** | **5–6 months** | |
| **Total to full deployment** | **10–12 months** | **16–18 months** | |

---

## Detailed Timeline

### Weeks 1–4 — Phase 1: Discovery & Validation

| Week | Activity | Owner | Output |
|---|---|---|---|
| 1 | CEO alignment meeting; scope and budget confirmation | CEO + project lead | Signed scope document |
| 1–2 | Stakeholder interviews: Operations, IT, Finance, Legal | Project lead | Validated assumptions log |
| 2–3 | Document volume audit — Germany–South Africa corridor | Operations + IT | Volume and format report |
| 2–3 | TMS integration feasibility assessment | IT lead | Integration complexity rating |
| 3–4 | Vendor shortlisting and initial demos (2–3 vendors) | Project lead + IT | Vendor shortlist with scores |
| 4 | Go/no-go review against Phase 1 criteria | CEO + project lead | Go/no-go decision |

**Milestone: Go/no-go decision — end of Week 4**

---

### Weeks 5–8 — Phase 2: Data Access & Preparation

| Week | Activity | Owner | Output |
|---|---|---|---|
| 5 | Document sample collection (200–500 documents) | Operations | Anonymised document set |
| 5–6 | GDPR and POPIA data flow review | Legal | DPA terms confirmed |
| 6–7 | TMS field mapping with selected vendor | IT + vendor | Field mapping document |
| 6–7 | Extraction rules defined (mandatory fields, cross-validation rules) | Operations + vendor | Extraction rule specification |
| 7–8 | DPA signed; data sharing agreement in place | Legal + vendor | Signed DPA |
| 8 | Phase 2 review: data ready for PoC | Project lead | Readiness confirmation |

**Milestone: Document sample ready and DPA signed — end of Week 8**

---

### Weeks 9–18 — Phase 3: Proof of Concept + Validation

Phase 3 is extended to include a dedicated validation period after initial extraction results are available. Given the complexity of Müller's corridor network — multiple customs regimes, document languages, and degraded document quality on African lanes — a single extraction test pass is insufficient to confirm production readiness. The validation period stress-tests the model before any commitment to pilot go-live.

**Phase 3a — PoC Execution (Weeks 9–14)**

| Week | Activity | Owner | Output |
|---|---|---|---|
| 9–10 | AI Engineer configures model on Müller's document sample | AI Engineer + vendor | Model configuration log |
| 9–10 | Vendor runs initial extraction on 200–500 document sample | Vendor | First extraction accuracy report |
| 10 | Accuracy review against acceptance criteria | Operations + project lead | Pass/fail per criterion |
| 11 | Confidence scoring interface configured and tested | Vendor + IT | Working review interface |
| 11–12 | Declarant workflow test (2–3 declarants, sample documents) | Head of Customs + declarants | Declarant feedback report |
| 12–13 | TMS integration test — pre-population rate measured | IT + Data Engineer + vendor | Integration test report |
| 13–14 | Initial PoC results reviewed; gaps identified | AI Engineer + project lead | Gap analysis report |

**Phase 3b — Validation Period (Weeks 15–18)**

The validation period addresses three specific complexity factors in Müller's environment:

1. **Multi-regime document variation** — customs declarations differ structurally between EU, North American, and Sub-Saharan African corridors. The model must be validated on documents from each regime, not just the pilot corridor.
2. **Degraded document quality** — African corridor documents frequently arrive as low-resolution scans, fax copies, or mobile photos. Extraction accuracy on degraded inputs must be confirmed separately from clean PDF performance.
3. **Hazardous goods documentation** — MSDS and DGD documents carry additional mandatory fields with high compliance risk. If these are in scope, they require a separate extraction validation pass.

| Week | Activity | Owner | Output |
|---|---|---|---|
| 15 | Model refinement based on PoC gap analysis | AI Engineer + vendor | Updated model configuration |
| 15–16 | Extended document sample test — include degraded quality documents | AI Engineer + Operations | Degraded document accuracy report |
| 15–16 | Multi-regime validation — test on EU, North American, and African corridor document formats | AI Engineer + Head of Customs | Regime coverage report |
| 16–17 | Hazardous goods document validation (if in scope) | AI Engineer + Legal | Hazmat extraction accuracy report |
| 17 | Declarant re-test on refined model — measure improvement vs Week 11–12 results | Head of Customs + declarants | Updated declarant feedback |
| 17–18 | Final accuracy measurement against all acceptance criteria | AI Engineer + project lead | Final PoC validation report |
| 18 | Validation sign-off meeting — go/no-go for pilot | CEO + Head of Customs + project lead | Signed validation sign-off |
| 18 | Vendor contract signed (conditional on validation sign-off) | Legal + CEO | Signed vendor contract |

**Validation acceptance criteria — must all pass before proceeding to pilot:**

| Criterion | Minimum threshold |
|---|---|
| Overall field extraction accuracy | 90%+ across all document types tested |
| HS code accuracy | 92%+ |
| Degraded document accuracy | 80%+ on low-resolution / fax / mobile photo inputs |
| Green (auto-approve) rate | 55%+ of fields |
| Declarant review time per flagged document | Under 90 seconds average |
| Multi-regime coverage | All three corridor types (EU, North America, Africa) validated |
| Hazardous goods fields (if in scope) | 95%+ accuracy on mandatory hazmat fields |

**If validation criteria are not met at Week 18:**
- AI Engineer identifies root cause (document quality, model gap, integration issue)
- Two-week remediation window added before re-test (pushes pilot start to Week 21)
- If criteria still not met after remediation → vendor reassessment before proceeding

**Milestone: PoC initial results — end of Week 14**
**Milestone: Validation sign-off — end of Week 18**

---

### Weeks 19–34 — Phase 4: Pilot (Germany–South Africa Corridor)

| Week | Activity | Owner | Output |
|---|---|---|---|
| 19–20 | System configuration for live corridor | Vendor + IT | Live system ready |
| 20 | Staff training — customs declarants and AP team | Vendor + Head of Customs | Trained pilot team |
| 21–22 | Parallel run — AI alongside manual; no live submissions yet | Declarants + Operations | Parallel run comparison data |
| 22 | Parallel run review — proceed to live? | Head of Customs + project lead | Go-live confirmation |
| 23 | **Go-live — AI system primary on Germany–South Africa corridor** | Operations | Live deployment |
| 23–34 | Weekly KPI monitoring: error rate, cost, confidence scores | Head of Customs + Finance | Weekly KPI report |
| 28 | Mid-pilot review — trajectory assessment | CEO + project lead | Mid-pilot status report |
| 34 | **Pilot end review — results vs success criteria** | CEO + all stakeholders | Pilot results report |
| 34 | Rollout decision | CEO | Proceed / extend / halt |

**Milestone: Pilot go-live — Week 23**
**Milestone: Pilot results review — Week 34**

---

### Months 8–14 — Phase 5: Full Network Rollout

| Stage | Corridors | Timeline | Key dependency |
|---|---|---|---|
| Stage 2 | Germany–Canada, Germany–USA | Months 8–10 | Pilot results confirmed positive |
| Stage 3 | Germany–France (intra-EU) | Months 10–11 | Stage 2 stable |
| Stage 4 | Ghana, Namibia, Mozambique lanes | Months 11–14 | Local legal review complete |

**Per corridor rollout time (Stages 2–4): 3–4 weeks each**

---

### Month 4 onwards — Phase 6: Monitoring & Improvement Loop

| Activity | Frequency | Owner |
|---|---|---|
| KPI dashboard review | Monthly | Head of Customs + Finance |
| Confidence score distribution review | Monthly | IT + Operations |
| Model accuracy audit | Quarterly | Vendor + IT |
| Corridor expansion assessment | At each stage gate | Project lead + CEO |
| Opportunity 2 readiness assessment | Month 12 | CEO + project lead |

---

## Key Milestones Summary

| Milestone | Target date |
|---|---|
| Go/no-go decision | End of Week 4 |
| DPA signed; data ready | End of Week 8 |
| PoC initial results | End of Week 14 |
| PoC validation sign-off | End of Week 18 |
| Vendor selected and contracted | End of Week 18 |
| Pilot go-live (Germany–South Africa) | Week 23 (~Month 6) |
| First measurable ROI data | Week 28 (~Month 7) |
| Pilot results review | Week 34 (~Month 9) |
| Stage 2 go-live (Canada/USA) | Month 11 |
| Stage 3 go-live (France) | Month 13 |
| Stage 4 go-live (African corridors) | Month 15 |
| Full network live | Month 16 |
| Opportunity 2 readiness review | Month 14 |

---

## Comparison: Benchmark vs Adjusted Timelines

| Event | Industry benchmark | This plan (adjusted) | Difference |
|---|---|---|---|
| Time to PoC initial results | 9–10 weeks | 14 weeks | +40% |
| Time to PoC validation sign-off | Not in benchmark | 18 weeks | Sector complexity addition |
| Time to pilot go-live | 10–12 weeks | 23 weeks | +40% + validation period |
| Time to first ROI data | 3–4 months | 5–6 months | +40% + validation period |
| Time to full deployment | 10–12 months | 16–18 months | +40% + validation period |
| Payback period | 60–90 days | 3–4 months | +40% |
| First-year ROI | 30–200% | 20–140% | Conservative adjustment |

**Why the adjustment is credible:**
The published benchmarks reflect best-case deployments at companies with clean data infrastructure, direct API integration, and dedicated project teams. Müller's environment adds mid-market complexity: TMS integration uncertainty, multi-corridor regulatory variation, and a team managing this alongside live operations. The 40% adjustment is a planning buffer, not a pessimistic forecast — if assumptions validate well in Phase 1, the timeline may compress back toward benchmark.
