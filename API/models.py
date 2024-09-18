from django.db import models

# Create your models here.

class Center(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    codename = models.CharField(max_length=2)

class User(models.Model):
    code = models.CharField(max_length=4, primary_key=True)
    pin = models.CharField(max_length=4)
    pin_reset = models.BooleanField(default=1)
    role = models.CharField(max_length=30)
    group = models.CharField(max_length=3)
    center_id = models.PositiveSmallIntegerField()
    since = models.TimeField()
    active = models.BooleanField(default=1)

class Bet(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    type = models.CharField(max_length=30)
    numbers = models.CharField(max_length=7)
    amount = models.FloatField()
    user_code = models.CharField(max_length=4)
    center_id = models.PositiveIntegerField()

class Winner(models.Model):
    id  = models.PositiveIntegerField(primary_key=True)
    date = models.DateField()
    user_code = models.CharField(max_length=4)
    numbers = models.CharField(max_length=7)
    bet_amount = models.FloatField()
    gained_amount = models.FloatField()
    center_id = models.PositiveIntegerField()

class Limit(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    type = models.CharField(max_length=30)
    amount = models.FloatField()
    center_id = models.PositiveIntegerField()

class Clasified(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    type = models.CharField(max_length=30)
    charged_amount = models.FloatField()
    delayed_days = models.PositiveIntegerField()
    center_id = models.PositiveIntegerField()

class Schedule(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    start_a = models.CharField(max_length=30)
    start_b = models.CharField(max_length=30)
    end_a = models.CharField(max_length=30)
    end_b = models.CharField(max_length=30)
    center_id = models.PositiveIntegerField()

class Throw(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    hundred = models.CharField(max_length=3)
    fix_number = models.CharField(max_length=2)
    dinamic_a = models.CharField(max_length=2)
    dinamic_b = models.CharField(max_length=2)
    session = models.CharField(max_length=30)
    created_at = models.DateTimeField()
    center_id = models.PositiveIntegerField()

class Plan(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    normal_fix_number = models.CharField(max_length=2)
    normal_dinamic_number = models.CharField(max_length=2)
    normal_parle = models.CharField(max_length=7)
    normal_hundred = models.CharField(max_length=3)
    limited_fix_number = models.CharField(max_length=2)
    limited_dinamic_number = models.CharField(max_length=2)
    limited_parle = models.CharField(max_length=7)
    limited_hundred = models.CharField(max_length=3)
    ball_list = models.FloatField()
    parle_list = models.FloatField()
    center_id = models.PositiveIntegerField()


