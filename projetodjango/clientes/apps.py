# Importa a classe AppConfig
from django.apps import AppConfig

# Define uma nova classe
class ClientesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    # Define o campo autoincrementável
    name = 'clientes'
