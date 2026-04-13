---
title: Stripe authentication_required
category: code
network: stripe
related: [[3d-secure]], [[stripe-decline-codes]]
sources: ["raw/codes.md"]
last_compiled: 2026-04-12
confidence: high
---

# Stripe authentication_required

## Summary
The card was declined because the transaction requires authentication such as [[3d-secure]].

## Details
This decline occurs when the card issuer requires additional authentication before approving the payment. Most commonly triggered by Strong Customer Authentication (SCA) requirements under PSD2 regulations.

### When it happens:
- First-time payments from new customers
- High-value transactions
- Payments from different devices/locations
- Off-session payments without prior authentication

### Merchant response:
When using Stripe's front-ends, this usually triggers an automatic authentication flow. For off-session payments, you may need to request the customer to retry with authentication.

## Compliance notes
This decline is directly related to [[strong-customer-authentication]] requirements under [[psd2]]. Merchants must handle this properly to remain compliant with European regulations.

## Technical reference
**Code**: `authentication_required`
**Network**: Stripe
**Action required**: Yes - must initiate authentication flow
**Retry recommended**: Yes, after authentication

### API handling:
```
"decline_code": "authentication_required"
```

If the card issuer returns this code despite successful authentication, the customer needs to contact their issuer.

## Related
- [[3d-secure]]
- [[stripe-decline-codes]]
- [[strong-customer-authentication]]

## Sources
- raw/codes.md