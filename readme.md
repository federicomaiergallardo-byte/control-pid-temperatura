# 🌡️ Primer Proyecto: Control PID de Temperatura

Este repositorio contiene mi primer proyecto del roadmap de Ingeniería Eléctrica. El objetivo principal es simular y estabilizar la temperatura de una habitación utilizando control automático.

## 🎯 Objetivos del Proyecto
- Modelar matemáticamente una habitación considerando la temperatura interior y la pérdida de calor hacia el exterior.
- Implementar desde cero un controlador Proporcional-Integral-Derivativo (PID) en Python.
- Realizar sintonía fina para evitar oscilaciones e inestabilidad en el sistema térmico.

## ⚙️ Sintonía del Controlador
Tras realizar pruebas de estabilidad térmica, los valores óptimos encontrados para el sistema fueron:
- **Kp (Proporcional):** 0.6 (Empuje inicial rápido)
- **Ki (Integral):** 0.015 (Eliminación del error en estado estacionario)
- **Kd (Derivativo):** 0.1 (Freno amortiguado para evitar sobreimpulso)

## 📊 Gráfica de Resultados
A continuación se muestra la curva de calentamiento y estabilización de la habitación al aplicar el controlador PID hasta alcanzar el *setpoint* de 24°C:

![Gráfico del Control PID](grafico_pid.png).

---
*Desarrollado en Python usando las librerías NumPy y Matplotlib.*