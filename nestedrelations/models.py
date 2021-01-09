from django.db import models

# Create your models here.
class Parent(models.Model):
    name = models.CharField(max_length=127)

    def __str__(self):
        return f'{self.__class__.__name__}: {self.name}'


class ChildA(models.Model):
    name = models.CharField(max_length=127)
    parent = models.ForeignKey(Parent, related_name='childAs', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.__class__.__name__}: {self.name}'


class ChildB(models.Model):
    name = models.CharField(max_length=127)
    parent = models.ForeignKey(Parent, related_name='childBs', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.__class__.__name__}: {self.name}'


class ChildA1(models.Model):
    name = models.CharField(max_length=127)
    parent = models.ForeignKey(ChildA, related_name='childA1s', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.__class__.__name__}: {self.name}'


class ChildA2(models.Model):
    name = models.CharField(max_length=127)
    parent = models.ForeignKey(ChildA, related_name='childA2s', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.__class__.__name__}: {self.name}'
