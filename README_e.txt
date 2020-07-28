Requerimientos:
-python3
-docker
-docker-compose

PASOS PARA EJECUTAR 
-Ubicarse en el directorio de la carpeta descargada desde terminal
-ejecutar "sudo docker-compose up" para iniciar los servicios
-abriri el navegador y pegar el link http://localhost:8181/


Acceder a la BD
-ejecutar sudo docker ps y copiar el id de mongodb
-ejecutar sudo socker exec -it id_mongo bash
-colocar mongo el la tarminal que se muestra, despues ejecutar:
    -show db
    -use testdb
    -show collections
    -db.users.find()
    -db.posts.find()

para vaciar los registros colocar
-db.posts.drop()


