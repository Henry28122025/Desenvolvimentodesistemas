temperaturas = [45, 80, 50, 95, 40]

for x in temperaturas:
    if x > 70:
        print("Alerta: Ponto crítico detectado")
        x += 1
    else:
        print("Ponto OK")
        x += 1