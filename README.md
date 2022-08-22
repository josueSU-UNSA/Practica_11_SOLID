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

    Super Clase Usuario:
  
  ![L_Usuario](https://user-images.githubusercontent.com/82920949/185823531-e695240c-3752-42ed-a028-25a33e3e57c4.PNG)
      
    Sub Clase Asistente:
  
  ![L_Asistente](https://user-images.githubusercontent.com/82920949/185823749-cdfdfdc6-368f-4caa-8d9c-eb9ed240cd06.PNG)

    Sub Clase Ponente:
    
   ![L_Ponentee](https://user-images.githubusercontent.com/82920949/185823791-6cf54861-1cd7-4f64-bf25-50f776a07483.PNG)

  
  ## 4. I — Segregación de la interfaz:
  Este principio tiene como objetivo dividir un conjunto de acciones en conjuntos más pequeños para que una Clase ejecute SÓLO   el conjunto de acciones que requiere.
  En nuestra implementacion de este principio, podemos ver que nuetra interfaz y superclase cumple con separar la funcionalidad   de las subclases Ponente y Asistente:
    
    Iterfaz de la Clase Usuario:
  
  ![I_User_Interface](https://user-images.githubusercontent.com/82920949/185824351-567be960-1d6e-4d47-b592-eda3e26a30a4.PNG)

    
    Super Clase Usuario:
  
  ![L_Usuario](https://user-images.githubusercontent.com/82920949/185823531-e695240c-3752-42ed-a028-25a33e3e57c4.PNG)
      
    Sub Clase Asistente:
  
  ![L_Asistente](https://user-images.githubusercontent.com/82920949/185823749-cdfdfdc6-368f-4caa-8d9c-eb9ed240cd06.PNG)

    Sub Clase Ponente:
    
   ![L_Ponentee](https://user-images.githubusercontent.com/82920949/185823791-6cf54861-1cd7-4f64-bf25-50f776a07483.PNG)

  
  
  ## 5. D — Inversión de dependencia:
  Este principio tiene como objetivo reducir la dependencia de una Clase de alto nivel en la Clase de bajo nivel mediante la     introducción de una interfaz.Para cumplir con este princpio debemos crear las interfaces de todas  nuestras clases:
    
    Iterfaz de la Clase Evento:
    
   ![D_Evento_Interfaz](https://user-images.githubusercontent.com/82920949/185825047-860ff0f0-6080-465b-a99f-1df07f461b9e.PNG)

    
    Iterfaz de la Clase Lista_de_eventos:
    
   ![D_Lista_de_eventos_Interface](https://user-images.githubusercontent.com/82920949/185825067-e96bf7d1-cde9-43b0-b5ab-9275bef1d39e.PNG)

    
    Iterfaz de la Clase Tema:
    
  ![D_Tema_interface](https://user-images.githubusercontent.com/82920949/185825109-58c6b90e-4ec8-4efd-a5b2-134e2ae5214c.PNG)

    
    Iterfaz de la Clase Usuario:
  
  ![D_Usuario_Interface](https://user-images.githubusercontent.com/82920949/185825147-bd8437c2-2d31-4ab2-9fb7-5ef06118a5b3.PNG)

  
  
