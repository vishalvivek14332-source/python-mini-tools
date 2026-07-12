import requests
from api import get_api_key

city = input("City: ").strip()

url = (
    "https://api.openweathermap.org/data/2.5/weather"
    f"?q={city}&appid={get_api_key()}&units=metric"
)

r = requests.get(url, timeout=10)
r.raise_for_status()
data = r.json()

print(f"{data['name']}: {data['main']['temp']}°C")
print(data["weather"][0]["description"].title())