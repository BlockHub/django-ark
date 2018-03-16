import django_filters
import ark.models as ark_blockchain


class TransactionFilter(django_filters.FilterSet):
    # Do case-insensitive lookups on 'name'
    class Meta:
        model = ark_blockchain.Transactions
        fields = {
            'id': ['exact'],
            'rowid': ['exact'],
            'blockid': ['exact'],
            'type':  ['exact', 'lt', 'gt', 'gte', 'lte'],
            'timestamp':  ['exact', 'lt', 'gt', 'gte', 'lte'],
            'senderid': ['exact'],
            'recipientid': ['exact'],
            'amount': ['exact', 'lt', 'gt', 'gte', 'lte'],
            'fee': ['exact', 'lt', 'gt', 'gte', 'lte'],
            'vendorfield': ['exact'],
            'rawasset': ['exact'],
                  }

