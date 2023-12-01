from django.core.management.base import BaseCommand
from app.tasks import convert,convertpst

class Command(BaseCommand):
    help = 'Run the convert task multiple times'

    def handle(self, *args, **options):
        while(True):
            x = 0
            start = 0
            end = 10

            while x != 10:
                print(start, end)

                for i in range(1):
                    reuslt=convert.apply_async(args=[start, end], countdown=(i+1) * 20)
                    reuslt.wait()

                start = end
                end = end + 10
                x = x + 1
            print('Done with UTC timezone')
        
            x = 0
            start = 0
            end = 10

            while x != 10:
                print(start, end)

                for i in range(1):
                    reuslt=convertpst.apply_async(args=[start, end], countdown=(i+1) * 20)
                    reuslt.wait()

                start = end
                end = end + 10
                x = x + 1
            print('Done with PST timezone')

