from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import View
from .forms import TodoForm
from .models import Todos
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView, UpdateView, DeleteView
from django.utils import timezone
from datetime import timedelta
from django.http import JsonResponse
# Display all todos on the home page.


'''class HomeView(View):
    def get(self, request):
        # Retrieve all todos from the database.
        todos = Todos.objects.all()
        return render(request, 'todo/index.html', {'todos': todos})'''


class HomeView(ListView):
    model = Todos
    template_name = 'todo/index.html'
    context_object_name = 'todos'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        todos = Todos.objects.order_by('-created_at')

        today = timezone.localdate()
        yesterday = today - timedelta(days=1)

        grouped_todos = {}

        for todo in todos:

            todo_date = timezone.localtime(todo.created_at).date()

            if todo_date == today:
                date_title = 'Today'

            elif todo_date == yesterday:
                date_title = 'Yesterday'

            else:
                date_title = todo_date.strftime('%B %d, %Y')

            if date_title not in grouped_todos:
                grouped_todos[date_title] = []

            grouped_todos[date_title].append(todo)

        context['grouped_todos'] = grouped_todos

        return context


class ToggleTodoView(View):

    def post(self, request, id):

        todo = Todos.objects.get(id=id)

        todo.completed = not todo.completed
        todo.save()

        return JsonResponse({
            'completed': todo.completed
        })


class DetailView(DetailView):
    model = Todos
    template_name = 'todo/detail.html'
    context_object_name = 'todos'


# Handle creating a new todo.
'''class AddView(View):

    # Display an empty todo form.
    def get(self, request):
        form = TodoForm()
        return render(request, 'todo/add.html', {'form': form})

    # Process the submitted form.
    def post(self, request):
        # Bind the submitted data to the form.
        form = TodoForm(request.POST)

        # Save the todo if the form is valid.
        if form.is_valid():
            form.save()

            # Redirect
            return HttpResponseRedirect('/')

        # Redisplay the form with validation errors.
        return render(request, 'todo/add.html', {'form': form})'''


class AddView(FormView):
    template_name = 'todo/add.html'
    form_class = TodoForm
    success_url = '/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class UpdateTodoView(UpdateView):
    model = Todos
    # fields = '__all__'
    template_name = 'todo/add.html'
    success_url = '/'
    form_class = TodoForm


class DeleteTodoView(DeleteView):
    model = Todos
    success_url = '/'


class AboutView(TemplateView):
    template_name = 'todo/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['companyname'] = 'chert'
        return context
