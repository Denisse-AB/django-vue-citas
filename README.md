# Django Appointments SPA

Single Page Application (SPA) to make appointments using Vue 3 composition API, Django, and Django Rest Framework.

## Requirements

Vue 3 | Python ^3.9.4 | Postgressql

## Description

This application consists of a form in which your clients or users are going to make appointments for your business or organization. The user will receive an email when the appointment is accepted.

The owner of this application will manage these appointments through the database. It is configured to receive four appointments every hour (You can change this in the views.py file), it has English and Spanish translation and the database it uses is Postgressql, you can configure it however you want 👍

## Setup Django Development

- Clone repository
- Create the virtual environment
  - [Instructions to create the .env](https://docs.djangoproject.com/en/3.2/howto/windows/#setting-up-a-virtual-environment/).
  - [Virtual Environment](https://docs.python.org/3/tutorial/venv.html).
- Activate the virtual environment

```python
cd citas_main
pip install -r requirements.txt
```
- Change the SECRET_KEY and variables in settings file
- Run the migrations
- Create superuser

## Setup Vue Development

```javascript
cd frontend
npm install
npm run serve
```

## Donación
If you liked this project, buy me a cup of :coffee: :wink:

[![paypal](https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif)](https://www.paypal.com/donate?business=263QJ8D5YHR8E&no_recurring=0&item_name=I+believe+in+open+source%2C+but+a+little+donation+will+be+appreciated.+Thanks%21&currency_code=USD)