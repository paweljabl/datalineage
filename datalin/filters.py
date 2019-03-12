from .models import Node, Relation
from django.db.models import Q
from django import forms
import django_filters

class RelationFilter(django_filters.FilterSet):
    class Meta:
        model = Relation
        fields = ['node_a', 'relation_type', 'relation_level', 'node_b', ]

class NodeFilter(django_filters.FilterSet):
    display_name = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Node
        fields = [
                    'id',
                    'name',
                    'display_name',
                    'description',
                    'entity',
                ]

    def __init__(self, *args, **kwargs):
        super(NodeFilter, self).__init__(*args, **kwargs)
        # at sturtup user doen't push Submit button, and QueryDict (in data) is empty
        if self.data == {}:
            self.queryset = self.queryset.none()

# class NodeFilter(django_filters.FilterSet):
#     data_node = django_filters.CharFilter(method='search_by_data_node')
#
#     def search_by_data_node(self, queryset, name, value):
#         return queryset.filter(
#             Q(name__icontains=value) | Q(display_name__icontains=value) )
#
#     class Meta:
#         model = Node
#
#         fields = [
#             'name',
#             'display_name',
#             'description',
#             'entity_id',
#         ]