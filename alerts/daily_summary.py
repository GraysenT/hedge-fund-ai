# Define the data structure for the report
report_data = {
    "alpha": 0.05,
    "mutations": [
        {"gene": "BRCA1", "mutation": "c.68_69del", "effect": "frameshift"},
        {"gene": "TP53", "mutation": "c.215C>G", "effect": "missense"},
        {"gene": "MLH1", "mutation": "c.350G>T", "effect": "nonsense"}
    ],
    "changes": [
        {"date": "2023-12-01", "description": "Updated analysis pipeline to version 3.1"},
        {"date": "2023-11-15", "description": "Added new reference genome GRCh38.p13"}
    ],
    "decisions": [
        {"date": "2023-12-05", "decision": "Proceed with clinical trial phase 2"},
        {"date": "2023-11-20", "decision": "Increase funding for mutation research"}
    ]
}

# Function to format the report
def format_report(report):
    alpha = report['alpha']
    mutations = report['mutations']
    changes = report['changes']
    decisions = report['decisions']

    report_text = f"Summary Report\n\n"
    report_text += f"Alpha Level: {alpha}\n\n"
    report_text += "Mutations Observed:\n"
    for mutation in mutations:
        report_text += f"- Gene: {mutation['gene']}, Mutation: {mutation['mutation']}, Effect: {mutation['effect']}\n"
    report_text += "\nRecent Changes:\n"
    for change in changes:
        report_text += f"- Date: {change['date']}, Description: {change['description']}\n"
    report_text += "\nDecisions Made:\n"
    for decision in decisions:
        report_text += f"- Date: {decision['date']}, Decision: {decision['decision']}\n"

    return report_text

# Generate and print the report
formatted_report = format_report(report_data)
print(formatted_report)
