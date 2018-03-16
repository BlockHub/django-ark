from graphene import relay
import graphene
from graphene_django import DjangoObjectType
import ark.models as ark_blockchain
from graphene_django.converter import convert_django_field
from django.db import models
from ark.converter import BigInt, Binary


@convert_django_field.register(models.BinaryField)
def convert_column_to_string(typ, column, registry=None):
    return graphene.Field(Binary)


class VotesType(DjangoObjectType):
    class Meta:
        model = ark_blockchain.Votes
        interfaces = (relay.Node,)
        filter_fields = {
            'votes': ['exact'],
            'transactionid': ['exact']
        }


class TransactionType(DjangoObjectType):
    amount = graphene.Field(BigInt)

    class Meta:
        model = ark_blockchain.Transactions
        interfaces = (relay.Node,)
        filter_fields = {
            'id': ['exact'],
            'rowid': ['exact'],
            'blockid': ['exact'],
            'type':  ['exact', 'lt', 'gt', 'gte', 'lte'],
            'timestamp':  ['exact', 'lt', 'gt', 'gte', 'lte'],
            # 'senderpublickey': ['exact'],
            'senderid': ['exact'],
            'recipientid': ['exact'],
            'amount': ['exact', 'lt', 'gt', 'gte', 'lte'],
            'fee': ['exact', 'lt', 'gt', 'gte', 'lte'],
            # 'signature': ['exact'],
            # 'signsignature': ['exact'],
            # 'requesterpublickey': ['exact'],
            'vendorfield': ['exact'],
            # 'signatures': ['exact'],
            'rawasset': ['exact'],
        }


class SignatureType(DjangoObjectType):
    class Meta:
        model = ark_blockchain.Signatures
        interfaces = (relay.Node,)
        filter_fields = {
            'transactionid': ['exact'],
            # 'publickey': ['exact'],
        }


class PeersType(DjangoObjectType):
    class Meta:
        model = ark_blockchain.Peers
        interfaces = (relay.Node,)
        filter_fields = {
            'ip': ['exact'],
            'port': ['exact'],
            'os': ['exact'],
            'version': ['exact'],
            'clock': ['exact', 'lt', 'gt', 'gte', 'lte'],
        }


class MultisignatureType(DjangoObjectType):
    # transactionid = graphene.ID
    class Meta:
        model = ark_blockchain.Multisignatures
        interfaces = (relay.Node,)
        filter_fields = {
            'min': ['exact', 'lt', 'gt', 'gte', 'lte'],
            'lifetime': ['exact', 'lt', 'gt', 'gte', 'lte'],
            'keysgroup': ['exact'],
            'transactionid': ['exact'],
        }


class MigrationsType(DjangoObjectType):
    class Meta:
        model = ark_blockchain.Migrations
        interfaces = (relay.Node,)
        filter_fields = {
            'id': ['exact', 'lt', 'gt', 'gte', 'lte'],
            'name': ['exact']
        }


class MemDelegatesType(DjangoObjectType):
    publickey = graphene.String()

    class Meta:
        model = ark_blockchain.MemDelegates
        interfaces = (relay.Node,)
        filter_fields = {
            'publickey': ['exact'],
            'vote': ['exact', 'lt', 'gt', 'gte', 'lte'],
            'round': ['exact', 'lt', 'gt', 'gte', 'lte'],
            'producedblocks': ['exact', 'lt', 'gt', 'gte', 'lte'],
            'missedblocks': ['exact', 'lt', 'gt', 'gte', 'lte'],
        }


class DelegateType(DjangoObjectType):
    username = graphene.String()
    id = graphene.ID

    class Meta:
        model = ark_blockchain.Delegates
        interfaces = (relay.Node,)
        filter_fields = {
            'username': ['exact']
        }


class ForksStatType(DjangoObjectType):
    class Meta:
        model = ark_blockchain.ForksStat
        interfaces = (relay.Node,)
        filter_fields = {
            # 'delegatepublickey': ['exact'],
            'blocktimestamp': ['exact', 'lt', 'gt', 'gte', 'lte'],
            'blockid': ['exact'],
            'blockheight': ['exact', 'lt', 'gt', 'gte', 'lte'],
            'previousblock': ['exact'],
            'cause': ['exact', 'lt', 'gt', 'gte', 'lte'],
        }


class MemAccounts2MultisignaturesType(DjangoObjectType):
    class Meta:
        model = ark_blockchain.MemAccounts2Multisignatures
        interfaces = (relay.Node,)
        filter_fields = {
            'accountid': ['exact'],
            'dependentid': ['exact'],

        }


class AccountType(DjangoObjectType):
    balance = graphene.Field(BigInt)
    vote = graphene.Field(BigInt)
    rewards = graphene.Field(BigInt)
    u_balance = graphene.Field(BigInt)

    class Meta:
        model = ark_blockchain.MemAccounts

        filter_fields = {
            'balance': ['exact', 'lt', 'gt', 'gte', 'lte'],
            'vote': ['exact', 'lt', 'gt', 'gte', 'lte'],
            'secondsignature': ['exact'],
            'isdelegate': ['exact'],
        }

        interfaces = (relay.Node,)


class DependantType(DjangoObjectType):

    class Meta:
        model = ark_blockchain.MemAccounts2Delegates
        filter_fields = {
            'accountid': ['exact'],
            'dependentid': ['exact']
        }
        interfaces = (relay.Node,)


class BlocksType(DjangoObjectType):
    rowid = graphene.Field(BigInt)
    timestamp = graphene.Field(BigInt)
    height = graphene.Field(BigInt)
    totalamount = graphene.Field(BigInt)
    totalfee = graphene.Field(BigInt)
    reward = graphene.Field(BigInt)

    class Meta:
        model = ark_blockchain.Blocks
        interfaces = (relay.Node,)

        filter_fields = {
            'height': ['exact', 'lt', 'gt', 'gte', 'lte'],
            'timestamp': ['exact', 'lt', 'gt', 'gte', 'lte'],
            'totalamount': ['exact', 'lt', 'gt', 'gte', 'lte'],
            'totalfee': ['exact', 'lt', 'gt', 'gte', 'lte'],
            'numberoftransactions': ['exact', 'lt', 'gt', 'gte', 'lte'],
        }