import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime, timedelta
import numpy as np

# Configure page
st.set_page_config(
    page_title="Ad Campaign Performance Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv('data/ad_sales_sample.csv')
    df['date'] = pd.to_datetime(df['date'])
    return df

df = load_data()

# Calculate metrics
def calculate_metrics(data):
    data['ctr'] = (data['clicks'] / data['impressions'] * 100).round(2)
    data['cpc'] = (data['cost'] / data['clicks']).round(2)
    data['cpa'] = (data['cost'] / data['conversions']).round(2)
    data['conversion_rate'] = (data['conversions'] / data['clicks'] * 100).round(2)
    data['roas'] = (data['revenue'] / data['cost']).round(2)
    data['revenue_per_impression'] = (data['revenue'] / data['impressions'] * 1000).round(2)
    return data

df = calculate_metrics(df)

# Sidebar filters
st.sidebar.header("🔍 Filters")

date_range = st.sidebar.date_input(
    "Select Date Range",
    value=(df['date'].min().date(), df['date'].max().date()),
    min_value=df['date'].min().date(),
    max_value=df['date'].max().date()
)

channels = st.sidebar.multiselect(
    "Select Channels",
    options=sorted(df['channel'].unique()),
    default=sorted(df['channel'].unique())
)

countries = st.sidebar.multiselect(
    "Select Countries",
    options=sorted(df['country'].unique()),
    default=sorted(df['country'].unique())
)

campaigns = st.sidebar.multiselect(
    "Select Campaigns",
    options=sorted(df['campaign_name'].unique()),
    default=sorted(df['campaign_name'].unique())
)

# Apply filters
filtered_df = df[
    (df['date'].dt.date >= date_range[0]) &
    (df['date'].dt.date <= date_range[1]) &
    (df['channel'].isin(channels)) &
    (df['country'].isin(countries)) &
    (df['campaign_name'].isin(campaigns))
].copy()

# Header
st.title("📊 Ad Campaign Performance Dashboard")
st.markdown("**Analyze digital advertising performance across channels, campaigns, and geographies.**")
st.divider()

# KPI Cards
col1, col2, col3, col4, col5 = st.columns(5)

total_spend = filtered_df['cost'].sum()
total_revenue = filtered_df['revenue'].sum()
total_conversions = filtered_df['conversions'].sum()
total_clicks = filtered_df['clicks'].sum()
overall_roas = (total_revenue / total_spend).round(2) if total_spend > 0 else 0

with col1:
    st.metric("💰 Total Spend", f"${total_spend:,.0f}")

with col2:
    st.metric("📈 Total Revenue", f"${total_revenue:,.0f}")

with col3:
    st.metric("🎯 Total Conversions", f"{total_conversions:,.0f}")

with col4:
    st.metric("🖱️ Total Clicks", f"{total_clicks:,.0f}")

with col5:
    st.metric("📊 Overall ROAS", f"{overall_roas:.2f}x", 
              delta=f"{((overall_roas - 1) * 100):.1f}%" if overall_roas > 1 else None)

st.divider()

# Row 1: Trend charts
col1, col2 = st.columns(2)

with col1:
    # Spend and Revenue Trend
    daily_trends = filtered_df.groupby('date').agg({
        'cost': 'sum',
        'revenue': 'sum'
    }).reset_index().sort_values('date')
    
    fig_trend = go.Figure()
    fig_trend.add_trace(go.Scatter(
        x=daily_trends['date'],
        y=daily_trends['cost'],
        name='Spend',
        line=dict(color='#FF6B6B', width=2),
        mode='lines'
    ))
    fig_trend.add_trace(go.Scatter(
        x=daily_trends['date'],
        y=daily_trends['revenue'],
        name='Revenue',
        line=dict(color='#51CF66', width=2),
        mode='lines'
    ))
    fig_trend.update_layout(
        title="Spend vs. Revenue Over Time",
        xaxis_title="Date",
        yaxis_title="Amount ($)",
        hovermode='x unified',
        height=400
    )
    st.plotly_chart(fig_trend, use_container_width=True)

with col2:
    # ROAS by Channel
    channel_metrics = filtered_df.groupby('channel').agg({
        'cost': 'sum',
        'revenue': 'sum'
    }).reset_index()
    channel_metrics['roas'] = (channel_metrics['revenue'] / channel_metrics['cost']).round(2)
    channel_metrics = channel_metrics.sort_values('roas', ascending=True)
    
    fig_roas = go.Figure(data=[
        go.Bar(
            y=channel_metrics['channel'],
            x=channel_metrics['roas'],
            orientation='h',
            marker=dict(
                color=channel_metrics['roas'],
                colorscale='RdYlGn',
                showscale=False
            ),
            text=channel_metrics['roas'],
            textposition='auto',
        )
    ])
    fig_roas.update_layout(
        title="ROAS by Channel",
        xaxis_title="ROAS (x)",
        yaxis_title="Channel",
        height=400
    )
    st.plotly_chart(fig_roas, use_container_width=True)

st.divider()

# Row 2: Performance metrics
col1, col2 = st.columns(2)

with col1:
    # Top 10 Campaigns by Revenue
    top_campaigns = filtered_df.groupby('campaign_name').agg({
        'revenue': 'sum',
        'cost': 'sum'
    }).reset_index()
    top_campaigns['roas'] = (top_campaigns['revenue'] / top_campaigns['cost']).round(2)
    top_campaigns = top_campaigns.nlargest(10, 'revenue')
    
    fig_top = px.bar(
        top_campaigns,
        x='revenue',
        y='campaign_name',
        orientation='h',
        title="Top 10 Campaigns by Revenue",
        labels={'revenue': 'Revenue ($)', 'campaign_name': 'Campaign'},
        color='roas',
        color_continuous_scale='Viridis'
    )
    fig_top.update_layout(height=400, showlegend=False)
    st.plotly_chart(fig_top, use_container_width=True)

with col2:
    # CTR and Conversion Rate by Channel
    channel_performance = filtered_df.groupby('channel').agg({
        'clicks': 'sum',
        'impressions': 'sum',
        'conversions': 'sum'
    }).reset_index()
    channel_performance['ctr'] = (channel_performance['clicks'] / channel_performance['impressions'] * 100).round(2)
    channel_performance['conversion_rate'] = (channel_performance['conversions'] / channel_performance['clicks'] * 100).round(2)
    
    fig_perf = go.Figure()
    fig_perf.add_trace(go.Bar(
        x=channel_performance['channel'],
        y=channel_performance['ctr'],
        name='CTR (%)',
        marker_color='#4C72B0'
    ))
    fig_perf.add_trace(go.Bar(
        x=channel_performance['channel'],
        y=channel_performance['conversion_rate'],
        name='Conversion Rate (%)',
        marker_color='#DD8452'
    ))
    fig_perf.update_layout(
        title="CTR and Conversion Rate by Channel",
        yaxis_title="Rate (%)",
        xaxis_title="Channel",
        barmode='group',
        height=400
    )
    st.plotly_chart(fig_perf, use_container_width=True)

st.divider()

# Row 3: Detailed metrics
col1, col2 = st.columns(2)

with col1:
    # CPA by Channel
    cpa_data = filtered_df.groupby('channel').agg({
        'cost': 'sum',
        'conversions': 'sum'
    }).reset_index()
    cpa_data['cpa'] = (cpa_data['cost'] / cpa_data['conversions']).round(2)
    cpa_data = cpa_data.sort_values('cpa', ascending=True)
    
    fig_cpa = go.Figure(data=[
        go.Bar(
            y=cpa_data['channel'],
            x=cpa_data['cpa'],
            orientation='h',
            marker=dict(color='#FF6B6B'),
            text=cpa_data['cpa'],
            textposition='auto'
        )
    ])
    fig_cpa.update_layout(
        title="Cost Per Acquisition (CPA) by Channel",
        xaxis_title="CPA ($)",
        yaxis_title="Channel",
        height=400
    )
    st.plotly_chart(fig_cpa, use_container_width=True)

with col2:
    # Revenue by Country
    country_revenue = filtered_df.groupby('country').agg({
        'revenue': 'sum',
        'cost': 'sum',
        'conversions': 'sum'
    }).reset_index()
    country_revenue['roas'] = (country_revenue['revenue'] / country_revenue['cost']).round(2)
    country_revenue = country_revenue.sort_values('revenue', ascending=False)
    
    fig_country = px.bar(
        country_revenue,
        x='country',
        y='revenue',
        title="Revenue by Country",
        labels={'revenue': 'Revenue ($)', 'country': 'Country'},
        color='roas',
        color_continuous_scale='Greens'
    )
    fig_country.update_layout(height=400, showlegend=False)
    st.plotly_chart(fig_country, use_container_width=True)

st.divider()

# Detailed Data Table
st.subheader("📋 Campaign Performance Details")

display_df = filtered_df.copy()
display_df['date'] = display_df['date'].dt.strftime('%Y-%m-%d')
display_df = display_df[[
    'date', 'campaign_name', 'channel', 'country', 'industry',
    'impressions', 'clicks', 'cost', 'conversions', 'revenue',
    'ctr', 'cpc', 'cpa', 'conversion_rate', 'roas'
]].sort_values('revenue', ascending=False)

st.dataframe(
    display_df,
    use_container_width=True,
    hide_index=True,
    column_config={
        'cost': st.column_config.NumberColumn(format="$%.2f"),
        'revenue': st.column_config.NumberColumn(format="$%.2f"),
        'cpc': st.column_config.NumberColumn(format="$%.2f"),
        'cpa': st.column_config.NumberColumn(format="$%.2f"),
        'ctr': st.column_config.NumberColumn(format="%.2f%%"),
        'conversion_rate': st.column_config.NumberColumn(format="%.2f%%"),
        'roas': st.column_config.NumberColumn(format="%.2f x"),
    }
)

st.divider()

# Summary Statistics
st.subheader("📊 Summary Statistics")

col1, col2, col3 = st.columns(3)

with col1:
    st.write("**Efficiency Metrics**")
    avg_ctr = filtered_df['ctr'].mean()
    avg_cpa = filtered_df['cpa'].mean()
    avg_conversion_rate = filtered_df['conversion_rate'].mean()
    st.write(f"Avg CTR: **{avg_ctr:.2f}%**")
    st.write(f"Avg CPA: **${avg_cpa:.2f}**")
    st.write(f"Avg Conversion Rate: **{avg_conversion_rate:.2f}%**")

with col2:
    st.write("**Campaign Insights**")
    num_campaigns = filtered_df['campaign_name'].nunique()
    num_channels = filtered_df['channel'].nunique()
    num_countries = filtered_df['country'].nunique()
    st.write(f"Active Campaigns: **{num_campaigns}**")
    st.write(f"Channels: **{num_channels}**")
    st.write(f"Countries: **{num_countries}**")

with col3:
    st.write("**Portfolio Performance**")
    best_campaign = filtered_df.groupby('campaign_name')['roas'].mean().idxmax()
    best_roas = filtered_df.groupby('campaign_name')['roas'].mean().max()
    roi = ((total_revenue - total_spend) / total_spend * 100).round(1) if total_spend > 0 else 0
    st.write(f"Best Campaign: **{best_campaign}**")
    st.write(f"Best ROAS: **{best_roas:.2f}x**")
    st.write(f"Overall ROI: **{roi:.1f}%**")

st.divider()
st.caption("Data updated: January - March 2024 | Dashboard built with Streamlit & Plotly")
