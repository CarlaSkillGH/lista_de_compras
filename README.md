# lista_de_compras
En este proyecto se llevará a cabo la creación de una lsita de compras con finalidad evaluativa

# Lista de Compras en Python

Este proyecto es una aplicación básica en Python para gestionar una lista de compras. A continuación, se detallan los pasos para utilizar y modificar el archivo `lista_compras.py` incluido en el repositorio.

## Descripción del Proyecto

`lista_compras.py` permite al usuario realizar las siguientes operaciones sobre una lista de compras:
- Agregar un artículo
- Eliminar un artículo
- Mostrar la lista de compras
- Salir del programa

## Funcionalidades

1. **Inicialización de la lista**:
   - Se inicializa una variable `lista_compras` como una lista vacía.

2. **Bucle principal**:
   - Un bucle `while` que se ejecuta hasta que el usuario decida salir del programa.

3. **Menú de opciones**:
   - **Agregar artículo**: Solicita al usuario el nombre del artículo y lo agrega a la lista.
   - **Eliminar artículo**: Muestra la lista actual, solicita el índice del artículo a eliminar y lo elimina de la lista.
   - **Mostrar lista**: Imprime la lista de compras actual.
   - **Salir**: Imprime un mensaje de despedida y termina el bucle.

## Uso

1. Ejecuta el archivo `lista_compras.py`.
2. Selecciona una opción del menú.
3. Sigue las instrucciones según la opción elegida para modificar o consultar la lista de compras.

## Ejemplo de Ejecución

```plaintext
1. Agregar artículo
2. Eliminar artículo
3. Mostrar lista
4. Salir

Elige una opción: 1
Introduce el nombre del artículo: Manzanas

Lista actual: ['Manzanas']

Elige una opción: 2
Lista actual: ['Manzanas']
Introduce el índice del artículo a eliminar: 0

Lista actual: []

