import requests
import customtkinter as ctk
from tkinter import messagebox

# Configuração da aparência e modo do CustomTkinter
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class WeatherApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Configurações da janela principal
        self.title("☁️ Painel do Tempo")
        self.geometry("800x600")

        # Lista de cidades
        self.cities = [
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

        # Configuração do layout da interface
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        # Frame principal
        self.main_frame = ctk.CTkFrame(self)
        self.main_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

        # Título
        self.title_label = ctk.CTkLabel(self.main_frame, text="☁️ Painel do Tempo", font=ctk.CTkFont(size=24, weight="bold"))
        self.title_label.pack(pady=10)

        # Botão para atualizar os dados
        self.update_button = ctk.CTkButton(self.main_frame, text="Atualizar Temperaturas", command=self.update_temperatures)
        self.update_button.pack(pady=5)

        # Criação da tabela com cabeçalhos
        self.table_frame = ctk.CTkScrollableFrame(self.main_frame)
        self.table_frame.pack(fill="both", expand=True, padx=10, pady=10)

        # Cabeçalhos da tabela
        self.city_header = ctk.CTkLabel(self.table_frame, text="Cidade", font=ctk.CTkFont(weight="bold"))
        self.city_header.grid(row=0, column=0, padx=5, pady=5, sticky="ew")

        self.temp_header = ctk.CTkLabel(self.table_frame, text="Temperatura (°C)", font=ctk.CTkFont(weight="bold"))
        self.temp_header.grid(row=0, column=1, padx=5, pady=5, sticky="ew")
        
        self.table_frame.grid_columnconfigure(0, weight=1)
        self.table_frame.grid_columnconfigure(1, weight=1)

        self.update_temperatures()

    def update_temperatures(self):
        """Atualiza a temperatura para cada cidade e exibe na interface."""
        for widget in self.table_frame.winfo_children():
            if widget not in (self.city_header, self.temp_header):
                widget.destroy()

        try:
            row_index = 1
            for city in self.cities:
                temp = requests.get(f"https://wttr.in/{city}?format=%t").text
                
                # Células da tabela
                city_label = ctk.CTkLabel(self.table_frame, text=city)
                city_label.grid(row=row_index, column=0, padx=5, pady=2, sticky="ew")
                
                temp_label = ctk.CTkLabel(self.table_frame, text=temp)
                temp_label.grid(row=row_index, column=1, padx=5, pady=2, sticky="ew")

                row_index += 1
            
            self.update() # Força a atualização da interface
        
        except requests.exceptions.RequestException:
            messagebox.showerror("Erro de Conexão", "Não foi possível conectar ao servidor. Verifique sua conexão com a internet.")

# Execução do aplicativo
if __name__ == "__main__":
    app = WeatherApp()
    app.mainloop()