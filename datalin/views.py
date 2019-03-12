from django.views import generic
from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from django.urls import reverse, reverse_lazy
import xlrd, os
# from django.contrib import messages

from .models import Technology, Entity, Node, Application, Relation, Relation_Type
from .forms import NodeForm, ApplicationForm, TechnologyForm, EntityForm
from .filters import RelationFilter, NodeFilter
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
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


class ApplicationView(generic.ListView):
    template_name = 'datalin/applications_list.html'

    def get_queryset(self):
        return Application.objects.all()


def load_application_from_xlsx(xlsx_file):

    # xlsx_path = os.path.join(os.path.dirname(os.path.dirname(__file__)),'datalin/data/applications.xlsx')
    # with xlrd.open_workbook(xlsx_path) as wb:
      with xlrd.open_workbook(filename=None, file_contents=xlsx_file.read()) as wb:
        sh = wb.sheet_by_name('Sheet1')
        new_rec = 0
        for row in range(1, sh.nrows):
            short_name = sh.cell(row, 0)
            print(short_name.value)
            try:
                Node.objects.get(name=sh.cell(row, 0).value)
            except Node.DoesNotExist:
                node = Node.objects.create(
                    name=sh.cell(row, 0).value,
                    display_name=sh.cell(row, 1).value,
                    description=sh.cell(row, 2).value,
                    entity=Entity.objects.get(name='Application'),
                )
                Application.objects.create(
                    node_id=node.id,
                    owner_name=sh.cell(row, 4).value,
                    contact_email=sh.cell(row, 5).value,
                    is_bi=sh.cell(row, 6).value,
                )
                new_rec += 1
        rec_details = {"total_rec":(sh.nrows-1), "new_rec":new_rec}
        return rec_details

def application_upload(request):
    if request.method == 'POST' and request.FILES['xlsx_file']:
        xlsx_file = request.FILES['xlsx_file']
        rec_details = load_application_from_xlsx(xlsx_file)
        return render(request, 'datalin/application_upload.html', {
            'rec_details': rec_details
        })
    return render(request, 'datalin/application_upload.html')


def load_node_from_xlsx(xlsx_file):

    # xlsx_path = os.path.join(os.path.dirname(os.path.dirname(__file__)),'datalin/data/nodes.xlsx')
    # with xlrd.open_workbook(xlsx_path) as wb:
    with xlrd.open_workbook(filename=None, file_contents=xlsx_file.read()) as wb:
        sh = wb.sheet_by_name('Sheet1')
        new_rec = 0
        for row in range(1, sh.nrows):
            short_name = sh.cell(row, 0)
            # print(short_name.value)
            technology_xs = sh.cell(row, 4).value
            if len(technology_xs) > 0:
                # print(technology_xs)
                technology = Technology.objects.get(name=technology_xs)
                # print(technology)
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
            new_rec += 1

        rec_details = {"total_rec":(sh.nrows-1),"new_rec":new_rec}
        return rec_details

def node_upload(request):
    if request.method == 'POST' and request.FILES['xlsx_file']:
        xlsx_file = request.FILES['xlsx_file']
        rec_details = load_node_from_xlsx(xlsx_file)
        return render(request, 'datalin/node_upload.html', {
            'rec_details': rec_details
        })
    return render(request, 'datalin/node_upload.html')


class NodeView(generic.ListView):
    template_name = 'datalin/node_list.html'
    # uncomment if y want to process application
    # load_application_from_xlsx()
    # uncomment if y want to process node
    # load_node_from_xlsx()

    def get_queryset(self):
        return Node.objects.all()


# def nodes(request):
#
#     node_list = Node.objects.all()
#     node_filter = NodeFilter(request.GET, queryset=node_list)
#
#     if request.method == 'GET':
#         if 'btn_form_1' in request.GET:
#
#             pagination_form = PaginationForm(request.GET)
#
#             if pagination_form.is_valid():
#                 initial_pagination_size = pagination_form.cleaned_data.get('pagination_size')
#
#                 request.session['initial_pagination_size'] = initial_pagination_size
#
#
#
#         elif 'btn_form_2' in request.GET:
#
#             request.session['initial_data_customer'] = request.GET.get("data_customer")
#
#
#
#     paginator = Paginator(customer_filter.qs, initial_pagination_size)
#
#     try:
#         customers = paginator.page(page)
#     except PageNotAnInteger:
#         customers = paginator.page(1)
#     except EmptyPage:
#         customers = paginator.page(paginator.num_pages)
#
#     context = {
#         'pagination_form': pagination_form,
#         'customer_filter': customer_filter,
#         'customers': customers,
#     }
#
#     return render(request, 'administrator/customers.html', context)

def load_relation_from_xlsx(xlsx_file):

    # xlsx_path = os.path.join(os.path.dirname(os.path.dirname(__file__)),'datalin/data/relations.xlsx')
    # with xlrd.open_workbook(xlsx_path) as wb:
    with xlrd.open_workbook(filename=None, file_contents=xlsx_file.read()) as wb:
        sh = wb.sheet_by_name('Sheet1')
        new_rec = 0
        for row in range(1, sh.nrows):
            node_a = Node.objects.get(name=sh.cell(row, 0).value)
            # print(node_a)
            relation_type = Relation_Type.objects.get(name=sh.cell(row, 1).value)
            # print(relation_type)
            node_b = Node.objects.get(name=sh.cell(row, 3).value)
            # print(node_b)
            relation, relation_created = Relation.objects.get_or_create(
                node_a=node_a,
                relation_type=relation_type,
                relation_level=sh.cell(row, 2).value,
                node_b=node_b,
            )
            new_rec += 1

        rec_details = {"total_rec": (sh.nrows - 1), "new_rec": new_rec}
        return rec_details

def relation_upload(request):
    if request.method == 'POST' and request.FILES['xlsx_file']:
        xlsx_file = request.FILES['xlsx_file']
        rec_details = load_relation_from_xlsx(xlsx_file)
        return render(request, 'datalin/relation_upload.html', {
            'rec_details': rec_details
        })
    return render(request, 'datalin/relation_upload.html')


class RelationView(generic.ListView):
    template_name = 'datalin/relation_pagination.html'
    paginate_by = 15
    # uncomment if y want to process relation
    # load_relation_from_xlsx()

    def get_queryset(self):
        return Relation.objects.all().order_by('node_a__display_name', 'node_b__display_name')[:200]

    def get_context_data(self, **kwargs):
        context = super(RelationView, self).get_context_data(**kwargs)
        if not context.get('is_paginated', False):
            return context

        paginator = context.get('paginator')
        num_pages = paginator.num_pages
        current_page = context.get('page_obj')
        page_no = current_page.number
        current_range = (page_no-1)//5

        pages = [x for x in range((current_range*5)+1, min(num_pages + 1,(current_range*5)+6))]

        context.update({'pages': pages})
        return context


def search(request):

    relation_list = Relation.objects.all()
    relation_filter = RelationFilter(request.GET, queryset=relation_list)
    page = request.GET.get('page', 1)

    paginator = Paginator(relation_list, 10)
    try:
        relations = paginator.page(page)
    except PageNotAnInteger:
        relations = paginator.page(1)
    except EmptyPage:
        relations = paginator.page(paginator.num_pages)

    return render(request, 'datalin/relation_search_pagination.html', {'relations': relations})
    # return render(request, 'datalin/relation_search.html', {'filter': relation_filter})

# def search2(request):
#     node_list = Node.objects.none()
#     node_filter = NodeFilter(request.GET, queryset=node_list)
#     return render(request, 'search/node_list.html', {'filter': node_filter})



