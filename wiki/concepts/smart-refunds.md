---
title: Smart Refunds
category: concept
network: stripe
related: [[stripe-reviews]], [[stripe-review-queue]], [[radar-fraud-teams]], [[fraud-detection]]
sources: [reviews.md]
last_compiled: 2026-04-16
confidence: high
---

# Smart Refunds

## Summary
Smart Refunds is Stripe's AI-powered system that provides recommendations to refund payments predicted to have high fraud risk. It extends fraud protection beyond payment completion by analyzing additional risk factors that emerge hours after transactions.

## Details
Smart Refunds evaluates the likelihood of transactions resulting in fraudulent disputes using Radar AI models. The system analyzes additional risk factors from other Stripe transactions processed in the hours following your payment completion.

Recommendations appear in the Smart Refunds quick filter within the [[stripe-review-queue]]. By default, only high and very high confidence recommendations are shown, but merchants can adjust the confidence threshold.

## Confidence Levels
Smart Refunds provides five confidence levels with associated fraud dispute probabilities:

- **Very high**: 72% chance of early fraud warning or dispute
- **High**: 60% chance of early fraud warning or dispute  
- **Medium**: 40% chance of early fraud warning or dispute
- **Low**: 30% chance of early fraud warning or dispute
- **Very low**: 15% chance of early fraud warning or dispute

## Business Impact
Refunding payments based on Smart Refunds recommendations can:
- Prevent fraudulent disputes before they occur
- Save dispute fees and administrative costs
- Reduce chargeback ratios
- Maintain good standing with card networks

## Technical Reference
Available exclusively through [[radar-fraud-teams]]. Recommendations are accessible via the Dashboard review queue with Smart Refunds filter.

## Related
- [[stripe-reviews]]
- [[stripe-review-queue]]
- [[radar-fraud-teams]]
- [[fraud-detection]]

## Sources
- reviews.md