# Generated by Django 2.0.3 on 2018-03-16 16:46

import datetime
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blocks',
            fields=[
                ('id', models.CharField(max_length=64, primary_key=True, serialize=False)),
                ('rowid', models.AutoField(db_column='rowId', primary_key=True)),
                ('version', models.IntegerField()),
                ('timestamp', models.IntegerField()),
                ('height', models.IntegerField(unique=True)),
                ('numberoftransactions', models.IntegerField(db_column='numberOfTransactions')),
                ('totalamount', models.BigIntegerField(db_column='totalAmount')),
                ('totalfee', models.BigIntegerField(db_column='totalFee')),
                ('reward', models.BigIntegerField()),
                ('payloadlength', models.IntegerField(db_column='payloadLength')),
                ('payloadhash', models.BinaryField(db_column='payloadHash')),
                ('generatorpublickey', models.BinaryField(db_column='generatorPublicKey')),
                ('blocksignature', models.BinaryField(db_column='blockSignature')),
                ('rawtxs', models.TextField()),
            ],
            options={
                'db_table': 'blocks',
                'get_latest_by': '-height',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ForksStat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('delegatepublickey', models.BinaryField(db_column='delegatePublicKey')),
                ('blocktimestamp', models.IntegerField(db_column='blockTimestamp')),
                ('blockid', models.CharField(db_column='blockId', max_length=64)),
                ('blockheight', models.IntegerField(db_column='blockHeight')),
                ('previousblock', models.CharField(db_column='previousBlock', max_length=64)),
                ('cause', models.IntegerField()),
            ],
            options={
                'db_table': 'forks_stat',
                'get_latest_by': '-blockheight',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MemAccounts',
            fields=[
                ('username', models.CharField(blank=True, max_length=20, null=True)),
                ('isdelegate', models.SmallIntegerField(blank=True, db_column='isDelegate', null=True)),
                ('u_isdelegate', models.SmallIntegerField(blank=True, db_column='u_isDelegate', null=True)),
                ('secondsignature', models.SmallIntegerField(blank=True, db_column='secondSignature', null=True)),
                ('u_secondsignature', models.SmallIntegerField(blank=True, db_column='u_secondSignature', null=True)),
                ('u_username', models.CharField(blank=True, max_length=20, null=True)),
                ('address', models.CharField(max_length=36, primary_key=True, serialize=False)),
                ('publickey', models.BinaryField(blank=True, db_column='publicKey', null=True)),
                ('secondpublickey', models.BinaryField(blank=True, db_column='secondPublicKey', null=True)),
                ('balance', models.BigIntegerField(blank=True, null=True)),
                ('u_balance', models.BigIntegerField(blank=True, null=True)),
                ('vote', models.BigIntegerField(blank=True, null=True)),
                ('rate', models.BigIntegerField(blank=True, null=True)),
                ('delegates', models.TextField(blank=True, null=True)),
                ('u_delegates', models.TextField(blank=True, null=True)),
                ('multisignatures', models.TextField(blank=True, null=True)),
                ('u_multisignatures', models.TextField(blank=True, null=True)),
                ('multimin', models.SmallIntegerField(blank=True, null=True)),
                ('u_multimin', models.SmallIntegerField(blank=True, null=True)),
                ('multilifetime', models.SmallIntegerField(blank=True, null=True)),
                ('u_multilifetime', models.SmallIntegerField(blank=True, null=True)),
                ('blockid', models.CharField(blank=True, db_column='blockId', max_length=64, null=True)),
                ('nameexist', models.SmallIntegerField(blank=True, null=True)),
                ('u_nameexist', models.SmallIntegerField(blank=True, null=True)),
                ('producedblocks', models.IntegerField(blank=True, null=True)),
                ('missedblocks', models.IntegerField(blank=True, null=True)),
                ('fees', models.BigIntegerField(blank=True, null=True)),
                ('rewards', models.BigIntegerField(blank=True, null=True)),
                ('virgin', models.SmallIntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'mem_accounts',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MemAccounts2UDelegates',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dependentid', models.CharField(db_column='dependentId', max_length=66)),
            ],
            options={
                'db_table': 'mem_accounts2u_delegates',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MemAccounts2UMultisignatures',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dependentid', models.CharField(db_column='dependentId', max_length=66)),
            ],
            options={
                'db_table': 'mem_accounts2u_multisignatures',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MemDelegates',
            fields=[
                ('publickey', models.CharField(db_column='publicKey', max_length=66, primary_key=True, serialize=False)),
                ('vote', models.BigIntegerField()),
                ('round', models.BigIntegerField()),
                ('producedblocks', models.IntegerField(blank=True, null=True)),
                ('missedblocks', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'mem_delegates',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Migrations',
            fields=[
                ('id', models.CharField(max_length=22, primary_key=True, serialize=False)),
                ('name', models.TextField()),
            ],
            options={
                'db_table': 'migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Peers',
            fields=[
                ('ip', models.GenericIPAddressField(primary_key=True, serialize=False)),
                ('port', models.SmallIntegerField()),
                ('state', models.SmallIntegerField()),
                ('os', models.CharField(blank=True, max_length=64, null=True)),
                ('version', models.CharField(blank=True, max_length=11, null=True)),
                ('clock', models.BigIntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'peers',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Transactions',
            fields=[
                ('id', models.CharField(max_length=64, primary_key=True, serialize=False)),
                ('rowid', models.AutoField(db_column='rowId', primary_key=True)),
                ('type', models.SmallIntegerField()),
                ('timestamp', models.IntegerField()),
                ('senderpublickey', models.BinaryField(db_column='senderPublicKey')),
                ('senderid', models.CharField(db_column='senderId', max_length=36)),
                ('recipientid', models.CharField(blank=True, db_column='recipientId', max_length=36, null=True)),
                ('amount', models.BigIntegerField()),
                ('fee', models.BigIntegerField()),
                ('signature', models.BinaryField()),
                ('signsignature', models.BinaryField(blank=True, db_column='signSignature', null=True)),
                ('requesterpublickey', models.BinaryField(blank=True, db_column='requesterPublicKey', null=True)),
                ('vendorfield', models.CharField(blank=True, db_column='vendorField', max_length=64, null=True)),
                ('signatures', models.TextField(blank=True, null=True)),
                ('rawasset', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'transactions',
                'get_latest_by': '-timestamp',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tx', django.contrib.postgres.fields.jsonb.JSONField()),
                ('desc', models.CharField(max_length=1000, null=True)),
                ('confirmations', models.IntegerField(default=0)),
                ('success', models.BooleanField(default=False)),
                ('error', models.CharField(max_length=10000, null=True)),
                ('tx_id', models.CharField(max_length=100, null=True, unique=True)),
                ('tries', models.IntegerField(default=0)),
                ('send', models.BooleanField(default=False)),
                ('res', models.CharField(max_length=10000, null=True)),
                ('network', models.CharField(default='dark', max_length=50)),
                ('broadcaster', models.IntegerField(default=0)),
                ('created', models.DateTimeField(default=datetime.datetime.now)),
            ],
            options={
                'ordering': ['-created', 'confirmations'],
                'get_latest_by': '-created',
            },
        ),
        migrations.CreateModel(
            name='Delegates',
            fields=[
                ('username', models.CharField(max_length=20)),
                ('id', models.ForeignKey(db_column='transactionId', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='ark.Transactions')),
            ],
            options={
                'db_table': 'delegates',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MemAccounts2Delegates',
            fields=[
                ('accountid', models.ForeignKey(db_column='accountId', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='ark.MemAccounts')),
                ('dependentid', models.CharField(db_column='dependentId', max_length=66)),
            ],
            options={
                'db_table': 'mem_accounts2delegates',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MemAccounts2Multisignatures',
            fields=[
                ('accountid', models.ForeignKey(db_column='accountId', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='ark.MemAccounts')),
                ('dependentid', models.CharField(db_column='dependentId', max_length=66)),
            ],
            options={
                'db_table': 'mem_accounts2multisignatures',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Multisignatures',
            fields=[
                ('min', models.IntegerField()),
                ('lifetime', models.IntegerField()),
                ('keysgroup', models.TextField()),
                ('transactionid', models.ForeignKey(db_column='transactionId', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='ark.Transactions')),
            ],
            options={
                'db_table': 'multisignatures',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Signatures',
            fields=[
                ('transactionid', models.ForeignKey(db_column='transactionId', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, related_name='transactions', serialize=False, to='ark.Transactions')),
                ('publickey', models.BinaryField(db_column='publicKey')),
            ],
            options={
                'db_table': 'signatures',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Votes',
            fields=[
                ('votes', models.TextField(blank=True, null=True)),
                ('transactionid', models.ForeignKey(db_column='transactionId', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='ark.Transactions')),
            ],
            options={
                'db_table': 'votes',
                'managed': False,
            },
        ),
    ]