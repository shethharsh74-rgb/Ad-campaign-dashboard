# Ad Campaign Performance Dashboard

A **data-driven Streamlit dashboard** for analyzing digital advertising performance across channels, campaigns, and geographies. Built as a portfolio project to demonstrate data literacy and sales/marketing understanding.

> **Perfect for:** Sales leaders, account executives, customer success managers, and marketing professionals who need to track campaign performance, optimize spend, and communicate ROI to stakeholders.

---

## 🎯 Project Overview

This dashboard showcases the ability to:

- **Work with real-world advertising data** (impressions, clicks, conversions, spend, revenue)
- **Calculate key performance indicators** (CTR, CPC, CPA, ROAS, conversion rates)
- **Build interactive visualizations** that communicate insights to non-technical stakeholders
- **Filter and segment data** by date, channel, geography, and campaign
- **Extract actionable insights** for performance optimization and strategic decision-making

### Why This Matters for Sales/Ad Sales Roles

As an account executive, sales development rep, or customer success manager in ad tech or SaaS, you need to understand:

- **How to measure campaign success** — ROAS, conversion rates, and cost efficiency
- **How to communicate with marketing teams** — understand their metrics and constraints
- **How to talk to customers about ROI** — show them data, prove value, reduce churn
- **How to optimize budget allocation** — which channels and campaigns drive real revenue

This dashboard demonstrates all four competencies.

---

## 📊 Dataset Description

### Fields

| Field | Type | Description |
|-------|------|-------------|
| **date** | Date | Campaign date (YYYY-MM-DD) |
| **campaign_name** | String | Name of the ad campaign (e.g., "Q1 Brand Awareness - Meta") |
| **channel** | String | Ad platform (Meta, Google, Pinterest, LinkedIn, TikTok) |
| **country** | String | Geographic market (Canada, US) |
| **industry** | String | Target industry segment (Technology, Financial Services, Retail) |
| **impressions** | Integer | Total ad impressions served |
| **clicks** | Integer | Total clicks on ads |
| **cost** | Float | Total ad spend ($) |
| **conversions** | Integer | Total conversions (purchases, signups, leads) |
| **revenue** | Float | Revenue attributed to conversions ($) |
| **customer_id** | String | Unique customer/account identifier |
| **funnel_stage** | String | Position in customer journey (Awareness, Consideration, Conversion) |
| **objective** | String | Campaign objective (Awareness, Consideration, Conversion) |

### Calculated Metrics

The dashboard automatically calculates:

| Metric | Formula | Interpretation |
|--------|---------|-----------------|
| **CTR** (Click-Through Rate) | (Clicks / Impressions) × 100 | Ad relevance; higher = better |
| **CPC** (Cost Per Click) | Cost / Clicks | Efficiency of driving traffic; lower = better |
| **CPA** (Cost Per Acquisition) | Cost / Conversions | Efficiency of driving conversions; lower = better |
| **Conversion Rate** | (Conversions / Clicks) × 100 | Quality of traffic; higher = better |
| **ROAS** (Return on Ad Spend) | Revenue / Cost | Revenue generated per dollar spent; 2.0x = breakeven + 100% profit |
| **ROI** | ((Revenue - Cost) / Cost) × 100 | Overall portfolio return |

### Sample Data Source

The `data/ad_sales_sample.csv` file contains **105 rows** of synthetic but realistic campaign data spanning **January - March 2024**, across 5 channels and 2 countries. The data is designed to reflect typical patterns:

- **Meta & TikTok:** High volume, lower conversion rates, good for awareness
- **Google Search:** High intent, higher conversion rates, higher CPA
- **LinkedIn:** B2B focus, strong for qualified leads, high ROAS
- **Pinterest:** Retail/lifestyle focus, good conversion rates

Use this to explore filtering, segmentation, and performance comparison.

---

## 🛠️ Tech Stack

| Technology | Purpose |
|-----------|---------|
| **Python 3.8+** | Core language |
| **Streamlit** | Interactive web dashboard framework |
| **Pandas** | Data manipulation and aggregation |
| **Plotly** | Interactive visualizations (charts) |
| **NumPy** | Numerical operations |

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- Git

### Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/shethharsh74-rgb/ad-campaign-dashboard.git
   cd ad-campaign-dashboard
   ```

2. **Create a virtual environment (optional but recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate    # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the dashboard:**
   ```bash
   streamlit run app.py
   ```

5. **Open in your browser:**
   - Streamlit will automatically open `http://localhost:8501`
   - If not, navigate there manually

---

## 📈 Dashboard Features

### KPI Cards (Top of Dashboard)

Displays key metrics at a glance:

- **Total Spend** — Sum of all ad costs in the filtered date range
- **Total Revenue** — Sum of all conversions × revenue per conversion
- **Total Conversions** — Number of conversions (customers acquired, leads generated)
- **Total Clicks** — Total click-throughs across all ads
- **Overall ROAS** — Return on ad spend (revenue ÷ cost)

### Sidebar Filters

Filter data interactively without code:

- **Date Range** — Select start and end date for analysis
- **Channels** — Multi-select: Meta, Google, Pinterest, LinkedIn, TikTok
- **Countries** — Multi-select: Canada, US (easily expandable)
- **Campaigns** — Multi-select: Choose specific campaigns to focus on

### Visualizations

1. **Spend vs. Revenue Over Time** (Line Chart)
   - See how spend and revenue track together
   - Identify trends, seasonal patterns, and anomalies

2. **ROAS by Channel** (Horizontal Bar Chart)
   - Compare efficiency across platforms
   - Identify best-performing channels for budget allocation

3. **Top 10 Campaigns by Revenue** (Horizontal Bar Chart)
   - Ranked by total revenue
   - Color-coded by ROAS for quick performance assessment
   - **Interview talking point:** "This shows which campaigns drive the most business value."

4. **CTR and Conversion Rate by Channel** (Grouped Bar Chart)
   - Compare traffic quality (CTR) vs. conversion quality (conversion rate)
   - Different channels have different strengths

5. **Cost Per Acquisition (CPA) by Channel** (Horizontal Bar Chart)
   - Show which channels are most cost-efficient for acquiring customers
   - Lower CPA = higher profitability per conversion

6. **Revenue by Country** (Bar Chart)
   - Geographic performance view
   - Easy to identify high-value markets

7. **Detailed Campaign Table**
   - Sortable, filterable table of all campaigns
   - All raw metrics visible for deep dives
   - **Export-friendly** for reports and stakeholder presentations

8. **Summary Statistics**
   - Efficiency Metrics: Avg CTR, Avg CPA, Avg Conversion Rate
   - Campaign Insights: Number of active campaigns, channels, countries
   - Portfolio Performance: Best campaign, best ROAS, overall ROI

---

## 💡 Example Use Cases (For Interviews)

### Use Case 1: "Why Should We Increase Budget in Meta?"

**Scenario:** Your manager asks why Meta is underperforming compared to Google.

**How to use the dashboard:**

1. Filter for the last 30 days
2. Navigate to "ROAS by Channel" chart
3. Compare Meta (e.g., 2.1x) vs. Google (e.g., 3.2x)
4. Go to "CTR and Conversion Rate by Channel"
5. Observe Meta has 3.5% CTR but 2% conversion rate; Google has 5% CTR but 3.8% conversion rate

**Talking Points:**
> "The data shows Google Search has a 3.2x ROAS vs. Meta's 2.1x, primarily due to higher conversion rates (3.8% vs. 2%). This suggests Google users have higher purchase intent. However, Meta's cost per acquisition is $12.50 vs. Google's $13.50—nearly identical. The real difference is volume: Meta reaches 5x more people. I'd recommend optimizing Meta's creative and targeting before pulling budget, or reallocating incrementally to Google Search."

### Use Case 2: "Where Should We Invest Next Quarter?"

**Scenario:** You have $50K additional budget for Q2.

**How to use the dashboard:**

1. Review the "Top 10 Campaigns by Revenue" chart
2. Check "Revenue by Country" to identify geographic opportunities
3. Look at "CPA by Channel" to find cost-efficient channels

**Talking Points:**
> "LinkedIn B2B campaigns show the highest ROAS (4.2x) and lowest CPA ($8), but they're running at only $4K/month spend. If we doubled budget there, we'd likely hit $18K-$20K monthly revenue at the same efficiency. TikTok is high-volume but lower ROAS (1.8x); I'd hold TikTok steady and shift $25K from Meta to LinkedIn, keeping $25K for new tests in emerging channels."

### Use Case 3: "Why Are Conversions Down 15% This Month?"

**Scenario:** Your customer success team flags a drop in conversions.

**How to use the dashboard:**

1. Set date filter to last month vs. this month
2. Check "Spend vs. Revenue" trend chart
3. Drill into "CPA by Channel" and "Conversion Rate by Channel"
4. Review the detailed campaign table for anomalies

**Talking Points:**
> "Conversions are down, but spend is actually up—which means conversion rate declined, not volume. The data shows conversion rates dropped across all channels this week (from 3% to 2.1% average). This isn't a channel issue; it's a creative issue. I recommend we pause underperforming ad sets, refresh creatives, and A/B test new messaging. Let's also check if there were any product or landing page changes that might explain lower conversion rates."

### Use Case 4: "Which Customers Are Most Profitable?"

**Scenario:** You're building an account management strategy.

**How to use the dashboard:**

1. Filter by industry segment (e.g., Technology vs. Financial Services)
2. Check "Revenue by Country" and campaign revenue
3. Review "ROAS by Campaign" to identify high-ROI accounts

**Talking Points:**
> "Customers in the Technology vertical show 30% higher ROAS (2.9x) compared to Retail (2.2x). LinkedIn campaigns targeting tech decision-makers deliver 4.1x ROAS vs. 1.9x for general awareness. I'd recommend increasing CSM touchpoints and retention efforts for tech clients—they're delivering 3x higher ROI. We should also probe why Retail campaigns underperform and either optimize them or redeploy budget to Tech."

---

## 🔧 How to Extend This Project

### Add More Data

1. Replace `data/ad_sales_sample.csv` with your own data (same schema)
2. Add additional campaigns, channels, or countries
3. Dashboard will automatically adapt to new data

### Add New Visualizations

Edit `app.py` to add:

- **Cohort analysis** — Track customer acquisition cohorts over time
- **Attribution modeling** — Multi-touch attribution across channels
- **Forecasting** — Predict next month's revenue based on trends
- **Anomaly detection** — Alert on unusual spikes or drops
- **A/B test results** — Compare campaign variants

### Connect Live Data

Replace the CSV load with:

```python
import gspread  # Google Sheets API
import requests  # Facebook Ads API

# Load from Google Sheets
gc = gspread.service_account(filename='credentials.json')
sheet = gc.open('Ad_Campaign_Data').sheet1
df = pd.DataFrame(sheet.get_all_records())

# Or pull from Meta Ads API
response = requests.get('https://graph.facebook.com/...')
```

### Deploy to the Cloud

Deploy your dashboard for free or low-cost:

- **Streamlit Cloud:** `streamlit run` → automatic deployment
- **Heroku:** $7-50/month for a production instance
- **AWS Elastic Beanstalk:** Pay-as-you-go pricing
- **Google Cloud Run:** Free tier available

---

## 📝 File Structure

```
ad-campaign-dashboard/
├── app.py                    # Main Streamlit app
├── requirements.txt          # Python dependencies
├── data/
│   └── ad_sales_sample.csv  # Sample dataset
└── README.md                # This file
```

---

## 🎓 Key Takeaways for Interviews

When discussing this project with recruiters or hiring managers, emphasize:

1. **Data Literacy**
   - "I calculated ROAS, CPA, and conversion rates from raw data to identify which channels drive profitability."

2. **Sales Mindset**
   - "The dashboard isn't just pretty charts—it answers real business questions: Where should we invest next? Why is performance declining?"

3. **Communication Skills**
   - "I built interactive filters so non-technical stakeholders (marketing, execs) can explore data without asking me."

4. **Technical Competency**
   - "Python, Pandas, and Plotly show I can build real tools. Streamlit means I can go from data to product in hours."

5. **Business Impact**
   - "This dashboard saves hours of manual reporting. A sales team could use it to optimize spend allocation and increase ROAS by 20-30%."

---

## 📧 Contact & Questions

For questions about this project or ad tech topics, feel free to reach out!

- GitHub: [@shethharsh74-rgb](https://github.com/shethharsh74-rgb)

---

## 📄 License

This project is open source and available under the MIT License. Feel free to fork, modify, and use for learning or portfolio purposes.

---

**Built with ❤️ for sales leaders and data-driven marketers.**
