import matplotlib.pyplot as plt

# 1. Parámetros físicos de la habitación
temp_exterior = 10.0
temp_interior = 20.0
resistencia_termica = 0.05

# 2. Parámetros del Controlador PID COMPLETO
setpoint = 24.0
kp = 0.6         # DUPLICAMOS la potencia inicial (antes 0.3) para que suba rapidísimo
ki = 0.015       # Aumentamos la memoria para que mantenga el ritmo
kd = 0.1         # REDUCIMOS el freno a la mitad (antes 0.2) para evitar la caída brusca
acumulacion_error = 0.0
error_previo = 0.0  # NUEVO: Memoria del error en el minuto anterior

tiempo = []
registro_temperatura = []
registro_setpoint = []

# 3. Bucle de simulación (100 minutos)
for minuto in range(100):
    # Calculamos el error actual
    error = setpoint - temp_interior
    
    # Acción Integral (Acumula)
    acumulacion_error = acumulacion_error + error
    
    # NUEVO: Acción Derivativa (Velocidad de cambio)
    derivada_error = error - error_previo
    
    # NUEVO: La potencia suma las 3 fuerzas (P + I + D)
    potencia_calefactor = (kp * error) + (ki * acumulacion_error) + (kd * derivada_error)
    
    # NUEVO: Guardamos el error actual para usarlo como "previo" en el próximo minuto
    error_previo = error
    
    # La física de la habitación
    perdida_calor = (temp_interior - temp_exterior) * resistencia_termica
    temp_interior = temp_interior + potencia_calefactor - perdida_calor
    
    tiempo.append(minuto)
    registro_temperatura.append(temp_interior)
    registro_setpoint.append(setpoint)

# 4. Generar gráficos
plt.plot(tiempo, registro_temperatura, label="Temp. Interior (PID Completo)", color="blue")
plt.plot(tiempo, registro_setpoint, label="Objetivo (Setpoint 24°C)", color="green", linestyle="--")
plt.axhline(y=temp_exterior, color='red', linestyle=':', label="Temp. Exterior (10°C)")
plt.title("Control PID Completo de Temperatura")
plt.xlabel("Tiempo (minutos)")
plt.ylabel("Temperatura (°C)")
plt.legend()
plt.grid()
plt.show()