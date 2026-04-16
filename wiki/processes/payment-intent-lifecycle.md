---
title: Payment Intent Lifecycle
category: process
network: stripe
related: [[stripe-payment-intents]], [[stripe-payment-methods]], [[stripe-webhooks]], [[3d-secure]]
sources: [raw/payment-intents.md]
last_compiled: 2026-04-16
confidence: high
---

# Payment Intent Lifecycle

## Summary
The Payment Intent lifecycle describes how Stripe processes payments from creation through final status, including handling authentication steps and status changes throughout the process.

## Details
The Payment Intent lifecycle involves two primary actions: creating and confirming a PaymentIntent. The status changes as the payment progresses through different stages.

### Creation phase
1. **Create PaymentIntent** - Server-side creation with amount, currency, and payment method details
2. **Generate client secret** - Unique key for secure client-side operations
3. **Pass to frontend** - Client secret transmitted securely to browser/app

### Confirmation phase
1. **Client confirmation** - Frontend calls Stripe.js confirmation functions
2. **Authentication handling** - Automatic 3D Secure or SCA processing if required
3. **Status updates** - PaymentIntent status changes based on payment outcome

### Completion monitoring
1. **Webhook notifications** - Server receives real-time status updates
2. **Charge creation** - Successful payments create associated Charge objects
3. **Multiple attempts** - Failed payments may create multiple Charges through retries

### Status progression
PaymentIntents progress through various statuses that indicate current payment state. Each status change triggers webhook events for server-side handling.

## Compliance notes
The lifecycle automatically handles regulatory requirements like Strong Customer Authentication, triggering additional steps when required by regional rules.

## Technical reference
- Creation: Server-side API call to `/v1/payment_intents`
- Confirmation: Client-side `stripe.confirmCardPayment()` or similar
- Monitoring: Webhook endpoints for status change notifications
- Retry handling: Multiple Charge objects may be created for failed attempts

## Cross-network comparison
Not applicable - This is Stripe's specific implementation of payment processing lifecycle.

## Related
- [[stripe-payment-intents]]
- [[stripe-payment-methods]]
- [[stripe-webhooks]]
- [[3d-secure]]

## Sources
- raw/payment-intents.md