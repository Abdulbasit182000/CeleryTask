import redis
from app.tasks import convert, convertpst
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Run the convert task multiple times"

    def handle(self, *args, **options):
        redis_client = redis.StrictRedis(host="localhost", port=6379, db=0)
        while True:
            redis_client.set("start", 0)
            redis_client.set("end", 10)
            redis_client.set("x", 0)
            while int(redis_client.get("x")) != 10:
                print(int(redis_client.get("start")), int(redis_client.get("end")))

                for i in range(1):
                    reuslt = convert.apply_async(
                        args=[
                            int(redis_client.get("start")),
                            int(redis_client.get("end")),
                        ],
                        countdown=(i + 1) * 20,
                    )
                    reuslt.wait()

                redis_client.set("start", int(redis_client.get("end")))
                redis_client.set("end", (int(redis_client.get("end")) + 10))
                redis_client.set("x", (int(redis_client.get("x")) + 1))
            print("Done with UTC timezone")

            redis_client.set("start", 0)
            redis_client.set("end", 10)
            redis_client.set("x", 0)
            while int(redis_client.get("x")) != 10:
                print(int(redis_client.get("start")), int(redis_client.get("end")))

                for i in range(1):
                    reuslt = convertpst.apply_async(
                        args=[
                            int(redis_client.get("start")),
                            int(redis_client.get("end")),
                        ],
                        countdown=(i + 1) * 20,
                    )
                    reuslt.wait()

                redis_client.set("start", int(redis_client.get("end")))
                redis_client.set("end", (int(redis_client.get("end")) + 10))
                redis_client.set("x", (int(redis_client.get("x")) + 1))
            print("Done with PST timezone")
