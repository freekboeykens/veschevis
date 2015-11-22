from django.db import models

# =============================================================================
# COOPERANT
# =============================================================================
class Cooperant(models.Model):
    class Meta:
        verbose_name = "Coöperant"
        verbose_name_plural = "Coöperanten"

    first_name = models.CharField('Voornaam', max_length=100)
    last_name = models.CharField('Achternaam', max_length=100)
    phone = models.CharField('Telefoon', max_length=100)
    email = models.EmailField('E-mail', max_length=100)
    code = models.CharField('Code', max_length=100)
    street_and_number = models.CharField('Straat + nummer', max_length=100)
    zip_code = models.PositiveIntegerField('Postcode')
    city = models.CharField('Stad', max_length=100)

    def __str__(self):
        return self.first_name + " " + self.last_name

# =============================================================================
# COLLECTION POINT
# =============================================================================
class CollectionPoint(models.Model):
    class Meta:
        verbose_name = "Afhaalpunt"
        verbose_name_plural = "Afhaalpunten"

    name = models.CharField('Naam', max_length=100)

    def __str__(self):
        return self.name

# =============================================================================
# SUBSCRIPTION TYPE
# =============================================================================
class SubscriptionType(models.Model):
    class Meta:
        verbose_name = "Pakket"
        verbose_name_plural = "Pakketten"

    name = models.CharField('Naam', max_length=100)
    weight = models.DecimalField('Gewicht', max_digits=2, decimal_places=1)
    cost = models.DecimalField('Prijs', max_digits=4, decimal_places=2)

    def __str__(self):
        return self.name

# =============================================================================
# WEEKLY SUBSCRIPTION
# =============================================================================
class WeeklySubscription(models.Model):
    class Meta:
        verbose_name = "Inschrijving"
        verbose_name_plural = "Inschrijvingen"

    cooperant = models.ForeignKey(
        Cooperant,
        verbose_name = "Coöperant",
        related_name = "subscription_set"
    )
    collection_point = models.ForeignKey(
        CollectionPoint,
        verbose_name = "Afhaalpunt",
        related_name = "subscription_set"
    )
    subscription_type = models.ForeignKey(
        SubscriptionType,
        verbose_name = "Pakket",
        related_name = "subscription_set"
    )
    date = models.DateField('Afhaaldatum')
    amount = models.PositiveIntegerField('Aantal', default=1)
    is_paid = models.BooleanField('Betaald', default=False)
