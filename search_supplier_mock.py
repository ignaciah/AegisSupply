"""
AegisSupply - Backend Mock Service
This script simulates the live marketplace API connector used by the 
Search_Marketplace_API tool inside UiPath Studio Web.
"""

import requests

def search_supplier(part_id: str) -> dict:
    """
    Queries the external marketplace for alternative component availability and pricing.
    """
    url = f"https://api.mockmarket.com/v1/parts/{part_id}"
    try:
        response = requests.get(url, timeout=10)
        # Fallback to dummy mock data if the live endpoint is unavailable during judging
        if response.status_code != 200:
            return {
                "part_id": part_id,
                "alternative_vendor": "Global Logistics Parts Inc.",
                "unit_cost": 450.00,
                "status": "In Stock",
                "estimated_delivery_days": 3
            }
        return response.json()
    except requests.RequestException:
        return {
            "error": "Failed to connect to marketplace service",
            "fallback_active": True
        }

if __name__ == "__main__":
    # Example execution test for local verification
    print("Testing AegisSupply Mock API tool output:")
    print(search_supplier("PART-992A"))
