from datetime import datetime, timedelta

# Obtenha a data atual
start_date = datetime.now()

# Inicialize a lista de intervalos de datas
date_ranges = []

# Itere 6 vezes para criar os intervalos de 30 dias retroativos
for i in range(6):
    # Calcule a data final subtraindo i * 30 dias da data atual
    start = start_date - timedelta(days=i * 30)
    # Calcule a data inicial subtraindo 30 dias da data final
    end = start - timedelta(days=30)
    # Adicione a tupla com o intervalo na lista de intervalos
    date_ranges.append((start.strftime("%Y-%m-%d"), end.strftime("%Y-%m-%d")))

# Exiba os intervalos de datas
for date_range in date_ranges:
    print(date_range)
