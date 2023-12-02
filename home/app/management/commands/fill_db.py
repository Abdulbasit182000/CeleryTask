from app.models import CustomUser
from django.core.management.base import BaseCommand
from django.utils import timezone
from faker import Faker


class Command(BaseCommand):
    help = "Fills DB with Custom Users"

    def add_arguments(self, parser):
        parser.add_argument("count", type=int, help="count of user")

    def handle(self, *args, **kwargs):
        count = kwargs["count"]
        faker = Faker()
        for i in range(count):
            obj = CustomUser()
            obj.email = f"abdul{i}@gmail.com"
            obj.phone_number = faker.phone_number()
            obj.date_of_birth = faker.date_time_between(
                start_date="-30y",
                end_date="now",
                tzinfo=timezone.get_current_timezone(),
            )
            obj.set_password(faker.name())
            obj.save()
