import requests

# Simulando uma API que retorna uma lista de várias máquinas de uma frota agrícola
# (Num sistema real, isto viria do comando requests.get("url_da_frota").json())
frota_tratores = [
    {"machine_id": "TRATOR-7R-001", "status": "Em operação", "fuel_level_percent": 85},
    {"machine_id": "TRATOR-8R-002", "status": "Manutenção", "fuel_level_percent": 20},
    {"machine_id": "PULVERIZADOR-4060", "status": "Em operação", "fuel_level_percent": 64},
    {"machine_id": "COLHEITADEIRA-S700", "status": "Parado", "fuel_level_percent": 90}
]

print("--- Relatório da Frota de Máquinas em Campo ---")

# O ciclo 'for' percorre cada dicionário (trator) dentro da lista um por um
for trator in frota_tratores:
    id_maquina = trator['machine_id']
    estado = trator['status']
    combustivel = trator['fuel_level_percent']
    
    # Imprimimos os dados formatados de cada máquina
    print(f"Máquina: {id_maquina} | Estado: {estado} | Combustível: {combustivel}%")