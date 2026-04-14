---
title: Stripe card input errors
category: concept
network: stripe
related: [[stripe-decline-codes]], [[payment-retry-strategy]]
sources: [raw/codes.md]
last_compiled: 2026-04-15
confidence: high
---

# Stripe card input errors

## Summary
Stripe provides specific decline codes for various card input errors, helping merchants identify and guide customers to correct payment information mistakes.

## Details
Stripe differentiates between multiple types of card input errors, each with its own decline code. This granular approach helps merchants provide specific guidance to customers for quick resolution.

### Card number errors:
- `incorrect_number` / `invalid_number`: Wrong card number entered
- Customer action: Re-enter correct card number

### Expiry date errors:
- `invalid_expiry_month`: Invalid expiry month
- `invalid_expiry_year`: Invalid expiry year
- `expired_card`: Card has expired
- Customer action: Use correct expiry date or different card

### Security code errors:
- `incorrect_cvc` / `invalid_cvc`: Wrong CVC/CVV entered
- Customer action: Re-enter correct security code

### Address verification errors:
- `incorrect_address`: Billing address mismatch
- `incorrect_zip`: Postal code mismatch
- Customer action: Use correct billing information

### PIN errors (card-present):
- `incorrect_pin` / `invalid_pin`: Wrong PIN entered
- `pin_try_exceeded`: Too many PIN attempts
- Customer action: Use correct PIN or different payment method

## Compliance notes
Address verification failures may be required for certain merchant categories or transaction types depending on card network rules.

## Technical reference
- **Retry approach**: Customer can immediately retry with corrected information
- **Validation timing**: Real-time during payment form completion
- **Error handling**: Specific field-level error messages recommended

## Cross-network comparison
Not covered in current sources.

## Related
- [[stripe-decline-codes]] — Complete list of Stripe decline codes
- [[payment-retry-strategy]] — When and how to retry failed payments

## Sources
- raw/codes.md