---
title: 3D Secure
category: concept
network: all
related: [[strong-customer-authentication]], [[psd2]], [[visa-secure]], [[mastercard-identity-check]], [[amex-safekey]]
sources: [3d-secure.md]
last_compiled: 2026-04-12
confidence: high
---

# 3D Secure

## Summary
3D Secure (3DS) is an authentication protocol that adds an extra security layer to online card payments by verifying the cardholder's identity before completing the transaction. It helps reduce fraud and is required by regulations like Strong Customer Authentication (SCA) in many regions.

## Details
When 3DS is activated, the card issuer may prompt the customer to authenticate themselves during checkout through:
- Password entry
- One-time code sent to their mobile device
- Biometric verification (fingerprint, face recognition)

Customers typically recognize this process through network-branded interfaces:
- **Visa**: Visa Secure
- **Mastercard**: Mastercard Identity Check  
- **American Express**: American Express SafeKey

3DS adds friction to the checkout process but provides significant fraud protection benefits. Modern implementations aim to balance security with user experience through risk-based authentication and exemptions.

## Compliance notes
**Required for SCA compliance** in:
- European Economic Area (EEA) under PSD2
- United Kingdom
- India
- Japan
- Australia

**Optional but recommended** in other regions as a fraud prevention tool.

Merchants in SCA-required regions must implement 3DS for most card-not-present transactions, with specific exemptions available for low-risk transactions.

## Technical reference
- **Protocol versions**: 3DS 1.0, 2.0, and 2.1+ (latest versions support app-based authentication)
- **Integration methods**: Direct API integration, hosted checkout, or third-party gateway processing
- **Data sharing**: 3DS 2.0+ shares additional transaction context to reduce authentication prompts
- **Exemption handling**: Supports SCA exemptions like low-value transactions, trusted beneficiaries, and transaction risk analysis

## Cross-network comparison
All major card networks support 3DS with their own branded experiences:
- **Visa**: Visa Secure (formerly Verified by Visa)
- **Mastercard**: Mastercard Identity Check (formerly Mastercard SecureCode)
- **American Express**: American Express SafeKey

The underlying technical protocol is standardized, but each network may have specific requirements for merchant enrollment and transaction processing.

## Related
- [[strong-customer-authentication]]
- [[psd2]]
- [[visa-secure]]
- [[mastercard-identity-check]]
- [[amex-safekey]]

## Sources
- 3d-secure.md