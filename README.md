# Proyecto Modelado 3D: Robot Compañero


Para el semiproyecto final que debemos realizar para la asignatura Modelado y Simulación de Robots, he utilizado la herramienta Blender para crear un pequeño robot mascota. El diseño del robot está basado en el famoso robot de Anki: Vector:

![image](https://user-images.githubusercontent.com/78983070/158219741-21ab660d-deee-449f-b2b7-48704aabc00f.png)

El objetivo para el proyecto era realizar un robot relativamente similar, que pudiese imprimirse en 3D y que tuviera algunos sensores incorporados para que pudiéramos contolar y programar diferentes aspectos de su funcionamiento.

El robot se ha ido construyendo a mano y en un script está recogido todo su proceso de creación. Script.py es el fichero python que utiliza código de la clase transformaciones (modificada para realizar más operaciones) y que tiene todas las funciones que crean el robot. Ejecutando dicho script aparecerá el robot en nuestro mundo de Blender.

Lo primero en construirse fue el chasis. Para ello, se realizó una funcion para crear una rueda con guia, para poder poner una goma de caucho que actúe como neumático y se clonó cuatro veces. Las dos ruedas del frontal del robot son algo más pequeñas para asemejarse al Vector. Dicho chasis incluye un bloque rectangular que une las ruedas y un pequeño módulo ultrasonidos formado a partir de un cubo y dos cilindros. Así queda el chasis por separado:


![image](https://user-images.githubusercontent.com/78983070/158220528-95371b3a-3034-4a9e-8984-f034b22f19ab.png)
