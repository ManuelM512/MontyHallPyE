# Simulación de Monty Hall
Este código en Python simula el famoso problema de Monty Hall, un acertijo de probabilidad basado en un escenario de concurso televisivo. El problema implica la toma de decisiones y el análisis de probabilidades.

## Estructura de Archivos
Monty.py
Este archivo contiene la clase Monty, que simula el juego de Monty Hall. Incluye métodos para inicializar el juego, jugar y determinar el resultado según la elección del jugador y si decide cambiar su selección.

simulation.py
Este archivo ejecuta la simulación del problema de Monty Hall. Incluye funciones para simular las rondas del juego, o simular una ronda con diálogos del juego, y calcular estadísticas sobre los resultados.

## Instrucciones
Para ejecutar la simulación, ejecuta la función game_sim(iterations) en simulation.py. Puedes especificar el número de iteraciones del juego a simular pasando el número deseado como argumento a game_sim.

## Ejemplo:

game_sim(100000)
Esto simulará 100,000 rondas del juego, tanto con el cambio como manteniendo la selección inicial.

## Salida
La simulación proporcionará resultados detallados de los juegos jugados, incluyendo el número de juegos ganados y perdidos, junto con la probabilidad de victorias para ambas estrategias (cambiar o mantener la selección inicial).