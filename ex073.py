#Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
#a) Os 5 primeiros times.
#b) Os últimos 4 colocados.
#c) Times em ordem alfabética.
#d) Em que posição está o time da Chapecoense.

times = ("Santos", "Atlético-MG", "Corinthias", "Cuiabá",
         "internacional", "Bragantino", "Palmeiras",
         "Flamengo", "Coritiba", "São Paulo", "Botafogo",
         "Fluminense", "América-MG", "Ceará SC", "Avaí",
         "Athletico-PR", "Atlético-GO", "Goiás", "Juventude",
         "Fortaleza")
print(f"Lista de times: {times}")
print("=-"*20)
print(f"Os cinco primeiros colocados são {times[:5]}")
print("=-"*20)
print(f"Os quatro últimos colocados são {times[-4:]}")
print("=-"*20)
print(f"Os times em ordem alfabética são: {sorted(times)}")
print("=-"*20)
print(f'O time da Chapecoense está na {times.index("Palmeiras")+1}ª posição.')