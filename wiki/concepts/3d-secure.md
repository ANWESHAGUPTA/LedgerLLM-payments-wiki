---
title: 3D Secure
category: concept
network: all
related: [[strong-customer-authentication]], [[psd2]], [[visa-secure]], [[mastercard-identity-check]], [[amex-safekey]], [[stripe-3ds-integration]], [[fraud-detection]]
sources: ["raw/3d-secure.md"]
last_compiled: 2026-04-16
confidence: high
---

# 3D Secure

## Summary
3D Secure (3DS) is an authentication protocol that adds an additional security layer to card transactions by verifying that the person making a purchase is the legitimate cardholder. It helps protect both businesses and customers from fraudulent activity through familiar security prompts like passwords, one-time codes, or biometric verification.

## Details
When 3DS is activated, the issuing bank may request cardholders to authenticate during checkout. This authentication typically appears as:
- Password entry
- One-time code sent to mobile device
- Biometric verification (fingerprint, face recognition)

Customers recognize this process through card network branding:
- [[visa-secure]] (Visa's implementation)
- [[mastercard-identity-check]] (Mastercard's implementation) 
- [[amex-safekey]] (American Express's implementation)

3DS is optional in most regions but can be used as a tool to reduce [[fraud-detection]]. However, it may impact conversion rates due to additional friction in the checkout process.

## Compliance notes
The [[strong-customer-authentication]] (SCA) regulation, as part of [[psd2]] in the EEA and similar regulations in the UK, India, Japan, and Australia, may require using 3DS for card payments. Effective dates and specific requirements vary by jurisdiction.

## Technical reference
3D Secure operates as a three-domain model:
1. Acquirer Domain (merchant)
2. Issuer Domain (cardholder's bank)
3. Interoperability Domain (card network)

The protocol enables secure authentication data exchange between these domains during transaction processing.

## Cross-network comparison
All major card networks support 3DS but brand it differently:
- **Visa**: [[visa-secure]]
- **Mastercard**: [[mastercard-identity-check]]
- **American Express**: [[amex-safekey]]

Implementation details and merchant integration requirements may vary across networks.

## Related
- [[strong-customer-authentication]]
- [[psd2]]
- [[visa-secure]]
- [[mastercard-identity-check]]
- [[amex-safekey]]
- [[stripe-3ds-integration]]
- [[fraud-detection]]

## Sources
- raw/3d-secure.md