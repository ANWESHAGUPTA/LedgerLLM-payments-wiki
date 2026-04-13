---
title: Mastercard Reason Codes
category: network
network: mastercard
related: [[mastercard-chargeback-rules]], [[visa-reason-codes]], [[chargeback-reason-codes]]
sources: mastercard-chargeback-rules.md
last_compiled: 2026-04-13
confidence: high
---

# Mastercard Reason Codes

## Summary
Mastercard reason codes are 4-digit identifiers that explain why a chargeback was initiated. They help merchants understand the dispute basis and determine appropriate response strategies. Codes are organized into categories: Authorization, Point of Interaction, Fraud, Cardholder Disputes, and Installment Billing.

## Details
When issuers file chargebacks, they attach reason codes to provide merchants with context about the dispute. Understanding these codes is crucial for effective chargeback management and representment strategies.

### Code Categories

#### Authorization Errors
- **4808**: Multiple authorization-related issues including warning bulletin file, expired protection periods, and missing authorizations
- **4834**: Late presentment and point-of-interaction errors

#### Point of Interaction Errors
- **4834**: Transaction amount differences, currency conversion issues, duplications, ATM disputes, and loss/theft/damages

#### No Cardholder Authorization (Fraud)
- **4837**: No cardholder authorization - classic fraud scenario
- **4849**: Questionable merchant activity
- **4870**: Questionable merchant activity (additional scenarios)
- **4871**: Chip/PIN liability shift for lost/stolen/never received fraud

#### Cardholder Disputes
- **4853**: Broad category covering recurring transaction disputes, goods/services not provided, no-show charges, credit processing issues, defective goods, digital goods disputes, counterfeit items, and incomplete transactions

#### Installment Billing Disputes
- **4850**: Installment billing dispute

#### Miscellaneous
- **4854**: Cardholder disputes not classified elsewhere (US region)

## Compliance notes

### Response Requirements
Each reason code may have specific evidence requirements and response deadlines. Merchants must:
- Understand the specific dispute reason
- Gather appropriate supporting documentation
- Respond within Mastercard's prescribed timeframes
- Follow proper representment procedures

### Evidence Standards
Different reason codes require different types of evidence:
- Authorization codes require proof of valid authorization
- Fraud codes need evidence of legitimate cardholder participation
- Service disputes require proof of delivery or completion
- Product disputes need evidence of quality and description accuracy

## Technical reference

### Code Structure
Mastercard uses 4-digit reason codes (e.g., 4837, 4853, 4834) compared to Visa's decimal format (e.g., 10.4, 13.1).

### Most Common Codes
- **4853**: Cardholder disputes (various subcategories)
- **4837**: No cardholder authorization (fraud)
- **4834**: Point of interaction errors
- **4808**: Authorization-related issues

### Code Evolution
Reason codes are periodically updated by Mastercard to address new fraud patterns and payment methods. Merchants should stay current with the latest code definitions and requirements.

## Cross-network comparison

### vs. Visa Reason Codes
- **Format**: Mastercard uses 4-digit codes vs Visa's decimal format
- **Categories**: Similar dispute categories but different organizational structure
- **Specificity**: Mastercard's 4853 is broader than Visa's more granular approach
- **Updates**: Both networks regularly update codes, but on different schedules

### Common Equivalents
- Mastercard 4837 (No Cardholder Authorization) ≈ Visa 10.4 (Fraud)
- Mastercard 4853 (Goods/Services Not Provided) ≈ Visa 13.1 (Services Not Provided)
- Mastercard 4834 (Point of Interaction Error) ≈ Visa 12.6.1 (Duplicate Processing)

## Related
- [[mastercard-chargeback-rules]]
- [[visa-reason-codes]]
- [[chargeback-reason-codes]]
- [[dispute-evidence-submission]]

## Sources
- mastercard-chargeback-rules.md