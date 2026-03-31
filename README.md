### Objetivo

Desplegar un modelo mediante API REST en algún entorno accesible a través de una dirección pública de internet (se sugiere **Render** pero es completamente voluntario). 

Por accesible se entiende poder hacer una petición con datos de entrada que permitan dar una predicción o etiquetado al modelo y que el servicio devuelva la etiqueta o predicción generada por el modelo. Esta funcionalidad se debe ofrecer a través de un endpoint accesible al menos mediante una petición requests.get de Python. 

Como complemento al anterior endpoint se debe proveer un endopoint ligado al "/" o landingpage que informe de cómo se debe acceder el resto de endpoints (si hay alguno más además del que permita el uso del modelo).

Finalmente, durante la exposición del trabajo además de hacer una prueba in-situ del uso de los endpoints proporcionados por la web-app del grupo, se pedirá hacer una modificación en el código y hacer un redespliegue de forma que se implemente dicho cambio (tened preparado un tercer endpoint comentado para descomentar y redesplegar).

### Extra voluntario
- Implementar un endpoint que permitar el reentrenamiento del modelo, añadiendo un dataset nuevo de entrenamiento al repositorio del código de la app.  
- Implementar un mecanismo de despliegue continuo mediante webhooks. Es decir que el despliegue se haga de forma continua y sin tocar en el servidor una vez "comprometidos" (commited) los cambios en el repositorio del grupo.
