from celery import Celery

app = Celery('main',
             broker_url="redis://redis/0",
             result_backend="redis://redis/0")

@app.task
def custom_header():
    return {"request.headers": custom_header.request.headers,
            "request.custom_foo": getattr(custom_header.request, "custom_foo", None)}

def main():
    app.conf.task_always_eager = True
    res = custom_header.apply_async(headers={"custom_foo": "custom_bar"}).get()
    print("Eager: %r" % res)

    app.conf.task_always_eager = False
    res = custom_header.apply_async(headers={"custom_foo": "custom_bar"}).get()
    print("Non-Eager: %r" % res)


if __name__ == "__main__":
    main()