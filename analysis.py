import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("data/bank-full.csv", sep=";")

# Funnel stages
contacts = len(df)
leads = len(df[df["contact"] != "unknown"])
customers = len(df[df["y"] == "yes"])

# Conversion rates
traffic_to_lead = (leads / contacts) * 100
lead_to_customer = (customers / leads) * 100

print("=== MARKETING FUNNEL ANALYSIS ===")
print(f"Total Contacts: {contacts}")
print(f"Leads: {leads}")
print(f"Customers: {customers}")
print(f"Traffic → Lead Conversion: {traffic_to_lead:.2f}%")
print(f"Lead → Customer Conversion: {lead_to_customer:.2f}%")

# Funnel Chart
stages = ["Contacts", "Leads", "Customers"]
values = [contacts, leads, customers]

plt.figure(figsize=(8,5))
plt.bar(stages, values)
plt.title("Marketing Funnel Analysis")
plt.ylabel("Number of Users")
plt.savefig("funnel_dashboard.png")
plt.show()