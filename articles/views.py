from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView

from articles.models import Article


class ArticleListView(ListView):
    model = Article
    template_name = 'article_list.html'
    extra_context = {
        'title': 'Home Page',
    }


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article_detail.html'
    extra_context = {
        'title': 'Article Detail',
    }


class ArticleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Article
    fields = ('title', 'body',)
    template_name = 'article_edit.html'
    extra_context = {
        'title': 'Update Article',
    }

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class ArticleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Article
    template_name = 'article_delete.html'
    success_url = reverse_lazy('home')
    extra_context = {
        'title': 'Delete Article',
    }

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class ArticleCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Article
    template_name = 'article_new.html'
    fields = ('title', 'body',)
    extra_context = {
        'title': 'New Article',
    }

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    # user superuser ekanini tekshirish
    def test_func(self):
        return self.request.user.is_superuser
