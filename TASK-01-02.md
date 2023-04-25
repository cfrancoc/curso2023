# Añadir seguridad (7)

Hacer dos grupos de usuario, helpdesk_manager y helpdesk_user, pertenecientes a una aplicación Helpdesk.

El usuario sólo podrá ver y modificar los tickets que tenga asignados (hemos creado user_id)

El administrador podrá crear, borrar, ver y modificar cualquier ticket.

# Mejorar vista (9)

Añadir el campo Estado [Nuevo, Asignado, En proceso, Pendiente, Resuelto, Cancelado], que por defecto sea Nuevo

El campo nombre que sea obligatorio

En algún campo añadir un texto de ayuda indicando su funcionalidad, luego revisar que funciona.

El campo Asignado hacer que sea solo de lectura


## En la vista tipo lista mostrar:

Añádir campo sequence y hacer el widget handle.

Mostrar nombre, asignado a y estado.

El campo fecha que sea opcional mostrarlo y mostrarlo por defecto.

El campo fecha limite que sea opcional mostrarlo y ocultarlo por defecto.

## En la vista formulario:

poner un header con el status bar
nombre con h1 como en pedido de venta
dos columnas:
- fecha, fecha límite
- asignado, tiempo dedicado

solapas:
- Descripción
- Acciones a realizar
