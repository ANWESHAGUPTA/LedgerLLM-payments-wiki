---
title: Order Insight
category: network
network: visa
related: [[visa-compelling-evidence-3-0]], [[visa-dispute-process]], [[chargeback-representment]], [[friendly-fraud]]
sources: [visa-compelling-evidence-3-0.md]
last_compiled: 2026-04-13
confidence: medium
---

# Order Insight

## Summary
Order Insight (OI) is Visa's platform that allows merchants to share transaction details with issuing banks before disputes are filed. It enables pre-dispute resolution and is the primary way to leverage [[visa-compelling-evidence-3-0]] for dispute prevention rather than just representment.

## Details
Order Insight facilitates real-time information sharing between merchants and issuers during the pre-dispute inquiry process. When integrated with [[visa-compelling-evidence-3-0]], it can automatically block invalid fraud claims before they become chargebacks.

### CE 3.0 Integration Process
1. Customer disputes a transaction with their bank
2. Bank attempts to initiate chargeback with reason code 10.4
3. Visa pre-selects up to 5 previous purchases from the same account
4. Qualified historical transactions sent to merchant as Order Insight inquiries
5. Merchant returns required data elements for 2+ transactions
6. Order Insight validates data and passes to Visa for liability assignment
7. If criteria met, dispute is blocked and liability remains with issuer

### Benefits
- **Dispute prevention** rather than post-dispute representment
- **No chargeback fees** when disputes are blocked
- **No impact** on chargeback or fraud ratios
- **Real-time resolution** without lengthy dispute process

### Requirements
Merchants must:
- Enroll in Order Insight platform
- Maintain organized historical transaction data
- Respond promptly to OI inquiries
- Have qualifying historical transactions (120-365 days old)

## Compliance Notes
Order Insight is Visa's recommended platform for sharing evidence in dispute responses. Enrollment is required to access CE 3.0's dispute prevention capabilities, though CE 3.0 can still be used in standard representments without OI enrollment.

## Technical Reference
- **Platform:** Visa Order Insight
- **Integration:** Required for CE 3.0 dispute prevention
- **Response time:** Real-time validation
- **Data elements:** Same as CE 3.0 requirements

## Cross-network Comparison
Order Insight is Visa-specific. Other networks have different pre-dispute platforms:
- **Mastercard:** Similar inquiry systems but different evidence requirements
- **Other networks:** May have proprietary dispute prevention tools

## Related
- [[visa-compelling-evidence-3-0]]
- [[visa-dispute-process]]
- [[chargeback-representment]]
- [[friendly-fraud]]

## Sources
- visa-compelling-evidence-3-0.md