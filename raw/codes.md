---
source: https://docs.stripe.com/declines/codes
title: Stripe decline codes | Stripe Documentation
type: reference
domain: payments
ingested: 2026-04-15
tags: []
---

# Stripe decline codes | Stripe Documentation

# Stripe decline codes

## Learn about Stripe decline codes and how to resolve them when a charge fails.

Stripe uses its own decline codes that cover many of the same potential reasons asissuer decline codes. Our decline codes expand on issuer decline codes by going into more detail about the specific reason for the decline. In addition to a decline code, an error can contain anadvice_codewith suggested next steps.

#### Other API errors

SomeAPI errorsinclude acodeattribute to help youresolve them.

## Card decline codes

These are the Stripe decline codes that are used for card payments:

Decline codeDescriptionNext steps

Decline code

Description

Next steps

authentication_requiredThe card was declined because the transaction requires authentication such as3D Secure.When using Stripe’s front ends, in most cases a soft decline from an issuer triggers an authentication flow, allowing the customer to try again and authenticate their card. In some cases, such asoff-session payments, you might need to request the customer to retry. If the card issuer returns thisdecline codedespite a successfully authenticated transaction, the customer needs to contact their card issuer for more information.

authentication_required

The card was declined because the transaction requires authentication such as3D Secure.

When using Stripe’s front ends, in most cases a soft decline from an issuer triggers an authentication flow, allowing the customer to try again and authenticate their card. In some cases, such asoff-session payments, you might need to request the customer to retry. If the card issuer returns thisdecline codedespite a successfully authenticated transaction, the customer needs to contact their card issuer for more information.

authentication_not_handledRelated toauthentication_required. You tried to proceed without performing the required authentication, so the issuer declined again.Run the EMV 3D Secure (3DS) or strong customer authentication (SCA) flow. For off-session payments, collect and prepare authentication on-session first, then fall back to on-session if needed.

authentication_not_handled

Related toauthentication_required. You tried to proceed without performing the required authentication, so the issuer declined again.

Run the EMV 3D Secure (3DS) or strong customer authentication (SCA) flow. For off-session payments, collect and prepare authentication on-session first, then fall back to on-session if needed.

approve_with_idThe payment can’t be authorised.Attempt the payment again. If you still can’t process it, the customer needs to contact their card issuer.

approve_with_id

The payment can’t be authorised.

Attempt the payment again. If you still can’t process it, the customer needs to contact their card issuer.

call_issuerThe card was declined for an unknown reason.The customer needs to contact their card issuer for more information.

call_issuer

The card was declined for an unknown reason.

The customer needs to contact their card issuer for more information.

card_not_supportedThe card doesn’t support this type of purchase.The customer needs to contact their card issuer to make sure their card can be used to make this type of purchase.

card_not_supported

The card doesn’t support this type of purchase.

The customer needs to contact their card issuer to make sure their card can be used to make this type of purchase.

card_velocity_exceededThe customer has exceeded the balance, credit limit, or transaction amount limit available on their card.The customer needs to contact their card issuer for more information.

card_velocity_exceeded

The customer has exceeded the balance, credit limit, or transaction amount limit available on their card.

The customer needs to contact their card issuer for more information.

currency_not_supportedThe card doesn’t support the specified currency.The customer needs to check with the issuer whether the card can be used for the type of currency specified.

currency_not_supported

The card doesn’t support the specified currency.

The customer needs to check with the issuer whether the card can be used for the type of currency specified.

do_not_honorThe card was declined for an unknown reason.The customer needs to contact their card issuer for more information.

do_not_honor

The card was declined for an unknown reason.

The customer needs to contact their card issuer for more information.

deprecateddo_not_try_againThe card was declined for an unknown reason.The customer needs to contact their card issuer for more information.

deprecateddo_not_try_again

The card was declined for an unknown reason.

The customer needs to contact their card issuer for more information.

duplicate_transactionA transaction with identical amount and credit card information was submitted very recently.Check to see if a recent payment already exists.

duplicate_transaction

A transaction with identical amount and credit card information was submitted very recently.

Check to see if a recent payment already exists.

expired_cardThe card has expired.The customer needs to use another card.

expired_card

The card has expired.

The customer needs to use another card.

fraudulentThe payment was declined because Stripe suspects that it’s fraudulent.Don’t report more detailed information to your customer. Instead, present it in the same manner asgeneric_declinebelow.

fraudulent

The payment was declined because Stripe suspects that it’s fraudulent.

Don’t report more detailed information to your customer. Instead, present it in the same manner asgeneric_declinebelow.

generic_declineThe card was declined for an unknown reason or Stripe Radar or Adaptive Acceptanceblocked the payment.The customer needs to contact their card issuer for more information.

generic_decline

The card was declined for an unknown reason or Stripe Radar or Adaptive Acceptanceblocked the payment.

The customer needs to contact their card issuer for more information.

incorrect_addressThe address entered by the customer is incorrect.The customer needs to try again using the correct address.

incorrect_address

The address entered by the customer is incorrect.

The customer needs to try again using the correct address.

incorrect_cvcThe CVC number is incorrect.The customer needs to try again using the correct CVC.

incorrect_cvc

The CVC number is incorrect.

The customer needs to try again using the correct CVC.

incorrect_numberThe card number is incorrect.The customer needs to try again using the correct card number.

incorrect_number

The card number is incorrect.

The customer needs to try again using the correct card number.

incorrect_pinThe PIN entered is incorrect. This decline code only applies to payments made with a card reader.The customer needs to try again using the correct PIN.

incorrect_pin

The PIN entered is incorrect. This decline code only applies to payments made with a card reader.

The customer needs to try again using the correct PIN.

incorrect_zipThe postal code is incorrect.The customer needs to try again using the correct billing postal code.

incorrect_zip

The postal code is incorrect.

The customer needs to try again using the correct billing postal code.

insufficient_fundsThe card has insufficient funds to complete the purchase.The customer needs to use an alternative payment method.

insufficient_funds

The card has insufficient funds to complete the purchase.

The customer needs to use an alternative payment method.

invalid_accountThe card, or account the card is connected to, is invalid.The customer needs to contact their card issuer to check that the card is working correctly.

invalid_account

The card, or account the card is connected to, is invalid.

The customer needs to contact their card issuer to check that the card is working correctly.

invalid_amountThe payment amount is invalid, or exceeds the amount that’s allowed.If the amount appears to be correct, the customer needs to check with their card issuer that they can make purchases of that amount.

invalid_amount

The payment amount is invalid, or exceeds the amount that’s allowed.

If the amount appears to be correct, the customer needs to check with their card issuer that they can make purchases of that amount.

invalid_cvcThe CVC number is incorrect.The customer needs to try again using the correct CVC.

invalid_cvc

The CVC number is incorrect.

The customer needs to try again using the correct CVC.

invalid_expiry_monthThe expiry month is invalid.The customer needs to try again using the correct expiry date.

invalid_expiry_month

The expiry month is invalid.

The customer needs to try again using the correct expiry date.

invalid_expiry_yearThe expiry year is invalid.The customer needs try again using the correct expiry date.

invalid_expiry_year

The expiry year is invalid.

The customer needs try again using the correct expiry date.

invalid_numberThe card number is incorrect.The customer needs try again using the correct card number.

invalid_number

The card number is incorrect.

The customer needs try again using the correct card number.

invalid_pinThe PIN entered is incorrect.The customer needs to try again using the correct PIN.

invalid_pin

The PIN entered is incorrect.

The customer needs to try again using the correct PIN.

issuer_not_availableThe card issuer couldn’t be reached, so the payment couldn’t be authorised.Attempt the payment again. If you still can’t process it, the customer needs to contact their card issuer.

issuer_not_available

The card issuer couldn’t be reached, so the payment couldn’t be authorised.

Attempt the payment again. If you still can’t process it, the customer needs to contact their card issuer.

lost_cardThe payment was declined because the card has been reported as lost.The specific reason for the decline shouldn’t be reported to the customer. Instead, present it as ageneric_decline.

lost_card

The payment was declined because the card has been reported as lost.

The specific reason for the decline shouldn’t be reported to the customer. Instead, present it as ageneric_decline.

merchant_blacklistThe payment was declined because it matches a value on the Stripe user’s block list.Don’t report more detailed information to your customer. Instead, present it in the same manner asgeneric_declinebelow.

merchant_blacklist

The payment was declined because it matches a value on the Stripe user’s block list.

Don’t report more detailed information to your customer. Instead, present it in the same manner asgeneric_declinebelow.

new_account_information_availableThe card, or account the card is connected to, is invalid.The customer needs to contact their card issuer for more information.

new_account_information_available

The card, or account the card is connected to, is invalid.

The customer needs to contact their card issuer for more information.

no_action_takenThe card was declined for an unknown reason.The customer needs to contact their card issuer for more information.

no_action_taken

The card was declined for an unknown reason.

The customer needs to contact their card issuer for more information.

not_permittedThe payment isn’t permitted.The customer needs to contact their card issuer for more information.

not_permitted

The payment isn’t permitted.

The customer needs to contact their card issuer for more information.

offline_pin_requiredThe card was declined because it requires a PIN.The customer needs to try again by inserting their card and entering a PIN.

offline_pin_required

The card was declined because it requires a PIN.

The customer needs to try again by inserting their card and entering a PIN.

online_or_offline_pin_requiredThe card was declined because it requires a PIN.If the card reader supports Online PIN, prompt the customer for a PIN without creating a new transaction. If the card reader doesn’t support Online PIN, the customer needs to try again by inserting their card and entering a PIN.

online_or_offline_pin_required

The card was declined because it requires a PIN.

If the card reader supports Online PIN, prompt the customer for a PIN without creating a new transaction. If the card reader doesn’t support Online PIN, the customer needs to try again by inserting their card and entering a PIN.

pickup_cardThe customer can’t use this card to make this payment (it’s possible it was reported lost or stolen).They need to contact their card issuer for more information.

pickup_card

The customer can’t use this card to make this payment (it’s possible it was reported lost or stolen).

They need to contact their card issuer for more information.

pin_try_exceededThe allowable number of PIN tries was exceeded.The customer must use another card or method of payment.

pin_try_exceeded

The allowable number of PIN tries was exceeded.

The customer must use another card or method of payment.

processing_errorAn error occurred while processing the card.The payment needs to be attempted again. If it still can’t be processed, try again later.

processing_error

An error occurred while processing the card.

The payment needs to be attempted again. If it still can’t be processed, try again later.

reenter_transactionThe payment couldn’t be processed by the issuer for an unknown reason.The payment needs to be attempted again. If it still can’t be processed, the customer needs to contact their card issuer.

reenter_transaction

The payment couldn’t be processed by the issuer for an unknown reason.

The payment needs to be attempted again. If it still can’t be processed, the customer needs to contact their card issuer.

restricted_cardThe customer can’t use this card to make this payment (it’s possible it was reported lost or stolen).The customer needs to contact their card issuer for more information.

restricted_card

The customer can’t use this card to make this payment (it’s possible it was reported lost or stolen).

The customer needs to contact their card issuer for more information.

revocation_of_all_authorizationsThe card was declined for an unknown reason.The customer needs to contact their card issuer for more information.

revocation_of_all_authorizations

The card was declined for an unknown reason.

The customer needs to contact their card issuer for more information.

revocation_of_authorizationThe card was declined for an unknown reason.The customer needs to contact their card issuer for more information.

revocation_of_authorization

The card was declined for an unknown reason.

The customer needs to contact their card issuer for more information.

security_violationThe card was declined for an unknown reason.The customer needs to contact their card issuer for more information.

security_violation

The card was declined for an unknown reason.

The customer needs to contact their card issuer for more information.

service_not_allowedThe card was declined for an unknown reason.The customer needs to contact their card issuer for more information.

service_not_allowed

The card was declined for an unknown reason.

The customer needs to contact their card issuer for more information.

stolen_cardThe payment was declined because the card is reported stolen.Don’t report more detailed information to your customer. Instead, present it in the same manner asgeneric_declinebelow.

stolen_card

The payment was declined because the card is reported stolen.

Don’t report more detailed information to your customer. Instead, present it in the same manner asgeneric_declinebelow.

stop_payment_orderThe card was declined for an unknown reason.The customer needs to contact their card issuer for more information.

stop_payment_order

The card was declined for an unknown reason.

The customer needs to contact their card issuer for more information.

testmode_declineA Stripe test card number was used.A genuine card must be used to make a payment.

testmode_decline

A Stripe test card number was used.

A genuine card must be used to make a payment.

transaction_not_allowedThe card was declined for an unknown reason.The customer needs to contact their card issuer for more information.

transaction_not_allowed

The card was declined for an unknown reason.

The customer needs to contact their card issuer for more information.

deprecatedtry_again_laterThe card was declined for an unknown reason.Ask the customer to attempt the payment again. If subsequent payments are declined, the customer needs to contact their card issuer for more information.

deprecatedtry_again_later

The card was declined for an unknown reason.

Ask the customer to attempt the payment again. If subsequent payments are declined, the customer needs to contact their card issuer for more information.

withdrawal_count_limit_exceededThe customer has exceeded the balance or credit limit available on their card.The customer needs to use an alternative payment method.

withdrawal_count_limit_exceeded

The customer has exceeded the balance or credit limit available on their card.

The customer needs to use an alternative payment method.

mobile_device_authentication_requiredThe card was declined because the transaction requires authentication.Retry attempts by tapping your mobile device again.

mobile_device_authentication_required

The card was declined because the transaction requires authentication.

Retry attempts by tapping your mobile device again.

## Local payment method decline codes

The following Stripe decline codes can be used for Local Payment Method (LPM) payments:

Decline codeCharge outcome reasonSeller messageAPI error message

Decline code

Charge outcome reason

Seller message

API error message

partner_generic_declinepartner_generic_declineThe payment provider has declined the payment.The payment provider has declined the payment.

partner_generic_decline

partner_generic_decline

The payment provider has declined the payment.

The payment provider has declined the payment.

invalid_customer_accountinvalid_customer_accountWe can’t charge the customer’s account.We can’t charge the customer’s account. Retry attempts might succeed after the customer takes action to resolve the issue with their account.

invalid_customer_account

invalid_customer_account

We can’t charge the customer’s account.

We can’t charge the customer’s account. Retry attempts might succeed after the customer takes action to resolve the issue with their account.

payment_limit_exceededpayment_limit_exceededThe order exceeds a limit on the customer’s account.The order exceeds a limit on the customer’s account. Retry attempts might succeed after the customer takes action to resolve the issue with their account.

payment_limit_exceeded

payment_limit_exceeded

The order exceeds a limit on the customer’s account.

The order exceeds a limit on the customer’s account. Retry attempts might succeed after the customer takes action to resolve the issue with their account.

invalid_billing_agreementinvalid_billing_agreementThe customer’s billing agreement is invalid.The customer’s payment method is invalid due to an invalid billing agreement. Retries won’t succeed.

invalid_billing_agreement

invalid_billing_agreement

The customer’s billing agreement is invalid.

The customer’s payment method is invalid due to an invalid billing agreement. Retries won’t succeed.

expired_cardpartner_expired_cardThe card registered with the payment provider has expired.The card registered with the payment provider has expired. Retry attempts might succeed after the customer takes action to resolve the issue with their account.

expired_card

partner_expired_card

The card registered with the payment provider has expired.

The card registered with the payment provider has expired. Retry attempts might succeed after the customer takes action to resolve the issue with their account.

processing_errorpartner_processing_errorThe payment provider encountered a processing error.The payment provider encountered a processing error.

processing_error

partner_processing_error

The payment provider encountered a processing error.

The payment provider encountered a processing error.

insufficient_fundspartner_insufficient_fundsThe customer has insufficient funds with the payment provider.The customer has insufficient funds with the payment provider. Retry attempts might succeed after the customer takes action to resolve the issue with their account.

insufficient_funds

partner_insufficient_funds

The customer has insufficient funds with the payment provider.

The customer has insufficient funds with the payment provider. Retry attempts might succeed after the customer takes action to resolve the issue with their account.

currency_not_supportedpartner_invalid_currencyThe payment provider doesn’t support this currency.The payment provider doesn’t support this currency. Retries won’t succeed.

currency_not_supported

partner_invalid_currency

The payment provider doesn’t support this currency.

The payment provider doesn’t support this currency. Retries won’t succeed.

invalid_amountpartner_invalid_amountThe payment provider doesn’t allow the amount.The payment provider doesn’t allow the amount. Retries won’t succeed.

invalid_amount

partner_invalid_amount

The payment provider doesn’t allow the amount.

The payment provider doesn’t allow the amount. Retries won’t succeed.

invalid_business_accountinvalid_business_accountThe business account is deactivated.The business account you’re trying to use for processing a payment or issuing a refund is deactivated and incapable of sending or receiving funds. If the account is reactivated, retry attempts might succeed.

invalid_business_account

invalid_business_account

The business account is deactivated.

The business account you’re trying to use for processing a payment or issuing a refund is deactivated and incapable of sending or receiving funds. If the account is reactivated, retry attempts might succeed.

partner_high_risk_customerpartner_high_risk_customerThe payment provider labelled this customer as high risk.The payment provider labelled this customer as high risk.

partner_high_risk_customer

partner_high_risk_customer

The payment provider labelled this customer as high risk.

The payment provider labelled this customer as high risk.

compliance_violationcompliance_violationThe payment violates terms of service, programme rules, or applicable laws.The payment violates terms of service, programme rules or applicable laws. Retries won’t succeed.

compliance_violation

compliance_violation

The payment violates terms of service, programme rules, or applicable laws.

The payment violates terms of service, programme rules or applicable laws. Retries won’t succeed.

payment_disputedpayment_disputedThere’s a dispute over the payment.There’s a dispute over the payment. If the dispute resolves in favour of the business, retry attempts might succeed.

payment_disputed

payment_disputed

There’s a dispute over the payment.

There’s a dispute over the payment. If the dispute resolves in favour of the business, retry attempts might succeed.

invalid_authorizationinvalid_authorizationThe authorisation is invalid or has been revoked.The payment didn’t receive authorisation or has revoked its authorisation. Retries won’t succeed.

invalid_authorization

invalid_authorization

The authorisation is invalid or has been revoked.

The payment didn’t receive authorisation or has revoked its authorisation. Retries won’t succeed.

invalid_payment_informationinvalid_payment_informationThe payment has invalid information.The payment has invalid information. Retries won’t succeed.

invalid_payment_information

invalid_payment_information

The payment has invalid information.

The payment has invalid information. Retries won’t succeed.

partner_payment_not_foundpartner_payment_not_foundThe payment provider can’t find this payment.The payment provider can’t find this payment.

partner_payment_not_found

partner_payment_not_found

The payment provider can’t find this payment.

The payment provider can’t find this payment.

expired_payment_informationexpired_payment_informationThe underlying payment instrument is expired.The payment has expired information. Retries may succeed after the customer updates their payment information.

expired_payment_information

expired_payment_information

The underlying payment instrument is expired.

The payment has expired information. Retries may succeed after the customer updates their payment information.

duplicate_transactionpartner_duplicate_transactionA recent transaction with identical details was submitted recently.A recent transaction with identical details was submitted recently to the partner.

duplicate_transaction

partner_duplicate_transaction

A recent transaction with identical details was submitted recently.

A recent transaction with identical details was submitted recently to the partner.