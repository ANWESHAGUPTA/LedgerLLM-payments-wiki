

## [2026-04-12] compile | 3d-secure.md

### Articles created
- wiki/concepts/3d-secure.md
- wiki/gaps/strong-customer-authentication.md
- wiki/gaps/psd2.md
- wiki/gaps/visa-secure.md
- wiki/gaps/mastercard-identity-check.md
- wiki/gaps/amex-safekey.md

### Articles updated
- None (first compile)

### Gap stubs created
- strong-customer-authentication: mentioned as SCA regulation but not explained
- psd2: referenced as regulatory framework but no details provided
- visa-secure: mentioned as Visa's branded 3DS but no specifics
- mastercard-identity-check: mentioned as Mastercard's branded 3DS but no specifics
- amex-safekey: mentioned as Amex's branded 3DS but no specifics

### Cross-links added
- 3d-secure → strong-customer-authentication (regulatory relationship)
- 3d-secure → network-branded implementations (visa-secure, mastercard-identity-check, amex-safekey)
- strong-customer-authentication → psd2 (part of regulatory framework)

### Reasoning log
- Applied synonym rule: "3D Secure" = "3DS" merged into single article
- Applied 2+ sentence threshold: 3DS had extensive coverage (full article), network brands only mentioned briefly (gap stubs)
- Cross-network comparison included: noted all three major networks have branded 3DS implementations
- Regulatory context preserved: noted SCA requirements across multiple jurisdictions
- Incomplete info handling: no contradictions found, but network-specific details flagged as gaps

### Contradictions found
- None in this compile pass.


## [2026-04-12] compile | raw/codes.md

### Articles created
- wiki/concepts/stripe-decline-codes.md
- wiki/codes/stripe-authentication-required.md
- wiki/codes/stripe-insufficient-funds.md
- wiki/processes/payment-retry-strategy.md
- wiki/gaps/fraud-detection.md

### Articles updated
- None (no existing articles covered these topics)

### Gap stubs created
- wiki/gaps/fraud-detection.md (mentioned in context of fraudulent declines but not explained)

### Cross-links added
- stripe-decline-codes → 3d-secure (authentication requirements)
- stripe-authentication-required → 3d-secure (requires authentication)
- stripe-authentication-required → strong-customer-authentication (SCA compliance)
- stripe-insufficient-funds → payment-retry-strategy (retry logic)
- payment-retry-strategy → stripe-decline-codes (based on decline types)

### Reasoning log
- Created concept article for Stripe decline codes rather than individual code articles for all 50+ codes - most provide similar guidance and would create excessive fragmentation
- Selected authentication_required and insufficient_funds as representative code articles since they have distinct handling requirements
- Cross-network comparison added to stripe-decline-codes showing how Stripe's descriptive codes compare to Visa/Mastercard numeric codes
- Payment retry strategy elevated to full process article due to 2+ paragraphs of guidance across multiple decline scenarios
- Fraud detection created as gap - mentioned in fraudulent code handling but no explanation of how Stripe's fraud systems work

### Incomplete information found
- Cross-network comparison for payment retry strategy: Visa and Mastercard retry guidelines not found in current sources. Flagged in article.
- Specific retry timing recommendations: Source provides general guidance but no specific timeframes for different decline types

### Contradictions found
- None in this compile pass.


## [2026-04-12] compile | dispute-resolution.md

### Articles created
- wiki/networks/visa-dispute-process.md
- wiki/concepts/chargebacks.md
- wiki/gaps/dispute-evidence-submission.md
- wiki/gaps/acquirer-processor-relationship.md
- wiki/gaps/chargeback-costs.md

### Articles updated
- None

### Gap stubs created
- wiki/gaps/dispute-evidence-submission.md (mentioned as step 3 but not detailed)
- wiki/gaps/acquirer-processor-relationship.md (referenced but not explained)
- wiki/gaps/chargeback-costs.md (mentioned but not quantified)

### Cross-links added
- visa-dispute-process → chargebacks, dispute-evidence-submission, acquirer-processor-relationship
- chargebacks → visa-dispute-process, dispute-evidence-submission, chargeback-costs

### Reasoning log
- Incomplete info: Visa-specific timeframes, evidence requirements, and chargeback reason codes not found in source. Flagged in articles as "Not covered in current sources".
- Gap creation: Multiple concepts mentioned (evidence submission, acquirer relationships, chargeback costs) but explained in 1 sentence or less. Created gap stubs per threshold rule.
- Cross-network comparison: No Mastercard or other network information available in source. Flagged in articles for future enhancement.
- Synonym check: "Disputes" and "chargebacks" treated as related but distinct concepts based on source context.

### Contradictions found
- None in this compile pass.


## [2026-04-13] compile | mastercard-chargeback-rules.md

### Articles created
- wiki/networks/mastercard-chargeback-rules.md
- wiki/networks/mastercard-reason-codes.md
- wiki/concepts/chargeback-thresholds.md

### Articles updated
- None (no existing articles required updates)

### Gap stubs created
- wiki/gaps/excessive-chargeback-merchants.md (ECM program mentioned but not explained)
- wiki/gaps/visa-monitoring-program.md (VAMP referenced for comparison but not detailed)
- wiki/gaps/chargeback-reason-codes.md (general concept mentioned but needs broader coverage)
- wiki/gaps/visa-reason-codes.md (referenced for comparison but not detailed)

### Cross-links added
- mastercard-chargeback-rules → chargebacks, visa-dispute-process, mastercard-reason-codes, chargeback-thresholds, dispute-evidence-submission
- mastercard-reason-codes → chargeback-reason-codes, visa-reason-codes, dispute-evidence-submission
- chargeback-thresholds → excessive-chargeback-merchants, visa-monitoring-program, mastercard-chargeback-rules

### Reasoning log
- Cross-network comparison: Applied comparison between Mastercard (1.5% threshold) and Visa VAMP (0.9% from existing wiki knowledge). Highlighted different reason code formats.
- Incomplete info: Visa reason code equivalents mentioned for comparison but not found in detailed form in any source. Flagged for future sourcing.
- Synonym detection: Applied "ECM" = "Excessive Chargeback Merchant" program terminology.
- Article creation threshold: Mastercard reason codes had 2+ sentences of discussion per category, warranting full article. ECM program only mentioned briefly, created gap stub.
- Domain rules applied: Automatically linked chargeback mentions to existing [[chargebacks]] article, dispute processes to [[dispute-evidence-submission]] gap.

### Contradictions found
- None in this compile pass. Source provided Mastercard-specific information without contradicting existing Visa or Stripe content.


## [2026-04-12] compile | smart-retries.md

### Articles created
- wiki/concepts/smart-retries.md
- wiki/concepts/hard-decline-codes.md
- wiki/concepts/direct-debit-retries.md
- wiki/gaps/custom-retry-schedule.md

### Articles updated
- None (existing payment-retry-strategy.md covers general retry concepts, Smart Retries is Stripe-specific implementation)

### Gap stubs created
- wiki/gaps/custom-retry-schedule.md (mentioned as alternative to Smart Retries but not detailed)

### Cross-links added
- smart-retries → payment-retry-strategy (part_of relationship)
- smart-retries → stripe-decline-codes (related)
- smart-retries → hard-decline-codes (related)
- hard-decline-codes → stripe-authentication-required (authentication_required is a hard decline code)
- direct-debit-retries → payment-retry-strategy (part_of relationship)

### Reasoning log
- Smart Retries identified as new Stripe-specific concept warranting its own article rather than merging with existing payment-retry-strategy.md due to AI-powered approach being fundamentally different from traditional rules-based systems
- Hard decline codes extracted as separate concept article due to their specific behavior in retry systems and cross-reference potential with existing stripe-authentication-required code
- Direct Debit retries treated as separate concept due to distinct rules, limitations, and availability across different Direct Debit methods
- Custom retry schedule created as gap stub - mentioned multiple times but implementation details not provided
- Applied cross-linking rules: authentication_required mentioned as hard decline code linked to existing stripe-authentication-required article
- Incomplete info noted: Cross-network comparison gaps flagged for hard decline codes (Visa/Mastercard equivalents) and Direct Debit retries (other processors)

### Contradictions found
- None in this compile pass. Smart Retries source is recent (2026) and doesn't contradict existing retry strategy concepts.

### Search for missing information
- Searched existing sources for Visa/Mastercard hard decline equivalents: not found in current raw sources
- Searched for other processor Direct Debit retry policies: not found in current raw sources
- Flagged gaps in hard-decline-codes.md and direct-debit-retries.md articles


## [2026-04-13] compile | raw/visa-chargeback-rules.md

### Articles created
- wiki/networks/visa-reason-codes.md
- wiki/networks/visa-dispute-monitoring-program.md
- wiki/processes/visa-pre-arbitration.md
- wiki/processes/visa-compliance-process.md
- wiki/concepts/friendly-fraud.md

### Gap stubs created
- wiki/gaps/visa-arbitration.md (final dispute stage mentioned but needs dedicated coverage)
- wiki/gaps/visa-core-rules.md (fundamental regulations mentioned but not explained)
- wiki/gaps/first-party-misuse.md (Visa's official term for friendly fraud, needs dedicated coverage)

### Articles updated
None - no existing articles required updates from this source.

### Cross-links added
- visa-reason-codes → chargeback-reason-codes, mastercard-reason-codes, visa-dispute-process
- visa-dispute-monitoring-program → chargeback-thresholds, excessive-chargeback-merchants, visa-monitoring-program
- visa-pre-arbitration → visa-dispute-process, dispute-evidence-submission, visa-arbitration, mastercard-chargeback-rules
- friendly-fraud → chargebacks, first-party-misuse, dispute-evidence-submission, visa-reason-codes

### Synonym merging applied
- "VDMP" merged with "Visa Dispute Monitoring Program" (full name used)
- "Pre-arbs" merged with "Pre-arbitration" (official Visa terminology used)
- "Friendly fraud" and "first-party misuse" treated as related concepts with separate articles

### Reasoning log
- Gap created for visa-arbitration: mentioned as final stage but only 2 sentences of detail
- Gap created for visa-core-rules: referenced in compliance process but not explained
- Friendly fraud promoted to full article: sufficient detail provided about prevention and impact
- Cross-network comparison noted for visa-reason-codes vs mastercard system
- Incomplete info flagged: Mastercard equivalent for VDMP not found in current sources

### Contradictions found
None in this compile pass.

### Index promotion
- visa-reason-codes promoted from gap to full network article
- visa-monitoring-program remains gap but now linked to new VDMP article


## [2026-04-13] compile | visa-compelling-evidence-3-0.md

### Articles created
- wiki/networks/visa-compelling-evidence-3-0.md
- wiki/codes/visa-reason-code-10-4.md
- wiki/networks/order-insight.md
- wiki/processes/chargeback-representment.md

### Articles updated
- None

### Gap stubs created
- wiki/gaps/visa-resolve-online.md (mentioned as platform but not explained)

### Cross-links added
- visa-compelling-evidence-3-0 → visa-reason-code-10-4 (applies specifically to this code)
- visa-compelling-evidence-3-0 → friendly-fraud (designed to combat)
- visa-compelling-evidence-3-0 → order-insight (integrates with for prevention)
- visa-reason-code-10-4 → friendly-fraud (commonly associated)
- order-insight → chargeback-representment (prevents need for)
- chargeback-representment → dispute-evidence-submission (requires)

### Reasoning log
- CE 3.0 categorized as network article (Visa-specific) rather than concept due to its network-specific implementation
- Reason code 10.4 qualified for full article with 2+ sentences of discussion and specific technical details
- Order Insight qualified for full article as integral part of CE 3.0 implementation
- Chargeback representment promoted from gap to full article based on detailed discussion in source
- Visa Resolve Online (VROL) mentioned as technical platform but not explained - created gap stub
- Applied synonym rule: "CE3.0" = "CE 3.0" = "Compelling Evidence 3.0" - used consistent terminology
- Cross-network comparison noted where Visa-specific features don't have direct equivalents

### Contradictions found
- None in this compile pass.

### Incomplete information handled
- Mastercard equivalent fraud dispute evidence requirements not covered in current sources - flagged in articles
- Other network dispute prevention platforms mentioned but not detailed - noted as gaps
- VROL technical specifications mentioned but not explained - gap stub created


## [2026-04-15] compile | raw/codes.md

### Articles created
- wiki/codes/stripe-authentication-required.md
- wiki/codes/stripe-insufficient-funds.md
- wiki/codes/stripe-fraudulent.md
- wiki/codes/stripe-generic-decline.md
- wiki/concepts/stripe-card-errors.md
- wiki/concepts/stripe-issuer-declines.md
- wiki/concepts/stripe-local-payment-declines.md

### Gap stubs created
- wiki/gaps/generic-decline-handling.md (mentioned as recommended approach for sensitive declines)

### Cross-links added
- stripe-authentication-required → 3d-secure (requires authentication protocol)
- stripe-authentication-required → strong-customer-authentication (SCA regulation)
- stripe-insufficient-funds → hard-decline-codes (permanent failure type)
- stripe-fraudulent → fraud-detection (generated by fraud systems)
- stripe-fraudulent → generic-decline-handling (security requirement)
- All new codes → stripe-decline-codes (part of Stripe's system)
- Card errors and issuer declines → payment-retry-strategy (retry guidance)

### Reasoning log
- Domain rule applied: Created individual code articles for specific Stripe decline codes with 2+ sentences of explanation
- Grouped related codes into concept articles: card input errors, issuer declines, LPM declines for better organization
- Security handling noted: fraudulent, lost_card, stolen_card should be presented as generic declines
- Cross-network comparison marked as "Not covered" - no Visa/Mastercard equivalent codes in source
- Gap created for "generic-decline-handling" - mentioned as security practice but not explained in detail
- Applied synonym detection: insufficient_funds appears in both card and LPM contexts, treated as related but separate codes

### Contradictions found
- None in this compile pass.

### Source coverage
- Comprehensive coverage of Stripe decline codes from official documentation
- Source date: 2026-04-15 (recent)
- High confidence level assigned due to official source


## [2026-04-15] compile | raw/disputes.md

### Articles created
- wiki/concepts/disputes.md
- wiki/networks/stripe-dispute-handling.md
- wiki/gaps/smart-disputes.md
- wiki/gaps/dispute-reason-codes.md

### Articles updated
- None

### Gap stubs created
- wiki/gaps/smart-disputes.md (mentioned as automation tool but not explained)
- wiki/gaps/dispute-reason-codes.md (referenced for evidence guidelines but not detailed)

### Cross-links added
- disputes → chargebacks (synonym relationship)
- disputes → chargeback-representment (related process)
- disputes → dispute-evidence-submission (required process)
- disputes → chargeback-thresholds (consequence relationship)
- stripe-dispute-handling → disputes (specific implementation)
- smart-disputes → stripe-dispute-handling (part of system)

### Reasoning log
- Applied synonym rule: "disputes" and "chargebacks" refer to same concept, linked appropriately
- Created separate Stripe network article for platform-specific dispute handling features
- Gap stubs created for Smart Disputes and dispute reason codes - mentioned but need dedicated sources for full coverage
- Cross-network comparison noted in disputes article - all networks support disputes with different structures
- Applied cross-linking rules for dispute-related processes and evidence submission

### Contradictions found
- None in this compile pass.

### Incomplete information handled
- Cross-network dispute differences noted but specific network comparison details need additional sources
- Smart Disputes automation features mentioned but implementation details require dedicated source material
