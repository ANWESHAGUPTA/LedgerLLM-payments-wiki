---
title: Stripe local payment method declines
category: concept
network: stripe
related: [[stripe-decline-codes]], [[payment-retry-strategy]]
sources: [raw/codes.md]
last_compiled: 2026-04-15
confidence: high
---

# Stripe local payment method declines

## Summary
Stripe provides specific decline codes for Local Payment Method (LPM) failures, covering various payment providers and account-specific issues beyond traditional card payments.

## Details
Local payment methods (bank transfers, digital wallets, buy-now-pay-later) have different failure modes than card payments. Stripe's LPM decline codes help merchants understand and respond to these provider-specific issues.

### Provider-level issues:
- `partner_generic_decline`: Payment provider declined
- `processing_error` / `partner_processing_error`: Provider system error
- `partner_payment_not_found`: Provider can't locate payment

### Customer account problems:
- `invalid_customer_account`: Customer's account with provider has issues
- `insufficient_funds` / `partner_insufficient_funds`: Insufficient funds with provider
- `payment_limit_exceeded`: Transaction exceeds customer's limits
- `partner_high_risk_customer`: Provider flagged customer as high risk

### Payment method validity:
- `invalid_billing_agreement`: Billing agreement is invalid
- `expired_card` / `partner_expired_card`: Registered card with provider expired
- `invalid_payment_information`: Payment details invalid
- `expired_payment_information`: Payment information expired

### Business and compliance issues:
- `invalid_business_account`: Business account deactivated
- `compliance_violation`: Violates terms, rules, or laws
- `invalid_authorization`: Authorization invalid or revoked
- `payment_disputed`: Dispute over the payment

### Duplicate and currency issues:
- `duplicate_transaction` / `partner_duplicate_transaction`: Recent identical transaction
- `currency_not_supported` / `partner_invalid_currency`: Currency not supported
- `invalid_amount` / `partner_invalid_amount`: Amount not allowed

## Technical reference
- **Retry success likelihood**: Varies significantly by decline reason
- **Customer action required**: Most require customer to resolve with payment provider
- **Provider dependency**: Success depends on third-party payment provider capabilities

## Cross-network comparison
Not covered in current sources.

## Related
- [[stripe-decline-codes]] — Complete list of Stripe decline codes
- [[payment-retry-strategy]] — When and how to retry failed payments

## Sources
- raw/codes.md