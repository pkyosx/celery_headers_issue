# Issue Description
Behavior discrepancy between eager and non-eager mode. When we turn on task_always_eager, headers will be stored in request.headers. When we turn off task_always_eager, items under headers will be stored directly on request's attributes.

```
python: 3.9
celery: 5.2.1
backend: redis
```

# Reproduce Step
```
docker-compose up -d --build
docker-compose exec -T worker python main.py
```