from polls.models import Osoba <br />
from polls.serializers import OsobaSerializer <br />
from rest_framework.renderers import JSONRenderer <br />
from rest_framework.parsers import JSONParser <br />

osoba = Osoba(imie='Damian', nazwisko='Banach', miesiac_urodzenia=7) <br /> <br />
osoba.save() <br /><br />
serializer = OsobaSerializer(osoba) <br /><br />
serializer.data <br /><br />
output: {'id': 11, 'imie': 'Damian', 'nazwisko': 'Banach', 'miesiac_urodzenia': '7', 'kraj': None} <br />
content = JSONRenderer().render(serializer.data) <br /><br />
content <br /><br />
output: b'{"id":11,"imie":"Damian","nazwisko":"Banach","miesiac_urodzenia":"7","kraj":null}' <br />
import io <br /><br />
stream = io.BytesIO(content) <br /><br />
data = JSONParser().parse(stream) <br /><br />
deserializer = OsobaSerializer(data=data) <br /><br />
deserializer.is_valid() <br /><br />
output: False <br /><br />
deserializer.errors <br /><br />
OUTPUT: <br /> {'kraj': [ErrorDetail(string='This field may not be null.', code='null')]} <br />
deserializer.fields <br />
{'id': IntegerField(read_only=True), 'imie': CharField(required=True), 'nazwisko': CharField(required=True), 'miesiac_urodzenia': ChoiceField(choices=(('1', 'styczeń'), ('2', 'luty'), ('3', 'marzec'), ('4', 'kwiecień'), ('5
', 'maj'), ('6', 'czerwiec'), ('7', 'lipiec'), ('8', 'sierpień'), ('9', 'wrzesień'), ('10', 'październik'), ('11', 'listopad'), ('12', 'grudzień')), default='1'), 'kraj': PrimaryKeyRelatedField(queryset=<QuerySet [<Druzyna:
 anioły (DE)>, <Druzyna: POLSKA GUROM (PL)>, <Druzyna: ANGOLE (EN)>, <Druzyna: DEMONY (RU)>]>)} <br />

PO DODANIU 'allow_null=True':<br /><br />
deserializer.is_valid()<br /><br />
OUTPUT: True <br /><br />
deserializer.validated_data <br /><br />
OUTPUT: OrderedDict([('imie', 'Damian'), ('nazwisko', 'Banaszek'), ('miesiac_urodzenia', '7'), ('kraj', None)])<br /><br />
deserializer.save()<br /><br />
OUTPUT: <Osoba: Damian Banaszek><br /><br />
deserializer.data<br /><br />
OUTPUT: {'id': 13, 'imie': 'Damian', 'nazwisko': 'Banaszek', 'miesiac_urodzenia': '7', 'kraj': None}<br /><br />
<br /><br />
DRUGI MODEL
<br /><br />
from polls.models import Druzyna<br /><br />
from polls.serializers import DruzynaSerializer<br /><br />
from rest_framework.renderers import JSONRenderer<br /><br />
from rest_framework.parsers import JSONParser<br /><br />
druzyna = Druzyna('PL', 'DRAVVA TEAM();')<br /><br />
druzyna.save()<br /><br />
serializer = DruzynaSerializer(druzyna)<br /><br />
serializer.data<br /><br />
OUTPUT: {'id': 2, 'kraj': 'PL', 'nazwa': 'DRAVVA TEAM();'}<br /><br />
content = JSONRenderer().render(serializer.data)<br /><br />
content<br /><br />
OUTPUT: b'{"id":2,"kraj":"PL","nazwa":"DRAVVA TEAM();"}'<br /><br />
import io<br /><br />
stream = io.BytesIO(content)<br /><br />
data = JSONParser().parse(stream)<br /><br />
deserializer = DruzynaSerializer(data=data) <br /><br />
deserializer.is_valid() <br /><br />
OUTPUT: True<br /><br />
deserializer.validated_data<br /><br />
OUTPUT: OrderedDict([('kraj', 'PL'), ('nazwa', 'DRAVVA TEAM();')])<br /><br />
deserializer.save()<br /><br />
OUTPUT: <Druzyna: DRAVVA TEAM(); (PL)><br /><br />
deserializer.data<br /><br />
OUTPUT: {'id': 5, 'kraj': 'PL', 'nazwa': 'DRAVVA TEAM();'}<br /><br />
