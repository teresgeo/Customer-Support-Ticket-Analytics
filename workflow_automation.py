
import pandas as pd
from datetime import datetime, timedelta

class TicketWorkflowAutomation:
    def __init__(self, tickets_file):
        self.df = pd.read_csv(tickets_file)
        self.df['Created_Date'] = pd.to_datetime(self.df['Created_Date'])

    def auto_prioritize_tickets(self):
        '''
        Automatically adjust priority based on ticket age and type
        '''
        print("Running Auto-Prioritization...")
        current_time = datetime.now()
        escalations = []

        for idx, row in self.df.iterrows():
            ticket_age = (current_time - row['Created_Date']).days

            # Escalate tickets based on age
            if ticket_age > 7 and row['Priority'] == 'Low':
                escalations.append({
                    'Ticket_ID': row['Ticket_ID'],
                    'Current_Priority': row['Priority'],
                    'Suggested_Priority': 'Medium',
                    'Reason': f'Ticket aged {ticket_age} days'
                })
            elif ticket_age > 3 and row['Priority'] == 'Medium':
                escalations.append({
                    'Ticket_ID': row['Ticket_ID'],
                    'Current_Priority': row['Priority'],
                    'Suggested_Priority': 'High',
                    'Reason': f'Ticket aged {ticket_age} days'
                })

            # Critical tickets for specific categories
            if row['Category'] in ['Data Loss', 'Authentication'] and row['Priority'] != 'Critical':
                escalations.append({
                    'Ticket_ID': row['Ticket_ID'],
                    'Current_Priority': row['Priority'],
                    'Suggested_Priority': 'Critical',
                    'Reason': f'Critical category: {row["Category"]}'
                })

        escalation_df = pd.DataFrame(escalations)
        if len(escalation_df) > 0:
            escalation_df.to_csv('auto_escalations.csv', index=False)
            print(f"Found {len(escalations)} tickets for escalation")
            print(escalation_df.head(10))
        else:
            print("No tickets require escalation")

        return escalation_df

    def auto_assign_tickets(self):
        '''
        Automatically assign tickets based on workload and expertise
        '''
        print("\nRunning Auto-Assignment...")

        # Calculate current workload per agent
        workload = self.df[self.df['Status'].isin(['Open', 'In Progress'])].groupby('Assigned_Agent').size()
        print(f"\nCurrent Workload Distribution:")
        print(workload.sort_values(ascending=False).head())

        # Find unassigned or open tickets
        open_tickets = self.df[self.df['Status'] == 'Open']
        print(f"\nOpen tickets to assign: {len(open_tickets)}")

        return workload

    def identify_sla_violations(self):
        '''
        Identify tickets at risk of SLA violation
        '''
        print("\nChecking SLA Violations...")

        sla_targets = {
            'Critical': {'response': 2, 'resolution': 24},
            'High': {'response': 8, 'resolution': 48},
            'Medium': {'response': 24, 'resolution': 96},
            'Low': {'response': 48, 'resolution': 168}
        }

        violations = []
        for idx, row in self.df.iterrows():
            target = sla_targets.get(row['Priority'], {})

            if row['First_Response_Time_Hours'] > target.get('response', float('inf')):
                violations.append({
                    'Ticket_ID': row['Ticket_ID'],
                    'Priority': row['Priority'],
                    'Violation_Type': 'Response Time',
                    'Actual': row['First_Response_Time_Hours'],
                    'Target': target['response']
                })

            if row['Resolution_Time_Hours'] > target.get('resolution', float('inf')):
                violations.append({
                    'Ticket_ID': row['Ticket_ID'],
                    'Priority': row['Priority'],
                    'Violation_Type': 'Resolution Time',
                    'Actual': row['Resolution_Time_Hours'],
                    'Target': target['resolution']
                })

        violation_df = pd.DataFrame(violations)
        if len(violation_df) > 0:
            violation_df.to_csv('sla_violations.csv', index=False)
            print(f"Found {len(violations)} SLA violations")
            print(violation_df.head(10))
        else:
            print("No SLA violations found")

        return violation_df

    def generate_daily_digest(self):
        '''
        Generate a daily digest report
        '''
        print("\nGenerating Daily Digest...")

        digest = {
            'Total_Tickets': len(self.df),
            'Open': len(self.df[self.df['Status'] == 'Open']),
            'In_Progress': len(self.df[self.df['Status'] == 'In Progress']),
            'Resolved_Today': len(self.df[self.df['Status'] == 'Resolved']),
            'Critical_Tickets': len(self.df[self.df['Priority'] == 'Critical']),
            'Avg_Response_Time': self.df['First_Response_Time_Hours'].mean(),
            'Avg_CSAT': self.df['CSAT_Score'].mean()
        }

        print("\nDaily Digest Summary:")
        for key, value in digest.items():
            print(f"{key}: {value}")

        return digest

# Run workflow automation
if __name__ == "__main__":
    print("=" * 70)
    print("TICKET WORKFLOW AUTOMATION SYSTEM")
    print("=" * 70)

    automation = TicketWorkflowAutomation('customer_support_tickets.csv')

    # Run all automation tasks
    automation.auto_prioritize_tickets()
    automation.auto_assign_tickets()
    automation.identify_sla_violations()
    automation.generate_daily_digest()

    print("\n" + "=" * 70)
    print("WORKFLOW AUTOMATION COMPLETE")
    print("=" * 70)
