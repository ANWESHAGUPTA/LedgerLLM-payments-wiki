---
title: Mastercard Chargeback Rules
category: network
network: mastercard
related: [[chargebacks]], [[visa-dispute-process]], [[mastercard-reason-codes]], [[chargeback-thresholds]], [[dispute-evidence-submission]]
sources: mastercard-chargeback-rules.md
last_compiled: 2026-04-13
confidence: high
---

# Mastercard Chargeback Rules

## Summary
Mastercard chargeback rules govern how disputes are processed on the Mastercard network. These rules define when cardholders can dispute transactions, how merchants must respond, and what thresholds trigger monitoring programs. Mastercard operates the second-largest card network globally with 3.1 billion cards in circulation.

## Details
Mastercard chargebacks are forced reversals of transactions initiated when cardholders file disputes with their issuing banks. The process protects cardholders against fraud and merchant errors, but places the burden of proof on merchants.

### Valid Dispute Reasons
Cardholders can dispute Mastercard transactions when they identify charges that:
- They believe are incorrect, invalid, or duplicate
- They believe are fraudulent
- Didn't match the seller's description
- Didn't arrive as promised

### Cardholder Process
1. Cardholder reviews statement and identifies problematic charge
2. Cardholder attempts to resolve directly with merchant
3. If unresolved, cardholder contacts issuing bank to dispute
4. Bank investigates and may issue chargeback with reason code

### Merchant Impact
Mastercard chargebacks create an uneven playing field that favors cardholders and issuers over merchants. Key impacts:
- Free for cardholders to file, expensive for merchants to receive
- Merchants are liable even when not at fault
- Shorter merchant response windows compared to cardholder filing periods
- Funds are immediately withdrawn from merchant accounts

## Compliance notes

### Disclosure Requirements
Merchants must clearly disclose refund and return policies to comply with Mastercard Transaction Processing Rules. Disclosures must be "sufficiently prominent and clear" and appear on:
- Transaction receipts
- Website checkout pages
- Physical store signage
- Point of sale systems

### Recurring Billing Rules
eCommerce merchants accepting subscription payments must:
- Communicate recurring terms separately from other terms
- Provide opportunity for cardholders to specifically accept recurring billing
- Use clear opt-in mechanisms (e.g., checkbox acceptance)

### Chargeback Thresholds
Merchants exceed Mastercard's excessive chargeback threshold when they have:
- More than 100 chargebacks per month AND
- Chargeback-to-transaction ratio of 1.5% or greater

Exceeding thresholds triggers enrollment in Mastercard's Excessive Chargeback Merchant (ECM) program.

### Time Limits
- Standard cardholder dispute window: 120 days from transaction date
- Extended window for specific situations: up to 540 days from transaction date
- Example: Services not provided (reason code 4853) allows 120 days from service failure date, not exceeding 540 days from original transaction

## Technical reference

### Network Statistics
- 110+ million merchants in 210 countries accept Mastercard
- 10.7 million merchants in the United States
- 3.1 billion Mastercard-branded cards in circulation
- Second-largest card network globally (behind Visa)

### Chargeback Process Flow
1. Cardholder disputes transaction with issuing bank
2. Issuer investigates claim and determines validity
3. If valid, issuer contacts acquirer with chargeback reason code
4. Mastercard withdraws funds from merchant account
5. Funds returned to cardholder account
6. Merchant may respond through representment process

## Cross-network comparison

### Similarities with Visa
- Both networks protect cardholders through chargeback mechanisms
- Similar merchant disclosure requirements
- Comparable dispute reason categories (fraud, authorization, cardholder disputes)

### Key Differences
- **Chargeback ratios**: Mastercard threshold is 1.5%, while Visa VAMP threshold is 0.9%
- **Time limits**: Mastercard's extended window can reach 540 days vs Visa's typically shorter periods
- **Reason code structure**: Mastercard uses 4-digit codes (4837, 4853) vs Visa's decimal format (10.4, 13.1)
- **Monitoring programs**: Mastercard ECM vs Visa's VAMP program

### Advantages for Merchants
- Relatively low processing fees compared to other networks
- Built-in fraud prevention tools
- Valuable analytics and reporting
- Generous representment time limits
- Multi-factor authentication options

## Related
- [[chargebacks]]
- [[visa-dispute-process]]
- [[mastercard-reason-codes]]
- [[chargeback-thresholds]]
- [[dispute-evidence-submission]]

## Sources
- mastercard-chargeback-rules.md