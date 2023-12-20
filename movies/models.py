from django.db import models


class WhichAge(models.TextChoices):
    GENERAL = "G"
    PARENTAL_GUIDANCE = "PG"
    PARENTS_CAUTIONED = "PG-13"
    RESTRICTED = "R"
    ADULTS_ONLY = "NC-17"


class Movie(models.Model):
    title = models.CharField(max_length=127)
    duration = models.CharField(max_length=10, blank=True, default="")
    rating = models.CharField(
        max_length=20,
        choices=WhichAge.choices,
        default=WhichAge.GENERAL
        )
    synopsis = models.TextField(blank=True, default="")
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="movies",
        null=True,
    )
    orders = models.ManyToManyField(
        "users.User",
        related_name="movies_orders",
        through="movies_orders.MovieOrder",
    )
