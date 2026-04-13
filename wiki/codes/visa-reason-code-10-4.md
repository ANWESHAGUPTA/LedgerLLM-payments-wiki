---
title: Visa Reason Code 10.4
category: code
network: visa
related: [[visa-compelling-evidence-3-0]], [[friendly-fraud]], [[visa-reason-codes]], [[chargebacks]]
sources: [visa-compelling-evidence-3-0.md]
last_compiled: 2026-04-13
confidence: high
---

# Visa Reason Code 10.4

## Summary
Visa reason code 10.4 (Other Fraud — Card-Absent Environment) is used for fraud disputes in card-not-present transactions. This code is commonly associated with friendly fraud due to its generic, open-ended nature that allows cardholders to dispute legitimate transactions.

## Details
Reason code 10.4 covers fraud claims where:
- Transaction occurred in a card-absent environment (online, phone, mail order)
- Cardholder claims they did not authorize the transaction
- No other specific fraud reason code applies

### Common Scenarios
- [[Friendly-fraud]] — legitimate transactions disputed by cardholders
- Genuine unauthorized use in CNP environments
- Family fraud (family member used card without permission)
- Account takeover fraud

### Why It's Problematic for Merchants
The broad, catch-all nature of 10.4 makes it easy for cardholders to file disputes on legitimate transactions. Unlike more specific reason codes, 10.4 doesn't require detailed justification, making it a common choice for fraudulent dispute claims.

## Compliance Notes
Disputes under reason code 10.4 must be filed within Visa's standard dispute timeline. As of 2026, merchants can use [[visa-compelling-evidence-3-0]] rules specifically for 10.4 disputes to strengthen their defense against invalid claims.

## Technical Reference
- **Code:** 10.4
- **Category:** Fraud
- **Environment:** Card-Absent (CNP)
- **Description:** Other Fraud — Card-Absent Environment
- **Applicable CE rules:** [[visa-compelling-evidence-3-0]]

## Cross-network Comparison
Other networks have similar catch-all fraud codes:
- **Mastercard:** Various 4837-series codes for unauthorized CNP transactions
- **American Express:** Different fraud code structure
- **Discover:** Similar CNP fraud classifications

Visa's 10.4 is notable for being specifically targeted by the [[visa-compelling-evidence-3-0]] framework.

## Related
- [[visa-compelling-evidence-3-0]]
- [[friendly-fraud]]
- [[visa-reason-codes]]
- [[chargebacks]]
- [[visa-dispute-process]]

## Sources
- visa-compelling-evidence-3-0.md