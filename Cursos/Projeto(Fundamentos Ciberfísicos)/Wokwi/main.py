import time
from machine import Pin

pino_lampada = Pin(14, Pin.OUT)
pino_trigger = Pin(23, Pin.OUT)
pino_echo = Pin(22, Pin.IN)
pino_movimento = Pin(4, Pin.IN)

#Calculo da distância
def medir_distancia():
    pino_trigger.on()
    time.sleep_us(10)
    pino_trigger.off()

    while pino_echo.value() == 0:
        pass
    tempo_inicial = time.ticks_us()

    while pino_echo.value() == 1:
        pass
    tempo_final = time.ticks_us()

    #Equanção para calcular a distância
    duracao = tempo_final - tempo_inicial
    distancia = duracao / 58.0

    return distancia

while True:
    #Detectar caso haja movimento
    movimento_detectado = pino_movimento.value()
    if movimento_detectado:
        distancia = medir_distancia()
        #Caso a distância seja menor que 45, ativa a luz do poste e manda a mensagem com o horário
        if distancia <= 50:
            pino_lampada.on()
            horario_atual = time.localtime()
            hora = horario_atual[3]
            minuto = horario_atual[4]
            segundo = horario_atual[5]
            horario_str = "{:02d}:{:02d}:{:02d}".format(hora, minuto, segundo)
            print("Movimento detectado dentro do limite de 50 metros! Acendendo luz! Horário de ativação:", horario_str)
        else:
            print("Movimento detectado além do limite de 50 metros! Luz desligada.")
            pino_lampada.off()
    else:
        print("Nenhum movimento detectado. Luz desligada.")
        pino_lampada.off()

    time.sleep(2)










