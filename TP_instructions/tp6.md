summary: TP6
id: tp6
categories: tp, api
tags: api, flask
status: Published
authors: OCTO Technology
Feedback Link: https://github.com/octo-technology/Formation-MLOps-2/issues/new/choose

# TP6 - Couplage / Découplage / Async / Sync

## Vue d'ensemble

Duration: 0:05:00


### À l'issue de cette section, vous aurez découvert

// TODO
### Mise en place du TP

// TODO

## Démonstration du couplage / découplage

Duration: 0:05:00
// TODO

## Démonstration de l'utilisation de Async / Sync 

Duration: 0:15:00

### Explorer le code mis à disposition

Aller explorer le fichier [async_sync_api.py](../demos/async_sync_api.py), dedans 3 routes d'api sont définies : 
- blocking : Une API asynchrone qui est exécute time.sleep
- nonblocking : Une API asynchrone qui attend un process asynchrone 
- sync : Une API synchrone qui attend un process synchrone, 

Le paramètre `n` est là pour illustrer une complexité métier de l'appel, plus n est grand plus l'appel est long.

Le sleep est un moyen de modéliser facilement un calcul long.

### Lancer l'api
```shell
uv run  fastapi dev demos/async_sync_api.py 
```

Et tester avec un curl 
```shell
curl localhost:8000/blocking/1
```

### Comparer les délais de l'API blocking
Pour cela nous allons utiliser deux terminaux : 1 pour chaque client : 

Lancer les commandes : 
```shell
curl localhost:8000/blocking/15
```

```shell
time curl localhost:8000/blocking/1
```

`time` permet de mesuré le temps mis. 

Combien de temps met le premier curl, et le deuxième ? 
Que se passe-t-il si on inverse l'ordre des curls ? 

### Comparer les temps de l'API non-blocking

Lancer les commandes : 
```shell
curl localhost:8000/nonblocking/15
```

```shell
time curl localhost:8000/nonblocking/1
```

`time` permet de mesuré le temps mis. 

Combien de temps met le premier curl, et le deuxième ? 
Que se passe-t-il si on inverse l'ordre des curls ? 

### Comparer les temps de l'API sync

Lancer les commandes : 
```shell
curl localhost:8000/sync/15
```

```shell
time curl localhost:8000/sync/1
```

`time` permet de mesuré le temps mis. 

Combien de temps met le premier curl, et le deuxième ? 

Il y a une parallélisation qui est faite au niveau des threads et non plus dans la boucle asyncio.

### Réduction du nombre de threads
Essayons de réduire le nombre de threads pour illustrer cette différence. 

Remplacer 
```python
app = FastAPI()
```

Par ce code qui passe de la valeur par défaut (40 threads) à 1 thread.
```python
@asynccontextmanager
async def lifespan(app: FastAPI):
    anyio.to_thread.current_default_thread_limiter().total_tokens = 1
    yield


app = FastAPI(lifespan=lifespan)
```

Relancer les temps sur les méthodes de sync et non-blocking.

## Pour aller plus loin

// TODO

## Lien vers le TP suivant

Duration: 0:01:00

Les instructions du tp suivant sont [ici](https://octo-technology.github.io/Formation-MLOps-2/tp7#0) // To update