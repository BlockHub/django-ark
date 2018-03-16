from ark.models import Blocks
import arky.rest


class DbManager:
    def __init__(self, db='ark_mainnet'):
        arky.rest.use('ark')
        self.db = db

    def check_height(self, max_dif=51):
        db_height = Blocks.objects.latest().height
        peers = arky.rest.GET.api.peers()['peers']
        api_height = max([peer['height'] for peer in peers])

        if api_height - db_height > max_dif:
            return False

        return True
