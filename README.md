# Django y Vue citas SPA

Aplicación de una página para sacar citas.

## Requisitos

@vue/cli 4.5.12 | Python 3.9.4

## Setup Django Development

- Clone repository
- Crea el virtual environment
  - Instrucciones para crear el env [Aquí](https://docs.djangoproject.com/en/3.2/howto/windows/#setting-up-a-virtual-environment/).

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