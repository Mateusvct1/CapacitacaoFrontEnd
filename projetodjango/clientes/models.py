from django.db import models

# Define o modelo Person
class Person(models.Model):
    # Define os campos do modelo
    first_name = models.CharField(max_length=30)  # Primeiro nome
    email = models.TextField()                     # email
    bio = models.TextField()                 # mensagem


    # Método para retornar uma representação em string do objeto
    def __str__(self):
        return f"{self.first_name} {self.email} {self.bio}"  # Retorna os dados da pessoa
