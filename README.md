#  Dynamic Pricing Model for E-commerce

A real-time AI-powered pricing system that suggests the **most profitable price** for your product based on:
- Inventory levels
- Demand forecasting
- Competitor prices (via SerpAPI or Flipkart)

Whether you're an e-commerce seller, inventory manager, or just exploring AI in pricing strategies, this tool helps you make **smart, data-driven pricing decisions** — instantly.

---

## Problem Statement

In highly competitive online marketplaces, pricing your product too low reduces profit, and pricing too high risks losing customers. A smart pricing engine should:
- Understand market competition
- Consider your stock level
- Predict customer demand

### Solution

This project uses **machine learning + real-time web scraping + time series forecasting** to recommend the optimal price for any product you sell.

---

## How It Works

1. **User inputs:**
   - Product name (e.g., "laptop bag")
   - Current inventory level

2. **Competitor Price Fetching:**
   - Scrapes live prices using [SerpAPI](https://serpapi.com/) (Google/Amazon/Flipkart)
   - Fallback: Flipkart scraping using BeautifulSoup
   - Backup: mock price if both fail

3. **Demand Forecasting:**
   - Uses **Prophet** (a time series forecasting library by Meta)
   - Simulates historical sales and predicts future demand for the product

4. **Dynamic Price Prediction:**
   - A **trained regression model** takes competitor price, inventory, and demand as input
   - Outputs the **best possible selling price**

---

## Features

-  Real-time competitor price scraping
-  Smart price prediction based on inventory & demand
-  Interactive Streamlit UI
-  Demand forecasting using Prophet
-  Fallback logic: SerpAPI → Flipkart → Mock
-  Modular, extendable architecture

---

## 🖥 Demo Preview

> `Input`: Product = **wireless mouse**, Inventory = **40 units**  
> `Suggested Price`: ₹**749** *(based on demand + stock + competition)*

![Screenshot of Streamlit App](https://yourdomain.com/preview_dynamic_pricing.png)

---

## 📁 Project Structure

