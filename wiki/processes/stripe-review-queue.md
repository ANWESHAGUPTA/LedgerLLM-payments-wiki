---
title: Stripe Review Queue
category: process
network: stripe
related: [[stripe-reviews]], [[manual-review-process]], [[smart-refunds]], [[radar-fraud-teams]]
sources: [reviews.md]
last_compiled: 2026-04-16
confidence: high
---

# Stripe Review Queue

## Summary
Stripe's review queue is a prioritized Dashboard interface for examining potentially fraudulent payments that require human inspection. It provides both list and detailed views to help merchants efficiently review transactions flagged by automated systems.

## Details
The review queue displays completed or to-be-captured payments that might need investigation. Merchants can access it through two views:

### List View
Quick overview showing:
- Risk level assigned by Stripe
- Customer name and payment method information
- Payment amount, date, and time
- The client used

### Detailed View
Comprehensive payment context including:
- Risk insights section identifying key fraud factors
- Related payments using same email, IP, or card
- Metadata for business-specific context
- Navigation between payments using Previous/Next buttons or J/K keyboard shortcuts

## Available Actions
After reviewing a payment, merchants can:
- **Approve**: Close review with no changes (can still refund later)
- **Capture**: For payments requiring later capture
- **Refund**: Refund without fraud reporting
- **Refund and report fraud**: Refund plus add to block lists

## Review Assignments
Team members can assign themselves to reviews to avoid duplicate work. The system shows:
- Which reviews others are working on
- Assignment history in the timeline
- Filtering options for owned or unassigned reviews

## Best Practices
- Focus on payments where human judgment adds value
- Use risk insights and related payments for informed decisions
- Collect reviewer insights to develop fraud prevention strategies
- Customize with business-specific metadata
- Consider customer impact - don't slow delivery unnecessarily

## Webhooks
Stripe sends events for review activity:
- `review.opened`: Transaction added to queue
- `review.closed`: Review completed with reason

## Technical Reference
Available through Stripe Dashboard for accounts with [[radar-fraud-teams]]. Not supported in Stripe Radar India.

## Related
- [[stripe-reviews]]
- [[manual-review-process]]
- [[smart-refunds]]
- [[radar-fraud-teams]]

## Sources
- reviews.md