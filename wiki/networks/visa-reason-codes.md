---
title: Visa Reason Codes
category: network
network: visa
related: [[chargeback-reason-codes]], [[mastercard-reason-codes]], [[visa-dispute-process]], [[chargebacks]]
sources: [visa-chargeback-rules.md]
last_compiled: 2026-04-13
confidence: high
---

# Visa Reason Codes

## Summary
Visa reason codes are 2-3 digit identifiers that explain why a chargeback was filed. Each code falls into one of four categories: fraud, authorization errors, processing errors, or consumer disputes.

## Details
Visa uses more than two dozen different reason codes to categorize disputes. Every chargeback must be assigned a specific reason code that explains the cardholder's claim. The reason code determines what evidence merchants can submit to contest the dispute and what timeframes apply.

### Fraud Codes
- **10.1** - EMV Liability Shift Counterfeit Fraud
- **10.2** - EMV Liability Shift Non-Counterfeit Fraud  
- **10.3** - Other Fraud: Card-Present Environment
- **10.4** - Other Fraud: Card-Absent Environment
- **10.5** - Visa Fraud Monitoring Program

### Authorization Codes
- **11.1** - Card Recovery Bulletin
- **11.2** - Declined Authorization
- **11.3** - No Authorization

### Processing Error Codes
- **12.2** - Incorrect Transaction Code
- **12.3** - Incorrect Currency
- **12.4** - Incorrect Account Number
- **12.5** - Incorrect Amount
- **12.6.1** - Duplicate Processing
- **12.6.2** - Paid by Other Means
- **12.7** - Invalid Data

### Consumer Dispute Codes
- **13.1** - Merchandise/Services Not Received
- **13.2** - Canceled Recurring Transaction
- **13.3** - Not as Described or Defective Merchandise
- **13.4** - Counterfeit Merchandise
- **13.5** - Misrepresentation
- **13.6** - Credit Not Processed
- **13.7** - Cancelled Merchandise/Services
- **13.8** - Original Credit Transaction Not Accepted
- **13.9** - Non-Receipt of Cash or Load Transaction Value

## Compliance notes
Each reason code has specific evidence requirements for merchant responses. Merchants have 30 days from when their acquirer receives the dispute notification to submit a response, though banks typically require responses within one week or less.

## Technical reference
Visa no longer officially uses the term "chargeback" and refers to all transaction reversals as "disputes." The reason code system determines the dispute workflow path and acceptable evidence types for representment.

## Cross-network comparison
Visa uses alphanumeric codes (like 10.4, 13.1) while Mastercard uses 4-digit numeric codes (like 4837, 4853). Both networks categorize disputes into similar buckets but use different numbering systems and have varying evidence requirements.

## Related
- [[chargeback-reason-codes]]
- [[mastercard-reason-codes]]
- [[visa-dispute-process]]
- [[chargebacks]]
- [[dispute-evidence-submission]]

## Sources
- raw/visa-chargeback-rules.md