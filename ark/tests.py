from django.test import TestCase
from ark.transactions import TX, TxBroadcaster



class TxTestCase(TestCase):
    def test_single_tx(self):
        tx = TX(
            amount=1,
            secret="talk coral spatial wall pipe wolf orient attack soft favorite ordinary buzz",
            recipient="DA1SPukujJqfVqiGfq9yFUnnEucpxevgbA",
            network="dark",
        )

        tx.send(use_open_peers=True)
        self.assertNotEqual(tx.tx.res["success"], '0,0%')


class TxBroadCasterTestCase(TestCase):
    def setUp(self):
        """
        We bake some transactions and store them in the db.
        """
        for i in range(10):
            tx = TX(
                amount=i+1,
                secret="talk coral spatial wall pipe wolf orient attack soft favorite ordinary buzz",
                recipient="DA1SPukujJqfVqiGfq9yFUnnEucpxevgbA",
                network="dark",
            )

            tx.queue()

    def test_broadcaster(self):
        caster = TxBroadcaster(uid=0, singlerun=True)
        caster.run()


