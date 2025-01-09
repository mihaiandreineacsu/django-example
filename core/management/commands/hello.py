from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Prints a personalized greeting with optional repetitions"

    def add_arguments(self, parser):
        # Add a required 'name' argument
        parser.add_argument("name", type=str, help="Name to greet")

        # Add an optional 'times' argument
        parser.add_argument(
            "--times",
            type=int,
            default=1,
            help="Number of times to repeat the greeting",
        )

    def handle(self, *args, **options):
        name = options["name"]
        times = options["times"]

        for _ in range(times):
            self.stdout.write(f"Hello, {name}!")
