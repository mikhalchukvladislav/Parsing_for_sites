from django.views import generic, View
from .models import News
from .filters import ParserFilter
from .forms import CreateForm
from django.shortcuts import render
from django.core.paginator import Paginator


class HomePageView(generic.ListView):
    template_name = 'home.html'
    context_object_name = 'articles'
    paginate_by = 7
    queryset = News.objects.order_by('create_date')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = ParserFilter(self.request.GET, queryset=self.get_queryset())
        context['url_list'] = set(News.objects.values_list('url', flat=True))
        context['country_list'] = set(News.objects.values_list('country', flat=True))
        return context


class UrlCreateView(generic.CreateView):
    template_name = 'url_create.html'
    form_class = CreateForm


class CertainPage(View):

    def get(self, request, link_id):
        url = News.objects.filter(link_id=link_id).values('url')[1]['url']
        url_list = set(News.objects.filter(link_id=link_id).values_list('url', flat=True))
        country_list = set(News.objects.filter(link_id=link_id).values_list('country', flat=True))
        filter = ParserFilter(self.request.GET, queryset=News.objects.filter(link_id=link_id).order_by('create_date'))
        p = Paginator(filter.qs, 5)  # создаём объект класса пагинатор, передаём ему список наших товаров и их количество для одной страницы
        qs = p.get_page(request.GET.get('page', 1))
        page_obj = p.get_page(request.GET.get('page'))
        context = {
            'url_list': url_list,
            'country_list': country_list,
            'url': url,
            'page_obj': page_obj,
            'filter' : filter,
            'qs': qs,
        }
        return render(request, 'page.html', context)