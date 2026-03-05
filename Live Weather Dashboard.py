import requests
from rich.console import Console
from rich.table import Table
from rich.live import Live
import time

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

def generate_table(data):
    """Gera o objeto da tabela com os dados atuais."""
    table = Table(title="☁️ Weather Dashboard", style="cyan")
    table.add_column("City", justify="center")
    table.add_column("Temperature (°C)", justify="center")
    
    for city, temp in data:
        table.add_row(city, temp)
    return table

# Lista para armazenar os resultados conforme chegam
weather_data = []

# O gerenciador 'Live' atualiza o terminal automaticamente
with Live(generate_table(weather_data), refresh_per_second=4) as live:
    for city in cities:
        try:
            # Busca a temperatura (com timeout para segurança)
            response = requests.get(f"https://wttr.in/{city}?format=%t", timeout=5)
            temp = response.text if response.status_code == 200 else "N/A"
        except:
            temp = "Erro"
            
        # Adiciona aos dados e atualiza a visualização 'ao vivo'
        weather_data.append((city, temp))
        live.update(generate_table(weather_data))

input("\nProcesso finalizado. Pressione Enter para sair...")
