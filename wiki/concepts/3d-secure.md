---
title: 3D Secure
category: concept
network: all
related: [[strong-customer-authentication]], [[visa-secure]], [[mastercard-identity-check]], [[amex-safekey]], [[psd2]], [[fraud-detection]], [[stripe-authentication-required]]
sources: ["3d-secure.md"]
last_compiled: 2026-04-16
confidence: high
---

# 3D Secure

## Summary
3D Secure (3DS) is an authentication protocol that adds an additional security layer to card transactions. By verifying that the person making a purchase is the legitimate cardholder, 3DS helps protect both businesses and customers from fraudulent activity.

## Details
When 3DS is activated, the issuing bank might request cardholders authenticate through familiar security prompts such as:
- Password entry
- One-time code sent to mobile device
- Biometric verification

Customers may recognize this process through card network branding such as:
- [[visa-secure]] (Visa)
- [[mastercard-identity-check]] (Mastercard)
- [[amex-safekey]] (American Express)

3DS serves dual purposes:
1. **Fraud reduction** - Available globally as an optional tool to reduce fraudulent transactions
2. **Regulatory compliance** - Required in certain regions for [[strong-customer-authentication]] compliance

## Compliance notes
The [[strong-customer-authentication]] (SCA) regulation, as part of [[psd2]] in the EEA and similar regulations in the UK, India, Japan, and Australia, might require using 3DS for card payments. Effective dates and specific requirements vary by jurisdiction.

3DS is optional in other regions but can still be implemented as a fraud prevention tool.

## Technical reference
When 3DS authentication is required but not completed, payments typically fail with decline codes such as [[stripe-authentication-required]].

Stripe provides several 3DS integration options:
- Standard 3DS integration in checkout flow
- SCA exemptions and Data Only to reduce friction
- 3DS authentication with third-party payment processing
- Processing payments when 3DS runs outside Stripe

## Cross-network comparison
All major card networks support 3DS but brand it differently:
- **Visa**: [[visa-secure]]
- **Mastercard**: [[mastercard-identity-check]]
- **American Express**: [[amex-safekey]]

Not covered in current sources: specific implementation differences between networks, authentication method preferences, or success rate variations.

## Related
- [[strong-customer-authentication]]
- [[visa-secure]]
- [[mastercard-identity-check]]
- [[amex-safekey]]
- [[psd2]]
- [[fraud-detection]]
- [[stripe-authentication-required]]

## Sources
- raw/3d-secure.md