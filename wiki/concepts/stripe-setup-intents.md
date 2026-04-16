---
title: Stripe Setup Intents
category: concept
network: stripe
related: [[stripe-payment-intents]], [[stripe-payment-methods]], [[strong-customer-authentication]], [[off-session-payments]]
sources: [raw/payment-intents.md]
last_compiled: 2026-04-16
confidence: medium
---

# Stripe Setup Intents

## Summary
Setup Intents is Stripe's API for saving payment methods for future use, working alongside Payment Intents and Payment Methods to handle dynamic authentication requirements.

## Details
Setup Intents enables merchants to securely save customer payment methods for future transactions while handling authentication requirements like 3D Secure. It works as part of Stripe's complete API suite for handling complex payment scenarios.

### Use cases
- Saving cards for subscription billing
- Storing payment methods for future one-time purchases
- Preparing for off-session payments
- Compliance with Strong Customer Authentication requirements

### Future payment optimization
The setup_future_usage parameter determines how saved payment methods are optimized:
- `on_session` - For payments where customer is present
- `off_session` - For automated payments without customer interaction
- Use `off_session` for both scenarios to maximize flexibility

## Compliance notes
Setup Intents helps comply with Strong Customer Authentication (SCA) by handling authentication during the setup process. Off-session setups may incur additional authentication friction.

## Technical reference
Not covered in current sources - needs dedicated Setup Intents documentation for complete API details.

## Cross-network comparison
Not applicable - Setup Intents is Stripe-specific functionality.

## Related
- [[stripe-payment-intents]]
- [[stripe-payment-methods]]
- [[strong-customer-authentication]]
- [[off-session-payments]]

## Sources
- raw/payment-intents.md