---
source: https://docs.stripe.com/billing/revenue-recovery/smart-retries
title: Automate payment retries | Stripe Documentation
type: reference
domain: payments
ingested: 2026-04-12
tags: []
---

# Automate payment retries | Stripe Documentation

# Automate payment retries

## Automatically retry failed subscription and invoice payments to reduce involuntary churn.

### Use the Accounts v2 API to represent customers

If your integration usescustomer-configured Accounts, replaceCustomerand event references in the code examples with the equivalent Accounts v2 API references. For more information, seeRepresent customers with Account objects.

Payments can fail for a number of reasons, but many of them are recoverable. Stripe Billing can automatically retry failed subscription and invoice payments for you.

To configure subscription retries in your Dashboard, go toBilling>Revenue recovery>Retries. For one-time invoice retries, go toAdvanced invoicing featuresunderSettings>Billing>Invoices.

Stripe recommends using Smart Retries, but you can also create acustom retry schedule.

#### Note

Stripe doesn’t retry payments if:

- No payment methods are available.

- The issuer returned ahard decline code.

- The payment card isIndia-issued.

- The StripeConnectaccount has been disconnected.

## Payment method ordering

When retrying, Stripe uses the first available payment method in this list, in this order:

PriorityPayment methodAPI attribute

Priority

Payment method

API attribute

1Subscription default payment methodsubscription.default_payment_method

1

Subscription default payment method

subscription.default_payment_method

2Subscription default payment sourcesubscription.default_source

2

Subscription default payment source

subscription.default_source

3Customer invoice default payment methodcustomer.invoice_settings.default_payment_method

3

Customer invoice default payment method

customer.invoice_settings.default_payment_method

4LegacyCustomer default payment sourcecustomer.default_source

4

LegacyCustomer default payment source

customer.default_source

When you update payment methods after a failed payment attempt, update the field where the previous payment failed. For example, if a subscription has adefault_payment_method, but you only updatecustomer.invoice_settings.default_payment_method, Stripe continues to retry on the subscription’sdefault_payment_method.

## Smart Retries

Using AI, Smart Retries chooses the best times to retry failed payment attempts to increase the chance of successfully paying an invoice. The AI model behind Smart Retries uses time-dependent, dynamic signals, such as:

- The number of different devices that have presented a given payment method in the lastNhours.

- The best time to pay (payments made for debit cards in certain countries might be slightly more successful at 12:01 AM in local time zones).

Stripe uses this information to assess when to retry payments. We continuously learn from new purchaser behaviours and transactions, which provide for a more targeted approach over traditional rules-based payment retry logic.

Smart Retries reattempts the charge according to your specifications for the number of retries and the maximum duration. You can set the Smart Retry policy to retry payment a specific number of times within a time period: 1 week, 2 weeks, 3 weeks, 1 month, or 2 months. The recommended default setting is 8 tries within 2 weeks. You can also useautomationsto create different retry policies for different customer segments.

You can override this behaviour bydisabling Smart Retriesand defining your own custom retry rules.When you enable dunning, thenext_payment_attemptattribute indicates when the next collection attempt will be.

## Webhook events

For both Smart Retries and custom retry schedules, Stripe reattempts the charge according to your specified schedule. Use theinvoice.payment_failedwebhookto receive subscription payment failure events and retry attempt updates.

Theattempt_countattribute on theinvoice.payment_failedwebhook indicates how many attempts have been made so far. If a failure returns ahard decline code, we can’t retry invoice payment without a new payment method. Retries continue to be scheduled, andattempt_countcontinues to increment, but retries only execute after detecting a new payment method. Unexecuted retries don’t create a newCharge.

Thenext_payment_attemptattribute on the invoice indicates the date when Stripe will attempt the next collection. Forautomationsusers,next_payment_attemptis no longer set ininvoice.payment_failedwebhooks but is set ininvoice.updatedwebhooks.

### Hard decline codes

Stripe can’t automatically retry a payment if the card issuer returns any of these hard decline codes:

- incorrect_number

- lost_card

- pickup_card

- stolen_card

- revocation_of_authorization

- revocation_of_all_authorizations

- authentication_required

- highest_risk_level

- transaction_not_allowed

For these failures, the scheduled retries continue but the payment only executes if you obtain a new payment method.

## Custom retry schedule

You can also modify the retry schedule withcustom rules. You can configure up to three retries, each with a specific number of days after the previous attempt.

You can use theinvoice.payment_failedevent to monitor subscription payment failure events and retry attempt updates. After a payment attempt on an invoice, itsnext_payment_attemptvalue is set using the current subscription settings in your Dashboard.

#### Warning

When using automations, thenext_payment_attemptis no longer set ininvoice.payment_failedwebhooks but is set ininvoice.updatedwebhooks.

If recovery fails, the subscription transitions according to your settings. The options are:

SettingDescription

Setting

Description

Cancel the subscriptionThe subscription changes to acanceledstate after the maximum number of days defined in the retry schedule.

Cancel the subscription

The subscription changes to acanceledstate after the maximum number of days defined in the retry schedule.

Mark the subscription as unpaidThe subscription changes to anunpaidstate after the maximum number of days defined in the retry schedule. Invoices continue to be generated and stay in a draft state.

Mark the subscription as unpaid

The subscription changes to anunpaidstate after the maximum number of days defined in the retry schedule. Invoices continue to be generated and stay in a draft state.

Leave the subscription overdueThe subscription remains in apast_duestate after the maximum number of days defined in the retry schedule. Invoices continue to be generated and charge customer based on retry settings.

Leave the subscription overdue

The subscription remains in apast_duestate after the maximum number of days defined in the retry schedule. Invoices continue to be generated and charge customer based on retry settings.

After the final payment attempt, we make no further payment attempts. Changing your subscription settings only affects future retries.

## Direct Debit retries

You can enable Direct Debit retries to have Stripe automatically retry failed Direct Debit payments caused by insufficient funds. You can turn on retries forrecurring subscription invoices,one-off invoicesor both.

#### Note

If you enable Direct Debit retries, a payment can still fail. Stripe isn’t responsible for any losses if a direct debit isn’t retried.

By default, Stripe doesn’t automatically retry failed Direct Debit payments, except for ACH Direct Debit which is generally available. To enable automatic retries for other Direct Debit payment methods, you must enrol in the corresponding private preview feature listed in the following table:

Direct DebitMaximum retriesMaximum retry periodMandate requirementsStatus

Direct Debit

Maximum retries

Maximum retry period

Mandate requirements

Status

ACH Direct Debit240 daysACH Direct Debit mandatesGeneral availability

ACH Direct Debit

2

40 days

ACH Direct Debit mandates

General availability

ACSS Direct Debit130 daysACSS Direct Debit mandatesPrivate preview

ACSS Direct Debit

1

30 days

ACSS Direct Debit mandates

Private preview

Australia BECS Direct Debit230 daysAU BECS Direct Debit mandatesPrivate preview

Australia BECS Direct Debit

2

30 days

AU BECS Direct Debit mandates

Private preview

Bacs Direct Debit230 daysBacs Direct Debit mandatesPrivate preview

Bacs Direct Debit

2

30 days

Bacs Direct Debit mandates

Private preview

New Zealand BECS Direct Debit130 daysNZ BECS Direct Debit mandatesPrivate preview

New Zealand BECS Direct Debit

1

30 days

NZ BECS Direct Debit mandates

Private preview

SEPA Direct Debit230 daysSEPA Direct Debit mandatesPrivate preview

SEPA Direct Debit

2

30 days

SEPA Direct Debit mandates

Private preview