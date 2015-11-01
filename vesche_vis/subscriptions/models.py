from django.db import models

class Cooperant(models.Model):
    class Meta:
        verbose_name = "Coöperant"
        verbose_name_plural = "Coöperanten"

    first_name = models.CharField('Voornaam', max_length=100)
    last_name = models.CharField('Achternaam', max_length=100)
    phone = models.CharField('Telefoon', max_length=100)
    email = models.EmailField('E-mail', max_length=100)
    code = models.CharField('Code', max_length=100)
    street = models.CharField('Straat', max_length=100)
    number = models.PositiveIntegerField('Nummer')
    mailbox = models.CharField('Bus', max_length=5)
    zip_code = models.PositiveIntegerField('Postcode')
    city = models.CharField('Stad', max_length=100)

    def __str__(self):
        return self.first_name + " " + self.last_name
