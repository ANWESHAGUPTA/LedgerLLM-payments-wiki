---
title: Stripe Decline Codes
category: concept
network: stripe
related: [[3d-secure]], [[payment-retry-strategy]], [[fraud-detection]]
sources: ["raw/codes.md"]
last_compiled: 2026-04-12
confidence: high
---

# Stripe Decline Codes

## Summary
Stripe uses its own decline codes that provide more specific detail than standard issuer decline codes. These codes help merchants understand why a payment failed and what action to take next.

## Details
Stripe decline codes fall into two main categories:
- **Card decline codes**: Used for traditional card payments
- **Local payment method decline codes**: Used for alternative payment methods like bank transfers, digital wallets

Each decline code includes:
- The specific code identifier
- A description of what caused the decline
- Recommended next steps for resolution

Some declines also include an `advice_code` with additional guidance on how to handle the situation.

## Compliance notes
Certain decline codes require careful handling to avoid revealing sensitive information:
- **fraudulent**, **lost_card**, **stolen_card**, **merchant_blacklist**: Should be presented to customers as generic declines to avoid alerting potential fraudsters
- Authentication-required declines must trigger proper [[3d-secure]] flows for PSD2 compliance

## Technical reference
Stripe decline codes are returned in the API error response under the `decline_code` attribute. Key categories include:

### Authentication-related codes:
- `authentication_required`: Requires [[3d-secure]] authentication
- `authentication_not_handled`: Authentication was required but not performed

### Card data issues:
- `incorrect_cvc`, `invalid_cvc`: CVC verification failed
- `incorrect_number`, `invalid_number`: Card number is wrong
- `expired_card`: Card has expired

### Insufficient funds/limits:
- `insufficient_funds`: Not enough money available
- `card_velocity_exceeded`: Transaction limits exceeded
- `withdrawal_count_limit_exceeded`: Too many transactions

### Security/fraud:
- `fraudulent`: Stripe's fraud detection blocked the payment
- `lost_card`, `stolen_card`: Card reported as compromised

### Processing issues:
- `processing_error`: Temporary processing problem
- `issuer_not_available`: Can't reach card issuer

## Cross-network comparison
Stripe's decline codes are more granular than traditional card network codes:
- **Visa/Mastercard**: Use numeric reason codes (e.g., "51" for insufficient funds)
- **Stripe**: Uses descriptive text codes (e.g., "insufficient_funds") that map to underlying issuer codes
- **Advantage**: Stripe codes provide clearer guidance on merchant actions without requiring code lookup tables

## Related
- [[3d-secure]]
- [[payment-retry-strategy]]
- [[fraud-detection]]

## Sources
- raw/codes.md