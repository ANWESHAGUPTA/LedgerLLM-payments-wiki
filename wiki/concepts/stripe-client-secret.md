---
title: Stripe Client Secret
category: concept
network: stripe
related: [[stripe-payment-intents]], [[stripe-setup-intents]], [[tls-encryption]]
sources: [raw/payment-intents.md]
last_compiled: 2026-04-16
confidence: high
---

# Stripe Client Secret

## Summary
The client secret is a unique key generated for each PaymentIntent that enables secure client-side payment completion without exposing sensitive payment details to the frontend.

## Details
Every PaymentIntent contains a client secret that serves as a secure parameter for client-side operations. Stripe.js uses this secret when invoking payment completion functions like `stripe.confirmCardPayment()` or `stripe.handleCardAction()`.

### Security model
The client secret allows the client to complete payments with the specific amount defined in the PaymentIntent, but doesn't expose other sensitive information. This enables secure frontend payment processing while maintaining server-side control over payment parameters.

### Implementation approaches
1. **Server endpoint** - Client fetches secret from dedicated API endpoint
2. **Direct embedding** - Server renders secret directly in page (less secure)
3. **Single-page applications** - Fetch via browser's native fetch function

### Best practices for client secrets
- Never log client secrets in application logs
- Don't embed in URLs or query parameters
- Only expose to the specific customer making the payment
- Always use TLS encryption on pages containing client secrets
- Retrieve from server endpoints rather than embedding directly

## Compliance notes
Proper client secret handling is essential for PCI compliance and secure payment processing.

## Technical reference
- Retrieved from PaymentIntent object after creation
- Used as parameter in Stripe.js functions
- Unique per PaymentIntent instance
- Required for all client-side payment completion

## Cross-network comparison
Not applicable - Client secret is Stripe's specific security implementation.

## Related
- [[stripe-payment-intents]]
- [[stripe-setup-intents]]
- [[tls-encryption]]

## Sources
- raw/payment-intents.md