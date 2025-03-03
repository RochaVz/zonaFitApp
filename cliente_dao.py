from cliente import Cliente
from conexion import Conexion


class ClienteDAO:
    SELECT = 'SELECT * FROM cliente'
    SELECT_ID = 'SELECT * FROM cliente WHERE id=%s'
    INSERT = 'INSERT INTO cliente(nombre, apellido, membresia) VALUES(%s,%s,%s)'
    UPDATE = 'UPDATE cliente SET nombre=%s, apellido=%s, membresia=%s WHERE id=%s'
    DELETE = 'DELETE FROM cliente WHERE id=%s'

    @classmethod
    def seleccionar(cls):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            cursor.execute(cls.SELECT)
            registros = cursor.fetchall()
            # mapeoo de clase tabla
            clientes = []
            for registro in registros:
                cliente = Cliente(registro[0], registro[1],
                                  registro[2], registro[3])
                clientes.append(cliente)
            return clientes
        except Exception as e:
            print(f'Ocurrio un error al seleccionar clientes: {e}')
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)

    @classmethod
    def seleccionar_por_id(cls, id):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            valores = (id,)
            cursor.execute(cls.SELECT_ID, valores)
            registro = cursor.fetchone()
            # Mapeo clase-tabla cliente
            cliente = Cliente(registro[0], registro[1],
                              registro[2], registro[3])
            return cliente
        except Exception as e:
            print(f'Excepcion al seleccionar cliente por id: {e}')
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)

    @classmethod
    def insertar(cls, cliente):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            valores = (cliente.nombre, cliente.apellido, cliente.membresia)
            cursor.execute(cls.INSERT, valores)
            conexion.commit()
            return cursor.rowcount
        except Exception as e:
            print(f'Ocurrio un error al insertar cliente: {e}')
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)

    @classmethod
    def actualizar(cls, cliente):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            valores = (cliente.nombre, cliente.apellido,
                       cliente.membresia, cliente.id)
            cursor.execute(cls.UPDATE, valores)
            conexion.commit()
            return cursor.rowcount
        except Exception as e:
            print(f'Ocurrio un error al actualizar cliente: {e}')
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)

    @classmethod
    def eliminar(cls, cliente):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            valores = (cliente.id,)
            cursor.execute(cls.DELETE, valores)
            conexion.commit()
            return cursor.rowcount
        except Exception as e:
            print(f'Ocurrio un error al eliminar cliente: {e}')
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)


if __name__ == '__main__':
    # insertar cliente
    # cliente1=Cliente(nombre='Carlos', apellido='Rocha', membresia=600)
    # clientes_insertados= ClienteDAO.insertar(cliente1)
    # print(f'clientes insertados: {clientes_insertados}')

    # seleccionar clientes
    clientes = ClienteDAO.seleccionar()
    for cliente in clientes:
        print(cliente)

    # actualizar cliente
    # cliente_actualizar= Cliente(6,'Matt', 'Roca', 700)
    # clientes_actualizados= ClienteDAO.actualizar(cliente_actualizar)
    # print(f'Cliente actualizados: {clientes_actualizados}')

    # eliminar cliente
    # cliente_eliminar= Cliente(id=6)
    # clientes_eliminados= ClienteDAO.eliminar(cliente_eliminar)
    # print(f'Cliente eliminado: {clientes_eliminados}')
