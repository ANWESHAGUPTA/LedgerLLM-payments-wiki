---
title: Stripe issuer decline codes
category: concept
network: stripe
related: [[stripe-decline-codes]], [[payment-retry-strategy]]
sources: [raw/codes.md]
last_compiled: 2026-04-15
confidence: high
---

# Stripe issuer decline codes

## Summary
Stripe provides specific decline codes for various issuer-generated declines, offering more detail than generic issuer responses while maintaining consistent merchant guidance.

## Details
When card issuers decline transactions, they often provide limited information. Stripe's decline codes expand on issuer responses to give merchants clearer guidance on next steps.

### Unknown reason declines:
Multiple codes indicate issuer declined for unspecified reasons:
- `call_issuer`: Customer needs to contact card issuer
- `do_not_honor`: Generic issuer decline
- `no_action_taken`: Issuer took no action on authorization
- `transaction_not_allowed`: Issuer blocked transaction type
- Standard response: "Contact your card issuer for more information"

### Account and card status issues:
- `invalid_account`: Card or linked account is invalid
- `card_not_supported`: Card doesn't support this purchase type
- `currency_not_supported`: Card doesn't support transaction currency
- `card_velocity_exceeded`: Card limits exceeded
- `withdrawal_count_limit_exceeded`: Transaction count limits exceeded

### Payment restrictions:
- `not_permitted`: Payment type not allowed
- `restricted_card`: Card usage restricted
- `service_not_allowed`: Service category blocked
- `invalid_amount`: Amount exceeds card limits

### Lost/stolen cards:
- `lost_card`: Card reported lost
- `stolen_card`: Card reported stolen
- `pickup_card`: Card should be retained
- **Important**: Present these as `generic_decline` to customer

### Processing issues:
- `issuer_not_available`: Issuer system unavailable
- `processing_error`: Processing system error
- `reenter_transaction`: Retry may succeed
- Action: Retry after delay

## Technical reference
- **Retry logic**: Varies by decline code
- **Customer messaging**: Most require "contact issuer" guidance
- **Security codes**: `lost_card`, `stolen_card` should be masked as generic declines

## Cross-network comparison
Not covered in current sources.

## Related
- [[stripe-decline-codes]] — Complete list of Stripe decline codes
- [[payment-retry-strategy]] — When and how to retry failed payments

## Sources
- raw/codes.md