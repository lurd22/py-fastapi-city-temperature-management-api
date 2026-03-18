import httpx

async def fetch_temperature(city_name: str) -> float:
    # Example using Open-Meteo (no API key needed)
    url = f"https://api.open-meteo.com/v1/forecast?current_weather=true&latitude=0&longitude=0"

    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        data = response.json()

    return data.get("current_weather", {}).get("temperature", 0.0)