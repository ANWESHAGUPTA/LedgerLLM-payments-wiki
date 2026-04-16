---
title: Stripe Dispute Handling
category: process
network: stripe
related: [[disputes]], [[chargeback-representment]], [[smart-disputes]], [[stripe-disputes-dashboard]]
sources: raw/disputes.md
last_compiled: 2026-04-16
confidence: high
---

# Stripe Dispute Handling

## Summary
Stripe provides a guided dispute management system through the Dashboard that walks merchants through challenging or accepting chargebacks with appropriate evidence and counterarguments.

## Details
When a dispute occurs, Stripe immediately debits your balance for both the payment amount and network dispute fees. The Stripe Dashboard then guides you through the response process:

### Response Options
- **Challenge the dispute** by providing evidence and counterarguments
- **Accept the dispute** if you believe it's valid

### Evidence Submission Process
1. Access the dispute in your Stripe Dashboard
2. Review the dispute reason code and category
3. Provide appropriate text and image evidence based on the specific dispute reason
4. Submit your counterargument through the guided interface

### Support Available
Stripe provides dispute support to help merchants craft the best possible response for each case.

## Compliance notes
Dispute responses must be submitted within network-mandated timeframes. Stripe's Dashboard provides deadline information for each case.

## Technical reference
Disputes are managed through the Stripe Dashboard interface. The system automatically handles:
- Balance debiting for payment amount and dispute fees
- Evidence formatting for different reason codes
- Submission to appropriate card networks

## Related
- [[disputes]] - General concept of payment disputes
- [[chargeback-representment]] - Process of challenging invalid chargebacks
- [[smart-disputes]] - Stripe's automated evidence system
- [[stripe-disputes-dashboard]] - Stripe's dispute management interface
- [[dispute-reason-codes]] - Network codes categorizing disputes

## Sources
- raw/disputes.md