---
source: https://docs.stripe.com/radar/reviews
title: Review card payments | Stripe Documentation
type: reference
domain: payments
ingested: 2026-04-16
tags: []
---

# Review card payments | Stripe Documentation

# Review card payments

## Use reviews to supplement automated systems with human expertise.

#### Note

StripeRadarin India doesn’t support manual review rules, the review queue, or API access to lists and reviews. For more information, seeIndia Data Storage Migration Resources.

While Stripe’s automated systems work to prevent fraud on your account, you can use reviews to provide an extra layer of fraud protection by giving card payments a manual inspection.

For example, you might want to review transactions that:

- Have anelevated riskof fraud according to Stripe’s fraud protection system

- Were made from outside your country

- Are greater than a certain amount

- Use an email address from an unusual domain

The review queue ofStripe Radar for Fraud Teamsallows you to examine unusual payments, without having to look at each payment individually. You can create a targeted list of payments to review with criteria that you specify, and review them in the Dashboard.

#### Note

Review rules apply only to card payments. For ACH and SEPA Direct Debit, we recommend you test your rules by drafting an allow or block rule and viewing the test results on theReview new rulepage to see how your rules might perform.

## Review payments

The Dashboardreview queueis a prioritised list of completed or to-be-captured payments that might need further investigation. You can review payments by:

- List view: Scan a list of reviews without seeing details about each payment.

- Detailed view: Review customisable payment context for a particular review item.

#### Note

Payments placed into review are typically already successfully processed, unless youcapture authorised payments later. You can approve a payment, refund it, or refund it and mark it as fraudulent.

### List view

The list view contains information to help you quickly get a sense for each payment’s possible risk of fraud.

The manual review queue in the Stripe Dashboard

The list view highlights:

- The risk level Stripe assigns after evaluating the payment

- Thecustomername

- Payment method information

- Customer information

- The amount, date, and time of the payment

- The client

### Detailed view

### Keyboard shortcuts

You can also use theJandKkeys to move between payments when viewing them in more detail.

Select the payment within the review queue to view its details page, which might containmetadatathat can help with your decision. You can navigate between payments to review using thePreviousandNextbuttons.

Stripe Radar’s AI model evaluates hundreds of risk factors when scoring a charge. Therisk insightssection on the payment page identifies some of the most relevant risk factors, along with some key data points that can help assess fraud on a payment. Therelated paymentssection shows other payments made to your business that use the same email address, IP address or card number as the payment you’re currently reviewing.

## Smart Refunds

Radar for Fraud Teamslets you use Smart Refunds to receive recommendations about payments to refund because we predict them to be high fraud risk. Smart Refunds uses Radar AI models to evaluate the likelihood of your transaction resulting in a fraudulent dispute. We base this likelihood on additional risk factors from other transactions that Stripe processes in the hours after your transaction completes. With Smart Refunds, Radar even extends fraud protection to after your payment has completed.

You can view Smart Refunds recommendations in theSmart Refundsquick filter in the Dashboard review queue. By default, you see recommendations that have a high or very high likelihood of turning into an early fraud warning or fraudulent dispute. You can view additional Smart Refunds recommendations by changing the Refund confidence level. The following table shows the expected chance of an early fraud warning or fraudulent dispute at each refund confidence level.

Refund confidence levelChance of early fraud warning or dispute

Refund confidence level

Chance of early fraud warning or dispute

Very high72%

Very high

72%

High60%

High

60%

Medium40%

Medium

40%

Low30%

Low

30%

Very low15%

Very low

15%

## Actions

After you review a completed payment, you can remove it from the review queue by taking one of the following actions:

- Approve: Closes the review with no changes made to the payment. You can still refund and, optionally, report fraud on an approved payment.

- If youcapture payments later, there is also aCapturebutton. You can capture a payment before or after approval.

- Refund: Refunds the payment without reporting it to Stripe as fraudulent. A completed refund is permanent, you can’t undo it – you must process a new payment. If you capture payments later, this button changes toCancel. You can read more aboutthis review process here.

- Refund and report fraud: Refunds the payment and also reports it to Stripe as fraudulent, for instance tosave dispute fees. This adds the associated card fingerprint and customer email address to yourblock listsand further increases the effectiveness of our fraud prevention.

#### Note

If a customerdisputesa payment that’s currently in your review queue, the review is automatically closed.

### Customise the review queue

WithStripe Radar for Fraud Teams, you can createrulesthat automatically place payments in review based on your unique business needs. This gives you the opportunity to identify payments that might require more investigation before you can make an informed decision.

## Review assignments

Anyone managing the review queue can assign themselves to reviews to avoid duplicating effort.

As a reviewer, you can see which reviews other people are working on and assign or remove yourself from reviews. You can also filter the review queue to see reviews you own or reviews that are currently unassigned.

#### Note

You can only change review assignments for yourself, not for other team members.

In the list view, use quick actions or the overflow menu to assign yourself to a review.

To assign yourself to a review in thelist view, hover over a review and click the person icon or theAssign to mebutton in the overflow menu (). In thedetail view, clickAssign to me.

You can take action on a review assigned to another team member or assign it to yourself. The review timeline shows a complete history of assignment changes and other actions.

The timeline in the detail view displays a history of assignment changes.

## Listen for review events

You can listen for webhook events related to review activity to trigger relevant response handling. Stripe sends the following review events:

- review.opened: Indicates that a transaction was added to the review queue, generating areviewobject.

- review.closed: Indicates that a review object closed and provides thereason.

## Best practices

Use the following best practices to get the most out of reviews and perform them efficiently.

- Focus time on payments where human judgment can add valuable insight to the decisionAutomated systems can make decisions on the majority of payments but human decision-making can significantly improve accuracy when identifying fraud in some cases. Because not every case benefits from human involvement, make sure you choose transactions where the benefit is clear.

Focus time on payments where human judgment can add valuable insight to the decision

Automated systems can make decisions on the majority of payments but human decision-making can significantly improve accuracy when identifying fraud in some cases. Because not every case benefits from human involvement, make sure you choose transactions where the benefit is clear.

- Use risk insights and related payments to make an informed decisionUse the data in therisk insightssection to see how Stripe Radar came up with a score for a charge. Combining the reasons for a score, knowledge about your business, and human judgement can help you make an informed choice about when to trust or ignore the score assigned by Radar.

Use risk insights and related payments to make an informed decision

Use the data in therisk insightssection to see how Stripe Radar came up with a score for a charge. Combining the reasons for a score, knowledge about your business, and human judgement can help you make an informed choice about when to trust or ignore the score assigned by Radar.

- Use the insights from reviewers to develop hypotheses for fraud prevention strategiesAs reviewers sort through your transactions, they develop intuitions for fraud prevention that you can translate into better rules. Collect insights from reviewers totest custom rules on your account.

Use the insights from reviewers to develop hypotheses for fraud prevention strategies

As reviewers sort through your transactions, they develop intuitions for fraud prevention that you can translate into better rules. Collect insights from reviewers totest custom rules on your account.

- Customize the process by presenting data unique to your business at review timePass along any additional customer or order information as metadata so that all relevant information is in the Dashboard at the time of review. Some examples of useful metadata include:More information about the order and its shipping informationGoogle Mapsand Street View links to the customer’s shipping address so the reviewer can see if the address might be a drop-shipping or freight-forwarding service

Customize the process by presenting data unique to your business at review time

Pass along any additional customer or order information as metadata so that all relevant information is in the Dashboard at the time of review. Some examples of useful metadata include:

- More information about the order and its shipping information

- Google Mapsand Street View links to the customer’s shipping address so the reviewer can see if the address might be a drop-shipping or freight-forwarding service

- Don’t slow down your customerA review implies some amount of time between order placement and delivery. If your business has an inherent delay of this type (for example, you’re shipping physical goods), taking the time to review a transaction doesn’t affect the customer’s delivery expectation. If you don’t have a built-in delay between orders andfulfillmentwith your business, adding a review process might slow down orders and create a bottleneck for good customers. Consider the impact on customers before you implement a review process.

Don’t slow down your customer

A review implies some amount of time between order placement and delivery. If your business has an inherent delay of this type (for example, you’re shipping physical goods), taking the time to review a transaction doesn’t affect the customer’s delivery expectation. If you don’t have a built-in delay between orders andfulfillmentwith your business, adding a review process might slow down orders and create a bottleneck for good customers. Consider the impact on customers before you implement a review process.

## See also

- Rules