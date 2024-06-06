from flask import Flask, render_template, request, redirect, url_for
from models.producto import Producto
from models.categoria import Categoria
from models.proveedor import Proveedor
from models.bodega import Bodega

app = Flask(__name__)

# Lista para almacenar productos
productos = []
categorias = []
proveedores = []
bodegas = []
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/registrar_producto', methods=['GET', 'POST'])
def registrar_producto():
    mensaje = ""
    if request.method == 'POST':
        if 'registrar' in request.form:
            nombre = request.form['nombre']
            descripcion = request.form['descripcion']
            precio = float(request.form['precio'])
            stock_inicial = int(request.form['stock_inicial'])
            categoria = request.form['categoria']
            proveedor= request.form['proveedor']
            
            nuevo_producto = Producto(nombre, descripcion, precio, stock_inicial, categoria,proveedor)
            productos.append(nuevo_producto)
            mensaje = f"Producto '{nombre}' registrado exitosamente."

        elif 'agregar_stock' in request.form:
            nombre = request.form['nombre']
            cantidad = int(request.form['cantidad'])
            for producto in productos:
                if producto.nombre == nombre:
                    producto.agregar_stock(cantidad)
                    mensaje = f"Stock agregado exitosamente a '{nombre}'."
                    break
            else:
                mensaje = "Producto no encontrado."

        elif 'retirar_stock' in request.form:
            nombre = request.form['nombre']
            cantidad = int(request.form['cantidad'])
            for producto in productos:
                if producto.nombre == nombre:
                    try:
                        producto.retirar_stock(cantidad)
                        mensaje = f"Stock retirado exitosamente de '{nombre}'."
                    except ValueError as e:
                        mensaje = str(e)
                    break
            else:
                mensaje = "Producto no encontrado."

        elif 'calcular_valor_total' in request.form:
            valor_total = sum(producto.calcular_valor_total() for producto in productos)
            mensaje = f"El valor total del stock es: {valor_total}"

        elif 'consultar_producto' in request.form:
            nombre = request.form['nombre']
            for producto in productos:
                if producto.nombre == nombre:
                    return render_template('registrar_producto.html', producto=producto, productos=productos)
            mensaje = "Producto no encontrado."

    return render_template('/registrar_producto.html', mensaje=mensaje, productos=productos)

@app.route('/registrar_categoria', methods=['GET', 'POST'])
def registrar_categoria():
    mensaje = ""
    categoria = None
    if request.method == 'POST':
        action = request.form.get('action')
        if action == 'registrar':
            nombre = request.form['nombre']
            descripcion = request.form['descripcion']
            nueva_categoria = Categoria(nombre, descripcion)
            categorias.append(nueva_categoria)
            mensaje = f"Categoría '{nombre}' registrada exitosamente."
            categoria = nueva_categoria
        elif action == 'agregar_producto':
            nombre_categoria = request.form['categoria']
            nombre_producto = request.form['nombre_producto']
            for cat in categorias:
                if cat.nombre == nombre_categoria:
                    cat.agregar_producto(nombre_producto)
                    mensaje = f"Producto '{nombre_producto}' agregado a la categoría '{nombre_categoria}'."
                    categoria = cat
                    break
            else:
                mensaje = "Categoría no encontrada."
        elif action == 'consultar':
            nombre = request.form['nombre']
            for cat in categorias:
                if cat.nombre == nombre:
                    categoria = cat
                    break
            else:
                mensaje = "Categoría no encontrada."

    return render_template('registrar_categoria.html', mensaje=mensaje, categoria=categoria, categorias=categorias)


@app.route('/registrar_proveedor', methods=['GET', 'POST'])
def registrar_proveedor():
    mensaje = ""
    proveedor = None
    if request.method == 'POST':
        action = request.form.get('action')
        if action == 'registrar':
            nombre = request.form['nombre']
            direccion = request.form['direccion']
            telefono = request.form['telefono']
            nuevo_proveedor = Proveedor(nombre, direccion, telefono)
            proveedores.append(nuevo_proveedor)
            mensaje = f"Proveedor '{nombre}' registrado exitosamente."
        elif action == 'agregar_producto':
            nombre_proveedor = request.form['proveedor']
            nombre_producto = request.form['producto']
            for prov in proveedores:
                if prov.nombre == nombre_proveedor:
                    prov.agregar_producto(nombre_producto)
                    mensaje = f"Producto '{nombre_producto}' agregado al proveedor '{nombre_proveedor}'."
                    break
            else:
                mensaje = "Proveedor no encontrado."
        elif action == 'eliminar_producto':
            nombre_proveedor = request.form['proveedor']
            nombre_producto = request.form['producto']
            for prov in proveedores:
                if prov.nombre == nombre_proveedor:
                    prov.eliminar_producto(nombre_producto)
                    mensaje = f"Producto '{nombre_producto}' eliminado del proveedor '{nombre_proveedor}'."
                    break
            else:
                mensaje = "Proveedor no encontrado."
        elif action == 'consultar':
            nombre_proveedor = request.form['nombre']
            for prov in proveedores:
                if prov.nombre == nombre_proveedor:
                    proveedor = prov
                    break
            else:
                mensaje = "Proveedor no encontrado."

    return render_template('registrar_proveedor.html', proveedores=proveedores, proveedor=proveedor, mensaje=mensaje)

@app.route('/registrar_bodega', methods=['GET', 'POST'])
def registrar_bodega():
    mensaje = ""
    bodega = None
    if request.method == 'POST':
        action = request.form.get('action')
        if action == 'registrar':
            nombre = request.form['nombre']
            ubicacion = request.form['ubicacion']
            capacidad_maxima = int(request.form['capacidad_maxima'])
            nueva_bodega = Bodega(nombre, ubicacion, capacidad_maxima)
            bodegas.append(nueva_bodega)
            mensaje = f"Bodega '{nombre}' registrada exitosamente."
        elif action == 'agregar_producto':
            nombre_bodega = request.form['bodega']
            nombre_producto = request.form['producto']
            cantidad = int(request.form['cantidad'])
            for bod in bodegas:
                if bod.nombre == nombre_bodega:
                    if bod.agregar_producto(nombre_producto, cantidad):
                        mensaje = f"Producto '{nombre_producto}' agregado a la bodega '{nombre_bodega}'."
                    else:
                        mensaje = "No hay suficiente espacio en la bodega."
                    break
            else:
                mensaje = "Bodega no encontrada."
        elif action == 'retirar_producto':
            nombre_bodega = request.form['bodega']
            nombre_producto = request.form['producto']
            cantidad = int(request.form['cantidad'])
            for bod in bodegas:
                if bod.nombre == nombre_bodega:
                    if bod.retirar_producto(nombre_producto, cantidad):
                        mensaje = f"Producto '{nombre_producto}' retirado de la bodega '{nombre_bodega}'."
                    else:
                        mensaje = "No hay suficiente stock en la bodega."
                    break
            else:
                mensaje = "Bodega no encontrada."
        elif action == 'consultar_producto':
            nombre_bodega = request.form['bodega']
            nombre_producto = request.form['producto']
            for bod in bodegas:
                if bod.nombre == nombre_bodega:
                    cantidad = bod.consultar_producto(nombre_producto)
                    if cantidad is not None:
                        mensaje = f"Producto '{nombre_producto}' tiene {cantidad} unidades en la bodega '{nombre_bodega}'."
                    else:
                        mensaje = f"Producto '{nombre_producto}' no encontrado en la bodega '{nombre_bodega}'."
                    bodega = bod
                    break
            else:
                mensaje = "Bodega no encontrada."

    return render_template('registrar_bodega.html', bodegas=bodegas, bodega=bodega, mensaje=mensaje)
@app.route('/generar_informe', methods=['GET'])
def generar_informe():
    # Calcular el stock total
    stock_total = sum(producto.stock for producto in productos)

    # Calcular el stock por categoría
    stock_por_categoria = {}
    for categoria in categorias:
        stock_por_categoria[categoria.nombre] = sum(
            producto.stock for producto in productos if producto.categoria == categoria.nombre)

    # Calcular el stock por proveedor
    stock_por_proveedor = {}
    for proveedor in proveedores:
        stock_por_proveedor[proveedor.nombre] = sum(
            producto.stock for producto in productos if producto.proveedor == proveedor.nombre)

    # Calcular el stock por bodega
    stock_por_bodega = {}
    for bodega in bodegas:
        stock_por_bodega[bodega.nombre] = sum(bodega.productos.values())

    return render_template('informe_stock.html', stock_total=stock_total, stock_por_categoria=stock_por_categoria, stock_por_proveedor=stock_por_proveedor, stock_por_bodega=stock_por_bodega)

if __name__ == '__main__':
    app.run(debug=True)