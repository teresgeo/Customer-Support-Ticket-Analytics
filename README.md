# Customer Support Ticket Analytics Project

## Project Overview

This is a comprehensive **Customer Support Ticket Analytics System** that contains:
- Customer Success Platform Administration
- Data Analysis & Reporting
- Workflow Automation
- SLA Monitoring
- Ticket Classification

---

## Key Features

### 1. **Ticket Analytics Dashboard**
- Real-time metrics tracking (response time, resolution time, CSAT)
- Channel performance analysis
- Agent performance monitoring
- Monthly trend analysis
- Product-wise issue tracking

### 2. **Workflow Automation**
- Auto-prioritization based on ticket age and severity
- Intelligent ticket assignment
- SLA violation detection
- Daily digest reports

### 3. **Auto-Tagging**
- Automatic ticket categorization using keyword patterns
- Tag-based performance analysis
- Issue trend identification

### 4. **SLA Compliance Tracking**
- Priority-based SLA targets
- Automated violation alerts
- Compliance reporting

---

## Quick Start

### Installation

```bash
# Install dependencies
pip install -r requirements.txt
```

### Running the Analytics

```bash
# 1. Generate ticket insights
python ticket_analytics.py

# 2. Run workflow automation
python workflow_automation.py

# 3. Auto-tag tickets with
python ticket_tagging.py
```

---

## Dataset Details

**Dataset:** `customer_support_tickets.csv`

**Size:** 1000 synthetic tickets

**Fields:**
- `Ticket_ID`: Unique ticket identifier
- `Created_Date`: Ticket creation timestamp
- `Ticket_Type`: Type of issue (Technical, Billing, etc.)
- `Priority`: Critical, High, Medium, Low
- `Status`: Open, In Progress, Pending, Resolved, Closed
- `Channel`: Email, Chat, Phone, Web Portal
- `Product`: Product A-E
- `Category`: Authentication, Payment, Performance, etc.
- `Assigned_Agent`: Agent handling the ticket
- `First_Response_Time_Hours`: Time to first response
- `Resolution_Time_Hours`: Time to resolution
- `CSAT_Score`: Customer satisfaction score (1-5)

---

## Key Metrics Tracked

### Performance Metrics
- **Average First Response Time:** Measures support team responsiveness
- **Average Resolution Time:** Tracks efficiency of issue resolution
- **CSAT Score:** Customer satisfaction rating

### Operational Metrics
- **Ticket Volume by Category**
- **Priority Distribution**
- **Channel Performance**
- **Agent Workload & Performance**

### Compliance Metrics
- **SLA Response Compliance:** % tickets meeting response SLA
- **SLA Resolution Compliance:** % tickets meeting resolution SLA

---

## Workflow Automation Features

### Auto-Prioritization
- Escalates tickets based on age
- Flags critical categories (Data Loss, Authentication)
- Generates escalation recommendations

### Auto-Assignment
- Workload balancing across agents
- Smart ticket routing

### SLA Monitoring
- Real-time violation detection
- Priority-based SLA targets:
  - **Critical:** 2h response, 24h resolution
  - **High:** 8h response, 48h resolution
  - **Medium:** 24h response, 96h resolution
  - **Low:** 48h response, 168h resolution

---

## Acknowledgments

- Dataset: https://www.kaggle.com/datasets/suraj520/customer-support-ticket-dataset
- Built with: Python, Pandas, NumPy
- Inspired by: Real-world customer support workflows

---
