from django.db import models # type: ignore
from django.contrib.auth.models import User  # type: ignore # Si vous utilisez un utilisateur existant
from django.urls import reverse # type: ignore

class Article(models.Model):
    # ... champs existants ...

    def get_absolute_url(self):
        return reverse('article-detail', args=[str(self.id)])

class Article(models.Model):
    titre = models.CharField(max_length=255)
    contenu = models.TextField()
    date_publication = models.DateTimeField(auto_now_add=True)
    auteur = models.ForeignKey(User, on_delete=models.CASCADE)  # Utilisation d'une clé étrangère pour l'auteur
    image = models.ImageField(upload_to='articles/images/', blank=True, null=True)

    def __str__(self):
        return self.titre