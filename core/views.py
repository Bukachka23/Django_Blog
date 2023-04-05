from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.utils.text import slugify
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

from .models import Post, Comment
from .forms import CommentForm


# A subclass of ListView that displays a list of objects.
class HomeView(ListView):
    template_name = 'core/home.html'
    queryset = Post.objects.all()
    paginate_by = 2


# A subclass of DeleteView that deletes an object.
class PostView(DetailView):
    model = Post
    template_name = "core/post.html"

    # A function that returns the context data.
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs["pk"]
        slug = self.kwargs["slug"]

        form = CommentForm()
        post = get_object_or_404(Post, pk=pk, slug=slug)
        comments = post.comment_set.all()

        context['post'] = post
        context['comments'] = comments
        context['form'] = form
        return context

    # A function that handles POST requests.
    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST)
        self.object = self.get_object()
        context = super().get_context_data(**kwargs)

        post = Post.objects.filter(id=self.kwargs['pk'])[0]
        comments = post.comment_set.all()

        context['post'] = post
        context['comments'] = comments
        context['form'] = form

        # Checks if the form is valid.
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            content = form.cleaned_data['content']

            comment = Comment.objects.create(
                name=name, email=email, content=content, post=post
            )

            form = CommentForm()
            context['form'] = form
            return self.render_to_response(context=context)

        return self.render_to_response(context=context)


# A subclass of CreateView that creates a new object.
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ["title", "content", "image", "tags"]

    # A function that returns the context data.
    def get_success_url(self):
        messages.success(
            self.request, 'Your post has been created successfully.')
        return reverse_lazy("core:home")

    # Called when valid form data has been POSTed.
    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user
        obj.slug = slugify(form.cleaned_data['title'])
        obj.save()
        return super().form_valid(form)


# A subclass of UpdateView that updates an object.
class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ["title", "content", "image", "tags"]

    # A function that returns the context data.
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        update = True
        context['update'] = update

        return context

    # A function that returns the URL to redirect to after processing a valid form.
    def get_success_url(self):
        messages.success(
            self.request, 'Your post has been updated successfully.')
        return reverse_lazy("core:home")

    # Used to filter the queryset.
    def get_queryset(self):
        return self.model.objects.filter(author=self.request.user)


# A subclass of DeleteView that deletes an object.
class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post

    # A function that returns the URL to redirect to after processing a valid form.
    def get_success_url(self):
        messages.success(
            self.request, 'Your post has been deleted successfully.')
        return reverse_lazy("core:home")

    # Used to filter the queryset.
    def get_queryset(self):
        return self.model.objects.filter(author=self.request.user)