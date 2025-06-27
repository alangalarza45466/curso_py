partidos_ganados = 3
partidos_empatados = 1
partidos_perdidos = 0

partidos_ganados_puntos = partidos_ganados * 3
partidos_empatados_puntos = partidos_empatados * 1
partidos_perdidos_puntos = partidos_perdidos * 0

p = (partidos_ganados) + float(partidos_empatados) + float(partidos_perdidos)

print(f"partidos ganados,perdidos y empatados: {p}")