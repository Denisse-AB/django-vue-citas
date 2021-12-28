# Django y Vue citas SPA

Aplicación de una página para sacar citas.

## Requisitos

@vue/cli 4.5.12 | Python 3.9.4 | Nodejs v14.6.0

## Setup Django Development

- Clone repository
- Crea el virtual environment
  - Instrucciones para crear el env [Aquí](https://docs.djangoproject.com/en/3.2/howto/windows/#setting-up-a-virtual-environment/).
  - Entorno Virtual Español [Aquí](https://docs.python.org/es/3/tutorial/venv.html).
- Activa el virtual environment

```python
cd citas_main
pip install -r requirements.txt
```
- Cambia el SECRET_KEY y las variables en settings file
- Corre los migrations
- Crea superuser

## Setup Vue Development

```javascript
cd frontend
npm install
npm run serve
```

## Donation
If you like this project, buy me a cup of :coffee: :wink:

[![paypal](https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif)](https://www.paypal.com/donate?business=263QJ8D5YHR8E&no_recurring=0&item_name=I+believe+in+open+source%2C+but+a+little+donation+will+be+appreciated.+Thanks%21&currency_code=USD)
