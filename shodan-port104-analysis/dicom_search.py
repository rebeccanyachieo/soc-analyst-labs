# Shodan

import json
import os
from datetime import datetime, timezone
import time
import shodan


# Read the key from an environment variable instead of putting it in the code.
SHODAN_API_KEY = os.getenv("SHODAN_API_KEY")

if not SHODAN_API_KEY:
    raise SystemExit(
        "SHODAN_API_KEY is not set. "
        "Set it in your terminal before running this script."
    )

api = shodan.Shodan(SHODAN_API_KEY)

# This searches for services recorded on port 104.
TARGET_QUERY = "port:104"

timestamp = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%SZ")
output_file = f"shodan_port104_{timestamp}.json"

try:
    # Count matches first without downloading the banners.
    count_results = api.count(query=TARGET_QUERY)
    print(f"Shodan reports {count_results.get('total', 0):,} matches.")

    # Download the first page of results.
    results = api.search(query=TARGET_QUERY, page=1)

    saved_results = []

    for device in results.get("matches", []):
        location = device.get("location") or {}

        record = {
            "ip": device.get("ip_str"),
            "port": device.get("port"),
            "country": location.get("country_name", "Unknown"),
            "organization": device.get("org", "Unknown"),
            "timestamp": device.get("timestamp"),
        }

        saved_results.append(record)

        print(
            f"[MATCH] "
            f"IP: {record['ip']} | "
            f"Port: {record['port']} | "
            f"Country: {record['country']} | "
            f"Organization: {record['organization']}"
        )

    with open(output_file, "w", encoding="utf-8") as file:
        json.dump(saved_results, file, indent=2)

    print(f"\nSaved {len(saved_results)} records to {output_file}")

    # Wait one second until the next API request
    time.sleep(1)

except shodan.APIError as error:
    print(f"Shodan API error: {error}")

except OSError as error:
    print(f"Could not save the results: {error}")
