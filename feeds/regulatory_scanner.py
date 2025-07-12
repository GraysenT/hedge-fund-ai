Below is a Python script that uses the `requests` library to fetch data from an API that provides information on global filings and regulatory events. For this example, I'll use the Financial Modeling Prep API, which offers various financial data including filings and regulatory events. You will need to get an API key from Financial Modeling Prep or any similar service that provides the data you need.

This script will periodically check for new updates and print them out. You'll need to adjust the API endpoints and data processing according to the actual API you decide to use.

```python
import requests
import time
from datetime import datetime

# Constants
API_KEY = 'your_api_key_here'
BASE_URL = 'https://financialmodelingprep.com/api/v3'
CHECK_INTERVAL = 3600  # check every hour

def fetch_filings():
    """Fetches the latest filings from the API."""
    url = f"{BASE_URL}/filings?apikey={API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to fetch data:", response.status_code)
        return None

def process_filings(filings):
    """Processes and prints filings."""
    for filing in filings:
        print("Filing Date:", filing['date'])
        print("Company Name:", filing['companyName'])
        print("Form Type:", filing['form'])
        print("Description:", filing['description'])
        print("Filing Link:", filing['link'])
        print("-" * 40)

def main():
    last_checked = None
    while True:
        print("Checking for new filings at", datetime.now())
        filings = fetch_filings()
        if filings:
            if last_checked is None or filings[0]['date'] > last_checked:
                print("New filings found:")
                process_filings(filings)
                last_checked = filings[0]['date']
            else:
                print("No new filings since last check.")
        else:
            print("Error fetching filings.")
        
        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    main()
```

### Explanation:
1. **API Key and Base URL**: Replace `'your_api_key_here'` with your actual API key from Financial Modeling Prep or another similar service.
2. **Fetch Function**: The `fetch_filings` function makes a GET request to the API to retrieve the latest filings.
3. **Process Function**: The `process_filings` function processes and prints details of each filing.
4. **Main Loop**: The script runs in an infinite loop, checking for new filings every hour (as set by `CHECK_INTERVAL`). It prints out new filings if any are found since the last check.

### Note:
- Ensure you have the `requests` library installed (`pip install requests`).
- You need to handle API rate limits and potential data structure differences depending on the actual API you use.
- This script assumes the latest filing is at index 0 in the response and uses the filing date to check for new filings. Adjust according to your data source's specifics.