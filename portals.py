import requests

auth = ""


class PortalsMarketClient:
    APP_URL = "https://app.portals-market.com/api"

    def __init__(self, auth_token: str):
        self.auth_token = auth_token
        self.session = requests.Session()
        self.session.headers.update(
            {
                "Authorization": auth_token,
                "User-Agent": "Mozilla/5.0",
                "Accept": "application/json",
            }
        )

    def search_nfts(self, collection="Toy Bear", model="Matrix", limit=20, offset=0):
        url = f"{self.APP_URL}/nfts/search"
        params = {
            "offset": offset,
            "limit": limit,
            "filter_by_collections": collection,
            "filter_by_models": model,
            "sort_by": "price asc",
            "status": "listed",
        }
        response = self.session.get(url, params=params)
        response.raise_for_status()
        return response.json().get("results", [])

    def check_wallet_balance(self):
        url = f"{self.APP_URL}/users/wallets/"
        response = self.session.get(url)
        response.raise_for_status()
        return response.json()

    def buy_nft(self, nft_id: str, price: str):
        url = f"{self.APP_URL}/nfts"
        payload = {"nft_details": [{"id": nft_id, "price": price}]}
        response = self.session.post(url, json=payload)
        response.raise_for_status()
        return response.json()


client = PortalsMarketClient(auth)

# Search NFTs
for nft in client.search_nfts():
    print(nft)

# Check balance
balance = client.check_wallet_balance()
print(balance)

# Buy NFT
result = client.buy_nft("126af54f-a9b5-4824-942f-399d5b04c879", "65")
print(result)
