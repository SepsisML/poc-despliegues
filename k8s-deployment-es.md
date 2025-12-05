# Despliegue en Kubernetes

## Preliminares

Para llevar a cabo las pruebas del despliegue del API se utilizó [minikube](https://minikube.sigs.k8s.io/docs/) como entorno Kubernetes.

## Despliegue de la aplicación

Para llevar a cabo el despliegue del API es necesario:

### 1. Construir la imagen de la aplicación

```
docker build -t <login-github>/fastapi-sepsis:latest ./app
```

### 2. Subir la imagen de la aplicación a Docker Hub

```
docker push <login-github>/fastapi-sepsis:latest 
```

### 3. Despliegue de la aplicación en Kubernetes

A continuación se debe aplicar el manifesto `app/deployment-app.yaml` pero antes de aplicar el manifesto se debe editar el archivo YAML.

  1. Editar el archivo `app/deployment-app.yaml`.

  2. Buscar la palabra `image` y renombrar el nombre de la imagen de Docker por `<login-github>/fastapi-sepsis:latest`. Guardar los cambios.

  3. Ejecutar ahora, `kubectl apply -f app/deployment-app.yaml` 

  4. Usando el comando `kubectl get all` debería tener un resultado similar a este:

```
NAME                                     READY   STATUS    RESTARTS   AGE
pod/fastapi-deployment-5c4c5955f-wf77m   1/1     Running   0          2m16s

NAME                 TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)   AGE
service/kubernetes   ClusterIP   10.96.0.1    <none>        443/TCP   9m34s

NAME                                 READY   UP-TO-DATE   AVAILABLE   AGE
deployment.apps/fastapi-deployment   1/1     1            1           2m16s

NAME                                           DESIRED   CURRENT   READY   AGE
replicaset.apps/fastapi-deployment-5c4c5955f   1         1         1       2m16s
```

### 4. Exposición de la aplicación

Para habilitar un _endpoint_ que permita interactuar con la aplicación corriendo en Kubernetes se debe ejecutar el comando 

```
kubectl apply -f app/service-app.yaml
```

Ahora al consultar por los servicios disponibles (`kubectl get service`) se debe ver algo como lo siguiente:

```
NAME              TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)        AGE
fastapi-service   NodePort    10.111.90.138   <none>        80:31000/TCP   2m32s
kubernetes        ClusterIP   10.96.0.1       <none>        443/TCP        12m
```

### 5. Accediendo al _endpoint_

En este caso se usó minikube como entorno de pruebas de Kubernetes. 
Para conocer el _endpoint_ para ser consumido se ejecuta el comando

```
minikube service fastapi-service --url
```

Esto puede arrojar algo como  `http://192.168.49.2:31000/`

### 6. Ejemplo de accesos al _endpoint_ 

PENDIENTE
