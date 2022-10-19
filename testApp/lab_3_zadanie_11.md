### 1
from polls.models import Osoba <br />
Osoba.objects.all() <br />
<QuerySet [<Osoba: Andrzej Analfabeta>, <Osoba: Andrzej Miły>, <Osoba: Andrzej Miły>, <Osoba: damian Miły>, <Osoba: Andrzej Miły>, <Osoba: Andrzej Miły>, <Osoba: Andrzej Stefan>, <Osoba: Bartek Stefan>, <Osoba: Andrzejs Ste
fan>]> <br />
### 2
Osoba.objects.get(id=3) <br />
<Osoba: Andrzej Miły> <br />
### 3
Osoba.objects.filter(imie__startswith='B') <br />
<QuerySet [<Osoba: Bartek Stefan>] <br />
### 4
nw
### 5
from polls.models import Druzyna <br />
Druzyna.objects.all().order_by('-nazwa') <br />
<QuerySet [<Druzyna: POLSKA GUROM (PL)>, <Druzyna: DEMONY (RU)>, <Druzyna: anioły (DE)>, <Druzyna: ANGOLE (EN)>]> <br />
### 6
from django.utils import timezone <br />
q = Osoba(imie='Michał', nazwisko='dobry', miesiac_urodzenia=5, data_dodania=timezone.now()) <br />
q.save() <br />