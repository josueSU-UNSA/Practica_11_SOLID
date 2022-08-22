# Principios SOLID

## 1. S-Principio de Resposabilidad Única:
  Este principio tiene como objetivo separar los comportamientos para que, si surgen errores como resultado de su cambio, no         afecten otros comportamientos no relacionados.
  Un ejemplo de este principio es aplicado en la clase Lista_de_eventos en la cual unicamente se encargaa de insertar y retornar     eventos:
  
  ![Responsabilidad_Unica](https://user-images.githubusercontent.com/82920949/185822105-f5dc1f4e-9e6d-4a54-a193-c04ea91d60cf.PNG)

## 2. O-Principio de Abierto-Cerrado:
  Este principio tiene como objetivo extender el comportamiento de una Clase sin cambiar el comportamiento existente de esa Clase.   Esto es para evitar causar errores dondequiera que se use la Clase.
  Para aplicar este ejemplo todas  las clases deben descender de una clase abstracta donde se presenten todos aquellos métodos que   son la base de las respectivas clases.
  
  ![Open_Closed](https://user-images.githubusercontent.com/82920949/185822594-98e96308-56dd-46ea-9886-87dfecc9a21f.PNG)

## 3. L - Sustitución de Liskov:
  Este principio tiene como objetivo hacer cumplir la coherencia para que la Clase principal o su Clase secundaria se puedan     usar de la misma manera sin errores.
  Para aplicar este ejemplo todas  las clases que sean subtipos de una superclase , y esta misma debe incluir solo aquellos       métodos que comparten ambas subclases sin romper la lógica.
  En nuestra superclase Usuario solo contiene aquellos métodos que comparten las subclases :Ponente y Asistente , ya  que el     ponente no tiene los mismos métodos que asistente y viceversa.
  
  
  
  ## 2. O-Principio de Abierto-Cerrado:
  Este principio tiene como objetivo extender el comportamiento de una Clase sin cambiar el comportamiento existente de esa Clase.   Esto es para evitar causar errores dondequiera que se use la Clase.
  Para aplicar este ejemplo todas  las clases deben descender de una clase abstracta donde se presenten todos aquellos métodos que   son la base de las respectivas clases.
  
  ## 2. O-Principio de Abierto-Cerrado:
  Este principio tiene como objetivo extender el comportamiento de una Clase sin cambiar el comportamiento existente de esa Clase.   Esto es para evitar causar errores dondequiera que se use la Clase.
  Para aplicar este ejemplo todas  las clases deben descender de una clase abstracta donde se presenten todos aquellos métodos que   son la base de las respectivas clases.
