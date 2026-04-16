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
- [[stripe-card-input-errors]] — Category of Stripe decline codes caused by incorrect card information
- [[stripe-local-payment-declines]] — Specialized decline codes for Local Payment Methods beyond traditional cards
- [[stripe-payment-intents]] — Stripe's primary API for handling payments with complex flows and authentication
- [[stripe-setup-intents]] — Stripe's API for saving payment methods for future use with authentication handling
- [[stripe-client-secret]] — Unique security key enabling secure client-side payment completion
- [[stripe-reviews]] — Manual fraud inspection capabilities that supplement automated fraud prevention systems
- [[smart-refunds]] — AI-powered recommendations to refund payments predicted to have high fraud risk

## Codes
- [[stripe-authentication-required]] — Card declined because transaction requires 3D Secure authentication
- [[stripe-insufficient-funds]] — Card has insufficient funds to complete the purchase
- [[visa-reason-code-10-4]] — Other Fraud — Card-Absent Environment, commonly associated with friendly fraud
- [[stripe-fraudulent]] — Payment declined by Stripe's fraud detection systems
- [[stripe-generic-decline]] — Card declined for unknown reason or blocked by Stripe risk management
- [[authentication-not-handled]] — Stripe decline when required authentication was skipped
- [[incorrect-number]] — Stripe decline for incorrect card number entry
- [[incorrect-cvc]] — Stripe decline for incorrect CVC entry
- [[expired-card]] — Stripe decline for cards past expiration date
- [[partner-generic-decline]] — Generic decline from Local Payment Method providers
- [[invalid-customer-account]] — LPM decline due to customer account issues
- [[withdrawal-count-limit-exceeded]] — Card spending limits exceeded
- [[card-velocity-exceeded]] — Card transaction velocity limits exceeded
- [[testmode-decline]] — Test card used in live payment environment

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
- [[stripe-dispute-handling]] — Stripe's guided process for responding to disputes through the Dashboard
- [[smart-disputes]] — Stripe's automated evidence collection and submission system for eligible disputes
- [[stripe-3ds-integration]] — Stripe's multiple approaches for integrating 3D Secure authentication
- [[payment-intent-lifecycle]] — Stripe's payment processing workflow from creation through completion
- [[payment-intent-creation]] — Process of creating Stripe Payment Intents with proper security and reuse strategies
- [[payment-intent-confirmation]] — Client-side process for completing Stripe payments using client secrets
- [[stripe-review-queue]] — Prioritized Dashboard interface for examining potentially fraudulent payments
- [[manual-review-process]] — Step-by-step workflow for examining potentially fraudulent payments using human judgment

## Gaps
- [[strong-customer-authentication]] — Mentioned in 2 sources, needs dedicated coverage
- [[psd2]] — Referenced but not explained
- [[visa-secure]] — Visa's branded 3DS implementation, needs dedicated coverage
- [[mastercard-identity-check]] — Mastercard's branded 3DS implementation, needs dedicated coverage
- [[amex-safekey]] — American Express's branded 3DS implementation, needs dedicated coverage
- [[fraud-detection]] — Mentioned in 3 sources, needs dedicated coverage
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
- [[dispute-reason-codes]] — Network codes categorizing dispute reasons, needs dedicated coverage
- [[stripe-disputes-dashboard]] — Stripe's interface for dispute management, mentioned but not detailed
- [[dispute-automation]] — General concept of automated dispute handling, needs dedicated coverage
- [[network-dispute-fees]] — Fees charged by card networks for disputes, needs dedicated coverage
- [[dispute-monitoring-programmes]] — Card network programs tracking merchant dispute rates, needs dedicated coverage
- [[stripe-payment-methods]] — Stripe's API for managing customer payment methods, needs dedicated coverage
- [[stripe-webhooks]] — Stripe's event notification system for payment status updates, needs dedicated coverage
- [[idempotency-keys]] — Mechanism for preventing duplicate API operations, needs dedicated coverage
- [[off-session-payments]] — Payments processed without customer interaction, needs dedicated coverage
- [[tls-encryption]] — Transport layer security for payment data protection, needs dedicated coverage
- [[purchase-funnel]] — Customer journey analytics for payment optimization, needs dedicated coverage
- [[statement-descriptors]] — Text appearing on customer card statements, needs dedicated coverage
- [[metadata]] — Custom data storage for payment reconciliation, needs dedicated coverage
- [[radar-fraud-teams]] — Stripe's advanced fraud prevention tools, needs dedicated coverage
- [[fulfillment]] — Order completion and delivery process, needs dedicated coverage