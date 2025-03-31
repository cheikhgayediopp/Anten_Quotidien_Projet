from django.urls import reverse_lazy # type: ignore
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView # type: ignore
from .models import Article

class ArticleListView(ListView):
    model = Article
    template_name = 'articles/article_list.html'
    context_object_name = 'articles'

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'articles/article_detail.html'
    context_object_name = 'article'

class ArticleCreateView(CreateView):
    model = Article
    template_name = 'articles/article_form.html'
    fields = ['titre', 'contenu', 'auteur', 'image']

class ArticleUpdateView(UpdateView):
    model = Article
    template_name = 'articles/article_form.html'
    fields = ['titre', 'contenu', 'auteur', 'image']

class ArticleDeleteView(DeleteView):
    model = Article
    template_name = 'articles/article_confirm_delete.html'
    success_url = reverse_lazy('article-list')