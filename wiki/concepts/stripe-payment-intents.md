---
title: Stripe Payment Intents
category: concept
network: stripe
related: [[payment-intent-lifecycle]], [[stripe-payment-methods]], [[stripe-setup-intents]], [[stripe-client-secret]], [[3d-secure]], [[strong-customer-authentication]], [[stripe-webhooks]], [[idempotency-keys]]
sources: [raw/payment-intents.md]
last_compiled: 2026-04-16
confidence: high
---

# Stripe Payment Intents

## Summary
Payment Intents is Stripe's primary API for handling payments with complex flows that change status over time. It tracks payments from creation through completion and automatically handles authentication steps like 3D Secure.

## Details
The Payment Intents API provides a complete payment processing solution that addresses common integration challenges:

- **Automatic authentication handling** - Manages 3D Secure and SCA requirements without additional code
- **No double charges** - Built-in protection against duplicate payments
- **Idempotency key support** - Prevents accidental duplicate payment creation
- **Regulatory compliance** - Supports Strong Customer Authentication and similar requirements

Each PaymentIntent correlates to a single shopping cart or customer session, encapsulating transaction details like supported payment methods, amount, and currency.

### Core workflow
1. Create a PaymentIntent when the payment amount is known
2. Pass the client secret to the frontend
3. Client confirms the payment using Stripe.js
4. Server monitors webhooks for completion status

### Best practices
- Create PaymentIntents early in checkout to track the purchase funnel
- Reuse PaymentIntents if checkout is interrupted and resumed
- Always provide idempotency keys to prevent duplicates
- Store PaymentIntent IDs on shopping carts for retrieval

## Compliance notes
Payment Intents automatically handles Strong Customer Authentication (SCA) requirements. The setup_future_usage parameter optimizes authorization rates in compliance with regional legislation and network rules.

## Technical reference
- API endpoint: `/v1/payment_intents`
- Key functions: `stripe.confirmCardPayment()`, `stripe.handleCardAction()`
- Client secret format: Unique per PaymentIntent, used for frontend completion
- Metadata limit: Custom fields for reconciliation and fraud prevention
- Statement descriptor limit: 22 characters, no special characters except standard separators

## Cross-network comparison
Not applicable - Payment Intents is Stripe-specific. Other processors have similar concepts but different implementations.

## Related
- [[payment-intent-lifecycle]]
- [[stripe-payment-methods]]
- [[stripe-setup-intents]]
- [[stripe-client-secret]]
- [[3d-secure]]
- [[strong-customer-authentication]]
- [[stripe-webhooks]]
- [[idempotency-keys]]

## Sources
- raw/payment-intents.md