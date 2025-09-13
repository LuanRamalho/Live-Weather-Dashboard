import requests
from rich.console import Console
from rich.table import Table

console = Console()

cities = [
    # América do Norte
    "New York", "Los Angeles", "Mexico City", "Toronto", "Chicago", "Vancouver",

    # América do Sul
    "São Paulo", "Rio de Janeiro", "Buenos Aires", "Santiago", "Bogota", "Lima", "Caracas",

    # Europa
    "London", "Paris", "Berlin", "Rome", "Madrid", "Lisbon", "Amsterdam", "Moscow", "Kyiv",

    # Ásia
    "Tokyo", "Beijing", "Seoul", "Delhi", "Mumbai", "Dubai", "Singapore", "Bangkok", "Istanbul", "Jerusalem",

    # África
    "Cairo", "Johannesburg", "Lagos", "Nairobi", "Marrakesh", "Cape Town", "Accra", "Dakar",

    # Oceania
    "Sydney", "Melbourne", "Auckland", "Perth", "Brisbane", "Canberra",
]

table = Table(title="☁️ Weather Dashboard", style="cyan")
table.add_column("City", justify="center")
table.add_column("Temperature (°C)", justify="center")

for city in cities:
    temp = requests.get(f"https://wttr.in/{city}?format=%t").text
    table.add_row(city, temp)

console.print(table)

input()