---
title: Stripe authentication_required
category: code
network: stripe
related: [[3d-secure]], [[strong-customer-authentication]], [[stripe-decline-codes]]
sources: [raw/codes.md]
last_compiled: 2026-04-15
confidence: high
---

# Stripe authentication_required

## Summary
Stripe's `authentication_required` decline code indicates the card was declined because the transaction requires additional security verification, typically 3D Secure authentication.

## Details
This is a soft decline that occurs when the card issuer requires strong customer authentication (SCA) to authorize the payment. When using Stripe's front-end components, this typically triggers an automatic authentication flow, allowing the customer to complete the verification and retry the payment.

### When it occurs:
- Card issuer requires 3D Secure verification
- Strong Customer Authentication (SCA) is mandated
- Payment appears to be higher risk to the issuer

### Merchant response:
- For on-session payments: Stripe's front-end automatically handles the authentication flow
- For off-session payments: Request the customer to retry with authentication
- If decline occurs despite successful authentication: Customer must contact their card issuer

## Technical reference
- **Stripe code**: `authentication_required`
- **Related code**: `authentication_not_handled` (when authentication is skipped)
- **Retry recommendation**: Yes, after authentication
- **API attribute**: May include `advice_code` with suggested next steps

## Cross-network comparison
Not covered in current sources.

## Related
- [[3d-secure]] — The authentication protocol required
- [[strong-customer-authentication]] — EU regulation driving authentication requirements
- [[stripe-decline-codes]] — Complete list of Stripe decline codes

## Sources
- raw/codes.md