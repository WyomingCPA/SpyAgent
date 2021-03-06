import django_tables2 as tables
from SMSApp.models import Sms

class SmsTable(tables.Table):
    from_phone = tables.Column(attrs={'class':'',},)
    to_phone = tables.Column()
    text = tables.Column()
    date = tables.Column()
    

    class Meta:
        attrs = {'class': 'table table-striped table-hover'}


class MoreIdSpyTable(tables.Table):
    to_phone = tables.Column()
    pin = tables.Column()

    class Meta:
        attrs = {'class': 'table table-striped table-hover'}