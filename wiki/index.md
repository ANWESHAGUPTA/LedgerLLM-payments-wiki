# Ledger Wiki Index

## Concepts
- [[3d-secure]] — Authentication protocol that adds security layer to online card payments
- [[stripe-decline-codes]] — Stripe's system of detailed decline codes for failed payments
- [[chargebacks]] — Transaction reversals initiated when cardholders dispute charges with issuing banks
- [[disputes]] — Payment disputes where cardholders question transactions with their card issuers
- [[chargeback-thresholds]] — Limits set by card networks to identify merchants with excessive dispute rates
- [[smart-retries]] — Stripe's AI-powered system for optimizing payment retry timing and success rates
- [[hard-decline-codes]] — Decline codes indicating permanent failures that require new payment methods
- [[direct-debit-retries]] — Stripe's automated retry system for failed Direct Debit payments
- [[friendly-fraud]] — Invalid chargeback claims on legitimate transactions, estimated at 75% of all disputes
- [[stripe-card-errors]] — Stripe's specific decline codes for card input errors like wrong numbers or expired dates
- [[stripe-issuer-declines]] — Stripe's detailed codes for issuer-generated payment declines
- [[stripe-local-payment-declines]] — Stripe's decline codes for Local Payment Method failures beyond traditional cards

## Codes
- [[stripe-authentication-required]] — Card declined because transaction requires 3D Secure authentication
- [[stripe-insufficient-funds]] — Card has insufficient funds to complete the purchase
- [[visa-reason-code-10-4]] — Other Fraud — Card-Absent Environment, commonly associated with friendly fraud
- [[stripe-fraudulent]] — Payment declined by Stripe's fraud detection systems
- [[stripe-generic-decline]] — Card declined for unknown reason or blocked by Stripe risk management

## Networks
- [[visa-dispute-process]] — Visa's structured workflow for handling transaction disputes
- [[mastercard-chargeback-rules]] — Mastercard's comprehensive dispute processing rules and procedures
- [[mastercard-reason-codes]] — Mastercard's 4-digit identifiers explaining chargeback reasons
- [[visa-reason-codes]] — Visa's alphanumeric codes categorizing disputes into fraud, authorization, processing, and consumer categories
- [[visa-dispute-monitoring-program]] — Visa's VDMP compliance program that penalizes merchants exceeding chargeback thresholds
- [[visa-compelling-evidence-3-0]] — Visa's CE 3.0 framework for fighting reason code 10.4 fraud disputes
- [[order-insight]] — Visa's pre-dispute platform enabling dispute prevention through real-time data sharing
- [[stripe-dispute-handling]] — Stripe's guided dispute management system through the Dashboard

## Processes
- [[payment-retry-strategy]] — Systematic approach to handling failed payments with appropriate retry logic
- [[visa-pre-arbitration]] — Visa's dispute escalation stage when issuers reject merchant representment submissions
- [[visa-compliance-process]] — Alternative dispute resolution for Visa Core Rules violations outside standard chargeback process
- [[chargeback-representment]] — Process of challenging invalid chargebacks by submitting compelling evidence

## Gaps
- [[strong-customer-authentication]] — Mentioned in 2 sources, needs dedicated coverage
- [[psd2]] — Referenced but not explained
- [[visa-secure]] — Visa's branded 3DS implementation, needs dedicated coverage
- [[mastercard-identity-check]] — Mastercard's branded 3DS implementation, needs dedicated coverage
- [[amex-safekey]] — American Express's branded 3DS implementation, needs dedicated coverage
- [[fraud-detection]] — Mentioned in 2 sources, needs dedicated coverage
- [[dispute-evidence-submission]] — Process for submitting dispute evidence, needs dedicated coverage
- [[acquirer-processor-relationship]] — Role of acquirers/processors in disputes, needs dedicated coverage
- [[chargeback-costs]] — Financial impact of chargebacks beyond transaction amount, needs dedicated coverage
- [[excessive-chargeback-merchants]] — Merchants enrolled in monitoring programs, needs dedicated coverage
- [[visa-monitoring-program]] — Visa's VAMP program, needs dedicated coverage
- [[chargeback-reason-codes]] — General concept of reason codes across networks, needs dedicated coverage
- [[custom-retry-schedule]] — Stripe's alternative to Smart Retries with configurable rules, needs dedicated coverage
- [[visa-arbitration]] — Final stage in Visa dispute process with high costs and tight deadlines, needs dedicated coverage
- [[visa-core-rules]] — Fundamental Visa transaction regulations, needs dedicated coverage
- [[first-party-misuse]] — Visa's official term for friendly fraud, needs dedicated coverage
- [[visa-resolve-online]] — Visa's platform for dispute case management, needs dedicated coverage
- [[generic-decline-handling]] — Standard approach for presenting sensitive declines, needs dedicated coverage
- [[smart-disputes]] — Stripe's automated dispute evidence collection system, needs dedicated coverage
- [[dispute-reason-codes]] — Network codes categorizing dispute reasons, needs dedicated coverage