---
title: Chargeback Thresholds
category: concept
network: all
related: [[mastercard-chargeback-rules]], [[visa-monitoring-program]], [[chargebacks]], [[excessive-chargeback-merchants]]
sources: mastercard-chargeback-rules.md
last_compiled: 2026-04-13
confidence: medium
---

# Chargeback Thresholds

## Summary
Chargeback thresholds are limits set by card networks to identify merchants with excessive dispute rates. When merchants exceed these thresholds, they enter monitoring programs that impose additional requirements, fees, and potential account termination. Each network has different threshold criteria.

## Details
Card networks use chargeback thresholds to maintain payment ecosystem integrity and protect cardholders. Merchants exceeding thresholds face escalating consequences designed to encourage better fraud prevention and customer service practices.

### Threshold Components
Most networks evaluate merchants on two metrics:
1. **Absolute volume**: Minimum number of chargebacks per month
2. **Chargeback ratio**: Percentage of transactions that result in disputes

Both criteria typically must be met to trigger monitoring program enrollment.

### Monitoring Program Consequences
Merchants exceeding thresholds may face:
- Increased processing fees
- Additional compliance requirements
- Regular reporting obligations
- Account review processes
- Potential account termination
- Enhanced fraud prevention mandates

## Compliance notes

### Monitoring Program Requirements
Merchants in monitoring programs typically must:
- Implement enhanced fraud prevention measures
- Submit detailed monthly reports
- Maintain comprehensive chargeback reduction plans
- Meet specific performance improvement targets
- Pay additional program fees

### Exit Criteria
To exit monitoring programs, merchants usually must:
- Maintain ratios below threshold for consecutive months (typically 3-6 months)
- Demonstrate sustainable fraud prevention improvements
- Meet all program compliance requirements
- Pay any outstanding fees

## Technical reference

### Mastercard Excessive Chargeback Threshold
- **Volume threshold**: 100+ chargebacks per month
- **Ratio threshold**: 1.5% chargeback-to-transaction ratio
- **Both criteria must be met** to trigger ECM program enrollment

### Calculation Method
Chargeback-to-transaction ratio = (Number of chargebacks ÷ Number of transactions) × 100%

### Measurement Periods
Networks typically evaluate thresholds monthly, using rolling averages to smooth out seasonal variations and prevent gaming.

## Cross-network comparison

### Mastercard vs. Visa Thresholds
- **Mastercard ECM**: 100+ chargebacks AND 1.5% ratio
- **Visa VAMP**: Lower thresholds around 0.9% ratio (from existing wiki knowledge)
- **Volume requirements**: Both networks require minimum absolute volumes
- **Monitoring approach**: Similar escalating consequence structures

### Network Variations
Not covered in current sources: American Express, Discover, and regional network thresholds may differ significantly from Visa/Mastercard standards.

## Related
- [[mastercard-chargeback-rules]]
- [[visa-monitoring-program]]
- [[chargebacks]]
- [[excessive-chargeback-merchants]]

## Sources
- mastercard-chargeback-rules.md