import pandas as pd
import re
from collections import Counter

class TicketAutoTagger:
    def __init__(self, tickets_file):
        self.df = pd.read_csv(tickets_file)

        # Define keyword patterns for auto-tagging
        self.tag_patterns = {
            'urgent': ['urgent', 'asap', 'emergency', 'immediately', 'critical'],
            'password_reset': ['password', 'reset', 'login', 'authentication', 'access'],
            'billing': ['invoice', 'charge', 'payment', 'billing', 'refund', 'cost'],
            'bug': ['error', 'bug', 'crash', 'broken', 'not working', 'issue'],
            'feature_request': ['feature', 'enhancement', 'improvement', 'request', 'add'],
            'integration': ['api', 'integration', 'connect', 'sync', 'webhook'],
            'performance': ['slow', 'performance', 'speed', 'timeout', 'lag'],
            'data_issue': ['data', 'missing', 'lost', 'corrupted', 'export', 'import']
        }

    def extract_keywords(self, text):
        '''
        Extract keywords from ticket type and category
        '''
        if pd.isna(text):
            return []

        text = str(text).lower()
        words = re.findall(r'\b\w+\b', text)
        return words

    def auto_tag_tickets(self):
        '''
        Automatically tag tickets based on content patterns
        '''
        print("Running Auto-Tagging System...")
        print("=" * 70)

        tags_list = []

        for idx, row in self.df.iterrows():
            # Combine ticket type and category for analysis
            content = f"{row['Ticket_Type']} {row['Category']}".lower()

            ticket_tags = []
            for tag, keywords in self.tag_patterns.items():
                if any(keyword in content for keyword in keywords):
                    ticket_tags.append(tag)

            tags_list.append({
                'Ticket_ID': row['Ticket_ID'],
                'Ticket_Type': row['Ticket_Type'],
                'Category': row['Category'],
                'Auto_Tags': ', '.join(ticket_tags) if ticket_tags else 'general',
                'Tag_Count': len(ticket_tags)
            })

        tags_df = pd.DataFrame(tags_list)
        tags_df.to_csv('auto_tagged_tickets.csv', index=False)

        print(f"Tagged {len(tags_df)} tickets")
        print(f"\nSample Tagged Tickets:")
        print(tags_df.head(10))

        # Tag distribution
        all_tags = []
        for tags in tags_df['Auto_Tags']:
            if tags != 'general':
                all_tags.extend(tags.split(', '))

        tag_distribution = Counter(all_tags)
        print(f"\nTag Distribution:")
        for tag, count in tag_distribution.most_common():
            print(f"{tag}: {count}")

        return tags_df

    def generate_tag_insights(self):
        '''
        Generate insights from tagged tickets
        '''
        tags_df = self.auto_tag_tickets()

        # Merge with original data
        merged = pd.merge(self.df, tags_df[['Ticket_ID', 'Auto_Tags']], on='Ticket_ID')

        # Analyze response times by tag
        print(f"\n" + "=" * 70)
        print("TAG-BASED PERFORMANCE ANALYSIS")
        print("=" * 70)

        # Get top tags
        all_tags = []
        for tags in tags_df['Auto_Tags']:
            if tags != 'general':
                all_tags.extend(tags.split(', '))

        top_tags = [tag for tag, count in Counter(all_tags).most_common(5)]

        for tag in top_tags:
            tag_tickets = merged[merged['Auto_Tags'].str.contains(tag, na=False)]
            if len(tag_tickets) > 0:
                print(f"\n{tag.upper()}:")
                print(f"  Count: {len(tag_tickets)}")
                print(f"  Avg Response Time: {tag_tickets['First_Response_Time_Hours'].mean():.2f} hours")
                print(f"  Avg Resolution Time: {tag_tickets['Resolution_Time_Hours'].mean():.2f} hours")
                if tag_tickets['CSAT_Score'].notna().any():
                    print(f"  Avg CSAT: {tag_tickets['CSAT_Score'].mean():.2f}")

# Run auto-tagging
if __name__ == "__main__":
    print("=" * 70)
    print("TICKET AUTO-TAGGING SYSTEM")
    print("=" * 70)
    print()

    tagger = TicketAutoTagger('customer_support_tickets.csv')
    tagger.generate_tag_insights()

    print("\n" + "=" * 70)
    print("AUTO-TAGGING COMPLETE")
    print("=" * 70)
