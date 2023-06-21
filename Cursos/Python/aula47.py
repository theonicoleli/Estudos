def converter_tempo(segundos):

    horas = segundos // 3600
    minutos = (segundos % 3600) // 60
    segundos = segundos % 60
    
    return f"{horas}h {minutos}min {segundos}s"

tempo_em_segundos = 3665
tempo_formatado = converter_tempo(tempo_em_segundos)

print(f"O tempo {tempo_em_segundos} segundos equivale a {tempo_formatado}")