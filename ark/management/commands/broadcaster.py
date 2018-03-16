from django.core.management.base import BaseCommand, CommandError
from ark.transactions import TxBroadcaster


class Command(BaseCommand):
    help = 'start/stop a TxBroadcaster'

    def add_arguments(self, parser):
        parser.add_argument('uid', nargs=1, type=int)
        parser.add_argument('network', nargs=1, type=str)

    def handle(self, *args, **options):
        self.stdout.write('creating TxBroadcaster: {uid}, network: {network}'.format(
            uid=options['uid'][0],
            network=options['network'][0]))

        caster = TxBroadcaster(uid=options['uid'][0], network=options['network'][0])
        self.stdout.write('created successfully')
        self.stdout.write('starting TxBroadcaster: {}'.format(options['uid'][0]))
        caster.run()



