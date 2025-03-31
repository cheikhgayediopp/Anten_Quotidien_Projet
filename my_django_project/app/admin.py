from django.contrib import admin # type: ignore
from .models import Article

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('titre', 'auteur', 'date_publication')  # Champs affichés dans la liste
    list_filter = ('date_publication', 'auteur')  # Filtres dans la barre latérale
    search_fields = ('titre', 'contenu')  # Champs pour la recherche