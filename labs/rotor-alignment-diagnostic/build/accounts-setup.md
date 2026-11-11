# Accounts setup · Rotor Alignment Diagnostic (Build step 2)

**For Brandon · 2026-11-11 · about 1.5 hours**
Three accounts, with the caps you approved. Menu names change often: if a button isn't where this says, look for the nearest match and tell Ines what you saw, so this guide gets fixed.

**One rule throughout: never paste a key into a chat, an email or the repo.** Each key goes straight into Google's locked key store (Secret Manager) in step 1d. That's the only place the app reads them from.

---

## 1. Google Cloud (about 40 min)

**a. Account and project**
1. Go to https://console.cloud.google.com and sign in with your Franklin Kinetics Google Workspace account (contact@franklinkinetics.com or your admin account).
2. Create a new project. Name it `rotor-diagnostic`.

**b. Billing, in Canadian dollars**
1. Open **Billing** and create a billing account. Choose **CAD** as the currency if asked. It can't be changed later.
2. Link the billing account to the `rotor-diagnostic` project.

**c. The CAD $10 budget alert**
1. In **Billing**, open **Budgets & alerts** and create a budget.
2. Scope: the `rotor-diagnostic` project. Amount: **$10 per month**.
3. Alerts at 50%, 90% and 100%, emailed to you.
   A budget alert warns you; it doesn't switch anything off. At this volume we expect $0.

**d. Turn on the key store**
1. Search the console for **Secret Manager** and enable it.
2. Leave it open. Steps 2 and 3 below each end by adding one secret here.

## 2. Anthropic API (about 20 min)

1. Go to https://console.anthropic.com and create an account for Franklin Kinetics Consulting Corp.
2. Add a payment method. If it asks you to buy credits up front, buy the smallest amount offered.
3. Find the **spending limit** (usually under settings, "Limits" or "Billing") and set it to **US$25 per month**.
4. Create an **API key**. Name it `rotor-diagnostic`.
5. Copy the key **once**, straight into Google Secret Manager: **Create secret**, name it `anthropic-api-key`, paste the key as the value, save. Then close the Anthropic page; you won't need the key again.

## 3. Squarespace Orders key (about 15 min)

1. In Squarespace, open **Settings** and look for **Developer Tools** or **Advanced**, then **Developer API Keys**.
2. Generate a key. Name it `rotor-diagnostic`.
3. Permissions: tick **Orders API: Read Only**. Nothing else.
4. Copy the key straight into Google Secret Manager: **Create secret**, name it `squarespace-orders-key`, paste, save.

## 4. Tell Ines when it's done

Reply with just "accounts done", plus anything that didn't match this guide. Don't send any key.

**What happens next:**
- **Step 3:** the real AI runs on the two invented companies and the trap blocks. Spend is about US$5–10, inside your US$25 cap.
- **Step 4:** the app goes online in Montréal. Before that, Ines brings you two small choices, so nothing changes without you:
  - how the crew gets permission to deploy into your Google Cloud project
  - how the app is allowed to send email from contact@franklinkinetics.com

Still to confirm before step 3: Juno checks Anthropic's current terms on data retention and training for API use.
