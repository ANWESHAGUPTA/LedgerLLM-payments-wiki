---
title: Disputes
category: concept
network: all
related: [[[chargebacks]], [[dispute-reason-codes]], [[chargeback-representment]], [[dispute-evidence-submission]], [[chargeback-thresholds]], [[stripe-dispute-handling]]]
sources: [disputes.md]
last_compiled: 2026-04-15
confidence: high
---

# Disputes

## Summary
Disputes (also known as chargebacks) occur when cardholders question payments with their card issuers. The issuer creates a formal dispute on the card network, immediately reversing the payment and charging dispute fees.

## Details
When a dispute occurs, the payment amount plus network dispute fees are pulled from the payment processor and debited from the merchant's account balance. The dispute creates an immediate reversal before the merchant has opportunity to respond.

Merchants can challenge disputes by submitting evidence through their payment processor's dispute management system. The quality of evidence and speed of response significantly impact dispute outcomes.

Key dispute management activities include:
- Analyzing dispute reason codes to understand the cardholder's claim
- Collecting appropriate evidence based on the dispute category
- Submitting compelling evidence within network deadlines
- Monitoring dispute rates to avoid threshold breaches

## Compliance notes
Excessive disputes can trigger enrollment in card network monitoring programs. Each network has specific thresholds and penalties:
- Dispute rates above network thresholds trigger monitoring program enrollment
- Monitoring programs impose additional fees and operational requirements
- Failure to reduce dispute rates can lead to payment processing restrictions

Merchants must respond to disputes within network-specific timeframes to avoid automatic liability.

## Technical reference
Dispute processing involves multiple system interactions:
- Card networks create formal dispute cases with unique identifiers
- Payment processors receive dispute notifications via network APIs
- Evidence submission systems accept text and image uploads
- Automated dispute prevention systems can intercept disputes before formal creation

## Cross-network comparison
All major card networks (Visa, Mastercard, American Express) support dispute processing, but with different:
- Reason code structures and numbering systems
- Evidence requirements for specific dispute types
- Timeline requirements for merchant responses
- Monitoring program thresholds and penalties

## Related
- [[chargebacks]] - Alternative term for disputes
- [[dispute-reason-codes]] - Codes explaining dispute rationale
- [[chargeback-representment]] - Process of challenging disputes
- [[dispute-evidence-submission]] - Evidence collection and submission
- [[chargeback-thresholds]] - Network limits on dispute rates
- [[stripe-dispute-handling]] - Stripe's dispute management system

## Sources
- raw/disputes.md