# Proyecto Modelado 3D: Robot Compañero


Para el semiproyecto final que debemos realizar para la asignatura Modelado y Simulación de Robots, he utilizado la herramienta Blender para crear un pequeño robot mascota. El diseño del robot está basado en el famoso robot de Anki: Vector:

![image](https://user-images.githubusercontent.com/78983070/158219741-21ab660d-deee-449f-b2b7-48704aabc00f.png)

El objetivo para el proyecto era realizar un robot relativamente similar, que pudiese imprimirse en 3D y que tuviera algunos sensores incorporados para que pudiéramos contolar y programar diferentes aspectos de su funcionamiento.

El robot se ha ido construyendo a mano y en un script está recogido todo su proceso de creación. Script.py es el fichero python que utiliza código de la clase transformaciones (modificada para realizar más operaciones) y que tiene todas las funciones que crean el robot. Ejecutando dicho script aparecerá el robot en nuestro mundo de Blender.

Lo primero en construirse fue el chasis. Para ello, se realizó una funcion para crear una rueda con guia, para poder poner una goma de caucho que actúe como neumático y se clonó cuatro veces. Las dos ruedas del frontal del robot son algo más pequeñas para asemejarse al Vector. Dicho chasis incluye un bloque rectangular que une las ruedas y un pequeño módulo ultrasonidos formado a partir de un cubo y dos cilindros. Así queda el chasis por separado:


![image](https://user-images.githubusercontent.com/78983070/158220528-95371b3a-3034-4a9e-8984-f034b22f19ab.png)


El posterior trabajo fue implementar las ruedas de oruga. Fue un trabajo complejo. Primero, había que realizar las tiras superiores e inferiores. Para ello, se crea un pequeño cubo rectangular que utilizando un bucle for, se copia y se repite a lo largo de la union entre ruedas. Tuvimos que añadir un ínfimo cambio en la posicion Z en cada iteración del bucle para hacer que la oruga se adecuase a ambas ruedas (la rueda trasera es más grande que la delantera).

Tras esto, el problema venía al hacer las orugas que cubrieran la parte circular de la rueda. Para ello, la solución fue, utilizando GeoGebra, obtener una función que generase una parábola horizontal para modificar la posición X en el bucle for e incrementar la posición Z un valor pequeño para que se recorriese la parábola. En GeoGebra, la parábola era la siguiente:

![image](https://user-images.githubusercontent.com/78983070/158607457-5f13f394-d97f-4648-b6e4-f93cded2627b.png)

Alternando el 10 por el que se divide, se consigue una parábola más o menos amplia. Tras probar, tuvimos que originar dos parabolas por rueda:
  -> Una parábola que comenzara en el centro y fuese hacia arriba hasta conectar con la oruga horizontal superior.
  -> Una parábola que comenzara en el centro y fuese hacia debajo hasta conectar con la oruga horizontal inferior.
  
Para la rueda trasera bastó con cambiar la orientación del crecimiento de las X y hacer algo más ancha la parábola. Copiando y pegando alterando la posición Y obtuvimos las orugas de ambos lados del robot.

Este es el resultado final:

![image](https://user-images.githubusercontent.com/78983070/158606736-c513c429-f3e4-4481-b626-9e993e088f7d.png)
