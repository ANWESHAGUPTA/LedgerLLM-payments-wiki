---
title: Visa Compelling Evidence 3.0
category: network
network: visa
related: [[visa-reason-code-10-4]], [[friendly-fraud]], [[visa-dispute-process]], [[order-insight]], [[visa-resolve-online]], [[chargeback-representment]]
sources: [visa-compelling-evidence-3-0.md]
last_compiled: 2026-04-13
confidence: high
---

# Visa Compelling Evidence 3.0

## Summary
Visa's Compelling Evidence 3.0 (CE 3.0) is a set of evidence requirements that makes it easier for merchants to fight fraudulent chargebacks filed under reason code 10.4. Instead of requiring all four data points to match from one previous transaction, merchants can now use two or more previous undisputed transactions with at least two matching data elements.

## Details
CE 3.0 specifically applies to disputes filed under [[visa-reason-code-10-4]] (Other Fraud — Card-Absent Environment), which is commonly associated with [[friendly-fraud]] due to its generic nature.

### Key Requirements
To qualify for CE 3.0 protection, merchants must provide:
- **2 or more** previous undisputed transactions from the same cardholder
- Transactions must be between **120-365 days old** (not newer than 120 days, not older than 365 days)
- At least **2 matching data elements** between the disputed transaction and each historical transaction
- **No fraud reports** on the historical transactions used as evidence

### Acceptable Data Elements
- Customer account/login ID
- IP address (required if using device ID)
- Physical/shipping address  
- Device ID/device fingerprint (required if not using IP address)
- Email address
- Telephone number

### Comparison with Previous Rules
| Criteria | Legacy Rules | CE 3.0 Rules |
|----------|-------------|---------------|
| Prior purchases required | 1 | 2 or more |
| Data matching requirement | All 4 elements (IP, email, address, phone) | At least 2 elements |
| Time restrictions | None | 120-365 days before dispute |
| Submission timing | Dispute response only | Pre-dispute or dispute response |

### Integration with Order Insight
When used through [[order-insight]], CE 3.0 can **prevent** chargebacks rather than just help win representments:

**Pre-dispute benefits:**
- Dispute blocked before filing
- No chargeback fees
- No impact on chargeback ratios
- No impact on fraud ratios

**Post-dispute benefits:**
- Higher representment success rates
- Streamlined evidence submission
- Cannot escalate to arbitration if successful

## Compliance Notes
Effective as of April 2023 under Visa's Core Rules. CE 3.0 only applies to Visa reason code 10.4 disputes. Merchants must maintain secure storage of qualifying transaction data to leverage these rules effectively.

## Technical Reference
- **Applicable reason code:** 10.4 (Other Fraud — Card-Absent Environment)
- **Submission platform:** [[visa-resolve-online]] (VROL)
- **Integration platform:** [[order-insight]]
- **Evidence validation:** Automated by Visa systems
- **Time window:** 120-365 days for historical transactions

## Cross-network Comparison
CE 3.0 is currently Visa-specific. Mastercard has different evidence requirements for similar fraud disputes under their reason code system. No equivalent streamlined evidence framework exists for other networks as of 2026.

## Related
- [[visa-reason-code-10-4]]
- [[friendly-fraud]]
- [[order-insight]]
- [[visa-resolve-online]]
- [[chargeback-representment]]
- [[visa-dispute-process]]

## Sources
- visa-compelling-evidence-3-0.md