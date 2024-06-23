import requests
import json

url = "https://testnet-graph.long.so"
query = """
query Pools {
    pools {
        id
        address
        tickSpacing
        price
        earnedFeesAPRFUSDC
        earnedFeesAPRToken1
    }
}
"""

headers = {
    "Content-Type": "application/json",

}

response = requests.post(url, json={'query': query}, headers=headers)

if response.status_code == 200:
    data = response.json()
    
    pools = data.get('data', {}).get('pools', [])
    if not pools:
        print("No pools data found in the response")
    else:
        total_price = 0.0
        pool_count = len(pools)
        
        transformed_pools = []
        
        for pool in pools:
            price = float(pool.get('price', 0))
            total_price += price
            pool_data = {
                "token": pool.get("id"),
                "current_price": pool.get("price")
            }
            transformed_pools.append(pool_data)
        
        average_price = total_price / pool_count if pool_count > 0 else 0
        
        transformed_response = {
                "average_swap_size_usd": f"{average_price:.2f}",
                "pools": transformed_pools  
        }
        print(json.dumps(transformed_response, indent=2))
else:
    print(f"Query failed to run by returning code of {response.status_code}. {response.text}")
