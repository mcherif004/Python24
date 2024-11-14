# ARRAYS UNIDIMENSIONALES

## Ejercicio 1

Escribe sentencias Python para realizar cada una de las siguientes tareas: 

- Muestra el valor del elemento 6 de un array f.
- Inicializa los 5 primeros elementos de un array unidimensional de enteros a 8.
- Total de los 100 elementos de punto-flotante de un array c. 
- Copia los 11 elementos de un array a en la primera porción de un array b, el cual contiene 34 elementos. 
- Calcula y muestra el valor mayor y menor contenidos en un array w de 99 elementos de punto-flotante

## Ejercicio 2

Escribe un programa que lea 10 números por teclado y que luego los muestre en orden inverso, es decir, el primero que se introduce es el último en mostrarse y viceversa.

## Ejercicio 3

Define tres arrays de 20 números enteros cada uno, con nombres numero, cuadrado y cubo. Carga el array numero con valores aleatorios entre 0 y 100. En el array cuadrado se deben almacenar los cuadrados de los valores que hay en el array numero. En el array cubo se deben almacenar los cubos de los valores que hay en numero. A continuación, muestra el contenido de los tres arrays dispuesto en tres columnas.

## Ejercicio 4

Escribe un programa que pida 10 números por teclado y que luego muestre los números introducidos junto con las palabras “máximo” y “mínimo” al lado del máximo y del mínimo respectivamente.

## Ejercicio 5

Realiza un programa que pida la temperatura media que ha hecho en cada mes de un determinado año y que muestre a continuación un diagrama de barras horizontales con esos datos. Las barras del diagrama se pueden dibujar a base de asteriscos o cualquier otro carácter.

## Ejercicio 6

Escribe un programa que genere 20 números enteros aleatorios entre 0 y 100 y que los almacene en un array. El programa debe ser capaz de pasar todos los números pares a las primeras posiciones del array (del 0 en adelante) y todos los números impares a las celdas restantes. Utiliza arrays auxiliares si es necesario.

## Ejercicio 7

Escribe un programa que lea 15 números por teclado y que los almacene en un array. Rota los elementos de ese array, es decir, el elemento de la posición 0 debe pasar a la posición 1, el de la 1 a la 2, etc. El número que se encuentra en la última posición debe pasar a la posición 0. Finalmente, muestra el contenido del array.

ARRAYS DE DOS DIMENSIONES

## Ejercicio 1

Escribe un programa que pida 20 números enteros. Estos números se deben introducir en un array de 4 filas por 5 columnas. El programa mostrará las sumas parciales de filas y columnas igual que si de una hoja de cálculo se tratara. La suma total debe aparecer en la esquina inferior derecha.

## Ejercicio 2

Modifica el programa anterior de tal forma que los números que se introducen en el array se generen de forma aleatoria (valores entre 100 y 999).

## Ejercicio 3

Modifica el programa anterior de tal forma que las sumas parciales y la suma total aparezcan en la pantalla con un pequeño retardo, dando la impresión de que el ordenador se queda “pensando” antes de mostrar los números.

## Ejercicio 4

Realiza un programa que rellene un array de 6 filas por 10 columnas con números enteros positivos comprendidos entre 0 y 1000 (ambos incluidos). A continuación, el programa deberá dar la posición tanto del máximo como del mínimo.

## Ejercicio 5

Modifica el programa anterior de tal forma que no se repita ningún número en el array.

## Ejercicio 6

Realiza un programa que calcule la estatura media, mínima y máxima en centímetros de personas de diferentes países. El array que contiene los nombres de los países es el siguiente: 

paises = [“España”, “Rusia”, “Japón”, “Australia”]

Los datos sobre las estaturas se deben simular mediante un array de 4 filas por 10 columnas con números aleatorios generados al azar entre 140 y 210. Los decimales de la media se pueden despreciar. Los nombres de los países se deben mostrar utilizando el array de países (no se pueden escribir directamente).

Ejemplo:                                                                       

                                                     MED MIN MAX

España:    178 165 148 185 155 141 165 149 155 201 | 164 141 201

Rusia:     189 208 167 186 174 152 192 173 179 179 | 179 152 208

Japón:     173 182 168 170 181 197 146 168 166 177 | 172 146 197

Australia: 172 170 187 186 197 143 190 199 187 191 | 182 143 199

## Ejercicio 7

Se desea almacenar las calificaciones del alumnado de 1DAW del IES Gran Capitán en los módulos de PROGRAMACIÓN, LENGUAJE DE MARCAS, BASES DE DATOS Y SISTEMAS INFORMATICOS.

El número de alumnos no lo sabemos de antemano por lo que se han de añadir conforme se vayan introduciendo los datos.

El programa pedirá el nombre y apellidos del alumno y a continuación las calificaciones en los módulos mencionados anteriormente.

Cuando el usuario desee dejar de introducir información deberá de introducir una cadena vacía al introducir el nombre.

Asimismo el programa deberá de proporcionar las siguientes funcionalidades:

Impresión de las calificaciones del curso completo.
Impresión de las calificaciones de un alumno en concreto. El programa pedirá nombre y apellidos del alumno y de encontrarlo mostrará las calificaciones de todos los módulos de este alumno.
Nota media de un módulo. Se pedirá al usuario el nombre del módulo tras lo cuál el programa mostrará la nota media.
Nota máxima en un módulo. Se pedirá al usuario el nombre del módulo tras lo cuál el programa mostrará la nota máxima así como el alumno con la misma. 
Nota más baja en un módulo. Se pedirá al usuario el nombre del módulo tras lo cuál el programa mostrará la nota más baja así como el alumno con la misma.
Listado ordenado de los datos con respecto a su nota (de mayor a menor). El programa pedirá el módulo y deberá de ser capaz de realizar una ordenación descendente por dicha nota. 
Nota: En las listas de python se pueden mezclar datos de diferente tipo. Aprovecha los módulos y funciones de python que faciliten las operaciones que se piden.