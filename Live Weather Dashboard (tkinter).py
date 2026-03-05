import requests
import customtkinter as ctk
from tkinter import messagebox
import threading # Necessário para não travar a interface

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class WeatherApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("☁️ Painel do Tempo")
        self.geometry("800x600")

        # Lista de cidades (mantive as mesmas do seu código)
        self.cities = [
            "New York", "Los Angeles", "Mexico City", "Toronto", "Chicago", "Vancouver",
            "São Paulo", "Rio de Janeiro", "Buenos Aires", "Santiago", "Bogota", "Lima", "Caracas",
            "London", "Paris", "Berlin", "Rome", "Madrid", "Lisbon", "Amsterdam", "Moscow", "Kyiv",
            "Tokyo", "Beijing", "Seoul", "Delhi", "Mumbai", "Dubai", "Singapore", "Bangkok", "Istanbul", "Jerusalem",
            "Cairo", "Johannesburg", "Lagos", "Nairobi", "Marrakesh", "Cape Town", "Accra", "Dakar",
            "Sydney", "Melbourne", "Auckland", "Perth", "Brisbane", "Canberra",
        ]

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        self.main_frame = ctk.CTkFrame(self)
        self.main_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

        self.title_label = ctk.CTkLabel(self.main_frame, text="☁️ Painel do Tempo", font=ctk.CTkFont(size=24, weight="bold"))
        self.title_label.pack(pady=10)

        self.update_button = ctk.CTkButton(self.main_frame, text="Atualizar Temperaturas", command=self.start_update_thread)
        self.update_button.pack(pady=5)

        self.table_frame = ctk.CTkScrollableFrame(self.main_frame)
        self.table_frame.pack(fill="both", expand=True, padx=10, pady=10)

        self.city_header = ctk.CTkLabel(self.table_frame, text="Cidade", font=ctk.CTkFont(weight="bold"))
        self.city_header.grid(row=0, column=0, padx=5, pady=5, sticky="ew")

        self.temp_header = ctk.CTkLabel(self.table_frame, text="Temperatura (°C)", font=ctk.CTkFont(weight="bold"))
        self.temp_header.grid(row=0, column=1, padx=5, pady=5, sticky="ew")
        
        self.table_frame.grid_columnconfigure(0, weight=1)
        self.table_frame.grid_columnconfigure(1, weight=1)

        # Inicia a atualização sem travar a abertura da janela
        self.after(100, self.start_update_thread)

    def start_update_thread(self):
        """Dispara a atualização em uma thread separada."""
        self.update_button.configure(state="disabled", text="Carregando...")
        threading.Thread(target=self.update_temperatures, daemon=True).start()

    def update_temperatures(self):
        """Busca os dados em background e atualiza a UI."""
        # Limpar linhas anteriores
        for widget in self.table_frame.winfo_children():
            if widget not in (self.city_header, self.temp_header):
                widget.destroy()

        try:
            for i, city in enumerate(self.cities):
                # Request com timeout para evitar espera infinita
                try:
                    response = requests.get(f"https://wttr.in/{city}?format=%t", timeout=10)
                    temp = response.text if response.status_code == 200 else "Erro"
                except:
                    temp = "N/A"
                
                # Agenda a criação do widget na thread principal (segurança do Tkinter)
                self.after(0, self.add_row_to_table, city, temp, i + 1)
            
        except Exception as e:
            self.after(0, lambda: messagebox.showerror("Erro", f"Falha ao atualizar: {e}"))
        finally:
            self.after(0, lambda: self.update_button.configure(state="normal", text="Atualizar Temperaturas"))

    def add_row_to_table(self, city, temp, row_index):
        """Adiciona uma única linha na tabela."""
        ctk.CTkLabel(self.table_frame, text=city).grid(row=row_index, column=0, padx=5, pady=2, sticky="ew")
        ctk.CTkLabel(self.table_frame, text=temp).grid(row=row_index, column=1, padx=5, pady=2, sticky="ew")

if __name__ == "__main__":
    app = WeatherApp()
    app.mainloop()
