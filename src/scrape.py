import requests
import pandas as pd
import os
import warnings
from urllib3.exceptions import NotOpenSSLWarning

warnings.filterwarnings("ignore", category=NotOpenSSLWarning)
warnings.filterwarnings("ignore", category=DeprecationWarning)

url = "https://api.usaspending.gov/api/v2/search/spending_by_award/"
payload = {
    "filters": {
        "award_type_codes": ["A", "B", "C", "D"],
        "time_period": [{"start_date": "2020-01-01", "end_date": "2025-02-23"}]
    },
    "fields": ["Recipient Name", "Awarding Agency", "Award Amount"],  # Swapped recipient_name for Recipient Name
    "limit": 100,
    "sort": "Award Amount"
}
response = requests.post(url, json=payload)

print("Status Code:", response.status_code)
print("Raw Response:", response.text[:500])

try:
    if response.status_code == 200 and "results" in response.json():
        data = response.json()["results"]
        df = pd.DataFrame(data)
        os.makedirs("data/raw", exist_ok=True)
        df.to_csv("data/raw/fed_spending.csv", index=False)
        print(f"Scraped {len(df)} contracts to data/raw/fed_spending.csv")
    else:
        print(f"Error: Status {response.status_code}, Response not processed")
except requests.exceptions.JSONDecodeError:
    print("Error: Failed to decode JSON - likely a server issue")