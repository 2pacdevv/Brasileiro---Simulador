import tkinter as tk
import random as rm
import random
from tkinter import messagebox
import os
from tkinter import font as tkFont
idioma_selecionado = 'Português'

def select_edition(edition):
    global edicao, times, confrontos, rodadas, rodada_atual, jogos_por_time
    edicao = edition
#vitorias em casa = 10
#derrotas em casa = 11
#vitorias como visitante = 12
    if edicao == 2024:
      times = {
    "Atlético-GO":  [0, 0, 0, 2, 0, 0, 0, 0, 0, 2, 0, 0],
    "Athletico-PR": [0, 0, 0, 4, 0, 0, 0, 0, 0, 3, 0, 0],
    "Atlético-MG":  [0, 0, 0, 5, 0, 0, 0, 0, 0, 3, 0, 0],
    "Bahia":        [0, 0, 0, 5, 0, 0, 0, 0, 0, 4, 0, 0],
    "Botafogo":     [0, 0, 0, 7, 0, 0, 0, 0, 0, 6, 0, 0],
    "Corinthians": [0, 0, 0, 4, 0,0,0,0,0,3, 0, 0],
    "Vitória": [0, 0, 0, 3, 0,0,0,0,0,2, 0, 0],
    "Cruzeiro": [0, 0, 0, 4, 0,0,0,0,0,5, 0, 0],
    "Cuiabá": [0, 0, 0, 2, 0,0,0,0,0,4, 0, 0],
    "Flamengo": [0, 0, 0, 6, 0,0,0,0,0,5, 0, 0],
    "Fluminense": [0, 0, 0, 3, 0,0,0,0,0,5, 0, 0],
    "Fortaleza": [0, 0, 0, 5, 0,0,0,0,0,4, 0, 0],
    "Juventude": [0, 0, 0, 4, 0,0,0,0,0,4, 0, 0],
    "Grêmio": [0, 0, 0, 4, 0,0,0,0,0,4, 0, 0],
    "Internacional": [0, 0, 0, 5, 0,0,0,0,0,6, 0, 0],
    "Palmeiras": [0, 0, 0, 6, 0,0,0,0,0,7, 0, 0],
    "RB Bragantino": [0, 0, 0, 4, 0,0,0,0,0,4, 0, 0],
    "Criciúma": [0, 0, 0, 5, 0,0,0,0,0,2, 0, 0],
    "São Paulo": [0, 0, 0, 5, 0,0,0,0,0,3, 0, 0],
    "Vasco da Gama": [0, 0, 0, 4, 0,0,0,0,0,2, 0, 0]
}
    elif edicao == 2025:
        times = {
    "Ceará-SC":  [0, 0, 0, 2, 0, 0, 0, 0, 0, 3, 0, 0],
    "Sport-Recife": [0, 0, 0, 4, 0, 0, 0, 0, 0, 3, 0, 0],
    "Atlético-MG":  [0, 0, 0, 5, 0, 0, 0, 0, 0, 4, 0, 0],
    "Bahia":        [0, 0, 0, 5, 0, 0, 0, 0, 0, 4, 0, 0],
    "Botafogo":     [0, 0, 0, 6, 0, 0, 0, 0, 0, 5, 0, 0],
    "Corinthians": [0, 0, 0, 6, 0,0,0,0,0,4, 0, 0],
    "Vitória": [0, 0, 0, 4, 0,0,0,0,0,2, 0, 0],
    "Cruzeiro": [0, 0, 0, 5, 0,0,0,0,0,3, 0, 0],
    "Mirassol": [0, 0, 0, 4, 0,0,0,0,0,3, 0, 0],
    "Flamengo": [0, 0, 0, 6, 0,0,0,0,0,5, 0, 0],
    "Fluminense": [0, 0, 0, 4, 0,0,0,0,0,5, 0, 0],
    "Fortaleza": [0, 0, 0, 5, 0,0,0,0,0,4, 0, 0],
    "Juventude": [0, 0, 0, 3, 0,0,0,0,0,4, 0, 0],
    "Grêmio": [0, 0, 0, 5, 0,0,0,0,0,4, 0, 0],
    "Internacional": [0, 0, 0, 5, 0,0,0,0,0,5, 0, 0],
    "Palmeiras": [0, 0, 0, 5, 0,0,0,0,0,6, 0, 0],
    "RB Bragantino": [0, 0, 0, 3, 0,0,0,0,0,3, 0, 0],
    "Santos": [0, 0, 0, 5, 0,0,0,0,0,3, 0, 0],
    "São Paulo": [0, 0, 0, 5, 0,0,0,0,0,5, 0, 0],
    "Vasco da Gama": [0, 0, 0, 4, 0,0,0,0,0,3, 0, 0]
}    
    jogos_por_time = {time: [] for time in times.keys()} 
    confrontos = criar_jogos()     
    rodadas = total_rodadas
    rodada_atual = 0 
    root.destroy()
    start_simulation() 
    
total_rodadas = 38
def carregar_jogos(nome_arquivo="placares_jogos.txt"):
  
    global jogos_por_time
    jogos_por_time = {time: [] for time in times.keys()} 

    try:
        with open(nome_arquivo, "r") as arquivo:
            for linha in arquivo:
                partes = linha.strip().split(" ")
                if len(partes) == 5:
                    time1, gols_time1, _, gols_time2, time2 = partes
                    gols_time1 = int(gols_time1)
                    gols_time2 = int(gols_time2)
                    jogos_por_time[time1].append(f"{time1} {gols_time1} x {gols_time2} {time2}")
                    jogos_por_time[time2].append(f"{time2} {gols_time2} x {gols_time1} {time1}")

    except FileNotFoundError:
        messagebox.showerror("Erro", "Arquivo de placares não encontrado!")
    except Exception as e:
        messagebox.showerror("Erro", str(e))

def criar_tela_jogos():
    tela_times = tk.Tk()
    tela_times.title("Escolha um Time")
    tela_times.geometry("600x600")
    tela_times.configure(bg="#2c3e50")  

    canvas = tk.Canvas(tela_times, width=580, height=580, bg="#2c3e50", highlightthickness=0)
    canvas.pack(side="left", fill="both", expand=True)

    scrollbar = tk.Scrollbar(tela_times, orient="vertical", command=canvas.yview, troughcolor="#34495e",
                             bg="#2980b9", activebackground="#3498db")
    scrollbar.pack(side="right", fill="y")

    frame_times = tk.Frame(canvas, bg="#2c3e50")
    frame_times.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    canvas.create_window((0, 0), window=frame_times, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)
    
    for time in times.keys():
        botao_time = tk.Button(frame_times, text=time, command=lambda t=time: mostrar_jogos(t),
                               width=40, bg="#3498db", fg="white", font=("Helvetica", 12, "bold"),
                               relief="flat", overrelief="raised")
        botao_time.pack(pady=5, padx=10)

    tela_times.mainloop()

def mostrar_jogos(time):
    global label_aviso, times, jogos, max_jogos
    tela_jogos = tk.Tk()
    tela_jogos.title(f"Jogos de {time}")
    tela_jogos.geometry("500x600")
    tela_jogos.configure(bg="#2c3e50")  

    jogos = jogos_por_time.get(time, [])
    max_jogos = 38

    frame_jogos = tk.Frame(tela_jogos, bg="#2c3e50")
    frame_jogos.pack(pady=20, padx=20, fill="both", expand=True)

    canvas = tk.Canvas(frame_jogos, bg="#34495e")
    scrollbar = tk.Scrollbar(frame_jogos, orient="vertical", command=canvas.yview)
    scrollable_frame = tk.Frame(canvas, bg="#34495e")

    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )

    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)
    if idioma_selecionado == "Português":
         label_aviso = tk.Label(
            tela_jogos,
           text=f"Total de jogos: {len(jogos)} (Máximo: {max_jogos})\n Posição do time: {times[time][4]}\n Vitorias em casa: {times[time][10]}\n Derrotas em casa: {times[time][11]}",
           font=("Helvetica", 10, "bold"),
        fg="#ecf0f1",
        bg="#2c3e50"
    )
    elif idioma_selecionado == "Inglês":
             label_aviso = tk.Label(
            tela_jogos,
           text=f"Total of games: {len(jogos)} (Max: {max_jogos})\n Team position: {times[time][4]}\n Wins in house: {times[time][10]}\n Loses in house: {times[time][11]}",
           font=("Helvetica", 10, "bold"),
        fg="#ecf0f1",
        bg="#2c3e50"
    )
    
    elif idioma_selecionado == "Alemão":
      label_aviso = tk.Label(
        tela_jogos,
        text=f"Gesamtzahl der Spiele: {len(jogos)} (Maximal: {max_jogos})\n Teamposition: {times[time][4]}\n Heimsiege: {times[time][10]}\n Heimniederlagen: {times[time][11]}",
        font=("Helvetica", 10, "bold"),
        fg="#ecf0f1",
        bg="#2c3e50"
    )
    
    
    label_aviso.pack(pady=(20, 10))

    if not jogos:
        label_aviso.config(text="Nenhum jogo encontrado.", font=("Helvetica", 10, "italic"), fg="#e74c3e")

    if jogos:
        for i, jogo in enumerate(jogos[:max_jogos]):
            label_jogo = tk.Label(
                scrollable_frame,
                text=jogo,
                font=("Helvetica", 9),
                fg="#ecf0f1",
                bg="#34495e",
                anchor="w",
                padx=10,
                pady=3
            )
            label_jogo.pack(fill="x", pady=2)

    scrollbar.pack(side="right", fill="y")
    canvas.pack(side="left", fill="both", expand=True)

    btn_fechar = tk.Button(
        tela_jogos,
        text="Fechar",
        command=tela_jogos.destroy,
        bg="#e74c3c",
        fg="white",
        font=("Helvetica", 10, "bold"),
        relief="flat",
        width=20
    )
    btn_fechar.pack(pady=20)

    tela_jogos.mainloop()

def criar_jogos():
    global edicao
    if edicao == 2024:
        confrontoss = [
("Corinthians", "Palmeiras"),
("Palmeiras", "Corinthians"),
("Corinthians", "Vasco da Gama"),
("Vasco da Gama", "Corinthians"),
("Corinthians", "Atlético-GO"),
("Atlético-GO", "Corinthians"),
("Corinthians", "Athletico-PR"),
("Athletico-PR", "Corinthians"),
("Corinthians", "Atlético-MG"),
("Atlético-MG", "Corinthians"),
("Corinthians", "Bahia"),
("Bahia", "Corinthians"),
("Corinthians", "Botafogo"),
("Botafogo", "Corinthians"),
("Corinthians", "Vitória"),
("Vitória", "Corinthians"),
("Corinthians", "Cruzeiro"),
("Cruzeiro", "Corinthians"),
("Corinthians", "Cuiabá"),
("Cuiabá", "Corinthians"),
("Corinthians", "Flamengo"),
("Flamengo", "Corinthians"),
("Corinthians", "Fluminense"),
("Fluminense", "Corinthians"),
("Corinthians", "Fortaleza"),
("Fortaleza", "Corinthians"),
("Corinthians", "Juventude"),
("Juventude", "Corinthians"),
("Corinthians", "Grêmio"),
("Grêmio", "Corinthians"),
("Corinthians", "Internacional"),
("Internacional", "Corinthians"),
("Corinthians", "RB Bragantino"),
("RB Bragantino", "Corinthians"),
("Corinthians", "Criciúma"),
("Criciúma", "Corinthians"),
("Corinthians", "São Paulo"),
("São Paulo", "Corinthians"),
("Palmeiras", "Vasco da Gama"),
("Vasco da Gama", "Palmeiras"),
("Palmeiras", "Atlético-GO"),
("Atlético-GO", "Palmeiras"),
("Palmeiras", "Athletico-PR"),
("Athletico-PR", "Palmeiras"),
("Palmeiras", "Atlético-MG"),
("Atlético-MG", "Palmeiras"),
("Palmeiras", "Bahia"),
("Bahia", "Palmeiras"),
("Palmeiras", "Botafogo"),
("Botafogo", "Palmeiras"),
("Palmeiras", "Vitória"),
("Vitória", "Palmeiras"),
("Palmeiras", "Cruzeiro"),
("Cruzeiro", "Palmeiras"),
("Palmeiras", "Cuiabá"),
("Cuiabá", "Palmeiras"),
("Palmeiras", "Flamengo"),
("Flamengo", "Palmeiras"),
("Palmeiras", "Fluminense"),
("Fluminense", "Palmeiras"),
("Palmeiras", "Fortaleza"),
("Fortaleza", "Palmeiras"),
("Palmeiras", "Juventude"),
("Juventude", "Palmeiras"),
("Palmeiras", "Grêmio"),
("Grêmio", "Palmeiras"),
("Palmeiras", "Internacional"),
("Internacional", "Palmeiras"),
("Palmeiras", "RB Bragantino"),
("RB Bragantino", "Palmeiras"),
("Palmeiras", "Criciúma"),
("Criciúma", "Palmeiras"),
("Palmeiras", "São Paulo"),
("São Paulo", "Palmeiras"),
("Vasco da Gama", "Atlético-GO"),
("Atlético-GO", "Vasco da Gama"),
("Vasco da Gama", "Athletico-PR"),
("Athletico-PR", "Vasco da Gama"),
("Vasco da Gama", "Atlético-MG"),
("Atlético-MG", "Vasco da Gama"),
("Vasco da Gama", "Bahia"),
("Bahia", "Vasco da Gama"),
("Vasco da Gama", "Botafogo"),
("Botafogo", "Vasco da Gama"),
("Vasco da Gama", "Vitória"),
("Vitória", "Vasco da Gama"),
("Vasco da Gama", "Cruzeiro"),
("Cruzeiro", "Vasco da Gama"),
("Vasco da Gama", "Cuiabá"),
("Cuiabá", "Vasco da Gama"),
("Vasco da Gama", "Flamengo"),
("Flamengo", "Vasco da Gama"),
("Vasco da Gama", "Fluminense"),
("Fluminense", "Vasco da Gama"),
("Vasco da Gama", "Fortaleza"),
("Fortaleza", "Vasco da Gama"),
("Vasco da Gama", "Juventude"),
("Juventude", "Vasco da Gama"),
("Vasco da Gama", "Grêmio"),
("Grêmio", "Vasco da Gama"),
("Vasco da Gama", "Internacional"),
("Internacional", "Vasco da Gama"),
("Vasco da Gama", "RB Bragantino"),
("RB Bragantino", "Vasco da Gama"),
("Vasco da Gama", "Criciúma"),
("Criciúma", "Vasco da Gama"),
("Vasco da Gama", "São Paulo"),
("São Paulo", "Vasco da Gama"),
("Atlético-GO", "Athletico-PR"),
("Athletico-PR", "Atlético-GO"),
("Atlético-GO", "Atlético-MG"),
("Atlético-MG", "Atlético-GO"),
("Atlético-GO", "Bahia"),
("Bahia", "Atlético-GO"),
("Atlético-GO", "Botafogo"),
("Botafogo", "Atlético-GO"),
("Atlético-GO", "Vitória"),
("Vitória", "Atlético-GO"),
("Atlético-GO", "Cruzeiro"),
("Cruzeiro", "Atlético-GO"),
("Atlético-GO", "Cuiabá"),
("Cuiabá", "Atlético-GO"),
("Atlético-GO", "Flamengo"),
("Flamengo", "Atlético-GO"),
("Atlético-GO", "Fluminense"),
("Fluminense", "Atlético-GO"),
("Atlético-GO", "Fortaleza"),
("Fortaleza", "Atlético-GO"),
("Atlético-GO", "Juventude"),
("Juventude", "Atlético-GO"),
("Atlético-GO", "Grêmio"),
("Grêmio", "Atlético-GO"),
("Atlético-GO", "Internacional"),
("Internacional", "Atlético-GO"),
("Atlético-GO", "RB Bragantino"),
("RB Bragantino", "Atlético-GO"),
("Atlético-GO", "Criciúma"),
("Criciúma", "Atlético-GO"),
("Atlético-GO", "São Paulo"),
("São Paulo", "Atlético-GO"),
("Athletico-PR", "Atlético-MG"),
("Atlético-MG", "Athletico-PR"),
("Athletico-PR", "Bahia"),
("Bahia", "Athletico-PR"),
("Athletico-PR", "Botafogo"),
("Botafogo", "Athletico-PR"),
("Athletico-PR", "Vitória"),
("Vitória", "Athletico-PR"),
("Athletico-PR", "Cruzeiro"),
("Cruzeiro", "Athletico-PR"),
("Athletico-PR", "Cuiabá"),
("Cuiabá", "Athletico-PR"),
("Athletico-PR", "Flamengo"),
("Flamengo", "Athletico-PR"),
("Athletico-PR", "Fluminense"),
("Fluminense", "Athletico-PR"),
("Athletico-PR", "Fortaleza"),
("Fortaleza", "Athletico-PR"),
("Athletico-PR", "Juventude"),
("Juventude", "Athletico-PR"),
("Athletico-PR", "Grêmio"),
("Grêmio", "Athletico-PR"),
("Athletico-PR", "Internacional"),
("Internacional", "Athletico-PR"),
("Athletico-PR", "RB Bragantino"),
("RB Bragantino", "Athletico-PR"),
("Athletico-PR", "Criciúma"),
("Criciúma", "Athletico-PR"),
("Athletico-PR", "São Paulo"),
("São Paulo", "Athletico-PR"),
("Atlético-MG", "Bahia"),
("Bahia", "Atlético-MG"),
("Atlético-MG", "Botafogo"),
("Botafogo", "Atlético-MG"),
("Atlético-MG", "Vitória"),
("Vitória", "Atlético-MG"),
("Atlético-MG", "Cruzeiro"),
("Cruzeiro", "Atlético-MG"),
("Atlético-MG", "Cuiabá"),
("Cuiabá", "Atlético-MG"),
("Atlético-MG", "Flamengo"),
("Flamengo", "Atlético-MG"),
("Atlético-MG", "Fluminense"),
("Fluminense", "Atlético-MG"),
("Atlético-MG", "Fortaleza"),
("Fortaleza", "Atlético-MG"),
("Atlético-MG", "Juventude"),
("Juventude", "Atlético-MG"),
("Atlético-MG", "Grêmio"),
("Grêmio", "Atlético-MG"),
("Atlético-MG", "Internacional"),
("Internacional", "Atlético-MG"),
("Atlético-MG", "RB Bragantino"),
("RB Bragantino", "Atlético-MG"),
("Atlético-MG", "Criciúma"),
("Criciúma", "Atlético-MG"),
("Atlético-MG", "São Paulo"),
("São Paulo", "Atlético-MG"),
("Bahia", "Botafogo"),
("Botafogo", "Bahia"),
("Bahia", "Vitória"),
("Vitória", "Bahia"),
("Bahia", "Cruzeiro"),
("Cruzeiro", "Bahia"),
("Bahia", "Cuiabá"),
("Cuiabá", "Bahia"),
("Bahia", "Flamengo"),
("Flamengo", "Bahia"),
("Bahia", "Fluminense"),
("Fluminense", "Bahia"),
("Bahia", "Fortaleza"),
("Fortaleza", "Bahia"),
("Bahia", "Juventude"),
("Juventude", "Bahia"),
("Bahia", "Grêmio"),
("Grêmio", "Bahia"),
("Bahia", "Internacional"),
("Internacional", "Bahia"),
("Bahia", "RB Bragantino"),
("RB Bragantino", "Bahia"),
("Bahia", "Criciúma"),
("Criciúma", "Bahia"),
("Bahia", "São Paulo"),
("São Paulo", "Bahia"),
("Botafogo", "Vitória"),
("Vitória", "Botafogo"),
("Botafogo", "Cruzeiro"),
("Cruzeiro", "Botafogo"),
("Botafogo", "Cuiabá"),
("Cuiabá", "Botafogo"),
("Botafogo", "Flamengo"),
("Flamengo", "Botafogo"),
("Botafogo", "Fluminense"),
("Fluminense", "Botafogo"),
("Botafogo", "Fortaleza"),
("Fortaleza", "Botafogo"),
("Botafogo", "Juventude"),
("Juventude", "Botafogo"),
("Botafogo", "Grêmio"),
("Grêmio", "Botafogo"),
("Botafogo", "Internacional"),
("Internacional", "Botafogo"),
("Botafogo", "RB Bragantino"),
("RB Bragantino", "Botafogo"),
("Botafogo", "Criciúma"),
("Criciúma", "Botafogo"),
("Botafogo", "São Paulo"),
("São Paulo", "Botafogo"),
("Vitória", "Cruzeiro"),
("Cruzeiro", "Vitória"),
("Vitória", "Cuiabá"),
("Cuiabá", "Vitória"),
("Vitória", "Flamengo"),
("Flamengo", "Vitória"),
("Vitória", "Fluminense"),
("Fluminense", "Vitória"),
("Vitória", "Fortaleza"),
("Fortaleza", "Vitória"),
("Vitória", "Juventude"),
("Juventude", "Vitória"),
("Vitória", "Grêmio"),
("Grêmio", "Vitória"),
("Vitória", "Internacional"),
("Internacional", "Vitória"),
("Vitória", "RB Bragantino"),
("RB Bragantino", "Vitória"),
("Vitória", "Criciúma"),
("Criciúma", "Vitória"),
("Vitória", "São Paulo"),
("São Paulo", "Vitória"),
("Cruzeiro", "Cuiabá"),
("Cuiabá", "Cruzeiro"),
("Cruzeiro", "Flamengo"),
("Flamengo", "Cruzeiro"),
("Cruzeiro", "Fluminense"),
("Fluminense", "Cruzeiro"),
("Cruzeiro", "Fortaleza"),
("Fortaleza", "Cruzeiro"),
("Cruzeiro", "Juventude"),
("Juventude", "Cruzeiro"),
("Cruzeiro", "Grêmio"),
("Grêmio", "Cruzeiro"),
("Cruzeiro", "Internacional"),
("Internacional", "Cruzeiro"),
("Cruzeiro", "RB Bragantino"),
("RB Bragantino", "Cruzeiro"),
("Cruzeiro", "Criciúma"),
("Criciúma", "Cruzeiro"),
("Cruzeiro", "São Paulo"),
("São Paulo", "Cruzeiro"),
("Cuiabá", "Flamengo"),
("Flamengo", "Cuiabá"),
("Cuiabá", "Fluminense"),
("Fluminense", "Cuiabá"),
("Cuiabá", "Fortaleza"),
("Fortaleza", "Cuiabá"),
("Cuiabá", "Juventude"),
("Juventude", "Cuiabá"),
("Cuiabá", "Grêmio"),
("Grêmio", "Cuiabá"),
("Cuiabá", "Internacional"),
("Internacional", "Cuiabá"),
("Cuiabá", "RB Bragantino"),
("RB Bragantino", "Cuiabá"),
("Cuiabá", "Criciúma"),
("Criciúma", "Cuiabá"),
("Cuiabá", "São Paulo"),
("São Paulo", "Cuiabá"),
("Flamengo", "Fluminense"),
("Fluminense", "Flamengo"),
("Flamengo", "Fortaleza"),
("Fortaleza", "Flamengo"),
("Flamengo", "Juventude"),
("Juventude", "Flamengo"),
("Flamengo", "Grêmio"),
("Grêmio", "Flamengo"),
("Flamengo", "Internacional"),
("Internacional", "Flamengo"),
("Flamengo", "RB Bragantino"),
("RB Bragantino", "Flamengo"),
("Flamengo", "Criciúma"),
("Criciúma", "Flamengo"),
("Flamengo", "São Paulo"),
("São Paulo", "Flamengo"),
("Fluminense", "Fortaleza"),
("Fortaleza", "Fluminense"),
("Fluminense", "Juventude"),
("Juventude", "Fluminense"),
("Fluminense", "Grêmio"),
("Grêmio", "Fluminense"),
("Fluminense", "Internacional"),
("Internacional", "Fluminense"),
("Fluminense", "RB Bragantino"),
("RB Bragantino", "Fluminense"),
("Fluminense", "Criciúma"),
("Criciúma", "Fluminense"),
("Fluminense", "São Paulo"),
("São Paulo", "Fluminense"),
("Fortaleza", "Juventude"),
("Juventude", "Fortaleza"),
("Fortaleza", "Grêmio"),
("Grêmio", "Fortaleza"),
("Fortaleza", "Internacional"),
("Internacional", "Fortaleza"),
("Fortaleza", "RB Bragantino"),
("RB Bragantino", "Fortaleza"),
("Fortaleza", "Criciúma"),
("Criciúma", "Fortaleza"),
("Fortaleza", "São Paulo"),
("São Paulo", "Fortaleza"),
("Juventude", "Grêmio"),
("Grêmio", "Juventude"),
("Juventude", "Internacional"),
("Internacional", "Juventude"),
("Juventude", "RB Bragantino"),
("RB Bragantino", "Juventude"),
("Juventude", "Criciúma"),
("Criciúma", "Juventude"),
("Juventude", "São Paulo"),
("São Paulo", "Juventude"),
("Grêmio", "Internacional"),
("Internacional", "Grêmio"),
("Grêmio", "RB Bragantino"),
("RB Bragantino", "Grêmio"),
("Grêmio", "Criciúma"),
("Criciúma", "Grêmio"),
("Grêmio", "São Paulo"),
("São Paulo", "Grêmio"),
("Internacional", "RB Bragantino"),
("RB Bragantino", "Internacional"),
("Internacional", "Criciúma"),
("Criciúma", "Internacional"),
("Internacional", "São Paulo"),
("São Paulo", "Internacional"),
("RB Bragantino", "Criciúma"),
("Criciúma", "RB Bragantino"),
("RB Bragantino", "São Paulo"),
("São Paulo", "RB Bragantino"),
("Criciúma", "São Paulo"),
("São Paulo", "Criciúma"),
    ]
    elif edicao == 2025:
        confrontoss=[
            ('Mirassol', 'Vasco da Gama') ,
('Ceará-SC', 'São Paulo') ,
('Atlético-MG', 'Sport-Recife') ,
('Bahia', 'RB Bragantino') ,
('Botafogo', 'Palmeiras') ,
('Corinthians', 'Internacional') ,
('Vitória', 'Grêmio') ,
('Cruzeiro', 'Juventude') ,
('Santos', 'Fortaleza') ,
('Flamengo', 'Fluminense') ,
('Mirassol', 'São Paulo') ,
('Vasco da Gama', 'Sport-Recife') ,
('Ceará-SC', 'RB Bragantino') ,
('Atlético-MG', 'Palmeiras') ,
('Bahia', 'Internacional') ,
('Botafogo', 'Grêmio') ,
('Corinthians', 'Juventude') ,
('Vitória', 'Fortaleza') ,
('Cruzeiro', 'Fluminense') ,
('Santos', 'Flamengo') ,
('Mirassol', 'Sport-Recife') ,
('São Paulo', 'RB Bragantino') ,
('Vasco da Gama', 'Palmeiras') ,
('Ceará-SC', 'Internacional') ,
('Atlético-MG', 'Grêmio') ,
('Bahia', 'Juventude') ,
('Botafogo', 'Fortaleza') ,
('Corinthians', 'Fluminense') ,
('Vitória', 'Flamengo') ,
('Cruzeiro', 'Santos') ,
('Mirassol', 'RB Bragantino') ,
('Sport-Recife', 'Palmeiras') ,
('São Paulo', 'Internacional') ,
('Vasco da Gama', 'Grêmio') ,
('Ceará-SC', 'Juventude') ,
('Atlético-MG', 'Fortaleza') ,
('Bahia', 'Fluminense') ,
('Botafogo', 'Flamengo') ,
('Corinthians', 'Santos') ,
('Vitória', 'Cruzeiro') ,
('Mirassol', 'Palmeiras') ,
('RB Bragantino', 'Internacional') ,
('Sport-Recife', 'Grêmio') ,
('São Paulo', 'Juventude') ,
('Vasco da Gama', 'Fortaleza') ,
('Ceará-SC', 'Fluminense') ,
('Atlético-MG', 'Flamengo') ,
('Bahia', 'Santos') ,
('Botafogo', 'Cruzeiro') ,
('Corinthians', 'Vitória') ,
('Mirassol', 'Internacional') ,
('Palmeiras', 'Grêmio') ,
('RB Bragantino', 'Juventude') ,
('Sport-Recife', 'Fortaleza') ,
('São Paulo', 'Fluminense') ,
('Vasco da Gama', 'Flamengo') ,
('Ceará-SC', 'Santos') ,
('Atlético-MG', 'Cruzeiro') ,
('Bahia', 'Vitória') ,
('Botafogo', 'Corinthians') ,
('Mirassol', 'Grêmio') ,
('Internacional', 'Juventude') ,
('Palmeiras', 'Fortaleza') ,
('RB Bragantino', 'Fluminense') ,
('Sport-Recife', 'Flamengo') ,
('São Paulo', 'Santos') ,
('Vasco da Gama', 'Cruzeiro') ,
('Ceará-SC', 'Vitória') ,
('Atlético-MG', 'Corinthians') ,
('Bahia', 'Botafogo') ,
('Mirassol', 'Juventude') ,
('Grêmio', 'Fortaleza') ,
('Internacional', 'Fluminense') ,
('Palmeiras', 'Flamengo') ,
('RB Bragantino', 'Santos') ,
('Sport-Recife', 'Cruzeiro') ,
('São Paulo', 'Vitória') ,
('Vasco da Gama', 'Corinthians') ,
('Ceará-SC', 'Botafogo') ,
('Atlético-MG', 'Bahia') ,
('Mirassol', 'Fortaleza') ,
('Juventude', 'Fluminense') ,
('Grêmio', 'Flamengo') ,
('Internacional', 'Santos') ,
('Palmeiras', 'Cruzeiro') ,
('RB Bragantino', 'Vitória') ,
('Sport-Recife', 'Corinthians') ,
('São Paulo', 'Botafogo') ,
('Vasco da Gama', 'Bahia') ,
('Ceará-SC', 'Atlético-MG') ,
('Mirassol', 'Fluminense') ,
('Fortaleza', 'Flamengo') ,
('Juventude', 'Santos') ,
('Grêmio', 'Cruzeiro') ,
('Internacional', 'Vitória') ,
('Palmeiras', 'Corinthians') ,
('RB Bragantino', 'Botafogo') ,
('Sport-Recife', 'Bahia') ,
('São Paulo', 'Atlético-MG') ,
('Vasco da Gama', 'Ceará-SC') ,
('Mirassol', 'Flamengo') ,
('Fluminense', 'Santos') ,
('Fortaleza', 'Cruzeiro') ,
('Juventude', 'Vitória') ,
('Grêmio', 'Corinthians') ,
('Internacional', 'Botafogo') ,
('Palmeiras', 'Bahia') ,
('RB Bragantino', 'Atlético-MG') ,
('Sport-Recife', 'Ceará-SC') ,
('São Paulo', 'Vasco da Gama') ,
('Mirassol', 'Santos') ,
('Flamengo', 'Cruzeiro') ,
('Fluminense', 'Vitória') ,
('Fortaleza', 'Corinthians') ,
('Juventude', 'Botafogo') ,
('Grêmio', 'Bahia') ,
('Internacional', 'Atlético-MG') ,
('Palmeiras', 'Ceará-SC') ,
('RB Bragantino', 'Vasco da Gama') ,
('Sport-Recife', 'São Paulo') ,
('Mirassol', 'Cruzeiro') ,
('Santos', 'Vitória') ,
('Flamengo', 'Corinthians') ,
('Fluminense', 'Botafogo') ,
('Fortaleza', 'Bahia') ,
('Juventude', 'Atlético-MG') ,
('Grêmio', 'Ceará-SC') ,
('Internacional', 'Vasco da Gama') ,
('Palmeiras', 'São Paulo') ,
('RB Bragantino', 'Sport-Recife') ,
('Mirassol', 'Vitória') ,
('Cruzeiro', 'Corinthians') ,
('Santos', 'Botafogo') ,
('Flamengo', 'Bahia') ,
('Fluminense', 'Atlético-MG') ,
('Fortaleza', 'Ceará-SC') ,
('Juventude', 'Vasco da Gama') ,
('Grêmio', 'São Paulo') ,
('Internacional', 'Sport-Recife') ,
('Palmeiras', 'RB Bragantino') ,
('Mirassol', 'Corinthians') ,
('Vitória', 'Botafogo') ,
('Cruzeiro', 'Bahia') ,
('Santos', 'Atlético-MG') ,
('Flamengo', 'Ceará-SC') ,
('Fluminense', 'Vasco da Gama') ,
('Fortaleza', 'São Paulo') ,
('Juventude', 'Sport-Recife') ,
('Grêmio', 'RB Bragantino') ,
('Internacional', 'Palmeiras') ,
('Mirassol', 'Botafogo') ,
('Corinthians', 'Bahia') ,
('Vitória', 'Atlético-MG') ,
('Cruzeiro', 'Ceará-SC') ,
('Santos', 'Vasco da Gama') ,
('Flamengo', 'São Paulo') ,
('Fluminense', 'Sport-Recife') ,
('Fortaleza', 'RB Bragantino') ,
('Juventude', 'Palmeiras') ,
('Grêmio', 'Internacional') ,
('Mirassol', 'Bahia') ,
('Botafogo', 'Atlético-MG') ,
('Corinthians', 'Ceará-SC') ,
('Vitória', 'Vasco da Gama') ,
('Cruzeiro', 'São Paulo') ,
('Santos', 'Sport-Recife') ,
('Flamengo', 'RB Bragantino') ,
('Fluminense', 'Palmeiras') ,
('Fortaleza', 'Internacional') ,
('Juventude', 'Grêmio') ,
('Mirassol', 'Atlético-MG') ,
('Bahia', 'Ceará-SC') ,
('Botafogo', 'Vasco da Gama') ,
('Corinthians', 'São Paulo') ,
('Vitória', 'Sport-Recife') ,
('Cruzeiro', 'RB Bragantino') ,
('Santos', 'Palmeiras') ,
('Flamengo', 'Internacional') ,
('Fluminense', 'Grêmio') ,
('Fortaleza', 'Juventude') ,
('Mirassol', 'Ceará-SC') ,
('Atlético-MG', 'Vasco da Gama') ,
('Bahia', 'São Paulo') ,
('Botafogo', 'Sport-Recife') ,
('Corinthians', 'RB Bragantino') ,
('Vitória', 'Palmeiras') ,
('Cruzeiro', 'Internacional') ,
('Santos', 'Grêmio') ,
('Flamengo', 'Juventude') ,
('Fluminense', 'Fortaleza') ,
('Vasco da Gama', 'Mirassol') ,
('São Paulo', 'Ceará-SC') ,
('Sport-Recife', 'Atlético-MG') ,
('RB Bragantino', 'Bahia') ,
('Palmeiras', 'Botafogo') ,
('Internacional', 'Corinthians') ,
('Grêmio', 'Vitória') ,
('Juventude', 'Cruzeiro') ,
('Fortaleza', 'Santos') ,
('Fluminense', 'Flamengo') ,
('São Paulo', 'Mirassol') ,
('Sport-Recife', 'Vasco da Gama') ,
('RB Bragantino', 'Ceará-SC') ,
('Palmeiras', 'Atlético-MG') ,
('Internacional', 'Bahia') ,
('Grêmio', 'Botafogo') ,
('Juventude', 'Corinthians') ,
('Fortaleza', 'Vitória') ,
('Fluminense', 'Cruzeiro') ,
('Flamengo', 'Santos') ,
('Sport-Recife', 'Mirassol') ,
('RB Bragantino', 'São Paulo') ,
('Palmeiras', 'Vasco da Gama') ,
('Internacional', 'Ceará-SC') ,
('Grêmio', 'Atlético-MG') ,
('Juventude', 'Bahia') ,
('Fortaleza', 'Botafogo') ,
('Fluminense', 'Corinthians') ,
('Flamengo', 'Vitória') ,
('Santos', 'Cruzeiro') ,
('RB Bragantino', 'Mirassol') ,
('Palmeiras', 'Sport-Recife') ,
('Internacional', 'São Paulo') ,
('Grêmio', 'Vasco da Gama') ,
('Juventude', 'Ceará-SC') ,
('Fortaleza', 'Atlético-MG') ,
('Fluminense', 'Bahia') ,
('Flamengo', 'Botafogo') ,
('Santos', 'Corinthians') ,
('Cruzeiro', 'Vitória') ,
('Palmeiras', 'Mirassol') ,
('Internacional', 'RB Bragantino') ,
('Grêmio', 'Sport-Recife') ,
('Juventude', 'São Paulo') ,
('Fortaleza', 'Vasco da Gama') ,
('Fluminense', 'Ceará-SC') ,
('Flamengo', 'Atlético-MG') ,
('Santos', 'Bahia') ,
('Cruzeiro', 'Botafogo') ,
('Vitória', 'Corinthians') ,
('Internacional', 'Mirassol') ,
('Grêmio', 'Palmeiras') ,
('Juventude', 'RB Bragantino') ,
('Fortaleza', 'Sport-Recife') ,
('Fluminense', 'São Paulo') ,
('Flamengo', 'Vasco da Gama') ,
('Santos', 'Ceará-SC') ,
('Cruzeiro', 'Atlético-MG') ,
('Vitória', 'Bahia') ,
('Corinthians', 'Botafogo') ,
('Grêmio', 'Mirassol') ,
('Juventude', 'Internacional') ,
('Fortaleza', 'Palmeiras') ,
('Fluminense', 'RB Bragantino') ,
('Flamengo', 'Sport-Recife') ,
('Santos', 'São Paulo') ,
('Cruzeiro', 'Vasco da Gama') ,
('Vitória', 'Ceará-SC') ,
('Corinthians', 'Atlético-MG') ,
('Botafogo', 'Bahia') ,
('Juventude', 'Mirassol') ,
('Fortaleza', 'Grêmio') ,
('Fluminense', 'Internacional') ,
('Flamengo', 'Palmeiras') ,
('Santos', 'RB Bragantino') ,
('Cruzeiro', 'Sport-Recife') ,
('Vitória', 'São Paulo') ,
('Corinthians', 'Vasco da Gama') ,
('Botafogo', 'Ceará-SC') ,
('Bahia', 'Atlético-MG') ,
('Fortaleza', 'Mirassol') ,
('Fluminense', 'Juventude') ,
('Flamengo', 'Grêmio') ,
('Santos', 'Internacional') ,
('Cruzeiro', 'Palmeiras') ,
('Vitória', 'RB Bragantino') ,
('Corinthians', 'Sport-Recife') ,
('Botafogo', 'São Paulo') ,
('Bahia', 'Vasco da Gama') ,
('Atlético-MG', 'Ceará-SC') ,
('Fluminense', 'Mirassol') ,
('Flamengo', 'Fortaleza') ,
('Santos', 'Juventude') ,
('Cruzeiro', 'Grêmio') ,
('Vitória', 'Internacional') ,
('Corinthians', 'Palmeiras') ,
('Botafogo', 'RB Bragantino') ,
('Bahia', 'Sport-Recife') ,
('Atlético-MG', 'São Paulo') ,
('Ceará-SC', 'Vasco da Gama') ,
('Flamengo', 'Mirassol') ,
('Santos', 'Fluminense') ,
('Cruzeiro', 'Fortaleza') ,
('Vitória', 'Juventude') ,
('Corinthians', 'Grêmio') ,
('Botafogo', 'Internacional') ,
('Bahia', 'Palmeiras') ,
('Atlético-MG', 'RB Bragantino') ,
('Ceará-SC', 'Sport-Recife') ,
('Vasco da Gama', 'São Paulo') ,
('Santos', 'Mirassol') ,
('Cruzeiro', 'Flamengo') ,
('Vitória', 'Fluminense') ,
('Corinthians', 'Fortaleza') ,
('Botafogo', 'Juventude') ,
('Bahia', 'Grêmio') ,
('Atlético-MG', 'Internacional') ,
('Ceará-SC', 'Palmeiras') ,
('Vasco da Gama', 'RB Bragantino') ,
('São Paulo', 'Sport-Recife') ,
('Cruzeiro', 'Mirassol') ,
('Vitória', 'Santos') ,
('Corinthians', 'Flamengo') ,
('Botafogo', 'Fluminense') ,
('Bahia', 'Fortaleza') ,
('Atlético-MG', 'Juventude') ,
('Ceará-SC', 'Grêmio') ,
('Vasco da Gama', 'Internacional') ,
('São Paulo', 'Palmeiras') ,
('Sport-Recife', 'RB Bragantino') ,
('Vitória', 'Mirassol') ,
('Corinthians', 'Cruzeiro') ,
('Botafogo', 'Santos') ,
('Bahia', 'Flamengo') ,
('Atlético-MG', 'Fluminense') ,
('Ceará-SC', 'Fortaleza') ,
('Vasco da Gama', 'Juventude') ,
('São Paulo', 'Grêmio') ,
('Sport-Recife', 'Internacional') ,
('RB Bragantino', 'Palmeiras') ,
('Corinthians', 'Mirassol') ,
('Botafogo', 'Vitória') ,
('Bahia', 'Cruzeiro') ,
('Atlético-MG', 'Santos') ,
('Ceará-SC', 'Flamengo') ,
('Vasco da Gama', 'Fluminense') ,
('São Paulo', 'Fortaleza') ,
('Sport-Recife', 'Juventude') ,
('RB Bragantino', 'Grêmio') ,
('Palmeiras', 'Internacional') ,
('Botafogo', 'Mirassol') ,
('Bahia', 'Corinthians') ,
('Atlético-MG', 'Vitória') ,
('Ceará-SC', 'Cruzeiro') ,
('Vasco da Gama', 'Santos') ,
('São Paulo', 'Flamengo') ,
('Sport-Recife', 'Fluminense') ,
('RB Bragantino', 'Fortaleza') ,
('Palmeiras', 'Juventude') ,
('Internacional', 'Grêmio') ,
('Bahia', 'Mirassol') ,
('Atlético-MG', 'Botafogo') ,
('Ceará-SC', 'Corinthians') ,
('Vasco da Gama', 'Vitória') ,
('São Paulo', 'Cruzeiro') ,
('Sport-Recife', 'Santos') ,
('RB Bragantino', 'Flamengo') ,
('Palmeiras', 'Fluminense') ,
('Internacional', 'Fortaleza') ,
('Grêmio', 'Juventude') ,
('Atlético-MG', 'Mirassol') ,
('Ceará-SC', 'Bahia') ,
('Vasco da Gama', 'Botafogo') ,
('São Paulo', 'Corinthians') ,
('Sport-Recife', 'Vitória') ,
('RB Bragantino', 'Cruzeiro') ,
('Palmeiras', 'Santos') ,
('Internacional', 'Flamengo') ,
('Grêmio', 'Fluminense') ,
('Juventude', 'Fortaleza') ,
('Ceará-SC', 'Mirassol') ,
('Vasco da Gama', 'Atlético-MG') ,
('São Paulo', 'Bahia') ,
('Sport-Recife', 'Botafogo') ,
('RB Bragantino', 'Corinthians') ,
('Palmeiras', 'Vitória') ,
('Internacional', 'Cruzeiro') ,
('Grêmio', 'Santos') ,
('Juventude', 'Flamengo') ,
('Fortaleza', 'Fluminense'),
        ]
        
        
        
        
        
    rm.shuffle(confrontoss)
    todososjogos = []
    for confrontos in confrontoss:
     todososjogos.append(confrontos)
    return todososjogos
    
def tela_inicial():
    global frame_times, labels_times, rodadas_label, btn_simular, rodadas, abrir_tela_jogos, label_introducao, rodadas_label, btn_simular

    tela_inicial = tk.Tk()
    tela_inicial.configure(bg="#1c1c1c")  
    tela_inicial.title("Simulator Brasileirão")
    tela_inicial.attributes("-fullscreen", True)
    
    font_titulo = tkFont.Font(family="Arial", size=24, weight="bold")
    font_btn = tkFont.Font(family="Arial", size=14, weight="bold")
    font_texto = tkFont.Font(family="Arial", size=16)

    btn_fechar = tk.Button(tela_inicial, text=" X ", command=tela_inicial.destroy, bg="#ff5c5c", fg="white", font=font_btn, relief="flat")
    btn_fechar.place(relx=1.0, y=10, anchor='ne')

    btn_config = tk.Button(tela_inicial, text="⚙️", command=config_tela, bg="#ffba08", fg="black", font=font_btn, relief="flat")
    btn_config.place(relx=0.97, y=10, anchor='ne')

    label_introducao = tk.Label(tela_inicial, text="Bem-vindo ao Simulador de Brasileirão", bg="#1c1c1c", fg="white", font=font_titulo)
    label_introducao.pack(pady=(50, 20))

    frame_times = tk.Frame(tela_inicial, bg="#2c2c2c", bd=2, relief="groove")
    frame_times.pack(pady=20, padx=50, fill="x")

    labels_times = {}

    rodadas_label = tk.Label(tela_inicial, text=f"Rodadas restantes: {rodadas}", bg="#1c1c1c", fg="#d3d3d3", font=font_texto)
    rodadas_label.pack(pady=10)

    btn_simular = tk.Button(tela_inicial, text="Simular Próxima Rodada", command=simular_rodada, bg="#00aaff", fg="white", font=font_btn, bd=0, padx=20, pady=5)
    btn_simular.pack(pady=10)

    abrir_tela_jogos = tk.Button(tela_inicial, text="Abrir telas De Jogos", command=criar_tela_jogos, bg="#ff8c42", fg="white", font=font_btn, bd=0, padx=20, pady=5)
    abrir_tela_jogos.pack(pady=10)
    
    tela_inicial.mainloop()

def iniciar_simulacao(nome_arquivo="placares_jogos.txt"):
    if os.path.exists(nome_arquivo):
        os.remove(nome_arquivo)
        print(f"Arquivo '{nome_arquivo}' excluído para nova simulação.")
iniciar_simulacao()
def simular_rodada():
    global rodadas, rodada_atual
    if rodada_atual < total_rodadas:
        with open("placares_jogos.txt", "a") as arquivo:
            arquivo.write(f"Rodada {rodada_atual + 1}\n")
        
        for i in range(10): 
            index = rodada_atual * 10 + i
            if index < len(confrontos):
                time1, time2 = confrontos[index]
                simular_jogo(time1, time2)

        organizar_tabela()
        rodada_atual += 1
        rodadas -= 1
        if idioma_selecionado == 'Português':
         rodadas_label.config(text=f"Rodadas restantes: {rodadas}")
        elif idioma_selecionado == 'Inglês':
         rodadas_label.config(text=f"Rounds remaining: {rodadas}")
        elif idioma_selecionado == 'Alemão':
         rodadas_label.config(text=f"verbleibende Runden: {rodadas}")
        if rodadas == 0:
            parabenizar_campeao()
    else:
        messagebox.showinfo("Fim do Campeonato", "O campeonato chegou ao fim!")

def simular_jogo(time1, time2, nome_arquivo="placares_jogos.txt"):
    chances_time1 = times[time1][3]  
    chances_time2 = times[time2][3]  
    gols_defendidos1 = times[time1][9]
    gols_defendidos2 = times[time2][9]

    gols_time1 = 0
    gols_time2 = 0
    defesas1 = 0
    defesas2 = 0

    for _ in range(chances_time1):
        if rm.choices([True, False], weights=[0.35, 0.65])[0]:  
            gols_time1 += 1

    for _ in range(chances_time2):
        if rm.choices([True, False], weights=[0.30, 0.70])[0]: 
            gols_time2 += 1

    for _ in range(gols_defendidos1):
        if rm.choices([True, False], weights=[0.2, 0.8])[0]:  
            defesas1 += 1

    for _ in range(gols_defendidos2):
        if rm.choices([True, False], weights=[0.15, 0.85])[0]: 
            defesas2 += 1

    if gols_time1 == 0:
        defesas2 = 0
    if gols_time2 == 0:
        defesas1 = 0

    gols_time1 = max(0, gols_time1 - defesas2)
    gols_time2 = max(0, gols_time2 - defesas1)
    
    times[time1][1] += gols_time1  
    times[time1][0] += gols_time2  
    times[time2][1] += gols_time2  
    times[time2][0] += gols_time1  

    if gols_time1 > gols_time2:
        times[time1][10] += 1
        times[time1][2] += 3  
        times[time1][5] += 1  
        times[time2][7] += 1  
    elif gols_time1 < gols_time2:
        times[time1][11] += 1
        times[time2][2] += 3  
        times[time2][5] += 1  
        times[time1][7] += 1 
    else:
        times[time1][2] += 1  
        times[time2][2] += 1  
        times[time1][6] += 1  
        times[time2][6] += 1  

    times[time1][8] += 1  
    times[time2][8] += 1  

    with open(nome_arquivo, "a") as arquivo:
        resultado = f"{time1} {gols_time1} x {gols_time2} {time2}\n"
        arquivo.write(resultado)

    resultado_time1 = f"{time1} {gols_time1} x {gols_time2} {time2}"
    resultado_time2 = f"{time1} {gols_time1} x {gols_time2} {time2}"
    jogos_por_time[time2].append(resultado_time1)
    jogos_por_time[time1].append(resultado_time2)

def organizar_tabela():
    global frame_times, label_time
 
   
    for widget in frame_times.winfo_children():
        widget.destroy()

    
    sorted_times = sorted(times.items(), key=lambda x: (x[1][2], x[1][1] - x[1][0]), reverse=True)

   
    for posicao, (time, stats) in enumerate(sorted_times, start=1):
        stats[4] = posicao  
        saldo_gols = stats[1] - stats[0] 

       
        if posicao <= 4:
            bg_color = "#2980b9"  
        elif posicao <= 6:
            bg_color = "#f39c12"  
        elif posicao <= 12:
            bg_color = "#27ae60"  
        elif posicao < 17:
            bg_color = "#1c1c1c"  
        else:
            bg_color = "#c0392b"  

        
        

       
        if idioma_selecionado == 'Inglês':
            texto_base = f"{posicao}º {time} | Games: {stats[8]} | Points: {stats[2]} | Wins: {stats[5]} | Draws: {stats[6]} | Loses: {stats[7]} | Goal difference: {saldo_gols} | Goals For: {stats[1]} | Goals Against: {stats[0]}"
        elif idioma_selecionado == 'Alemão':
            texto_base = f"{posicao}º {time} | Spiele: {stats[8]} | Punkte: {stats[2]} | Siege: {stats[5]} | Unentschieden: {stats[6]} | Niederlagen: {stats[7]} | Tordifferenz: {saldo_gols} | Tore: {stats[1]} | Gegentore: {stats[0]}"
        elif idioma_selecionado == 'Português':
            texto_base = f"{posicao}º {time} | Jogos: {stats[8]} | Pontos: {stats[2]} | Vitórias: {stats[5]} | Empates: {stats[6]} | Derrotas: {stats[7]} | Saldo: {saldo_gols} | Gols Feitos: {stats[1]} | Gols Tomados: {stats[0]}"
       
        label_time = tk.Label(
            frame_times,
            text=texto_base,
            bg=bg_color,
            fg="#ecf0f1", 
            font=("Helvetica", 10, "bold"),  
            padx=5,
            pady=2,
            relief="flat"
        )
        label_time.pack(anchor="w", fill="x", padx=5, pady=1)

        label_time.config(
            borderwidth=1,
            highlightbackground="#34495e",
            highlightcolor="#34495e",
            highlightthickness=1
        )
            
def parabenizar_campeao():
    global btn_simular
    sorted_times = sorted(times.items(), key=lambda x: (x[1][2], x[1][1] - x[1][0]), reverse=True)
    if idioma_selecionado == 'Português':
      for posicao, (time, stats) in enumerate(sorted_times, start=1):
        stats[4] = posicao
        if posicao == 1:
            messagebox.showinfo(
                title="Campeão definido",
                message=f"🎉 Parabéns! O campeão foi **{time}**! 🎉",
                icon='info'
            )
        btn_simular.config(
        text="Informações do campeonato",
        command=lambda: Informar(),
        bg='red',
        fg='white',  
        font=('Arial', 12, 'bold')
    )
    elif idioma_selecionado == 'Inglês':
      for posicao, (time, stats) in enumerate(sorted_times, start=1):
        stats[4] = posicao
        if posicao == 1:
            messagebox.showinfo(
                title="Champion decided",
                message=f"🎉 Congratiulation! The Champion is **{time}**! 🎉",
                icon='info'
            )
        btn_simular.config(
        text="Champioship infomations",
        command=lambda: Informar(),
        bg='red',
        fg='white',  
        font=('Arial', 12, 'bold')
    )
    elif idioma_selecionado == 'Alemão':
     for posicao, (time, stats) in enumerate(sorted_times, start=1):
        stats[4] = posicao
        if posicao == 1:
            messagebox.showinfo(
                title="Meister entschieden",
                message=f"🎉 Glückwunsch! Der Meister ist **{time}**! 🎉",
                icon='info'
            )
        btn_simular.config(
        text="Meisterschaftsinformationen",
        command=lambda: Informar(),
        bg='red',
        fg='white',  
        font=('Arial', 12, 'bold')
    )

def Informar():
    tela_informativa = tk.Tk()
    tela_informativa.configure(bg="#2c3e50")  
    tela_informativa.title("Informações da Simulação")
    tela_informativa.geometry('600x600')  
    titulo = tk.Label(tela_informativa, text="Resultados da Simulação", bg="#2c3e50", fg="#ecf0f1", font=('Arial', 18, 'bold'))
    titulo.pack(pady=(20, 10))

    sorted_times = sorted(times.items(), key=lambda x: (x[1][2], x[1][1] - x[1][0]), reverse=True)
    
    maiortomados = -1
    Golstomados = ""
    maior = -1  
    Artilheiro = ""
    maiorsaldo = -1
    saldoo = ""
    melhor_mandante = ""
    maior_mandante = -1
    for posicao, (time, stats) in enumerate(sorted_times, start=1):
        if stats[1] - stats[0] > maiorsaldo:
            maiorsaldo = stats[1] - stats[0]
            saldoo = time
        if stats[1] > maior: 
            maior = stats[1]
            Artilheiro = time  
        if stats[0] > maiortomados: 
            maiortomados = stats[0]
            Golstomados = time  
        if stats[10] > maior_mandante:
            maior_mandante = stats[10]
            melhor_mandante = time
    if idioma_selecionado == 'Português':
      for posicao, (time, stats) in enumerate(sorted_times, start=1):
        if posicao <= 4:
            label = tk.Label(tela_informativa, text=f"{posicao}° lugar: {time} com {stats[2]} pontos", bg="#27ae60", fg="white", font=('Arial', 12))
            label.pack(pady=(5, 5))
        if posicao >= 17:
            label = tk.Label(tela_informativa, text=f"O time que caiu no Z{(21 - posicao)} foi o {time} com {stats[2]} pontos", bg="#e74c3c", fg="white", font=('Arial', 12))
            label.pack(pady=(5, 5))
            
        
      stats_title = tk.Label(tela_informativa, text="Estatísticas Finais", bg="#34495e", fg="#ecf0f1", font=('Arial', 16, 'underline'))
      stats_title.pack(pady=(20, 10))
      
      labelArtilheiro = tk.Label(tela_informativa, text=f"O artilheiro do campeonato foi {Artilheiro} com {maior} gols", bg="#f39c12", fg="white", font=('Arial', 12))
      labelArtilheiro.pack(pady=(5, 5))
    
      labelTomados = tk.Label(tela_informativa, text=f"O time que tomou mais gols foi o {Golstomados} com {maiortomados} gols tomados", bg="#e67e22", fg="white", font=('Arial', 12))
      labelTomados.pack(pady=(5, 5))
    
      labelSaldo = tk.Label(tela_informativa, text=f"O time com maior saldo de gols foi {saldoo} com {maiorsaldo} de saldo de gols", bg="#8e44ad", fg="white", font=('Arial', 12))
      labelSaldo.pack(pady=(5, 5))
    
      labelMandante = tk.Label(tela_informativa, text=f"O time que ficou como melhor mandante foi {melhor_mandante} com {maior_mandante} vitórias em casa", bg="#2980b9", fg="white", font=('Arial', 12))
      labelMandante.pack(pady=(5, 5))

      fechar_btn = tk.Button(tela_informativa, text="Fechar", command=tela_informativa.destroy, bg="#c0392b", fg="white", font=('Arial', 12, 'bold'))
      fechar_btn.pack(pady=(20, 10))

      tela_informativa.mainloop()
    elif idioma_selecionado == 'Inglês':
        for posicao, (time, stats) in enumerate(sorted_times, start=1):
         if posicao <= 4:
            label = tk.Label(tela_informativa, text=f"{posicao}° place: {time} with {stats[2]} points", bg="#27ae60", fg="white", font=('Arial', 12))
            label.pack(pady=(5, 5))
         if posicao >= 17:
           label = tk.Label(tela_informativa, text=f"The team that was relegated to Z{(21 - posicao)} was {time} with {stats[2]} points", bg="#e74c3c", fg="white", font=('Arial', 12))
           label.pack(pady=(5, 5))
        

        stats_title = tk.Label(tela_informativa, text="Final Statistics", bg="#34495e", fg="#ecf0f1", font=('Arial', 16, 'underline'))
        stats_title.pack(pady=(20, 10))

        labelArtilheiro = tk.Label(tela_informativa, text=f"The top scorer of the championship was {Artilheiro} with {maior} goals", bg="#f39c12", fg="white", font=('Arial', 12))
        labelArtilheiro.pack(pady=(5, 5))

        labelTomados = tk.Label(tela_informativa, text=f"The team that conceded the most goals was {Golstomados} with {maiortomados} goals conceded", bg="#e67e22", fg="white", font=('Arial', 12))
        labelTomados.pack(pady=(5, 5))

        labelSaldo = tk.Label(tela_informativa, text=f"The team with the best goal difference was {saldoo} with {maiorsaldo} goal difference", bg="#8e44ad", fg="white", font=('Arial', 12))
        labelSaldo.pack(pady=(5, 5))

        labelMandante = tk.Label(tela_informativa, text=f"The best home team was {melhor_mandante} with {maior_mandante} home wins", bg="#2980b9", fg="white", font=('Arial', 12))
        labelMandante.pack(pady=(5, 5))

        fechar_btn = tk.Button(tela_informativa, text="Close", command=tela_informativa.destroy, bg="#c0392b", fg="white", font=('Arial', 12, 'bold'))
        fechar_btn.pack(pady=(20, 10))

        tela_informativa.mainloop()

      
    if idioma_selecionado == 'Alemão':
          for posicao, (time, stats) in enumerate(sorted_times, start=1):
           if posicao <= 4:
            label = tk.Label(tela_informativa, text=f"{posicao}. Platz: {time} mit {stats[2]} Punkten", bg="#27ae60", fg="white", font=('Arial', 12))
            label.pack(pady=(5, 5))

           if posicao >= 17:
            label = tk.Label(tela_informativa, text=f"Das Team, das in die Z{(21 - posicao)} abgestiegen ist, war {time} mit {stats[2]} Punkten", bg="#e74c3c", fg="white", font=('Arial', 12))
            label.pack(pady=(5, 5))
    
          stats_title = tk.Label(tela_informativa, text="Endstatistiken", bg="#34495e", fg="#ecf0f1", font=('Arial', 16, 'underline'))
          stats_title.pack(pady=(20, 10))

          labelArtilheiro = tk.Label(tela_informativa, text=f"Der Torschützenkönig des Turniers war {Artilheiro} mit {maior} Toren", bg="#f39c12", fg="white", font=('Arial', 12))
          labelArtilheiro.pack(pady=(5, 5))
    
          labelTomados = tk.Label(tela_informativa, text=f"Das Team, das die meisten Gegentore kassiert hat, war {Golstomados} mit {maiortomados} Gegentoren", bg="#e67e22", fg="white", font=('Arial', 12))
          labelTomados.pack(pady=(5, 5))
    
          labelSaldo = tk.Label(tela_informativa, text=f"Das Team mit der besten Tordifferenz war {saldoo} mit {maiorsaldo} Toren", bg="#8e44ad", fg="white", font=('Arial', 12))
          labelSaldo.pack(pady=(5, 5))
    
          labelMandante = tk.Label(tela_informativa, text=f"Das beste Heimteam war {melhor_mandante} mit {maior_mandante} Heimsiegen", bg="#2980b9", fg="white", font=('Arial', 12))
          labelMandante.pack(pady=(5, 5))

          fechar_btn = tk.Button(tela_informativa, text="Schließen", command=tela_informativa.destroy, bg="#c0392b", fg="white", font=('Arial', 12, 'bold'))
          fechar_btn.pack(pady=(20, 10))

          tela_informativa.mainloop()

def statsteams():
    global tela_times
    tela_times = tk.Toplevel()
    tela_times.title("Status dos Times")
    tela_times.configure(bg="#2c3e50")  
    tela_times.geometry("500x640")

    times_por_pagina = 5
    pagina_atual = [0]

    def exibir_times():
        global btn_anterior, btn_atualizar, btn_proximo
        for widget in tela_times.winfo_children():
            widget.destroy()

        inicio = pagina_atual[0] * times_por_pagina
        fim = inicio + times_por_pagina
        times_pagina = list(times.items())[inicio:fim]

        for nome_time, stats in times_pagina:
            frame_time = tk.Frame(tela_times, bg="#34495e")
            frame_time.pack(pady=5, padx=10, fill="x")

            tk.Label(frame_time, text=nome_time, bg="#34495e", fg="#ecf0f1", font=("Arial", 14, 'bold')).grid(row=0, column=0, sticky="w")
            if idioma_selecionado == "Português":
             tk.Label(frame_time, text="Ataque:", bg="#34495e", fg="white").grid(row=1, column=0, sticky="w")
             ataque = tk.Entry(frame_time, width=5)
             ataque.insert(0, stats[3])
             ataque.grid(row=1, column=1)

             tk.Label(frame_time, text="Defesa:", bg="#34495e", fg="white").grid(row=2, column=0, sticky="w")
             defesa = tk.Entry(frame_time, width=5)
             defesa.insert(0, stats[9])
             defesa.grid(row=2, column=1)

            elif idioma_selecionado == "Inglês":
                 tk.Label(frame_time, text="Attack:", bg="#34495e", fg="white").grid(row=1, column=0, sticky="w")
                 ataque = tk.Entry(frame_time, width=5)
                 ataque.insert(0, stats[3])
                 ataque.grid(row=1, column=1)

                 tk.Label(frame_time, text="Defense:", bg="#34495e", fg="white").grid(row=2, column=0, sticky="w")
                 defesa = tk.Entry(frame_time, width=5)
                 defesa.insert(0, stats[9])
                 defesa.grid(row=2, column=1)

            elif idioma_selecionado == "Alemão":
                 tk.Label(frame_time, text="Angriff:", bg="#34495e", fg="white").grid(row=1, column=0, sticky="w")
                 ataque = tk.Entry(frame_time, width=5)
                 ataque.insert(0, stats[3])
                 ataque.grid(row=1, column=1)

                 tk.Label(frame_time, text="Verteidigung:", bg="#34495e", fg="white").grid(row=2, column=0, sticky="w")
                 defesa = tk.Entry(frame_time, width=5)
                 defesa.insert(0, stats[9])
                 defesa.grid(row=2, column=1)

            global textt
            def atualizar_stats(nome=nome_time, atk_entry=ataque, def_entry=defesa):
                times[nome][3] = int(atk_entry.get())
                times[nome][9] = int(def_entry.get())
                if idioma_selecionado == 'Português':
                  times[nome][3] = int(atk_entry.get())
                  times[nome][9] = int(def_entry.get())
                  print(f"Time {nome}: Ataque = {times[nome][3]}, Defesa = {times[nome][9]}")
                elif idioma_selecionado == 'Inglês':
                  times[nome][3] = int(atk_entry.get())
                  times[nome][9] = int(def_entry.get())
                  print(f"Time {nome}: Attack = {times[nome][3]}, Defense = {times[nome][9]}")
                elif idioma_selecionado == "Alemão":
                  print(f"Mannschaft {nome}: Angriff = {times[nome][3]}, Verteidigung = {times[nome][9]}")
            if idioma_selecionado == 'Português':
             btn_atualizar = tk.Button(frame_time, text=f"Atualizar", command=atualizar_stats, bg="#f39c12", fg="black", font=("Arial", 10))
             btn_atualizar.grid(row=3, column=0, columnspan=2, pady=(5, 0))
            elif idioma_selecionado == 'Inglês':
             btn_atualizar = tk.Button(frame_time, text=f"Update", command=atualizar_stats, bg="#f39c12", fg="black", font=("Arial", 10))
             btn_atualizar.grid(row=3, column=0, columnspan=2, pady=(5, 0))  
            elif idioma_selecionado == "Alemão":
             btn_atualizar = tk.Button(frame_time, text=f"Aktualisieren", command=atualizar_stats, bg="#f39c12", fg="black", font=("Arial", 10))
             btn_atualizar.grid(row=3, column=0, columnspan=2, pady=(5, 0))    
                
        btn_frame = tk.Frame(tela_times, bg="#2c3e50")
        btn_frame.pack(pady=10)
        if idioma_selecionado == "Português":
          if pagina_atual[0] > 0:
            btn_anterior = tk.Button(btn_frame, text="Anterior", command=lambda: mudar_pagina(-1), bg="#2980b9", fg="white", font=("Arial", 12))
            btn_anterior.pack(side="left", padx=20)

          if fim < len(times):
            btn_proximo = tk.Button(btn_frame, text="Próximo", command=lambda: mudar_pagina(1), bg="#2980b9", fg="white", font=("Arial", 12))
            btn_proximo.pack(side="right", padx=20)
            
        if idioma_selecionado == "Inglês":
          if pagina_atual[0] > 0:
            btn_anterior = tk.Button(btn_frame, text="Previous", command=lambda: mudar_pagina(-1), bg="#2980b9", fg="white", font=("Arial", 12))
            btn_anterior.pack(side="left", padx=20)

          if fim < len(times):
            btn_proximo = tk.Button(btn_frame, text="Next", command=lambda: mudar_pagina(1), bg="#2980b9", fg="white", font=("Arial", 12))
            btn_proximo.pack(side="right", padx=20)
            
                   
        if idioma_selecionado == "Alemão":
          if pagina_atual[0] > 0:
           btn_anterior = tk.Button(btn_frame, text="Zurück", command=lambda: mudar_pagina(-1), bg="#2980b9", fg="white", font=("Arial", 12))
           btn_anterior.pack(side="left", padx=20)

          if fim < len(times):
              btn_proximo = tk.Button(btn_frame, text="Weiter", command=lambda: mudar_pagina(1), bg="#2980b9", fg="white", font=("Arial", 12))
              btn_proximo.pack(side="right", padx=20)

    def mudar_pagina(direcao):
        pagina_atual[0] += direcao
        exibir_times()

    exibir_times()

def selecionar_linguagem():
    global idioma_selecionado
    
    tela_linguagem = tk.Toplevel()
    tela_linguagem.title("Seleção de Idioma")
    tela_linguagem.geometry("400x300")
    tela_linguagem.configure(bg="#2c3e50")
    
    lbl_instrucao = tk.Label(tela_linguagem, text="Escolha um idioma:", font=("Arial", 16), bg="#2c3e50", fg="#ecf0f1")
    lbl_instrucao.pack(pady=20)
   #  label_aviso = tk.Label(
     #   tela_jogos,
      #  text=f"Total de jogos: {len(jogos)} (Máximo: {max_jogos})\n Posição do time: {times[time][4]}\n Vitorias em casa: {times[time][10]}\n Derrotas em casa: {times[time][11]}"
    def definir_idioma(idioma):
        global idioma_selecionado
        idioma_selecionado = idioma
        if idioma == "Inglês":
            btn_config_teams.config(text="Change team status")
            btn_colocar_time_5.config(text="Status 5 in teams")
            btn_colocar_time_6.config(text="Randomize Status")
            btn_colocar_time_7.config(text="Language")
            labelconfig1.config(text="Settings")
            label_introducao.config(text="Welcome to Brasileirão Simulator")
            if rodada_atual == 38:
               btn_simular.config(text="Championship Information")
            else:
               btn_simular.config(text="Simulate next round")
            abrir_tela_jogos.config(text="Open match history screen")
            rodadas_label.config(text=f"Rounds remaining: {rodadas}")
            organizar_tabela()
        elif idioma == "Alemão":
            btn_config_teams.config(text="Team-Status ändern")
            btn_colocar_time_5.config(text="Status 5 in Teams")
            btn_colocar_time_6.config(text="Status randomisieren")
            btn_colocar_time_7.config(text="Sprache")
            labelconfig1.config(text="Einstellungen")
            label_introducao.config(text="Willkommen im Brasileirão-Simulator")
            if rodada_atual == 38:
              btn_simular.config(text="Meisterschaftsinformationen")
            else:
              btn_simular.config(text="Nächste Runde simulieren")
            abrir_tela_jogos.config(text="Öffnen Sie die Spielbildschirme")
            rodadas_label.config(text=f"verbleibende Runden: {rodadas}")
            organizar_tabela()
        elif idioma == "Português":
            btn_config_teams.config(text="Mudar status dos times")
            btn_colocar_time_5.config(text="Status 5 em times")
            btn_colocar_time_6.config(text="Randomizar Status")
            btn_colocar_time_7.config(text="Linguagem")
            labelconfig1.config(text="Configurações")
            label_introducao.config(text="Bem-vindo ao Simulador de Brasileirão")
            if rodada_atual == 38:
               btn_simular.config(text="Informações do campeonato")
            else:
               btn_simular.config(text="Simular proxima rodada")
            abrir_tela_jogos.config(text="Abrir telas De Jogos")
            rodadas_label.config(text=f"Rodadas restantes: {rodadas}")
            organizar_tabela()
        tela_linguagem.destroy()
        fechar_tela_times()
        
        
    idiomas = ["Inglês", "Português", "Alemão"]
    for idioma in idiomas:
        btn = tk.Button(tela_linguagem, text=idioma, command=lambda i=idioma: [definir_idioma(i), organizar_tabela()],
                        bg="#2980b9", fg="white", font=("Arial", 14), relief="solid", bd=2)
        btn.pack(pady=10, fill="x", padx=40)
        

def config_tela():
    global tela_configuracao, btn_config_teams, labelconfig1, btn_colocar_time_5, btn_colocar_time_6, btn_colocar_time_7

        
        
    tela_configuracao = tk.Toplevel()
    tela_configuracao.configure(bg="#2c3e50")  
    tela_configuracao.title("Configurações")
    tela_configuracao.geometry('500x500')
    
    labelconfig1 = tk.Label(tela_configuracao, text="Configurações", bg="#2c3e50", fg="#ecf0f1", font=("Arial", 24, 'bold'))
    labelconfig1.pack(pady=20)
    
    btn_config_teams = tk.Button(tela_configuracao, text="Mudar status dos times", bg="#2980b9", fg="white", font=("Arial", 14), command=statsteams)
    btn_config_teams.pack(pady=20)
    
    btn_colocar_time_5 = tk.Button(tela_configuracao, text="Status 5 em times", bg="#2980b9", fg="white", font=("Arial", 14), command=stats5teams)
    btn_colocar_time_5.pack(pady=20)
    
    btn_colocar_time_6 = tk.Button(tela_configuracao, text="Randomizar Status", bg="#2980b9", fg="white", font=("Arial", 14), command=randomizestats)
    btn_colocar_time_6.pack(pady=20)
    
    btn_colocar_time_7 = tk.Button(tela_configuracao, text="Linguagem", bg="#2980b9", fg="white", command=selecionar_linguagem, font=("Arial", 14))
    btn_colocar_time_7.pack(pady=20)
    if idioma_selecionado == "Inglês":
         btn_config_teams.config(text="Change team status")
         btn_colocar_time_5.config(text="Status 5 in teams")
         btn_colocar_time_6.config(text="Randomize Status")
         btn_colocar_time_7.config(text="Language")
         labelconfig1.config(text="Settings")
         label_introducao.config(text="Welcome to Brasileirão Simulator")
         if rodada_atual == 38:
          btn_simular.config(text="Championship Information")
         else:
          btn_simular.config(text="Simulate next round")
         abrir_tela_jogos.config(text="Open match history screen")
         rodadas_label.config(text=f"Rounds remaining: {rodadas}")
    elif idioma_selecionado == "Alemão":
        btn_config_teams.config(text="Team-Status ändern")
        btn_colocar_time_5.config(text="Status 5 in Teams")
        btn_colocar_time_6.config(text="Status randomisieren")
        btn_colocar_time_7.config(text="Sprache")
        labelconfig1.config(text="Einstellungen")
        label_introducao.config(text="Willkommen im Brasileirão-Simulator")
        if rodada_atual == 38:
              btn_simular.config(text="Meisterschaftsinformationen")
        else:
              btn_simular.config(text="Nächste Runde simulieren")
        abrir_tela_jogos.config(text="Öffnen Sie die Spielbildschirme")
        rodadas_label.config(text=f"verbleibende Runden: {rodadas}")
    elif idioma_selecionado == "Português":
        btn_colocar_time_5.config(text="Status 5 em times")
        btn_colocar_time_6.config(text="Randomizar Status")
        btn_colocar_time_7.config(text="Linguagem")
        labelconfig1.config(text="Configurações")
        label_introducao.config(text="Bem-vindo ao Simulador de Brasileirão")
        btn_simular.config(text="Simular Proxima Rodada")
        abrir_tela_jogos.config(text="Abrir telas De Jogos")
        rodadas_label.config(text=f"Rodadas restantes: {rodadas}")

    tela_configuracao.mainloop()

def randomizestats():
    global times
    for team, stats in times.items():
        stats[3] = random.randint(1, 10)
        stats[9] = random.randint(1, 10)
        print(f"{team} updated - Attack: {stats[3]}, Defense: {stats[9]}")

def stats5teams():
    global times
    for team, stats in times.items():
        stats[3] = 5  
        stats[9] = 5 
        print(f"{team} updated - Attack: {stats[3]}, Defense: {stats[9]}")

def start_simulation():
    tela_inicial()

def fechar_tela_times():
    global tela_times
    if tela_times is not None and tela_times.winfo_exists():  # Verifica se a janela existe
        tela_times.destroy()  # Fecha a janela
        tela_times = None  # Reseta a variável para evitar referências inválidas







global Label_escolha_edicao
root = tk.Tk()

root.title("Select Championship Edition")
root.geometry("300x200")

tk.Label(root, text="Choose the Championship Edition:", font=("Arial", 12, "bold")).pack(pady=10)

btn_2024 = tk.Button(root, text="2024", font=("Arial", 12, "bold"), bg="#27AE60", fg="white", width=10, command=lambda: select_edition(2024))
btn_2024.pack(pady=5)

btn_2025 = tk.Button(root, text="2025", font=("Arial", 12, "bold"), bg="#E74C3C", fg="white", width=10, command=lambda: select_edition(2025))
btn_2025.pack(pady=5)

root.mainloop()
