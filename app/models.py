from django.db import models



class Pessoa(models.Model):
    sexo_choices = (
                    ('M', 'Masculino'),
                    ('F', 'Ferminino'),
                    )

    nome = models.CharField(max_length=100)
    email = models.EmailField()
    profissao = models.CharField(max_length=100)
    salario = models.FloatField()
    sexo = models.CharField(max_length=1, choices=sexo_choices)

    def __str__(self) -> str:
        return self.nome