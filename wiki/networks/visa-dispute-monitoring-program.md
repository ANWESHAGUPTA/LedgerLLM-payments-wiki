---
title: Visa Dispute Monitoring Program
category: network
network: visa
related: [[chargeback-thresholds]], [[excessive-chargeback-merchants]], [[visa-dispute-process]], [[chargebacks]]
sources: [visa-chargeback-rules.md]
last_compiled: 2026-04-13
confidence: high
---

# Visa Dispute Monitoring Program (VDMP)

## Summary
VDMP is Visa's compliance program that monitors merchant chargeback rates and imposes penalties on merchants who exceed established thresholds. Merchants face fees, restrictions, and reviews if they exceed the monthly limits.

## Details
The Visa Dispute Monitoring Program tracks merchant chargeback ratios and absolute volumes monthly. Merchants who breach the thresholds enter a tiered program with increasing penalties:

### VDMP Thresholds
- **Early Warning**: 0.65% chargeback ratio AND 75 chargebacks per month
- **Standard**: 0.9% chargeback ratio AND 100 chargebacks per month  
- **Excessive**: 1.8% chargeback ratio AND 1,000 chargebacks per month

### Penalties
Merchants in VDMP face:
- Punitive fees per chargeback
- Operating restrictions
- Costly periodic reviews
- Potential account termination at higher tiers

### Exit Requirements
To exit VDMP, merchants must maintain chargeback rates below the threshold for three consecutive months. If they breach again after two compliant months, they must restart the three-month countdown.

## Compliance notes
Visa has introduced an Issuer Excessive Dispute Fee in the US, charging issuers $5 per dispute above thresholds when their dispute-to-sales ratios exceed 150% of the regional average. Low-value disputes under $2.50 are also subject to fees.

## Technical reference
Both ratio AND absolute volume thresholds must be exceeded for program enrollment. The program operates on calendar month periods with monthly assessments.

## Cross-network comparison
Mastercard has similar monitoring programs but uses different threshold calculations and penalty structures. Not covered in current sources.

## Related
- [[chargeback-thresholds]]
- [[excessive-chargeback-merchants]]
- [[visa-dispute-process]]
- [[chargebacks]]
- [[visa-monitoring-program]]

## Sources
- raw/visa-chargeback-rules.md