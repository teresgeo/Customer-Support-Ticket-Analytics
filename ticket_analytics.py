
import pandas as pd
import numpy as np
from datetime import datetime

# Load the dataset
df = pd.read_csv('customer_support_tickets.csv')
df['Created_Date'] = pd.to_datetime(df['Created_Date'])

# ============================================
# TICKET ANALYTICS DASHBOARD
# ============================================

def generate_ticket_insights():
    print("=" * 70)
    print("CUSTOMER SUPPORT TICKET ANALYTICS DASHBOARD")
    print("=" * 70)

    # 1. Overall Metrics
    print("\n1. OVERALL METRICS")
    print("-" * 70)
    print(f"Total Tickets: {len(df)}")
    print(f"Date Range: {df['Created_Date'].min().date()} to {df['Created_Date'].max().date()}")
    print(f"Average First Response Time: {df['First_Response_Time_Hours'].mean():.2f} hours")
    print(f"Average Resolution Time: {df['Resolution_Time_Hours'].mean():.2f} hours")
    print(f"Average CSAT Score: {df['CSAT_Score'].mean():.2f} / 5.0")

    # 2. Ticket Volume Analysis
    print("\n2. TICKET VOLUME BY CATEGORY")
    print("-" * 70)
    ticket_volume = df.groupby('Ticket_Type').size().sort_values(ascending=False)
    print(ticket_volume)

    # 3. Priority Distribution
    print("\n3. PRIORITY DISTRIBUTION")
    print("-" * 70)
    priority_dist = df['Priority'].value_counts()
    print(priority_dist)

    # 4. Status Breakdown
    print("\n4. CURRENT STATUS BREAKDOWN")
    print("-" * 70)
    status_breakdown = df['Status'].value_counts()
    print(status_breakdown)

    # 5. Channel Performance
    print("\n5. CHANNEL PERFORMANCE")
    print("-" * 70)
    channel_perf = df.groupby('Channel').agg({
        'Ticket_ID': 'count',
        'First_Response_Time_Hours': 'mean',
        'Resolution_Time_Hours': 'mean',
        'CSAT_Score': 'mean'
    }).round(2)
    channel_perf.columns = ['Total_Tickets', 'Avg_Response_Time', 'Avg_Resolution_Time', 'Avg_CSAT']
    print(channel_perf)

    # 6. Agent Performance
    print("\n6. TOP 5 AGENTS BY TICKET VOLUME")
    print("-" * 70)
    agent_perf = df.groupby('Assigned_Agent').agg({
        'Ticket_ID': 'count',
        'First_Response_Time_Hours': 'mean',
        'Resolution_Time_Hours': 'mean',
        'CSAT_Score': 'mean'
    }).round(2)
    agent_perf.columns = ['Total_Tickets', 'Avg_Response_Time', 'Avg_Resolution_Time', 'Avg_CSAT']
    agent_perf = agent_perf.sort_values('Total_Tickets', ascending=False).head()
    print(agent_perf)

    # 7. SLA Compliance (assuming SLA targets)
    print("\n7. SLA COMPLIANCE ANALYSIS")
    print("-" * 70)
    sla_targets = {
        'Critical': {'response': 2, 'resolution': 24},
        'High': {'response': 8, 'resolution': 48},
        'Medium': {'response': 24, 'resolution': 96},
        'Low': {'response': 48, 'resolution': 168}
    }

    for priority in ['Critical', 'High', 'Medium', 'Low']:
        priority_tickets = df[df['Priority'] == priority]
        if len(priority_tickets) > 0:
            response_compliance = (priority_tickets['First_Response_Time_Hours'] <= 
                                  sla_targets[priority]['response']).mean() * 100
            resolution_compliance = (priority_tickets['Resolution_Time_Hours'] <= 
                                    sla_targets[priority]['resolution']).mean() * 100
            print(f"{priority}: Response SLA: {response_compliance:.1f}%, Resolution SLA: {resolution_compliance:.1f}%")

    # 8. Monthly Trend Analysis
    print("\n8. MONTHLY TICKET TRENDS")
    print("-" * 70)
    df['Month'] = df['Created_Date'].dt.to_period('M')
    monthly_trends = df.groupby('Month').agg({
        'Ticket_ID': 'count',
        'First_Response_Time_Hours': 'mean',
        'CSAT_Score': 'mean'
    }).round(2)
    monthly_trends.columns = ['Ticket_Count', 'Avg_Response_Time', 'Avg_CSAT']
    print(monthly_trends)

    # 9. Product Issues
    print("\n9. PRODUCT-WISE ISSUE DISTRIBUTION")
    print("-" * 70)
    product_issues = df.groupby('Product').size().sort_values(ascending=False)
    print(product_issues)

    print("\n" + "=" * 70)
    print("END OF ANALYTICS REPORT")
    print("=" * 70)

# Generate insights
generate_ticket_insights()

# Save summary statistics to CSV
summary_stats = {
    'Metric': ['Total Tickets', 'Avg Response Time (hrs)', 'Avg Resolution Time (hrs)', 
               'Avg CSAT Score', 'Open Tickets', 'Resolved Tickets'],
    'Value': [len(df), 
              df['First_Response_Time_Hours'].mean(),
              df['Resolution_Time_Hours'].mean(),
              df['CSAT_Score'].mean(),
              len(df[df['Status'] == 'Open']),
              len(df[df['Status'] == 'Resolved'])]
}
summary_df = pd.DataFrame(summary_stats)
summary_df.to_csv('ticket_summary_stats.csv', index=False)
print("\nSummary statistics saved to 'ticket_summary_stats.csv'")
