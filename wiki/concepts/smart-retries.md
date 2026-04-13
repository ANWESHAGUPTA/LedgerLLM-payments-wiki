---
title: Smart Retries
category: concept
network: stripe
related: [[payment-retry-strategy]], [[stripe-decline-codes]], [[hard-decline-codes]], [[direct-debit-retries]]
sources: [smart-retries.md]
last_compiled: 2026-04-12
confidence: high
---

# Smart Retries

## Summary
Stripe's AI-powered payment retry system that automatically chooses optimal times to retry failed subscription and invoice payments. Unlike traditional rules-based systems, Smart Retries uses dynamic signals and machine learning to maximize recovery success rates.

## Details
Smart Retries uses AI to analyze time-dependent signals including:
- Number of devices that have used a payment method in recent hours
- Optimal payment timing (e.g., debit cards may succeed better at 12:01 AM local time)
- Customer behavior patterns and transaction history

The system continuously learns from new purchaser behaviors to improve targeting over traditional rules-based retry logic.

### Configuration Options
You can configure Smart Retries to:
- Retry a specific number of times (recommended: 8 tries)
- Within specific time periods: 1 week, 2 weeks, 3 weeks, 1 month, or 2 months (recommended: 2 weeks)
- Use different retry policies for different customer segments via automations

### Payment Method Priority
When retrying, Stripe uses payment methods in this order:
1. Subscription default payment method (`subscription.default_payment_method`)
2. Subscription default payment source (`subscription.default_source`)
3. Customer invoice default payment method (`customer.invoice_settings.default_payment_method`)
4. Legacy customer default payment source (`customer.default_source`)

## Compliance notes
Stripe will NOT retry payments if:
- No payment methods are available
- The issuer returned a [[hard-decline-codes|hard decline code]]
- The payment card is India-issued
- The Stripe Connect account has been disconnected

## Technical reference
### Webhook Events
- `invoice.payment_failed` - Receives payment failure events and retry updates
- `invoice.updated` - Contains `next_payment_attempt` for automations users

### Key Attributes
- `attempt_count` - Number of retry attempts made so far
- `next_payment_attempt` - Date of next scheduled collection attempt

## Cross-network comparison
Smart Retries is specific to Stripe's platform. Traditional payment processors typically use rules-based retry logic with fixed schedules, while Stripe's AI-powered approach adapts dynamically to optimize success rates.

## Related
- [[payment-retry-strategy]]
- [[stripe-decline-codes]]
- [[hard-decline-codes]]
- [[direct-debit-retries]]
- [[custom-retry-schedule]]

## Sources
- smart-retries.md