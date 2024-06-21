# 2023_wa_sa_jankovic_gaflix

## První inicializace projektu

### Vyklonovat repozitar a vlezt do nej
```shell
git clone https://github.com/gyarab/2023_wa_sa_jankovic_gaflix
cd 2023_wa_sa_jankovic_gaflix/
```
### Vytvorit venv a aktivovat
```shell
py -3 -m venv venv
source ./venv/Scripts/activate
```
### Nainstalovat zavislosti
```shell
pip install -r requirements.txt
```
## Vytvoreni a ulozeni admin usera
```shell
./manage.py migrate
./manage.py createsuperuser
./manage.py dumpdata auth.User --indent 2 > fixtures/users.json
```

## Spuštění projektu

```shell
git pull
source ./venv/Scripts/activate
./manage.py migrate
./manage.py runserver
```

## Po změně `models.py`

```shell
./manage.py makemigrations
./manage.py migrate
```

## Reset databáze

### Smazat aktualni DB
```shell
rm db.sqlite3
```
### Obnovit strukturu
```shell
./manage.py migrate
```

### Nahrat data
```shell
./manage.py loaddata fixtures/*.json
```