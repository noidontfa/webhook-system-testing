# Setup Command

## Set up ngrok
```
https://ngrok.com/
```
## Set up event
```
pip install -r requirements.txt

python3 main.py

ngrok http 3000
```

# API Usage
## Subscribe an event

```
curl --location 'http://127.0.0.1:8000/ws/v1/webhook' \
--header 'Content-Type: application/json' \
--data '{
    "event_type": "EV_ONE",
    "url": "https://ba95-116-109-60-166.ngrok-free.app/webhook/post/verify_success",
    "headers": {
        "hello": "world"
    },
    "secret_key": "thisissecretkey",
    "user_id": 1,
    "is_active": false
}'
```

```
curl --location 'http://127.0.0.1:8000/ws/v1/webhook' \
--header 'Content-Type: application/json' \
--data '{
    "event_type": "EV_TWO",
    "url": "https://ba95-116-109-60-166.ngrok-free.app/webhook/post/verify_failed",
    "headers": {
        "hello": "world"
    },
    "secret_key": "thisissecretkey",
    "user_id": 1,
    "is_active": false
}'
```
```
curl --location 'http://127.0.0.1:8000/ws/v1/webhook' \
--header 'Content-Type: application/json' \
--data '{
    "event_type": "EV_THREE",
    "url": "https://ba95-116-109-60-166.ngrok-free.app/webhook/post/delivery_success",
    "headers": {
        "hello": "world"
    },
    "secret_key": "thisissecretkey",
    "user_id": 1,
    "is_active": false
}'
```
```
curl --location 'http://127.0.0.1:8000/ws/v1/webhook' \
--header 'Content-Type: application/json' \
--data '{
    "event_type": "EV_FOUR",
    "url": "https://ba95-116-109-60-166.ngrok-free.app/webhook/post/delivery_failed",
    "headers": {
        "hello": "world"
    },
    "secret_key": "thisissecretkey",
    "user_id": 1,
    "is_active": false
}'
```
## Verify event webhook
```
curl --location 'http://127.0.0.1:8000/ws/v1/webhook/:webhook_id
curl --location 'http://127.0.0.1:8000/ws/v1/webhook/1
curl --location 'http://127.0.0.1:8000/ws/v1/webhook/2
curl --location 'http://127.0.0.1:8000/ws/v1/webhook/3
curl --location 'http://127.0.0.1:8000/ws/v1/webhook/4
```

## Trigger a webhook event
```
curl --location 'http://127.0.0.1:8000/ws/v1/event' \
--header 'Content-Type: application/json' \
--data '{
    "trigger_type": "NOW",
    "execution_time": 0,
    "event_type": "EV_ONE",
    "user_id": 1,
    "payload": {
        "msg": "message and data delivery to the user system",
    }
}'
```

```
curl --location 'http://127.0.0.1:8000/ws/v1/event' \
--header 'Content-Type: application/json' \
--data '{
    "trigger_type": "SCHEDULED",
    "execution_date": 1710852359,
    "event_type": "EV_ONE",
    "user_id": 1,
    "payload": {
        "msg": "message and data delivery to the user system"
    }
}'
```