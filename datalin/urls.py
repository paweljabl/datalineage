from django.urls import path

from . import views
from django_filters.views import FilterView
from .filters import RelationFilter, NodeFilter

urlpatterns = [
    path('', views.index, name='index'),
    path('technology/', views.TechnologyView.as_view(), name='technology'),
    path('entity/', views.EntityView.as_view(), name='entity'),
    path('application/', views.ApplicationView.as_view(), name='application'),
    path('application_upload/', views.application_upload, name='application_upload'),
    path('node/', views.NodeView.as_view(), name='node'),
    path('node_upload/', views.node_upload, name='node_upload'),
    path('relation/', views.RelationView.as_view(), name='relation'),
    path('relation_upload/', views.relation_upload, name='relation_upload'),
    path('add3/', views.NodeCreateView.as_view(), name='node_add2'),
    path('add_technology/', views.TechnologyCreateView.as_view(), name='add_technology'),
    path('add_entity/', views.EntityCreateView.as_view(), name='add_entity'),
    path('add/', views.add_node, name='node_add'),
#    path('node_new/', views.node_new, name='node_new'),

    path('ajax/load-entities/', views.load_entities, name='ajax_load_entities'),
    path('search/', views.search, name='search'),
    # path('search2/', views.search2, name='search2'),
    path('search3/', FilterView.as_view(filterset_class=NodeFilter, template_name='search/node_list.html'), name='search3'),
]