# Análisis del Repositorio: Sistema de Inventario en Python

## ¿Qué hace este repositorio?

Este repositorio contiene un **Sistema de Inventario Sencillo** desarrollado en Python que permite gestionar el stock de productos, proveedores y bodegas de manera eficiente. Es una solución ideal para pequeñas empresas que necesitan un sistema de inventario básico pero funcional.

## Componentes del Sistema

### 1. **Productos** (`producto.py`)
- **Clase**: `Producto`
- **Funcionalidad**: Representa un producto en el inventario
- **Atributos**: nombre, descripción, precio, stock, categoría, proveedor
- **Métodos**:
  - `agregar_stock()`: Aumenta el stock del producto
  - `retirar_stock()`: Disminuye el stock (con validación)
  - `calcular_valor_total()`: Calcula el valor total del stock (precio × cantidad)

### 2. **Bodegas** (`bodega.py`)
- **Clase**: `Bodega`
- **Funcionalidad**: Gestiona el almacenamiento físico de productos
- **Atributos**: nombre, ubicación, capacidad máxima, productos almacenados
- **Métodos**:
  - `agregar_producto()`: Añade productos respetando la capacidad máxima
  - `retirar_producto()`: Retira productos del almacén
  - `consultar_producto()`: Verifica la cantidad de un producto específico

### 3. **Proveedores** (`proveedor.py`)
- **Clase**: `Proveedor`
- **Funcionalidad**: Gestiona la información de los proveedores
- **Atributos**: nombre, dirección, teléfono, lista de productos
- **Métodos**:
  - `agregar_producto()`: Asocia productos al proveedor
  - `eliminar_producto()`: Desasocia productos del proveedor

### 4. **Categorías** (`categoria.py`)
- **Clase**: `Categoria`
- **Funcionalidad**: Organiza productos por categorías
- **Atributos**: nombre, descripción, lista de productos
- **Métodos**:
  - `agregar_producto()`: Añade productos a la categoría

## Características Principales

✅ **Consultar Stock**: Verifica las cantidades disponibles de cada producto  
✅ **Gestión de Proveedores**: Agregar y eliminar proveedores del sistema  
✅ **Registro de Productos**: Añadir nuevos productos con detalles completos  
✅ **Administración de Bodegas**: Gestionar ubicaciones de almacenamiento  
✅ **Control de Capacidad**: Validación de capacidad máxima en bodegas  
✅ **Organización por Categorías**: Clasificación de productos  

## Arquitectura

El sistema utiliza un diseño orientado a objetos con clases independientes que se relacionan entre sí:

```
Producto ←→ Proveedor
    ↓
Categoria
    ↓
  Bodega
```

- Los **productos** están asociados a **proveedores** y **categorías**
- Las **bodegas** almacenan **productos** con control de capacidad
- Cada componente tiene responsabilidades bien definidas

## Público Objetivo

Este sistema está diseñado para:
- Pequeñas empresas
- Tiendas locales
- Negocios que requieren control básico de inventario
- Proyectos educativos de programación orientada a objetos

## Tecnología

- **Lenguaje**: Python
- **Paradigma**: Programación Orientada a Objetos
- **Dependencias**: Solo librerías estándar de Python (sin dependencias externas)