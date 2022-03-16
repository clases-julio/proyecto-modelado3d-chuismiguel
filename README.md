# Proyecto Modelado 3D: Robot Compañero


Para el semiproyecto final que debemos realizar para la asignatura Modelado y Simulación de Robots, he utilizado la herramienta Blender para crear un pequeño robot mascota. El diseño del robot está basado en el famoso robot de Anki: Vector:

![image](https://user-images.githubusercontent.com/78983070/158219741-21ab660d-deee-449f-b2b7-48704aabc00f.png)

El objetivo para el proyecto era realizar un robot relativamente similar, que pudiese imprimirse en 3D y que tuviera algunos sensores incorporados para que pudiéramos contolar y programar diferentes aspectos de su funcionamiento.

El robot se ha ido construyendo a mano y en un script está recogido todo su proceso de creación. Script.py es el fichero python que utiliza código de la clase transformaciones (modificada para realizar más operaciones) y que tiene todas las funciones que crean el robot. Ejecutando dicho script aparecerá el robot en nuestro mundo de Blender.

Lo primero en construirse fue el chasis. Para ello, se realizó una funcion para crear una rueda con guia, para poder poner una goma de caucho que actúe como neumático y se clonó cuatro veces. Las dos ruedas del frontal del robot son algo más pequeñas para asemejarse al Vector. Dicho chasis incluye un bloque rectangular que une las ruedas y un pequeño módulo ultrasonidos formado a partir de un cubo y dos cilindros. Así queda el chasis por separado:


![image](https://user-images.githubusercontent.com/78983070/158220528-95371b3a-3034-4a9e-8984-f034b22f19ab.png)


El posterior trabajo fue implementar las ruedas de oruga. Fue un trabajo complejo. Primero, había que realizar las tiras superiores e inferiores. Para ello, se crea un pequeño cubo rectangular que utilizando un bucle for, se copia y se repite a lo largo de la union entre ruedas. Tuvimos que añadir un ínfimo cambio en la posicion Z en cada iteración del bucle para hacer que la oruga se adecuase a ambas ruedas (la rueda trasera es más grande que la delantera).

Tras esto, el problema venía al hacer las orugas que cubrieran la parte circular de la rueda. Para ello, la solución fue, utilizando GeoGebra, obtener una función que generase una parábola horizontal para modificar la posición X en el bucle for e incrementar la posición Z un valor pequeño para que se recorriese la parábola. En GeoGebra, la parábola era la siguiente:

![image](https://user-images.githubusercontent.com/78983070/158608100-9bf49e9a-3943-4dbc-8921-ab43bc81e581.png)

Alternando el 10 por el que se divide, se consigue una parábola más o menos amplia. Tras probar, tuvimos que originar dos parabolas por rueda:

  -> Una parábola que comenzara en el centro y fuese hacia arriba hasta conectar con la oruga horizontal superior.
  
  -> Una parábola que comenzara en el centro y fuese hacia debajo hasta conectar con la oruga horizontal inferior.
  
Para la rueda trasera bastó con cambiar la orientación del crecimiento de las X y hacer algo más ancha la parábola. Copiando y pegando alterando la posición Y obtuvimos las orugas de ambos lados del robot.

Este es el resultado final:

![image](https://user-images.githubusercontent.com/78983070/158606736-c513c429-f3e4-4481-b626-9e993e088f7d.png)

Posteriormente, construimos el cuerpo del robot, la cabeza y los brazos. El cuerpo del robot es una combinación de cubos variados, algunos orientados y algún cilindro para variar. Traté de modificarlos cortando para aportar una superficie más agradable a la vista pero fue imposible hacerlo mediante comandos.

La cabeza es un cilindro con un pequeño panel que representa la pantalla del robot. Dicha pantalla puede representar emociones, como la que hay cargada en la textura del robot en blender o en el fichero happy.png.

Para aportar rigidez a lo que luego será la pinza, hemos creado dos brazos iguales en diferentes alturas. También se han modificado ligeramente el escalado de las orugas para que se acoplen perfectamente al surco que teníamos en las ruedas. 

El progreso es el siguiente:

![image](https://user-images.githubusercontent.com/78983070/158655683-a3e939b3-d9e5-4bdf-acbb-06a8ec0247b5.png)

Visto con renderizado, de momento solo vemos la cara del robot:

![image](https://user-images.githubusercontent.com/78983070/158656675-80a9ee31-d904-4e91-b52e-9eaf16c77d9c.png)

El siguiente añadido fue el "gripper", que es el final de los brazos que incluye unos salientes para que el robot pueda manipular ligeramente objetos, como Vector hace con su cubo. También acabamos de cerrar el robot por arriba. Echándole un vistazo con el lateral le vi un cierto parecido a Mate, de Cars, por lo que decidí también hacerle una pequeña grúa que se podría manipular con un motor paso a paso, ya que la grúa también tiene su cuerda diseñada.

![image](https://user-images.githubusercontent.com/78983070/158667958-62fc4328-008b-41b5-86b7-33df4a7b4f21.png)

Con esto podemos dar por acabado el diseño del robot. Todo el diseño se puede hacer ejecutando el script script.py

Ahora, el objetivo es darle unas texturas y unos colores bonitos para que el renderizado en blender se vea curioso. Vector es un robot totalmente negro, pero yo he decidido agregarle más colores para poder tener un robot algo más vivo. Es por esto por lo que durante el desarrollo del script, cuidadosamente he ido juntando las diferentes partes y no añadiendolas al modelo completamente, para poder pintarlas una a una.


