---
title: Hard Decline Codes
category: concept
network: stripe
related: [[smart-retries]], [[stripe-decline-codes]], [[payment-retry-strategy]]
sources: [smart-retries.md]
last_compiled: 2026-04-12
confidence: high
---

# Hard Decline Codes

## Summary
Decline codes that indicate permanent payment failures that cannot be automatically retried without obtaining a new payment method from the customer. These represent fundamental issues like stolen cards or invalid card numbers.

## Details
When a payment fails with a hard decline code, Stripe's retry system will continue to schedule retries, but they will only execute after detecting a new payment method. The `attempt_count` continues to increment, but unexecuted retries don't create new Charge objects.

### Stripe Hard Decline Codes
- `incorrect_number` - Invalid card number
- `lost_card` - Card reported as lost
- `pickup_card` - Card should be picked up by merchant
- `stolen_card` - Card reported as stolen
- `revocation_of_authorization` - Authorization revoked
- `revocation_of_all_authorizations` - All authorizations revoked
- `authentication_required` - Requires 3D Secure authentication
- `highest_risk_level` - Flagged as highest fraud risk
- `transaction_not_allowed` - Transaction type not permitted

## Compliance notes
Merchants should never attempt to retry payments with hard decline codes using the same payment method, as this violates card network rules and may result in penalties or account restrictions.

## Technical reference
Hard decline codes prevent automatic retry execution but scheduled retries remain active until a new payment method is provided or the retry period expires.

## Cross-network comparison
Not covered in current sources - Visa and Mastercard hard decline equivalents need dedicated coverage.

## Related
- [[smart-retries]]
- [[stripe-decline-codes]]
- [[payment-retry-strategy]]
- [[stripe-authentication-required]]

## Sources
- smart-retries.md