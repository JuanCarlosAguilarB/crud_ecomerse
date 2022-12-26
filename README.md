# Crud para productos de un ecommerse frutas

## Ejecución del código

En primer lugar, necesitamos crear las variables de entorno tal como se muestra en el archivo e.n-example

Es necesario correr las migracions para poder trabajar con el prouyecto
```
python manage.py makemigrations --settings=crud_ecomerse.settings.local
python manage.py migrate --settings=crud_ecomerse.settings.local
```

Dorrer el proyecto con las configuraciones de desarrollo

```
python manage.py runserver --settings=crud_ecomerse.settings.local
```
Ver proyecto en el navegador

Abrir [http://localhost:8000](http://localhost:8000)

