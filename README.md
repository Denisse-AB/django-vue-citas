# Django y Vue citas SPA

Aplicación de una página para sacar citas.

## Requisitos

@vue/cli 4.5.12 | Python 3.9.4

## Setup Django Development

- Clone repository
- Create virtual environment
  - For instructions creating environment [Click Here](https://docs.djangoproject.com/en/3.2/howto/windows/#setting-up-a-virtual-environment/).

```python
cd citas_main
pip install -r requirements.txt
```
- Setup SECRET_KEY y environ variables en settings file
- Corre los migrations
- Crea superuser

## Setup Vue Development

```javascript
cd frontend
npm install
npm run serve
```