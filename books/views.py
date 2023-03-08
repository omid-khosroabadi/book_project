from django.shortcuts import render, get_object_or_404, redirect
from .models import Books, Comment
from .forms import CommentForm, AddBookForm, SearchForm
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin


def book_list(request):
    book = Books.objects.all()
    form = SearchForm()
    if 'search' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            cd = form.cleaned_data['search']
            book = book.filter(title__icontains=cd)
            form = SearchForm()

    return render(request, 'books/book_list.html', context={'books': book,
                                                            'search_book': form,
                                                            })


def book_detail(request, pk):
    book = get_object_or_404(Books, id=pk)
    return render(request, 'books/book_detail.html', context={'book': book,
                                                              'comment_form': CommentForm(),
                                                              })


class CommentCreate(LoginRequiredMixin, generic.CreateView):
    model = Comment
    form_class = CommentForm

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user
        pk = int(self.kwargs['pk'])
        book = get_object_or_404(Books, id=pk)
        obj.book = book
        messages.success(self.request, 'saved your comment')
        return super().form_valid(form)


class CommentDelete(LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
    model = Comment
    template_name = 'books/comment_delete.html'

    def test_func(self):
        obj = self.get_object()
        self.book_id = obj.book_id
        return obj.author == self.request.user

    def form_invalid(self, form):
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        messages.success(self.request, 'your comment deleted successfully')
        return reverse('book_detail', kwargs=dict(pk=self.book_id))


class CommentUpdate(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    model = Comment
    fields = ['body', 'star', 'recommend']
    template_name = 'books/comment_update.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

    def form_invalid(self, form):
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        messages.success(self.request, 'edited your comment')
        return reverse('book_detail', kwargs=dict(pk=self.kwargs['pk']))


@login_required
def book_add(request):
    form = AddBookForm()
    if request.method == 'POST':
        form = AddBookForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'new book added')
            return redirect('book_list')
    return render(request, 'books/book_add.html', context={'add_book_form': form})


class BookDelete(LoginRequiredMixin, SuccessMessageMixin, generic.DeleteView):
    success_message = 'book deleted successfully'
    model = Books
    template_name = 'books/book_delete.html'
    success_url = reverse_lazy('book_list')


class BookUpdate(LoginRequiredMixin, SuccessMessageMixin, generic.UpdateView, ):
    success_message = 'book edited'
    model = Books
    template_name = 'books/book_update.html'
    success_url = reverse_lazy('book_list')
    fields = ['title', 'text', 'price']

