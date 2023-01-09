from django.db import models
from django.core.validators import MaxValueValidator
from clients.models import Client


class Service(models.Model):
    name = models.CharField(max_length=50)
    full_price = models.PositiveIntegerField()

    def __str__(self) -> str:
        return f"Сервис: {self.name}"


class Plan(models.Model):
    PLAN_TYPES = (
        ('full', 'Full'),
        ('student', 'Student'),
        ('discount', 'Discount')
    )

    def __str__(self) -> str:
        return f"Тарифный план: {self.plan_type} скидка: {self.discount_percent}"

    plan_type = models.CharField(choices=PLAN_TYPES, max_length=10)
    discount_percent = models.PositiveIntegerField(default=0,
                                                   validators=[
                                                       MaxValueValidator(100)
                                                   ])


class Subscription(models.Model):
    client = models.ForeignKey(
        Client, related_name='subscriptions', on_delete=models.PROTECT)
    service = models.ForeignKey(
        Service, related_name='subscriptions', on_delete=models.PROTECT)
    plan = models.ForeignKey(
        Plan, related_name='subscriptions', on_delete=models.PROTECT)
