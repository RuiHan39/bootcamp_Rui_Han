
# Stakeholder Memo  
**Subject:** Cross-Sell Feasibility – Auto to Medical Insurance  

## Background  
Our book of auto-insurance customers is large, loyal, and demographically aligned with private medical insurance. Yet fewer than one in ten auto policyholders currently hold a medical product, suggesting substantial untapped revenue. Rebalancing our outreach from broad-brush campaigns to precision targeting is now a Board-level priority.

## Problem  
How can we identify which auto-insurance customers are most likely to purchase medical coverage, and through which channel, so that we can reduce acquisition cost and increase lifetime value without eroding trust or triggering regulatory scrutiny?


## Proposed Solution  
- **Descriptive:** Exploratory visuals showing overlap of auto vs medical customer profiles by age, geography, payment behavior, claims history.  
- **Predictive / Prescriptive:** Uplift model estimating incremental probability of medical purchase under a cross-sell treatment, with interpretable driver features.  
- **Activation Layer:** API returning nightly scores + rule-based channel recommendations (email, SMS, agent call).


## Data & Assumptions  
- Historical auto and medical policy records linkable at customer level.  
- Marketing consent flags and opt-in status available.  
- Permitted variables only (no protected health data beyond allowed attributes).  
- Forecast pipeline must complete on existing on-prem cluster (< 45 min nightly).  


## Risks & Mitigations  

| Risk | Impact | Mitigation |
|------|--------|------------|
| Class imbalance (rare conversions) | Model instability | Use uplift modeling + cost-sensitive loss; monitor weekly. |
| Temporal drift (policy changes, seasonality) | Degraded lift | Schedule monthly retrain; monitor PSI. |
| Over-contact causing auto churn | Brand damage | Cap touches per customer via governance rules. |
| Regulatory scrutiny on variable usage | Launch delay | Pre-clear feature list with Legal; maintain interpretable model. |


## Next Steps & Commitments  
- **Product Marketing:** Finalize offer variants and contact rules by 25 Aug.  
- **Compliance:** Complete variable whitelist review by 30 Aug.  
- **Data Science:** Deliver v0 descriptive insights by 1 Sep, v1 uplift API by 15 Sep.
