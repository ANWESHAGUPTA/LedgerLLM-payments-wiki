---
title: Stripe insufficient_funds
category: code
network: stripe
related: [[stripe-decline-codes]], [[payment-retry-strategy]]
sources: ["raw/codes.md"]
last_compiled: 2026-04-12
confidence: high
---

# Stripe insufficient_funds

## Summary
The card has insufficient funds to complete the purchase.

## Details
This decline occurs when the customer's account doesn't have enough available balance or credit to cover the transaction amount. It's one of the most common decline reasons.

### Common causes:
- Account balance below transaction amount
- Credit limit reached on credit cards
- Pending transactions reducing available balance
- Currency conversion reducing available funds

### Merchant response:
The customer needs to use an alternative payment method. Retrying the same card is unlikely to succeed unless the customer adds funds or pays down their balance.

## Compliance notes
No specific compliance requirements for this decline type.

## Technical reference
**Code**: `insufficient_funds`
**Network**: Stripe
**Action required**: No - customer issue
**Retry recommended**: No, unless customer confirms they've resolved the funding issue

### API handling:
```
"decline_code": "insufficient_funds"
```

## Cross-network comparison
**Visa**: Reason code 51 (Insufficient funds/over credit limit)
**Mastercard**: Reason code 51 (Insufficient funds)
**Stripe**: `insufficient_funds` (more descriptive than numeric codes)

## Related
- [[stripe-decline-codes]]
- [[payment-retry-strategy]]

## Sources
- raw/codes.md