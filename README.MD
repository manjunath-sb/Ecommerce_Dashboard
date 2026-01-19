# E-commerce Business Performance Dashboard (Power BI)

## Project Overview

This project focuses on analysing **sales performance, order fulfilment efficiency, and customer behaviour** for a fictional e-commerce business.  
The objective is to provide **stakeholder-ready insights** through a structured Power BI dashboard that supports **business and operational decision-making**.

The project mirrors real-world data analyst work in service companies, covering the full lifecycle from **raw data to insights**.

---

## Business Problem

E-commerce teams often struggle with fragmented reporting across sales, operations, and customer metrics.  
The business needed a **single, reliable dashboard** to answer questions such as:

- Are we growing month over month?
- How efficient is order delivery?
- Where are SLA breaches occurring?
- Are we retaining customers?
- Which products and categories drive revenue?

---

## Data Used

The project uses structured e-commerce data similar to production systems:

- **Orders** – order status, order date, delivery date, region  
- **Order Items** – product-level transactions and pricing  
- **Customers** – customer details and signup information  
- **Products** – category and sub-category hierarchy  
- **Date Table** – dedicated calendar table for time intelligence  

The data was synthetically generated to simulate realistic volume and variability.

---

## Data Cleaning & Preparation

Data preparation was performed entirely in **Power BI (Power Query)**:

- Standardised date formats and data types  
- Validated order status vs delivery date logic  
- Removed invalid quantity and pricing records  
- Created delivery duration and SLA breach indicators  
- Ensured referential integrity across tables  

Raw data was left untouched, following best practices.

---

## Data Modelling

A **star schema** was implemented for reliable analysis:

### Fact Tables
- Orders  
- Order Items  

### Dimension Tables
- Customers  
- Products  
- Date Table  

Relationships were defined with **single-direction filtering** to prevent ambiguity and incorrect aggregations.

---

## KPIs & Metrics

KPIs were implemented using **DAX measures** and grouped by business area.

### Sales KPIs
- Total Revenue  
- Total Orders  
- Average Order Value (AOV)  
- Month-on-Month Revenue Growth  

### Operations KPIs
- Delivered Orders  
- Delivery Success %  
- Delayed Orders  
- SLA Breach %  

### Customer KPIs
- Total Customers  
- New vs Returning Customers  
- Customer Retention %  

Customer type was derived based on actual ordering behaviour rather than relying on raw data fields.

---

## Dashboard Structure

The Power BI report contains **three focused pages**, each designed for a specific audience.

### 1. Executive Summary
- High-level KPIs
- Revenue trend over time
- Revenue by product category  

**Audience:** Leadership and management  

---

### 2. Operations Overview
- Order status distribution
- SLA breach monitoring
- Delay trends over time
- Regional delay analysis  

**Audience:** Operations and fulfilment teams  

---

### 3. Customer & Product Insights
- New vs returning customer mix
- Revenue by customer type
- Product sub-category contribution  

**Audience:** Business, product, and marketing teams  

---

## Time Intelligence

A dedicated **Date Table** was created and marked as the official date table to enable:

- Monthly aggregation  
- Month-on-Month growth calculations  
- Consistent time-based filtering across visuals  

All time analysis uses the Date Table instead of raw date fields.

---

## Key Insights (Sample)

- Revenue shows consistent month-on-month variation with identifiable peak periods  
- A small number of product categories contribute the majority of revenue  
- Returning customers generate higher revenue compared to new customers  
- Certain regions experience disproportionately higher SLA breaches  

---

## Assumptions

- SLA threshold assumed as **5 days** for delivery  
- Customer retention defined as customers with more than one order  
- Synthetic data used for demonstration purposes  

---

## Tools Used

- Power BI Desktop  
- Power Query  
- DAX  
- Python (only for data generation)  

---

## Outcome

This project demonstrates:

- End-to-end Power BI workflow  
- Strong data modelling fundamentals  
- KPI-driven business analysis  
- Stakeholder-focused dashboard design  

It closely reflects the type of analytics work performed in real-world e-commerce and service-based environments.
