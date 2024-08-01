# App deployed on GCP, App Engine

### https://infoeduka.k1k1.dev

-- OR --

### https://infoeduka.oa.r.appspot.com

**IMPORTANT: Startup may take up to a 10s due to cold start.**

| EMAIL ADDRESS      | PASSWORD | STAFF STATUS |
| ------------------ | -------- | ------------ |
| admin1@admin.com   | 1        | Yes          |
| predavac1@user.com | 1        | No           |

Visit `/admin` to access Django admin interface.

### About deployment

Steps to deploy a Django app with an SQLite database to the App Engine standard environment:
1. add `app.yaml` to root
2. update `settings.py`: allowed hosts, trusted origins and database initialization
3. run `python manage.py collectstatic`
4. run `gcloud app deploy`

The key is to have `init-db.sqlite3` deployed to the App Engine `/tmp` directory, which is writable.
This allows for a prepopulated database that resets with each new instance.
Instances can scale down to zero when not in use.
The `init-db.sqlite3` file contains only the user data as shown above.

### Azure DevOps

https://dev.azure.com/PRA23-Tim5/_git/Infoeduka%20project

---

⬇ _Original README_ ⬇

## Instalacija

Potreban je Python 3.8 ili noviji za Django 4.2. Više na: [How to install Django](https://docs.djangoproject.com/en/4.2/topics/install/)

```
pip install -r requirements.txt
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
