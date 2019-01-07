from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('technology/', views.TechnologyView.as_view(), name='technology'),
    path('entity/', views.EntityView.as_view(), name='entity'),
    path('node/', views.NodeView.as_view(), name='node'),
    path('relation/', views.RelationView.as_view(), name='relation'),
    path('add3/', views.NodeCreateView.as_view(), name='node_add2'),
    path('add_technology/', views.TechnologyCreateView.as_view(), name='add_technology'),
    path('add_entity/', views.EntityCreateView.as_view(), name='add_entity'),
    path('add/', views.add_node, name='node_add'),
#    path('node_new/', views.node_new, name='node_new'),
    path('application/', views.ApplicationView.as_view(), name='application'),
    path('ajax/load-entities/', views.load_entities, name='ajax_load_entities'),
]