---
title: Stripe insufficient_funds
category: code
network: stripe
related: [[hard-decline-codes]], [[stripe-decline-codes]], [[payment-retry-strategy]]
sources: [raw/codes.md]
last_compiled: 2026-04-15
confidence: high
---

# Stripe insufficient_funds

## Summary
Stripe's `insufficient_funds` decline code indicates the customer's card has insufficient funds to complete the purchase.

## Details
This is a hard decline meaning the payment cannot be retried with the same payment method until the customer's account situation changes. The customer needs to use an alternative payment method to complete the transaction.

### Common causes:
- Insufficient account balance (debit cards)
- Credit limit exceeded (credit cards)
- Account restrictions or holds

### Merchant response:
- Do not retry with the same payment method
- Offer alternative payment methods
- Consider payment installment options if available
- Clear messaging to customer about account status

## Technical reference
- **Stripe code**: `insufficient_funds`
- **Retry recommendation**: No (hard decline)
- **Alternative payment required**: Yes
- **Customer action required**: Use different payment method or resolve account issue

## Cross-network comparison
Not covered in current sources.

## Related
- [[hard-decline-codes]] — Category of permanent declines requiring new payment methods
- [[stripe-decline-codes]] — Complete list of Stripe decline codes
- [[payment-retry-strategy]] — When and how to retry failed payments

## Sources
- raw/codes.md