---
title: Payment Retry Strategy
category: process
network: all
related: [[stripe-decline-codes]], [[3d-secure]]
sources: ["raw/codes.md"]
last_compiled: 2026-04-12
confidence: medium
---

# Payment Retry Strategy

## Summary
A systematic approach to handling failed payments by determining when and how to retry based on the specific decline reason.

## Details
Not all payment failures should be retried. The retry strategy depends on the decline code:

### Retry recommended:
- `processing_error`: Temporary processing issues
- `issuer_not_available`: Issuer connectivity problems
- `reenter_transaction`: Unknown processing issues
- `approve_with_id`: Authorization issues that may resolve

### Retry after customer action:
- `authentication_required`: After completing [[3d-secure]] flow
- `incorrect_cvc`, `incorrect_address`: After customer corrects information
- `expired_card`: After customer provides new card details

### Do not retry:
- `insufficient_funds`: Unless customer confirms they've added funds
- `fraudulent`, `stolen_card`, `lost_card`: Security blocks
- `card_not_supported`: Card type incompatibility
- `testmode_decline`: Test card used in production

### Retry timing:
- **Immediate**: For processing errors and issuer availability issues
- **Delayed**: Wait increasing intervals (1 hour, 4 hours, 24 hours)
- **Customer-triggered**: Only retry after customer takes corrective action

## Compliance notes
Excessive retry attempts may trigger fraud detection systems. Most payment processors limit retry attempts to prevent abuse.

## Technical reference
Based on Stripe decline codes, but principles apply across payment providers.

### Implementation considerations:
- Track retry attempts per payment
- Implement exponential backoff
- Monitor retry success rates
- Respect payment processor limits

## Cross-network comparison
Not covered in current sources.

## Related
- [[stripe-decline-codes]]
- [[3d-secure]]

## Sources
- raw/codes.md