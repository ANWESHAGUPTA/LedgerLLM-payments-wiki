---
title: Direct Debit Retries
category: concept
network: stripe
related: [[smart-retries]], [[payment-retry-strategy]]
sources: [smart-retries.md]
last_compiled: 2026-04-12
confidence: high
---

# Direct Debit Retries

## Summary
Stripe's automated retry system for failed Direct Debit payments, primarily targeting insufficient funds failures. Different Direct Debit methods have varying retry limits and availability status.

## Details
By default, Stripe doesn't automatically retry failed Direct Debit payments except for ACH Direct Debit (generally available). Other Direct Debit methods require enrollment in private preview features.

### Retry Specifications by Method
- **ACH Direct Debit**: 2 retries, 40-day period, generally available
- **ACSS Direct Debit**: 1 retry, 30-day period, private preview
- **Australia BECS Direct Debit**: 2 retries, 30-day period, private preview
- **Bacs Direct Debit**: 2 retries, 30-day period, private preview
- **New Zealand BECS Direct Debit**: 1 retry, 30-day period, private preview
- **SEPA Direct Debit**: 2 retries, 30-day period, private preview

### Configuration Options
You can enable retries for:
- Recurring subscription invoices
- One-off invoices
- Both types

## Compliance notes
Stripe disclaims responsibility for losses if a direct debit isn't retried. Each Direct Debit method requires specific mandate requirements that must be met before retries can be enabled.

## Technical reference
Direct Debit retries operate separately from standard Smart Retries and have method-specific limitations on retry count and timing.

## Cross-network comparison
Not covered in current sources - other payment processors' Direct Debit retry policies need dedicated coverage.

## Related
- [[smart-retries]]
- [[payment-retry-strategy]]

## Sources
- smart-retries.md