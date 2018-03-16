from django.db import models
from django.contrib.postgres.fields import JSONField
from datetime import datetime

class Blocks(models.Model):
    id = models.CharField(primary_key=True, max_length=64)
    rowid = models.AutoField(db_column='rowId', primary_key=True)  # Field name made lowercase.
    version = models.IntegerField()
    timestamp = models.IntegerField()
    height = models.IntegerField(unique=True)
    previousblock = models.ForeignKey('self', models.DO_NOTHING, db_column='previousBlock', unique=True, blank=True, null=True)  # Field name made lowercase.
    numberoftransactions = models.IntegerField(db_column='numberOfTransactions')  # Field name made lowercase.
    totalamount = models.BigIntegerField(db_column='totalAmount')  # Field name made lowercase.
    totalfee = models.BigIntegerField(db_column='totalFee')  # Field name made lowercase.
    reward = models.BigIntegerField()
    payloadlength = models.IntegerField(db_column='payloadLength')  # Field name made lowercase.
    payloadhash = models.BinaryField(db_column='payloadHash')  # Field name made lowercase.
    generatorpublickey = models.BinaryField(db_column='generatorPublicKey')  # Field name made lowercase.
    blocksignature = models.BinaryField(db_column='blockSignature')  # Field name made lowercase.
    rawtxs = models.TextField()

    class Meta:
        managed = False
        db_table = 'blocks'
        get_latest_by = "-height"


class Delegates(models.Model):
    username = models.CharField(max_length=20)
    id = models.ForeignKey('Transactions', models.DO_NOTHING, db_column='transactionId', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'delegates'


class ForksStat(models.Model):
    delegatepublickey = models.BinaryField(db_column='delegatePublicKey')  # Field name made lowercase.
    blocktimestamp = models.IntegerField(db_column='blockTimestamp')  # Field name made lowercase.
    blockid = models.CharField(db_column='blockId', max_length=64)  # Field name made lowercase.
    blockheight = models.IntegerField(db_column='blockHeight')  # Field name made lowercase.
    previousblock = models.CharField(db_column='previousBlock', max_length=64)  # Field name made lowercase.
    cause = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'forks_stat'
        get_latest_by = "-blockheight"


class MemAccounts(models.Model):
    username = models.CharField(max_length=20, blank=True, null=True)
    isdelegate = models.SmallIntegerField(db_column='isDelegate', blank=True, null=True)  # Field name made lowercase.
    u_isdelegate = models.SmallIntegerField(db_column='u_isDelegate', blank=True, null=True)  # Field name made lowercase.
    secondsignature = models.SmallIntegerField(db_column='secondSignature', blank=True, null=True)  # Field name made lowercase.
    u_secondsignature = models.SmallIntegerField(db_column='u_secondSignature', blank=True, null=True)  # Field name made lowercase.
    u_username = models.CharField(max_length=20, blank=True, null=True)
    address = models.CharField(primary_key=True, max_length=36)
    publickey = models.BinaryField(db_column='publicKey', blank=True, null=True)  # Field name made lowercase.
    secondpublickey = models.BinaryField(db_column='secondPublicKey', blank=True, null=True)  # Field name made lowercase.
    balance = models.BigIntegerField(blank=True, null=True)
    u_balance = models.BigIntegerField(blank=True, null=True)
    vote = models.BigIntegerField(blank=True, null=True)
    rate = models.BigIntegerField(blank=True, null=True)
    delegates = models.TextField(blank=True, null=True)
    u_delegates = models.TextField(blank=True, null=True)
    multisignatures = models.TextField(blank=True, null=True)
    u_multisignatures = models.TextField(blank=True, null=True)
    multimin = models.SmallIntegerField(blank=True, null=True)
    u_multimin = models.SmallIntegerField(blank=True, null=True)
    multilifetime = models.SmallIntegerField(blank=True, null=True)
    u_multilifetime = models.SmallIntegerField(blank=True, null=True)
    blockid = models.CharField(db_column='blockId', max_length=64, blank=True, null=True)  # Field name made lowercase.
    nameexist = models.SmallIntegerField(blank=True, null=True)
    u_nameexist = models.SmallIntegerField(blank=True, null=True)
    producedblocks = models.IntegerField(blank=True, null=True)
    missedblocks = models.IntegerField(blank=True, null=True)
    fees = models.BigIntegerField(blank=True, null=True)
    rewards = models.BigIntegerField(blank=True, null=True)
    virgin = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mem_accounts'


class MemAccounts2Delegates(models.Model):
    accountid = models.ForeignKey(MemAccounts, models.DO_NOTHING, db_column='accountId', primary_key=True)  # Field name made lowercase.
    dependentid = models.CharField(db_column='dependentId', max_length=66)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'mem_accounts2delegates'


class MemAccounts2Multisignatures(models.Model):
    accountid = models.ForeignKey(MemAccounts, models.DO_NOTHING, db_column='accountId', primary_key=True)  # Field name made lowercase.
    dependentid = models.CharField(db_column='dependentId', max_length=66)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'mem_accounts2multisignatures'


class MemAccounts2UDelegates(models.Model):
    accountid = models.ForeignKey(MemAccounts, models.DO_NOTHING, db_column='accountId')  # Field name made lowercase.
    dependentid = models.CharField(db_column='dependentId', max_length=66)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'mem_accounts2u_delegates'


class MemAccounts2UMultisignatures(models.Model):
    accountid = models.ForeignKey(MemAccounts, models.DO_NOTHING, db_column='accountId')  # Field name made lowercase.
    dependentid = models.CharField(db_column='dependentId', max_length=66)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'mem_accounts2u_multisignatures'


class MemDelegates(models.Model):
    publickey = models.CharField(db_column='publicKey', max_length=66, primary_key=True)  # Field name made lowercase.
    vote = models.BigIntegerField()
    round = models.BigIntegerField()
    producedblocks = models.IntegerField(blank=True, null=True)
    missedblocks = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mem_delegates'


class Migrations(models.Model):
    id = models.CharField(primary_key=True, max_length=22)
    name = models.TextField()

    class Meta:
        managed = False
        db_table = 'migrations'


class Multisignatures(models.Model):
    min = models.IntegerField()
    lifetime = models.IntegerField()
    keysgroup = models.TextField()
    transactionid = models.ForeignKey('Transactions', models.DO_NOTHING, db_column='transactionId', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'multisignatures'


class Peers(models.Model):
    ip = models.GenericIPAddressField(primary_key=True)
    port = models.SmallIntegerField()
    state = models.SmallIntegerField()
    os = models.CharField(max_length=64, blank=True, null=True)
    version = models.CharField(max_length=11, blank=True, null=True)
    clock = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'peers'
        unique_together = (('ip', 'port'),)


class Signatures(models.Model):
    transactionid = models.ForeignKey('Transactions', models.DO_NOTHING, db_column='transactionId', primary_key=True,
                                      related_name='transactions')  # Field name made lowercase.
    publickey = models.BinaryField(db_column='publicKey')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'signatures'


class Transactions(models.Model):
    id = models.CharField(primary_key=True, max_length=64)
    rowid = models.AutoField(db_column='rowId', primary_key=True)  # Field name made lowercase.
    blockid = models.ForeignKey(Blocks, models.DO_NOTHING, db_column='blockId')  # Field name made lowercase.
    type = models.SmallIntegerField()
    timestamp = models.IntegerField()
    senderpublickey = models.BinaryField(db_column='senderPublicKey')  # Field name made lowercase.
    senderid = models.CharField(db_column='senderId', max_length=36)  # Field name made lowercase.
    recipientid = models.CharField(db_column='recipientId', max_length=36, blank=True, null=True)  # Field name made lowercase.
    amount = models.BigIntegerField()
    fee = models.BigIntegerField()
    signature = models.BinaryField()
    signsignature = models.BinaryField(db_column='signSignature', blank=True, null=True)  # Field name made lowercase.
    requesterpublickey = models.BinaryField(db_column='requesterPublicKey', blank=True, null=True)  # Field name made lowercase.
    vendorfield = models.CharField(db_column='vendorField', max_length=64, blank=True, null=True)  # Field name made lowercase.
    signatures = models.TextField(blank=True, null=True)
    rawasset = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'transactions'
        get_latest_by = "-timestamp"


class Votes(models.Model):
    votes = models.TextField(blank=True, null=True)
    transactionid = models.ForeignKey(Transactions, models.DO_NOTHING, db_column='transactionId', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'votes'


# a table where we store transactions and leak them to the relay node as we continue along.
class Transaction(models.Model):
    # the specific transaction we send (by using the same transaction we ensure we don't double send.
    tx = JSONField()
    desc = models.CharField(max_length=1000, null=True)

    # check/rebroadcast tx until we reach thi amount of confirmations
    confirmations = models.IntegerField(default=0)

    success = models.BooleanField(default=False)
    error = models.CharField(null=True, max_length=10000)
    tx_id = models.CharField(null=True, max_length=100, unique=True)
    tries = models.IntegerField(default=0)
    send = models.BooleanField(default=False)
    res = models.CharField(null=True, max_length=10000)
    network = models.CharField(default='dark', max_length=50)
    broadcaster = models.IntegerField(default=0)
    created = models.DateTimeField(default=datetime.now)

    class Meta:
        ordering = ['-created', 'confirmations']
        get_latest_by = "-created"