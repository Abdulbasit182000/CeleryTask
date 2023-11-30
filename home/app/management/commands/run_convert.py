from django.core.management.base import BaseCommand
from app.tasks import convert,convertpst

class Command(BaseCommand):
    help = 'Run the convert task multiple times'

    def handle(self, *args, **options):
        x = 0
        start = 0
        end = 10

        while x != 10:
            print('while start')
            print(start, end)

            for i in range(1):
                print(f'This is chunk {x+1}')
                reuslt=convertpst.apply_async(args=[start, end], countdown=(i+1) * 20)
                reuslt.wait()

            print('Chunk', x+1, 'completed')
            start = end
            end = end + 10
            x = x + 1

        self.stdout.write(self.style.SUCCESS('Successfully ran convert task multiple times.'))
