# Proyecto FastAPI CRUD con Autenticación JWT

Este proyecto es un CRUD (Crear, Leer, Actualizar y Eliminar) desarrollado con FastAPI, un framework web rápido para construir API con Python 3.7+ basado en estándares tipo OpenAPI y JSON Schema.

## Características

- **Operaciones CRUD:** El proyecto ofrece operaciones básicas de Crear, Leer, Actualizar y Eliminar sobre un conjunto de datos almacenado en una lista de Python.

- **Rutas Protegidas:** Se implementan rutas protegidas que requieren autenticación para acceder a ellas.

- **Autenticación JWT:** La autenticación de usuarios se realiza utilizando PyJWT (JSON Web Tokens). Los usuarios deben proporcionar un token válido para acceder a las rutas protegidas.

## Instalación

1. Clona el repositorio:

```bash
git clone https://github.com/tuusuario/proyecto-fastapi-crud.git
```

2. Instala las dependencias:

```bash
cd proyecto-fastapi-crud
pip install -r requirements.txt
```

## Uso

1. Ejecuta la aplicación FastAPI:

```bash
uvicorn main:app --reload
```

2. Accede a la documentación generada automáticamente en [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) para probar las rutas y conocer los endpoints disponibles.

## Rutas Protegidas

Las siguientes rutas requieren autenticación:

- `/items/create`: Crea un nuevo item en el conjunto de datos.
- `/items/update/{item_id}`: Actualiza un item existente.
- `/items/delete/{item_id}`: Elimina un item existente.

Para autenticarse, se debe incluir el token JWT en la cabecera de la solicitud:

```bash
curl -X GET "http://127.0.0.1:8000/items/create" -H "Authorization: Bearer tu-token-jwt"
```

## Contribuciones

¡Las contribuciones son bienvenidas! Si encuentras algún problema o tienes sugerencias de mejora, no dudes en abrir un problema o enviar un pull request.

## Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo [LICENSE](LICENSE) para obtener más detalles.
