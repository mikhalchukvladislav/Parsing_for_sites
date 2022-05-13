from django.forms import SelectDateWidget, SelectMultiple, Select, RadioSelect, CheckboxSelectMultiple
from django_filters import FilterSet, DateFilter, CharFilter, ModelChoiceFilter
from .models import News


class ParserFilter(FilterSet):


    update_date = DateFilter(field_name='update_date',
                               lookup_expr='gt',
                               label='Updated after',
                               widget=SelectDateWidget)

    create_date = DateFilter(field_name='create_date',
                             lookup_expr='gt',
                             label='Created after',
                             widget=SelectDateWidget)



    class Meta:
        model = News
        fields = (
            'domain',
            'create_date',
            'update_date',
            'url',
            'country',
            )