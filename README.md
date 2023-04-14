## Instalacija

Potreban je Python 3.8 ili noviji za Django 4.2. Više na: [How to install Django](https://docs.djangoproject.com/en/4.2/topics/install/)
```
python -m pip install Django==4.2
```

## Pokretanje

```
python manage.py migrate
python manage.py runserver
```
Nakon dodavanja modela potrebno je napraviti migraciju i spremiti ju u bazu podataka:
```
python manage.py makemigrations
python manage.py migrate
```
Nakon izmjene modela najlakše je izbrisati bazu i migracije te započeti iznova.


## Korisnici

Predavači su `Useri`.

Administratori su `Superuseri` (`Useri` sa `is_staff=True` i `is_superuser=True`)

Provjera administratora u kodu se provjerava sa `user.is_staff`.

Više na: [Using the Django authentication system](https://docs.djangoproject.com/en/4.2/topics/auth/default/) i [django.contrib.auth](https://docs.djangoproject.com/en/4.2/ref/contrib/auth/#django-contrib-auth)

### Primjeri korisnika:

| USERNAME           | EMAIL ADDRESS      | FIRST NAME   | LAST NAME        | STAFF STATUS | PASSWORD |
| ------------------ | ------------------ | ------------ | ---------------- | ------------ | -------- |
| admin1@admin.com   | admin1@admin.com   | AdminIme1    | AdminPrezime1    | Yes          | 1        |
| predavac1@user.com | predavac1@user.com | PredavacIme1 | PredavacPrezime1 | No           | 1        |

### Dodavanje korisnika iz primjera:

```
python manage.py shell
```

```
from django.contrib.auth.models import User
User.objects.create_superuser(username="admin1@admin.com", email="admin1@admin.com", first_name="AdminIme1", last_name="AdminPrezime1", password="1")
User.objects.create_user(username="predavac1@user.com", email="predavac1@user.com", first_name="PredavacIme1", last_name="PredavacPrezime1", password="1")
```

### Dodavanje superusera (drugi način):

```
python manage.py createsuperuser
```

## TODO

Prije završetka/objave treba pregledati "TODO!" komentare.
