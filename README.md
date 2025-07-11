# 📦 Sistema de Inventario en Python

Un sistema de gestión de inventario simple pero funcional desarrollado en Python, diseñado para pequeñas y medianas empresas que necesitan controlar su stock, proveedores y bodegas de manera eficiente.

## 🚀 Características

- **Gestión de Productos**: Registro, modificación y consulta de productos con categorías
- **Control de Stock**: Seguimiento en tiempo real de inventarios y movimientos
- **Gestión de Bodegas**: Administración de múltiples ubicaciones de almacenamiento con capacidades máximas
- **Proveedores**: Gestión completa de proveedores y sus productos asociados
- **Categorización**: Organización de productos por categorías
- **Validaciones**: Control de stock y capacidades para evitar errores

## 📁 Estructura del Proyecto

```
inventario-python/
├── README.md           # Documentación del proyecto
├── bodega.py          # Clase para gestión de bodegas
├── producto.py        # Clase para gestión de productos
├── proveedor.py       # Clase para gestión de proveedores
├── categoria.py       # Clase para categorización de productos
└── proyecto python.png # Imagen del proyecto
```

## 📋 Requisitos

- Python 3.6 o superior
- No requiere librerías externas

## 🔧 Instalación

1. Clona o descarga este repositorio
2. Asegúrate de tener Python instalado en tu sistema
3. Los archivos están listos para usar sin instalación adicional

## 💻 Uso

### Crear una Bodega

```python
from bodega import Bodega

# Crear una nueva bodega
mi_bodega = Bodega("Bodega Central", "Av. Principal 123", 1000)

# Agregar productos a la bodega
mi_bodega.agregar_producto("Laptop", 10)
mi_bodega.agregar_producto("Mouse", 50)

# Consultar stock de un producto
stock_laptops = mi_bodega.consultar_producto("Laptop")
print(f"Stock de laptops: {stock_laptops}")

# Retirar productos
mi_bodega.retirar_producto("Laptop", 2)
```

### Gestionar Productos

```python
from producto import Producto
from categoria import Categoria
from proveedor import Proveedor

# Crear categoría y proveedor
categoria_tech = Categoria("Tecnología", "Productos tecnológicos")
proveedor_tech = Proveedor("TechCorp", "Calle Tech 456", "555-0123")

# Crear un producto
laptop = Producto(
    nombre="Laptop Gaming",
    descripcion="Laptop para gaming de alta gama",
    precio=1200.00,
    stock_inicial=15,
    categoria=categoria_tech,
    proveedor=proveedor_tech
)

# Gestionar stock
laptop.agregar_stock(5)  # Agregar 5 unidades
laptop.retirar_stock(3)  # Retirar 3 unidades

# Calcular valor total del inventario
valor_total = laptop.calcular_valor_total()
print(f"Valor total del stock: ${valor_total}")
```

### Gestionar Proveedores

```python
from proveedor import Proveedor

# Crear proveedor
proveedor = Proveedor("Distribuidora ABC", "Zona Industrial", "555-0456")

# Asociar productos al proveedor
proveedor.agregar_producto("Teclado")
proveedor.agregar_producto("Monitor")

# Eliminar producto del proveedor
proveedor.eliminar_producto("Teclado")
```

## 🏗️ Arquitectura

### Clases Principales

#### Bodega
- **Atributos**: nombre, ubicación, capacidad_máxima, productos
- **Métodos**: agregar_producto(), retirar_producto(), consultar_producto()

#### Producto
- **Atributos**: nombre, descripción, precio, stock, categoría, proveedor
- **Métodos**: agregar_stock(), retirar_stock(), calcular_valor_total()

#### Proveedor
- **Atributos**: nombre, dirección, teléfono, productos
- **Métodos**: agregar_producto(), eliminar_producto()

#### Categoria
- **Atributos**: nombre, descripción, productos
- **Métodos**: agregar_producto()

## 🛡️ Validaciones

El sistema incluye validaciones automáticas:
- **Control de capacidad**: Las bodegas no pueden exceder su capacidad máxima
- **Stock suficiente**: No se puede retirar más stock del disponible
- **Productos únicos**: Los proveedores no pueden tener productos duplicados

## 🚀 Posibles Mejoras

- [ ] Interfaz gráfica de usuario (GUI)
- [ ] Base de datos para persistencia
- [ ] Sistema de reportes
- [ ] API REST
- [ ] Autenticación y roles de usuario
- [ ] Historial de movimientos
- [ ] Alertas de stock mínimo

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Por favor:

1. Haz fork del proyecto
2. Crea una rama para tu feature (`git checkout -b feature/nueva-funcionalidad`)
3. Commit tus cambios (`git commit -am 'Agrega nueva funcionalidad'`)
4. Push a la rama (`git push origin feature/nueva-funcionalidad`)
5. Abre un Pull Request

## 📄 Licencia

Este proyecto es de código abierto y está disponible bajo la licencia MIT.

## 📞 Contacto

Si tienes preguntas o sugerencias sobre este proyecto, no dudes en abrir un issue en el repositorio.

---

⭐ **¡No olvides dar una estrella al proyecto si te resulta útil!**
