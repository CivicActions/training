<!--
author: Bentley Hensel
email: bentley.hensel@civicactions.com
version: 2.0
language: en
narrator: US English Female
-->

# Company-Managed Laptop
    ## Pre-Order + Setup Training

We're excited to ship your company-managed laptop 🎉

Before we place your order, please complete the steps below.
This ensures accurate shipping, smooth enrollment, and a clean setup experience.

---

# Step 1: Complete the Company Managed Device Rollout Form (Required)

Please complete the rollout form:

👉 https://docs.google.com/forms/d/e/1FAIpQLSeFr-2WdNqumHbsj8jKtDdho5blSOQHZy3Qz637BJzvRSZFnw/viewform?usp=dialog

This form confirms:

- Your shipping address & phone number
- Signature availability for delivery
- Preferred delivery timing
- Alternate shipping notes (if needed)
- Tech stipend timing

After submitting the form, continue to the next step.


# Step 2: Prepare Your Google Password

You will log into your new laptop using:

> Your CivicActions Google email + password

Important:

- Password managers do **not** work on the macOS login screen
- You will type this password every time you unlock your device

If your password is long and difficult to type manually, consider updating it before your laptop arrives.

Recommended format:

- A memorable phrase
OR
- Four random words separated by symbols

Example:
`river-harbor-glass-map`

You can update your password anytime via your [Google Account page](https://myaccount.google.com/signinoptions/password).

---

# Step 3: Deployment Readiness Confirmation (Required)

Once you have:

- [ ] Submitted the rollout form
- [ ] Reviewed this training

Go to [**#it-laptops-wave-2**](https://civicactions.slack.com/archives/C0A72LVNVNZ) in Slack and post this message:

> I am ready to deploy my laptop and have completed the Company Managed Device Rollout form and required training.

After posting:

1. Click the **three dots (...)** on your message
2. Click Connect to Apps >> **Raise a Request**
2. Select **Create ticket**
3. Submit the ticket

This creates your official deployment ticket and signals IT to begin ordering your device.

---

## Quick Check

What triggers your laptop order?

[( ) Completing the training only
 ( ) Submitting the form only
 (x) Posting in Slack and creating a ticket from that message
 ( ) Emailing IT ]

---

# What Happens Next

After your ticket is created:

- IT reviews your form submission
- Your device is ordered
- Your Slack thread will be updated with shipping & tracking information

> If any issues arise with your delivery, please discuss them on this slack thread/ticket.


---

# When Your Laptop Arrives

Please do not power it on immediately.

    ### First:

- Unpack carefully
- Confirm charger + cable are included
- Please add the device serial number to the slack thread

> IT will let you know when it is safe to power on the device. **DO NOT POWER ON THE DEVICE UNTIL YOU HEAR FROM IT.**

---

## Packaging

The device packaging may vary. All devices should contain a laptop, charging cable, and charger. If any of those are missing, let IT know.

You do **not** need to keep the box.

### What should you do with packaging?

[( ) Store it indefinitely
 (x) Reuse or recycle it
 ( ) Ship it back
 ( ) Ship it to Henry with his gift cards ]

---

# Initial Setup (After IT Approval)

Once IT says it is safe to power on your device, you can begin the setup process. It should take around a half hour for the entire process.

---

## Power & Basics

1. Plug into wall power
![Plug](it/assets/new-device-plug.jpg)
2. Press the power button (top right)

During setup, select:

![Setup](it/assets/new-device-screen.jpg)

- Language
- Region
- **Set Up as New**
- Accessibility Options
- Connect to WiFi

> You can always access the docs about this process on [Confluence](https://civicactions.atlassian.net/wiki/x/AoCAHw)--no need to remember everything.

---

## Remote Management

During the setup process, you will see a Remote Management screen.

Once you see this screen, click Continue/Enroll and then log in with your CivicActions Google account.

Wait for Kandji to complete installation.

---

## Migration Assistant

On the Migration Assistant screen:

[( ) Restore from personal Mac
 (x) Click “Not Now” or "Setup as New Machine"
 ( ) Restore from Time Machine
 ( ) Use iCloud ]

**Do not migrate from a personal device or backup.**

---

## Account Setup

Log in using your CivicActions Google account.

If prompted:

- Confirm **Enable Now** for FileVault

If you are not prompted, Kandji may enable FileVault automatically.

---

# System Customization

After login:

- Set Accessibility options
- Skip iCloud setup for now, you can sign-in later if desired. iCloud is **NOT** approved for CivicActions' data.
- Set up Touch ID
- Choose appearance

---

## Applications

Wait for the setup processes to complete and apps to install. When on this screen, we recommend you move the mouse every few minutes to prevent the device from going to sleep. Once this step completes, additional processes will run in the background to finish setting up the device.

---

## Storage Rules

Use the Google Drive sync folder for:

- Documents
- Project files

Do NOT sync:

- Code repositories
- `.env` files
- Database backups

> See the [Data Security and Handling Policy](https://civicactions.atlassian.net/wiki/x/HgBVKg) for more information.

### Why shouldn't you sync Code repositories, .env files, or similar files to Google Drive?

[( ) It is slower
 (x) It can expose secrets
 ( ) It breaks Zoom
 ( ) It is not allowed by Sammy ]


---

## Kandji Self Service & Additional Apps

Use **Kandji Self Service** for a "one-click" install of approved tools. If an app is available here, IT handles the heavy lifting for updates.

* **Role-Specific Apps:** Find tools tailored to your department.
* **macOS Updates:** Install these via the Kandji menu bar icon (look for the red dot 🔴).
* **The 14-Day Rule:** Updates have a 14-day grace period. **If you don't update manually, Kandji will force the install—even in the middle of a meeting!**

![Kandji Update Notification](it/assets/new-device-kandji-update.png)

### The "App Support" Breakdown

Not every app on your machine is managed by IT. It is crucial to understand who is in the driver's seat for updates. While Security reviews all installed apps, **it remains your responsibility to keep non-Kandji apps updated and secure.**

![IT Security Reminder & App Ownership Breakdown](it/assets/it-app-ownership-infographic.png)

| App Source | Who Updates It? | IT Support Level |
| :--- | :--- | :--- |
| **Kandji / Pre-installed** | **Automatic (Kandji)** | Full Support |
| **CivicBrew (Homebrew)** | **You** (`brew upgrade`) | Community / Self-Help |
| **Direct Downloads** | **You** (Manual) | Security Review Only |

> **Note:** For direct installs (e.g., specific client-provided tools), limit these to only what is required.

### Knowledge Check: Ownership

Whose responsibility is it to keep "Direct Install" or Homebrew apps updated?

[( ) IT (via a magic background script)
 ( ) My Project Lead
 (x) Me (the user)
 ( ) Sammy the CivicActions Sea Otter ]

*******************************************************************************

**Scenario:** You downloaded a design tool directly from a vendor's website. A security patch is released. What is the correct move?

[( ) Ignore it; Kandji will catch it eventually.
 ( ) Delete the app and reinstall it next year.
 (x) Manually check for and install the update immediately.
 ( ) Open an IT ticket for them to update it for me. ]

*******************************************************************************

---


# Final Check

Before starting work, confirm:

- [ ] Slack + Zoom working
- [ ] You can unlock the machine
- [ ] YubiKey works when signing into Google Chrome


---

# Need Help?

Device or setup issue?
→ Reply in your laptop's IT ticket.

Shipping question?
→ Reply in your laptop's IT ticket.

Live help available?
→ IT Office Hours.

---

# Completion

Once:

- The rollout form is submitted
- Your Slack deployment ticket is created
- Your device is enrolled successfully

Your laptop is ready for use and you can begin customizing it to fit your needs. Once the laptop is operational, you can close the Laptop Deployment ticket.

