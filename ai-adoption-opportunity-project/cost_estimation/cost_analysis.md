# Cost Analysis — Document Intelligence
**Project:** AI Adoption Opportunity — Document Intelligence
**Client:** CEO Olaf Müller, Hamburg-based logistics and transportation company (500 employees, 16 locations, 8 countries)
**Prepared:** June 2026
**Note:** All figures are estimates based on published mid-market benchmarks. Actual costs must be validated during Phase 1 vendor assessment. A 30% contingency is built into all ranges per Gartner guidance (62% of AI initiatives exceed budget by an average of 45%).

---

## 1. Cost Summary

| Cost component | Low estimate | High estimate | Notes |
|---|---|---|---|
| Platform / SaaS licence (annual) | EUR 18,000 | EUR 60,000 | Consumption or per-document pricing typical |
| Implementation & integration | EUR 15,000 | EUR 45,000 | TMS integration is the primary variable |
| Internal staff time (Phase 1–3) | EUR 25,000 | EUR 55,000 | IT, Operations, Legal, AI Engineer, Data Engineer |
| Training and change management | EUR 3,000 | EUR 8,000 | Half-day sessions across pilot locations |
| Legal / DPA review | EUR 2,000 | EUR 6,000 | GDPR + POPIA review; external legal if needed |
| Contingency (30%) | EUR 19,000 | EUR 52,000 | Per Gartner AI project overrun guidance |
| **Total Year 1** | **EUR 82,000** | **EUR 226,000** | |
| **Ongoing annual (Year 2+)** | **EUR 20,000** | **EUR 65,000** | Platform licence + maintenance only |

---

## 2. Platform Cost Assumptions

Document Intelligence platforms typically price on one of three models:

| Pricing model | Typical range | Best for |
|---|---|---|
| Per document processed | EUR 0.05–0.50 per document | Low-medium volume; predictable cost scaling |
| Monthly SaaS subscription | EUR 1,500–5,000/month | Medium-high volume; fixed cost preferred |
| Enterprise licence (annual) | EUR 20,000–60,000/year | High volume; multi-corridor deployment |

**Müller's estimated document volume (pilot corridor):**
- Invoices: estimated 200–800/month (to be confirmed in Phase 1)
- Customs declarations: estimated 100–400/month
- Bills of lading and PODs: estimated 100–300/month
- **Total pilot corridor estimate: 400–1,500 documents/month**

At EUR 0.10–0.20 per document, monthly platform cost ranges from EUR 40–300/month at low volume to EUR 150–300/month at high volume — well within SaaS subscription alternatives at this volume level. A monthly SaaS model (EUR 1,500–2,500/month) likely offers better value once volume is confirmed.

---

## 3. Implementation Cost Assumptions

| Component | Low | High | Driver |
|---|---|---|---|
| TMS API integration | EUR 5,000 | EUR 20,000 | Direct API = low; custom build = high |
| Field mapping configuration | EUR 3,000 | EUR 8,000 | Number of document types and corridors |
| Confidence scoring interface setup | EUR 2,000 | EUR 5,000 | Vendor-provided vs custom UI |
| Testing and QA | EUR 3,000 | EUR 7,000 | Complexity of document sample |
| Go-live support | EUR 2,000 | EUR 5,000 | Vendor on-site or remote |

**Primary cost driver:** TMS integration. If the existing TMS supports a direct REST API, integration cost is at the low end. If integration requires a custom middleware build, cost moves to the high end. Confirming this in Phase 1 is the single most important cost validation step.

---

## 4. Internal Staff Time Estimates

| Role | Phase 1–3 (days) | Phase 4 pilot (days) | Rate assumption | Total cost estimate |
|---|---|---|---|---|
| IT / Systems lead | 8 | 5 | EUR 400/day | EUR 5,200 |
| Head of Customs / Operations | 5 | 8 | EUR 350/day | EUR 4,550 |
| Legal / Compliance | 4 | 2 | EUR 500/day | EUR 3,000 |
| Finance / AP lead | 3 | 4 | EUR 350/day | EUR 2,450 |
| Customs declarants (training + parallel run) | — | 6 per declarant × 3 | EUR 250/day | EUR 4,500 |
| AI Engineer | 10 | 15 | EUR 600/day | EUR 15,000 |
| Data Engineer | 8 | 10 | EUR 550/day | EUR 9,900 |
| **Total internal time cost** | | | | **EUR 44,600** |

---

## 5. ROI Model — Conservative Estimate

### Assumptions
- Monthly document volume (pilot corridor): 600 documents/month
- Current cost per invoice/declaration: EUR 15 (midpoint of EUR 12–20 range)
- AI cost per document: EUR 3 (midpoint of EUR 2–3 range)
- Error rate reduction: from 11.5% to 5% (conservative — not full benchmark)
- Cost per error (customs hold + rework): EUR 500 average (conservative)
- Payback calculation based on Year 1 total cost: EUR 120,000 (midpoint)

### Monthly savings calculation

| Saving source | Monthly saving |
|---|---|
| Processing cost reduction (600 docs × EUR 12 saving) | EUR 7,200 |
| Error reduction saving (600 × 6.5% fewer errors × EUR 500) | EUR 1,950 |
| **Total monthly saving** | **EUR 9,150** |

### Payback timeline

| Total Year 1 cost | Monthly saving | Payback period |
|---|---|---|
| EUR 82,000 (low) | EUR 9,150 | ~9 months |
| EUR 145,000 (midpoint) | EUR 9,150 | ~16 months |
| EUR 226,000 (high) | EUR 9,150 | ~25 months |

**Note:** These are conservative pilot-corridor estimates. Full network rollout multiplies the monthly saving by the number of corridors (8 countries) while implementation costs do not scale linearly — platform cost increases modestly, but integration and training costs are largely fixed after Phase 4.

### Year 1 ROI at midpoint scenario
- Total cost: EUR 145,000
- Total annual saving: EUR 9,150 × 12 = EUR 109,800
- Net Year 1 position: −EUR 35,200
- Year 2 annual saving: EUR 109,800 (platform cost only ~EUR 35,000)
- **Year 2 net return: ~EUR 75,000**
- **3-year cumulative return: ~EUR 115,000 net of all costs**

---

## 6. Budget Recommendation

Present three scenarios to Olaf:

| Scenario | Total Year 1 | Description |
|---|---|---|
| Conservative | EUR 82,000–100,000 | Direct API integration; single vendor SaaS; internal team handles most configuration |
| Base case | EUR 130,000–160,000 | Medium integration complexity; vendor-supported implementation; full legal review |
| High complexity | EUR 180,000–226,000 | Custom TMS integration; scanning infrastructure required; multi-vendor assessment |

**Recommendation:** Budget for the base case (EUR 130,000–160,000) with the conservative scenario as the floor and high complexity as the ceiling. Present to Olaf as a range with the integration assessment in Phase 1 as the key narrowing event.
