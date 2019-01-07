from django.views import generic
from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from django.urls import reverse, reverse_lazy
import xlrd, os
# from django.contrib import messages

from .models import Technology, Entity, Node, Application, Relation, Relation_Type
from .forms import NodeForm, ApplicationForm, TechnologyForm, EntityForm
# import ipdb

def index(request):
    """
    View function for home page of site.
    """

    # Render the HTML template index.html with the data in the context variable.
    return render(
        request,
        'datalin/index.html',
    )

def add_node(request):

    # template_name = 'datalin/node_form.html'

    if request.method == 'POST':
        # ipdb.set_trace()
        print('lalala')
        node_form = NodeForm(request.POST)
        print(request.POST)
        application_form = ApplicationForm(request.POST)
        is_application = application_form.data['is_application']
        print(application_form.data)
        if node_form.is_valid(): # and application_form.is_valid():
            node = node_form.save()
            print('Sialalal')
            node_id = node.id
            if is_application == 'Y':
                # if application_form.data['is_bi'] == 'on':
                #     application_form.data['is_bi'] = 'Y'
                # else:
                #     application_form.data['is_bi'] = 'N'
                print('node_id:', node_id)
                print(application_form.data['is_bi'])
                # node_form.save()
                if application_form.is_valid():
                    application = application_form.save(commit=False)
                    application.node_id = node_id
                    application.save()
                    return redirect('node')
        else:
            print('bleee')
            # print(messages.error(request, "Error"))
            # messages.error(request, "Error")
    else:
        node_form = NodeForm()
        application_form = ApplicationForm()

    context = {
        'node_form': node_form,
        'application_form': application_form,
    }
    return render(request, 'datalin/node_form.html', context)

class NodeCreateView(generic.CreateView):
    model = Node
    form_class = NodeForm
    template_name = 'datalin/node_form2.html'
    success_url = reverse_lazy('node')

def load_entities(request):
    technology_id = request.GET.get('technology')
    entities = Entity.objects.filter(technology_id=technology_id).order_by('name')
    return render(request, 'datalin/entity_dropdown_list_options.html', {'entities': entities})

class TechnologyCreateView(generic.CreateView):
    model = Technology
    form_class = TechnologyForm
    success_url = reverse_lazy('technology')

class EntityCreateView(generic.CreateView):
    model = Entity
    form_class = EntityForm
    success_url = reverse_lazy('entity')

class TechnologyView(generic.ListView):
    template_name = 'datalin/technology_list.html'

    def get_queryset(self):
        return Technology.objects.all().order_by('provider', 'name')


class EntityView(generic.ListView):
    template_name = 'datalin/entity_list.html'

    def get_queryset(self):
        return Entity.objects.all()

def load_application_from_xlsx():

    xlsx_path = os.path.join(os.path.dirname(os.path.dirname(__file__)),'datalin/data/applications.xlsx')
    with xlrd.open_workbook(xlsx_path) as wb:
        sh = wb.sheet_by_name('Sheet1')
        for row in range(1, sh.nrows):
            short_name = sh.cell(row, 0)
            print(short_name.value)
            node, node_created = Node.objects.get_or_create(
                name=sh.cell(row, 0).value,
                display_name=sh.cell(row, 1).value,
                description=sh.cell(row, 2).value,
                entity=Entity.objects.get(name='Application'),
            )

            application, application_created = Application.objects.get_or_create(
                node_id=node.id,
                owner_name=sh.cell(row, 4).value,
                contact_email=sh.cell(row, 5).value,
                is_bi=sh.cell(row, 6).value,
            )

class ApplicationView(generic.ListView):
    template_name = 'datalin/applications_list.html'

    def get_queryset(self):
        return Application.objects.all()



def load_node_from_xlsx():

    xlsx_path = os.path.join(os.path.dirname(os.path.dirname(__file__)),'datalin/data/nodes.xlsx')
    with xlrd.open_workbook(xlsx_path) as wb:
        sh = wb.sheet_by_name('Sheet1')
        for row in range(1, sh.nrows):
            short_name = sh.cell(row, 0)
            print(short_name.value)
            technology_xs = sh.cell(row, 4).value
            if len(technology_xs) > 0:
                print(technology_xs)
                technology = Technology.objects.get(name=technology_xs)
                print(technology)
            else:
                technology = None
                # entity = Entity.objects.get(name=sh.cell(row, 3).value)
            entity = Entity.objects.get(name=sh.cell(row, 3).value, technology=technology)
            node, node_created = Node.objects.get_or_create(
                name=sh.cell(row, 0).value,
                display_name=sh.cell(row, 1).value,
                description=sh.cell(row, 2).value,
                entity_id=entity.id,
            )

class NodeView(generic.ListView):
    template_name = 'datalin/node_list.html'
    # uncomment if y want to process application
    # load_application_from_xlsx()
    # uncomment if y want to process node
    # load_node_from_xlsx()

    def get_queryset(self):
        return Node.objects.all()


def load_relation_from_xlsx():

    xlsx_path = os.path.join(os.path.dirname(os.path.dirname(__file__)),'datalin/data/relations.xlsx')
    with xlrd.open_workbook(xlsx_path) as wb:
        sh = wb.sheet_by_name('Sheet1')
        for row in range(1, sh.nrows):
            node_a = Node.objects.get(name=sh.cell(row, 0).value)
            print(node_a)
            relation_type = Relation_Type.objects.get(name=sh.cell(row, 1).value)
            print(relation_type)
            node_b = Node.objects.get(name=sh.cell(row, 3).value)
            print(node_b)
            relation, relation_created = Relation.objects.get_or_create(
                node_a=node_a,
                relation_type=relation_type,
                relation_level=sh.cell(row, 2).value,
                node_b=node_b,
            )

class RelationView(generic.ListView):
    template_name = 'datalin/relation_list.html'

    # uncomment if y want to process relation
    # load_relation_from_xlsx()

    def get_queryset(self):
        return Relation.objects.all().order_by('-id')[:200]






