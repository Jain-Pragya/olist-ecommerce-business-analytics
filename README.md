# E-Commerce Operations & Logistics Performance Analysis
**Role:** Data Analyst at a B2B Technology Company
**Dataset:** Brazilian E-Commerce Public Dataset by Olist (112k+ Transactions)

## Project Overview
This project evaluates fulfillment timelines, shipping charges, and customer review ratings across 95,000+ delivered orders to identify operational bottlenecks impacting customer churn and marketplace satisfaction.

## Key Insights
* **Delivery Delay Cliff:** On-time shipments average 4.21 / 5.0 stars, whereas delayed orders drop to 2.55 / 5.0 (47% of late orders receive 1 star).
* **21-Day Threshold:** Customer satisfaction drops sharply after 21 days in transit, reaching 2.23 stars for orders over 30 days.
* **Padded ETAs:** 92.2% of orders arrive an average of 11.4 days before the quoted delivery date, which can depress checkout conversion.
* **Freight Drag:** Lightweight goods (<500g) average a 42% freight-to-price ratio, causing purchase friction on low-cost items.

## Repository Contents
* `data_cleaning_and_analysis.ipynb` - End-to-end Python pipeline (cleaning, transformations, KPI calculations).
* `README.md` - Project architecture and methodology summary.

## Project Deliverables
* **Google Sheet:** [Paste your Google Sheet view link here]
* **Interactive Looker Studio Dashboard:** [Paste your Looker Studio link here]
* **Management Slide Deck:** [Paste your Google Slides link here]

## How to Reproduce
1. Clone this repository.
2. Download the Olist dataset from Kaggle.
3. Run `data_cleaning_and_analysis.ipynb` to clean data and generate the processed metrics.
