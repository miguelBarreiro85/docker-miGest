from django.db import models
from django.contrib.auth.models import User
from .models import Funcionario
from django.test import TestCase

class FuncionarioTestCase(TestCase):
    def setup(self):
        func = User.objects.create_user(username='duarte', password='mlpbarreiro2018')
        Funcionario.objects.create(user=func.id)

        func = User.objects.create_user(username='electrorainha', password='mlpbarreiro2018')
        Funcionario.objects.create(user=func.id)

        func = User.objects.create_user(username='jorge', password='mlpbarreiro2018')
        Funcionario.objects.create(user=func.id)

        func = User.objects.create_user(username='serafim', password='mlpbarreiro2018')
        Funcionario.objects.create(user=func.id)

        func = User.objects.create_user(username='teleconde', password='mlpbarreiro2018')
        Funcionario.objects.create(user=func.id)

        func = User.objects.create_user(username='astecaldas', password='mlpbarreiro2018')
        Funcionario.objects.create(user=func.id)