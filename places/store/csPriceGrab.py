import os
import requests
from csgo_market_api import CSGOMarket

API_KEY = "BJ77jDRXu0gw3m9U4mUTM5aCQQXa86H"  # Replace with your CS:GO Market API key
from csgo_market_api import CSGOMarket

market = CSGOMarket(api_key=API_KEY)
FULL_EXPORT_URL = "https://market.csgo.com/api/full-export/USD.json"


def get_current_prices(item_names):
    resp = market.get_list_items_info(list_hash_name=item_names)
    if not resp.get("success"):
        raise RuntimeError(f"API error: {resp}")
    data = resp.get("data", {})
    prices = {}
    for name in item_names:
        info = data.get(name)
        prices[name] = info.get("min") if info else None
    return prices



if __name__ == "__main__":
    item_list = [
        "AK-47 | Redline (Field-Tested)",
        "AWP | Asiimov (Battle-Scarred)",
    ]
    prices = get_current_prices(item_list)
    print("=== Specific Item Prices ===")
    for item, price in prices.items():
        print(f"{item}: {price}")
    
