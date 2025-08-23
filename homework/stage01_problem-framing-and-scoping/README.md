
# Cross-Sell Feasibility: Auto Insurance → Medical Insurance
**Stage:** Problem Framing & Scoping (Stage 01)

## Problem Statement
The company’s existing auto-insurance portfolio contains a large, engaged customer base whose demographic and behavioral traits align closely with prospects for medical coverage. Despite strong overlap, the attach rate of medical policies among auto customers remains low. The problem is to determine whether targeted cross-selling can convert a meaningful share of this base without degrading the core auto experience. Solving this would unlock incremental premium revenue, lower acquisition costs (versus cold leads), and strengthen customer loyalty through a unified protection bundle.


## Stakeholder & User
·Executive Sponsor (Chief Growth Officer): Sets financial targets, allocates budget, and signs off on go / no-go decisions.
·Product Marketing Team: Consumes model outputs to design campaigns, creative assets, and channel mix.
·Data Science & Analytics: Owns the predictive framework, monitors performance, and schedules retraining.
·Legal & Compliance: Reviews feature sets and outreach scripts for regulatory adherence.
·Customer-Facing Teams (call-center, mobile app, web): Receive real-time next-best-offer prompts to use during service interactions.

## Useful Answer & Decision
*Type: Predictive (propensity) and Prescriptive (uplift).
*Metric: Incremental lift in medical-policy conversion rate relative to random targeting.
*Decision: Which auto customers to include in cross-sell campaigns, via which channel, and with what offer.
*Artifacts:
·Nightly customer-level propensity and uplift scores.
·Explainability summary highlighting the top drivers behind each score.
·Campaign playbook with recommended segments, messaging, and contact rules.

## Assumptions & Constraints
·Historical auto and medical policy data exist and are linkable at customer level.
·Marketing consent flags are available and respected.
·Model must be interpretable enough for compliance review.
·Runtime budget: nightly batch must complete within existing on-prem infrastructure.
·No use of protected health data beyond explicitly allowed variables.

## Known Unknowns / Risks
·Class imbalance: Medical conversions are rare; will test resampling and cost-sensitive methods.
·Temporal drift: Consumer attitudes toward medical coverage may shift; will track monthly.
·Channel saturation: Over-contact could hurt auto retention; will cap touches per customer.
·Regulatory changes: New privacy rules could restrict variable usage; will maintain fallback feature sets.

## Lifecycle Mapping
Goal → Stage → Deliverable
-Define opportunity → Problem Framing & Scoping (Stage 01) → This scoping document

## Repo Plan
/data/, /src/, /notebooks/, /docs/ ; cadence for updates
