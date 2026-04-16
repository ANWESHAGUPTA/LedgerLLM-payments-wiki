---
source: https://docs.stripe.com/payments/payment-intents
title: The Payment Intents API | Stripe Documentation
type: reference
domain: payments
ingested: 2026-04-16
tags: []
---

# The Payment Intents API | Stripe Documentation

# The Payment Intents API

## Learn how to use the Payment Intents API for Stripe payments.

Use thePayment IntentsAPI to build an integration that can handle complex payment flows with a status that changes over thePaymentIntent’s lifecycle. It tracks a payment from creation through checkout, and triggers additional authentication steps when required.

Some advantages of using thePayment IntentsAPI include:

- Automatic authentication handling

- No double charges

- Noidempotency keyissues

- Support forStrong Customer Authentication(SCA) and similar regulatory changes

## A complete set of APIs

Use thePayment IntentsAPI together with theSetup IntentsandPayment MethodsAPIs. These APIs help you handle dynamic payments (for example, additional authentication like3D Secure) and prepare you for expansion to other countries while allowing you to support new regulations and regional payment methods.

Building an integration with the Payment Intents API involves two actions: creating andconfirminga PaymentIntent. Each PaymentIntent typically correlates with a single shopping cart or customer session in your application. The PaymentIntent encapsulates details about the transaction, such as the supported payment methods, the amount to collect, and the desired currency.

## Creating a PaymentIntent

To get started, see theaccept a payment guide. It describes how to create a PaymentIntent on the server and pass itsclient secretto the client instead of passing the entire PaymentIntent object.

When youcreate the PaymentIntent, you can specify options like the amount and currency:

### Best practices

- We recommend creating a PaymentIntent as soon as you know the amount, such as when the customer begins the checkout process, to help track yourpurchase funnel. If the amount changes, you canupdateitsamount. For example, if your customer backs out of the checkout process and adds new items to their cart, you might need to update the amount when they start the checkout process again.

We recommend creating a PaymentIntent as soon as you know the amount, such as when the customer begins the checkout process, to help track yourpurchase funnel. If the amount changes, you canupdateitsamount. For example, if your customer backs out of the checkout process and adds new items to their cart, you might need to update the amount when they start the checkout process again.

- If the checkout process is interrupted and resumes later, attempt to reuse the same PaymentIntent instead of creating a new one. Each PaymentIntent has a unique ID that you can use toretrieveit if you need it again. In the data model of your application, you can store the ID of the PaymentIntent on the customer’s shopping cart or session to facilitate retrieval. The benefit of reusing the PaymentIntent is that theobject statehelps track any failed payment attempts for a given cart or session.

If the checkout process is interrupted and resumes later, attempt to reuse the same PaymentIntent instead of creating a new one. Each PaymentIntent has a unique ID that you can use toretrieveit if you need it again. In the data model of your application, you can store the ID of the PaymentIntent on the customer’s shopping cart or session to facilitate retrieval. The benefit of reusing the PaymentIntent is that theobject statehelps track any failed payment attempts for a given cart or session.

- Remember to provide anidempotency keyto prevent the creation of duplicate PaymentIntents for the same purchase. This key is typically based on the ID that you associate with the cart or customer session in your application.

Remember to provide anidempotency keyto prevent the creation of duplicate PaymentIntents for the same purchase. This key is typically based on the ID that you associate with the cart or customer session in your application.

## Passing the client secret to the client side

The PaymentIntent contains aclient secret, a key that’s unique to the individual PaymentIntent. On the client side of your application, Stripe.js uses the client secret as a parameter when invoking functions (such asstripe.confirmCardPaymentorstripe.handleCardAction) to complete the payment.

### Retrieve the client secret

ThePaymentIntentincludes aclient secretthat the client side uses to securely complete the payment process. You can use different approaches to pass the client secret to the client side.

Retrieve the client secret from an endpoint on your server, using the browser’sfetchfunction. This approach is best if your client side is a single-page application, particularly one built with a modern front-end framework such as React. Create the server endpoint that serves the client secret:

And then fetch the client secret with JavaScript on the client side:

#### Caution

You can use the client secret to complete the payment process with the amount specified on the PaymentIntent. Don’t log it, embed it in URLs, or expose it to anyone other than the customer. Make sure that you haveTLSon any page that includes the client secret.

## After the payment

After the client confirms the payment, it’s a best practice for your server tomonitor webhooksto detect when the payment successfully completes or fails.

APaymentIntentmight have more than oneChargeobject associated with it if there were multiple payment attempts. For example, retries can create multipleCharges. For each charge you can inspect theoutcomeanddetails of the payment methodused.

## Optimising payment methods for future payments

Thesetup_future_usageparameter saves payment methods to use again in the future. For cards, it also optimises authorisation rates in compliance with regional legislation and network rules, such asSCA. To determine which value to use, consider how you want to use this payment method in the future.

How you intend to use the payment methodsetup_future_usage enum value to use

How you intend to use the payment method

setup_future_usage enum value to use

On-sessionpayments onlyon_session

On-sessionpayments only

on_session

Off-sessionpayments onlyoff_session

Off-sessionpayments only

off_session

Both on and off-session paymentsoff_session

Both on and off-session payments

off_session

You can still acceptoff-sessionpayments with a card set up for on-session payments, but the bank is more likely to reject the off-session payment and require authentication from the cardholder.

The following example shows how to create a PaymentIntent and specifysetup_future_usage:

#### Caution

Setups for off-session payments are more likely to incur additional friction. Useon-sessionsetup if you don’t intend to accept off-session payments with the saved card.

## Dynamic statement descriptor

By default, your Stripe account’sstatement descriptorappears on customer statements whenever you charge their card. To provide a different description on a per-payment basis, use thestatement_descriptorparameter.

#### Note

Use thestatement_descriptorparameter for non-card charges andstatement_descriptor_suffixfor card charges.

Statement descriptorsare limited to 22 characters, can’t use the special characters<,>,',", or*, and must not consist solely of numbers. When using dynamic statement descriptors, the dynamic text is appended to thestatement descriptor prefixset in the Stripe Dashboard. An asterisk (*) and an empty space are also added to separate the default statement descriptor from the dynamic portion. These 2 characters count towards the 22 character limit.

## Storing information in metadata

Stripe supports addingmetadatato the most common requests you make, such as processing payments. Metadata isn’t shown to customers or factored into whether a payment is declined or blocked by our fraud prevention system.

Through metadata, you can associate information that’s meaningful to you with Stripe activity.

Any metadata you include is viewable in the Dashboard (for example, when looking at the page for an individual payment), and is also available in common reports. As an example, you can attach the order ID for your store to the PaymentIntent for that order. Doing so allows you to easily reconcile payments in Stripe to orders in your system.

If you’re usingRadar for Fraud Teams, consider passing additional customer information and order information as metadata. Then you can writeRadar rules using metadata attributesand have more information available within the Dashboard, which can expedite your review process.

When a PaymentIntent creates a charge, the PaymentIntent copies its metadata to the charge. Subsequent updates to the PaymentIntent’s metadata won’t modify the metadata of charges previously created by the PaymentIntent.

#### Caution

Don’t store any sensitive information (personally identifiable information, card details, and so on) as metadata or in thedescriptionparameter of the PaymentIntent.

## See also

- Accept a payment online

- Accept a payment in an iOS app

- Accept a payment in an Android app

- Set up future payments