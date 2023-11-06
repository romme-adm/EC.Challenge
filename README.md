## Envio click Challenge

### Puntos a evaluar:

 - Solución de problemas
 - Lógica de programación
 - Buenas practicas
 
## Lenguaje seleccionado : Python

### Estructura de solucion
- **EC_Challenge_DataSources**
		Se depositan los archivos que contienen las fuentes de datos base para realizar las operaciones
- **EC_Challenge_Ordering**
		Paquete que contiene la clase de python que realiza las operaciones busqueda y ordenamiento del Ejercicio 2
- **EC_Challenge_ProcessCoincidences**
	Paquete que contiene la clase de python que realiza parte de las operaciones para buscar el numero de coincidencias de una palabra, ejercicio 1.
- **EC_Challenge_Tasks**
	Este paquete contiene la clase para resolver el ejercisio 1 usando **multiprocesamiento** 
	
- **EC_Challenge_UnitTest**
	Se agregan pruebas unitarias para ciertos componentes.
- **EC_Challenge_Utils**
	Contienen clases con mecanismos para para carga de archivos inputs para procesos de ejercisio 1 y 2.

- **ec_config.json**
	Este archivo contiene las entradas para el ejercicio 1.
	
`{
"w":"ocurrido",
"n":4,
"df":"source_text_for_coincidences.txt",
"dp":"./EC_Challenge_DataSources",
"m":false
}`
	
	w = palabra a buscar
	n = numero de subprocesos o nodos a usar (sumulando procesos distribuidos)
	df = nombre del archivo que contiene el o los parrafos.
	dp = nombre del directorio donde se encuentra en archivo que contiene el o los parrafos
	m = (True | False) Activa o no el multiprocesamiento
-**entries_for_search.txt**
	Se encuentran los criterios de entrada para el ejecicio 2.
	`criteria2 = [
('id', '>=', 12366),
('priority','=',2)
]`


## Ejecucion
- Ejercicio 1
![Ejecucion ejercicio 1](/e11.png)`

![Resultado ejercicio 1](/e12.png)`


- Ejercicio 2
![Ejecucion ejercicio 1](/e21.png)`

![Resultado ejercicio 1](/e22.png)`