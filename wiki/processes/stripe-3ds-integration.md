---
title: Stripe 3DS Integration
category: process
network: stripe
related: [[3d-secure]], [[strong-customer-authentication]], [[stripe-authentication-required]]
sources: ["3d-secure.md"]
last_compiled: 2026-04-16
confidence: medium
---

# Stripe 3DS Integration

## Summary
Stripe provides multiple approaches for integrating 3D Secure authentication into payment flows, from standard checkout integration to specialized configurations for regulatory compliance and fraud reduction.

## Details
Stripe offers several 3DS integration options:

1. **Standard Integration**: Integrate [[3d-secure]] directly into your checkout flow
2. **SCA Compliance**: Use SCA exemptions and Data Only to reduce cardholder friction on eligible transactions
3. **Hybrid Processing**: Run 3DS on Stripe while processing the subsequent payment on a third-party gateway
4. **External 3DS**: Process payments when 3DS authentication runs outside Stripe
5. **Performance Monitoring**: Track how 3DS affects payment success rates through the Stripe Dashboard

## Compliance notes
Stripe's 3DS implementation supports [[strong-customer-authentication]] requirements under [[psd2]] and similar regulations. SCA exemptions can be applied to eligible transactions to reduce friction while maintaining compliance.

## Technical reference
When 3DS authentication fails or is required but not provided, Stripe returns decline codes such as [[stripe-authentication-required]].

Dashboard analytics show the impact of 3DS on payment success rates, helping merchants optimize their authentication strategy.

## Cross-network comparison
Not covered in current sources: how Stripe's 3DS implementation differs from other payment processors or direct network integrations.

## Related
- [[3d-secure]]
- [[strong-customer-authentication]]
- [[stripe-authentication-required]]

## Sources
- raw/3d-secure.md