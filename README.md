## Survey Website

***
This is a simple site meant to make simple surveys

### Screnshots
***

+ #### Register
![Register](https://i.imgur.com/UMNagzp.png)

+ #### Survey
![Survey](https://i.imgur.com/EPjqoBk.png)

+ #### Survey Example
![Survey answer](https://i.imgur.com/SVR1vNw.png)

+ #### Profile
![Profile]()

### How to build.
***
Requeriments:
    Django >= 3.1.5

### Instructions to run
***
```
git clone https://github.com/Thestias/Survey-Website.git

cd Survey-Website

python manage.py makemigrations --setings=SurveyWebsite.settings.dev

python manage.py migrate --settings=SurveyWebsite.settings.dev

python manage.py runserver --settings=SurveyWebsite.settings.dev
```