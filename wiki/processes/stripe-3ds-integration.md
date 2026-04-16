---
title: Stripe 3DS Integration
category: process
network: stripe
related: [[3d-secure]], [[stripe-payment-intents]], [[stripe-setup-intents]], [[strong-customer-authentication]]
sources: ["raw/3d-secure.md"]
last_compiled: 2026-04-16
confidence: medium
---

# Stripe 3DS Integration

## Summary
Stripe provides multiple approaches for integrating [[3d-secure]] authentication into checkout flows, including options for SCA exemptions, Data Only authentication, and third-party gateway processing.

## Details
Stripe offers several 3DS integration methods:

### Primary Integration Options
1. **Integrate 3D Secure into checkout flow** - Full 3DS authentication during payment processing
2. **Use SCA exemptions and Data Only** - Reduce cardholder friction on eligible transactions
3. **Run 3DS on Stripe, process on third-party** - Use Stripe for authentication while processing payments elsewhere
4. **Process when 3DS runs outside Stripe** - Handle payments when authentication occurs on external systems

### Dashboard Analytics
Stripe provides analytics showing how [[3d-secure]] affects payment success rates through the Dashboard, enabling merchants to optimize their authentication strategy.

## Compliance notes
Stripe's 3DS integration helps merchants comply with [[strong-customer-authentication]] requirements under [[psd2]] and similar regulations in multiple jurisdictions.

## Technical reference
Integration typically involves:
- [[stripe-payment-intents]] for handling complex payment flows
- [[stripe-setup-intents]] for saving payment methods with authentication
- Dashboard configuration for exemption rules
- Analytics tracking for success rate optimization

## Related
- [[3d-secure]]
- [[stripe-payment-intents]]
- [[stripe-setup-intents]]
- [[strong-customer-authentication]]

## Sources
- raw/3d-secure.md