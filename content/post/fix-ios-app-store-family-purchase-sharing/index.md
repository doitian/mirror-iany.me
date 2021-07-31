---
date: 2020-03-22T19:01:28+0800
tags:
- ios
title: Fix iOS App Store Family Purchase Sharing
---

I have created a family group using the Apple ID *A*, and the account *B* is a member. However, I can't download apps purchased by *A* in the device logged in by *B*. Today, I finally find out the cause. The Purchase Sharing setting in account *B* is incorrect, which is by accident set to share as *A* and I don't know why.

<!--more-->

To fix it, just ensure every family member has set to share purchase as themselves in the Purchase Sharing setting.

{{< image-card src="ensure-correct-purchase-sharing-settings-squashed.png" caption="Ensure Correct Purchase Sharing Settings in the Family Member Accounts" >}}

In case you don't know how to download the Family Shared Purchase:

{{< image-card src="download-ios-app-store-family-purchase-sharings-squashed.png" caption="Download Family Purchase Sharing" >}}
