from tronpy import Tron
from tronpy.providers import HTTPProvider

provider = HTTPProvider(api_key="be561084-72d2-453c-af39-ef76204191a0")
client = Tron(provider, network="shasta")

wallet = client.generate_address()
print(wallet)