# se puede instalar Django con 'pip install django'
# hay que ubicarse en la carpeta en la que se quiere crear el proyecto.
# para iniciar en powershell:  "django-admin startproject miproyecto .""

# Un proyecto esta compuesto por multiples APLICACIONES, todas bajo un mismo control administrativo. POr ejemplo en una tiend aonline tenemos las sig APPs: 'carrito de compra', 'usuarios', 'contct'.
#
# django necesita guardar los datos en alguna base de datos. MySQL, SQLite,etc. por defectoen SETTINGS lo configura con la libreria que este por defecto instalada.(en este caso estaba instalada sqlite3).

# Para comprobarlo "python3 manage.py runserver" esto nos creara un servidor web

######Para creas dichas APPs:
"""python3 manage.py startapp 'nombreDelaApp' """

# Conectar proyecto general (miproyecto) con las APPs: para este ejemplo 'catalog': configurarlo en 'sttings.py' en la seccion 'INSTALLED_APPS' incluir 'catalog.apps.CatalogConfig' de esta forma djando sepa que hay algo más instalado.

# conectar la ruta o vista (views): ficheros 'urls.py' :
# urlpatterns = [
# #path('admin/', admin.site.urls),
# #path('catalog/', include('catalag.urls'))
# #]

# luego hay que ir al fichero 'urls.py' dentro de la APP (catalog), si este no existe hay que crearlo. E importar los modulos= "From django.urls import include, re_path, from . import views". además crear la conxion a el proyecto con= "urlpatterns= []"

# situarse nuevamente sobre la carpeta donde se enceuntra el proyecto desde powershell y realizar la migración de datos con = "python3 manage.py migrate" para importar los combios a la base de datos que se han realizado

###### Crear Usuario y Contraseña #######
"""
python3 manage.py createsuperuser
"""
######siempre se deben trabajar los modelos dentro de las aplicaciones;:

#Luego se crean todos los modelos (clases/objetos) que se van a usar en la APP para que pueda almacenarse los datos ingresado para cada una en la BD: fichero 'models.py' dentro de la app.

# Luego en el fichero 'admin.py' se importyan los modelos definidos en models.py y posteriormente se registran los modelos: 'admin.site.register(Book)', 'admin.site.register(Author)', 'admin.site.register(Genere)'
