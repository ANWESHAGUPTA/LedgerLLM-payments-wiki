---
title: Chargeback Representment
category: process
network: all
related: [[chargebacks]], [[visa-compelling-evidence-3-0]], [[dispute-evidence-submission]], [[visa-resolve-online]]
sources: [visa-compelling-evidence-3-0.md]
last_compiled: 2026-04-13
confidence: medium
---

# Chargeback Representment

## Summary
Chargeback representment is the process where merchants challenge invalid chargebacks by submitting evidence to prove the original transaction was legitimate. It's the formal dispute response mechanism that can reverse chargebacks and recover lost revenue.

## Details
Representment involves merchants gathering and submitting compelling evidence to prove that a chargeback claim is invalid and the original transaction should stand.

### Key Components
- **Compelling evidence** — documentation proving the transaction was valid
- **Rebuttal letters** — written explanation of why the chargeback is invalid
- **Reason code knowledge** — understanding what evidence is required for each dispute type
- **Proper timing** — meeting network deadlines for submission

### Process Flow
1. Chargeback filed by issuing bank
2. Merchant receives chargeback notification
3. Merchant gathers appropriate evidence based on reason code
4. Evidence package submitted through acquirer/processor
5. Issuer reviews evidence and makes decision
6. Chargeback either reversed or upheld

### Evidence Types
Acceptable evidence varies by reason code and network but commonly includes:
- Transaction receipts and confirmations
- Shipping and delivery records
- Customer communications
- Device and IP address data
- Historical transaction patterns (especially with [[visa-compelling-evidence-3-0]])

## Compliance Notes
Each network has specific deadlines and evidence requirements for representments. Missing deadlines or submitting inadequate evidence typically results in automatic losses. Networks may charge additional fees for invalid representment attempts.

## Technical Reference
- **Visa platform:** [[visa-resolve-online]] (VROL)
- **Submission method:** Through acquiring bank or processor
- **Time limits:** Vary by network and reason code
- **Success tracking:** Important for measuring representment ROI

## Cross-network Comparison
All major networks support representment but with different:
- **Evidence requirements** — what documents are acceptable
- **Submission platforms** — how evidence is delivered
- **Time limits** — deadlines for response
- **Fee structures** — costs for representment attempts

Visa's [[visa-compelling-evidence-3-0]] provides more standardized evidence requirements for certain dispute types.

## Related
- [[chargebacks]]
- [[visa-compelling-evidence-3-0]]
- [[dispute-evidence-submission]]
- [[visa-resolve-online]]
- [[friendly-fraud]]

## Sources
- visa-compelling-evidence-3-0.md