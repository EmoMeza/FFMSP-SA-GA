# FFMSP-SA-GA
FFMSP-SA-GA
Trabajo de Sistemas Adaptativos
Integrandes: Ana Vargas, Emilio Meza

Programa dedicado a la creacion de un algoritmo genetico aplicable a FFMSP. El Programa consiste en crear una generacion inicial utilizando Greedy Probabilista de entregas anteriores. De esta generacion se obtendran los mejores dos agentes, y dividiendo la secuencia de cada uno en 10 partes iguales, las cuales se mezclaran entre ambos para crear una nueva generacion. Esta nueva generacion tiene la probabilidad de ser mutada, cambiando valores de forma aleatoria a lo largo de la secuencia. Finalmente esto se va repitiendo.

Importante aclarar que ademas de lo anterior, el programa cuenta con una lista donde se guarda primera generacion. Debido a problemas que se presentaban a lo largo de la creacion de secuencias mediante el algoritmo genetico, se decidio que una vez haya una calidad repetida un total de 10 veces, se añadira una respuesta de la primera generacion. Igualmente los agentes dentro de la lista de primera generacion, uno de los agentes será reemplazado al azar cada vez que se encuentre una mejor respuesta. 

Para correr el programa basta con introducir lo siguiente

"python3 main.py -i [Filename] -t [MaxTimeInSeconds] -th [ThresholdValue] -p [PopulationSize] -mr [MutationRate]"
