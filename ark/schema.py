from graphene_django.filter import DjangoFilterConnectionField
from graphene_django.debug import DjangoDebug
from ark.types import *
from django.db.models import Q


class Query(graphene.ObjectType):
    debug = graphene.Field(DjangoDebug, name='__debug')

    all_accounts = DjangoFilterConnectionField(AccountType)
    all_blocks = DjangoFilterConnectionField(BlocksType)
    all_dependants = DjangoFilterConnectionField(DependantType)
    all_delegates = DjangoFilterConnectionField(DelegateType)
    all_forksstats = DjangoFilterConnectionField(ForksStatType)
    all_mem2multisignatures = DjangoFilterConnectionField(MemAccounts2MultisignaturesType)
    all_memdelegates = DjangoFilterConnectionField(MemDelegatesType)
    all_migrations = DjangoFilterConnectionField(MigrationsType)
    all_multisignatures = DjangoFilterConnectionField(MultisignatureType)
    all_peers = DjangoFilterConnectionField(PeersType)
    all_signatures = DjangoFilterConnectionField(SignatureType)
    all_transactions = DjangoFilterConnectionField(TransactionType, SenderOrRecipient=graphene.String())
    all_votes = DjangoFilterConnectionField(VotesType)

    vote = graphene.Field(
        type=VotesType
    )

    transaction = graphene.Field(
        type=TransactionType,
    )

    signature = graphene.Field(
        type=SignatureType
    )

    peer = graphene.Field(
        type=PeersType
    )

    multisignature = graphene.Field(
        type=MultisignatureType
    )

    migration = graphene.Field(
        type=MigrationsType,
        id=graphene.ID(),
    )

    memdelegate = graphene.Field(
        type=MemDelegatesType
    )

    mem2multisignature = graphene.Field(
        type=MemAccounts2MultisignaturesType
    )

    forksstat = graphene.Field(
        type=ForksStatType
    )

    account = graphene.Field(
        type=AccountType,
        address=graphene.String(),
        username=graphene.String(),
        isdelegate=graphene.Int(),
        secondsignature=graphene.Int(),
        dependentid=graphene.String(),
    )

    dependent = graphene.Field(
        type=DependantType,
        accountid=graphene.String(),
        dependantid=graphene.String(),
    )

    block = graphene.Field(
        type=BlocksType,
        id=graphene.ID(),
        height=graphene.Int(),
        timestamp=graphene.Int()
    )

    delegate = graphene.Field(
        type=DelegateType,
        id=graphene.ID(),
        username=graphene.String(),
    )

    def resolve_all_votes(self, info, **kwargs):
        return ark_blockchain.Transactions.objects.prefetch_related('blockid__transactions_set__votes_set')

    def resolve_all_transactions(self, info, **kwargs):

        or_term = kwargs.get('SenderOrRecipient', '')

        if or_term:
            return ark_blockchain.Transactions.objects.prefetch_related('blockid__transactions_set__delegates_set').all().\
                filter(Q(senderid=or_term) | Q(recipientid=or_term))

        return ark_blockchain.Transactions.objects.prefetch_related('blockid__transactions_set__delegates_set').all()

    def resolve_all_signatures(self, info, **kwargs):
        return ark_blockchain.Signatures.objects.select_related('transactionid__blockid')

    def resolve_all_peers(self, info, **kwargs):
        return ark_blockchain.Peers.objects.all()

    def resolve_all_multisignatures(self, info, **kwargs):
        return ark_blockchain.Multisignatures.objects.select_related('transactionid__blockid_id')

    def resolve_all_migrations(self, info, **kwargs):
        return ark_blockchain.Migrations.objects.all()

    def resolve_all_memdelegates(self, info, **kwargs):
        return ark_blockchain.MemDelegates.objects.all()

    def resolve_all_mem2multisignatures(self, info, **kwargs):
        return ark_blockchain.MemAccounts2Multisignatures.objects.select_related('accountid')

    def resolve_all_forksstats(self, info, **kwargs):
        return ark_blockchain.ForksStat.objects.all()

    def resolve_all_blocks(self, info, **kwargs):
        return ark_blockchain.Blocks.objects.all()

    def resolve_all_accounts(self, info, **kwargs):
        return ark_blockchain.MemAccounts.objects.all()

    def resolve_all_dependents(self, info, **kwargs):
        return ark_blockchain.MemAccounts2Delegates.objects.select_related('accountid')

    def resolve_all_delegates(self, info, **kwargs):
        return ark_blockchain.Delegates.objects.all()

    def resolve_vote(self, info, **kwargs):
        transactionid = kwargs.get('transactionid')

        if transactionid is not None:
            return ark_blockchain.Votes.objects.select_related('transactionid__blockid')
        return None

    def resolve_transaction(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            ark_blockchain.Transactions.objects.select_related('blockid').get(id=id)
        return None

    def resolve_signature(self, info, **kwargs):
        transactionid = kwargs.get('transactionid')

        if transactionid is not None:
            return ark_blockchain.Signatures.objects.get(transactionid=transactionid)
        return None

    def resolve_peer(self, info, **kwargs):
        ip = kwargs.get('ip')

        if ip is not None:
            return ark_blockchain.Peers.objects.get(ip=ip)
        return None

    def resolve_multisignature(self, info, **kwargs):
        transactionid = kwargs.get('transactionid')

        if transactionid is not None:
            return ark_blockchain.Multisignatures.objects.get(transactionid=transactionid)

        return None

    def resolve_migration(self, info, **kwargs):
        id = kwargs.get('id')
        name = kwargs.get('name')

        if id is not None:
            return ark_blockchain.Migrations.objects.get(id=id)

        if name is not None:
            return ark_blockchain.Migrations.objects.get(name=name)

        return None

    def resolve_memdelegate(self, info, **kwargs):
        publickey = kwargs.get('publickey')

        if publickey is not None:
            return ark_blockchain.MemDelegates.objects.get(publickey=publickey)

        return None

    def resolve_mem2multisignature(self, info, **kwargs):
        accountid = kwargs.get('accountid')
        dependentid = kwargs.get('dependentid')

        if accountid is not None:
            return ark_blockchain.MemAccounts2Multisignatures.objects.get(accountid=accountid)

        if dependentid is not None:
            return ark_blockchain.MemAccounts2Multisignatures.objects.get(dependentid=dependentid)

        return None

    def resolve_forksstat(self, info, **kwargs):
        delegatepublickey = kwargs.get('delegatepublickey')
        blocktimestamp = kwargs.get('blocktimestamp')
        blockid = kwargs.get('blockid')
        blockheight = kwargs.get('blockheight')
        previousblock = kwargs.get('previousblock')

        if delegatepublickey is not None:
            return ark_blockchain.ForksStat.objects.get(delegatepublickey=delegatepublickey)

        if blocktimestamp is not None:
            return ark_blockchain.ForksStat.objects.get(blocktimestamp=blocktimestamp)

        if blockid is not None:
            return ark_blockchain.ForksStat.objects.get(blockid=blockid)

        if blockheight is not None:
            return ark_blockchain.ForksStat.objects.get(blockheight=blockheight)

        if previousblock is not None:
            return ark_blockchain.ForksStat.objects.get(previousblock=previousblock)

        return None

    def resolve_delegate(self, info, **kwargs):
        username = kwargs.get('username')

        if username is not None:
            return ark_blockchain.Delegates.objects.get(username=username)

        return None

    def resolve_block(self, info, **kwargs):
        id = kwargs.get('id')
        timestamp = kwargs.get('timestamp')
        height = kwargs.get('height')

        if id is not None:
            return ark_blockchain.Blocks.objects.get(id=id)

        if height is not None:
            return ark_blockchain.Blocks.objects.get(height=height)

        if timestamp is not None:
            return ark_blockchain.Blocks.objects.get(timestamp=timestamp)

        return None

    def resolve_dependent(self, info, **kwargs):
        accountid = kwargs.get('accountid')

        if accountid is not None:
            return ark_blockchain.MemAccounts2Delegates.objects.get(accountid=accountid)

        return None

    def resolve_account(self, info, **kwargs):
        address = kwargs.get('address')
        username = kwargs.get('username')

        if address is not None:
            return ark_blockchain.MemAccounts.objects.prefetch_related('memaccounts2delegates_set').get(address=address)

        if username is not None:
            return ark_blockchain.MemAccounts.objects.get(username=username)

        return None
