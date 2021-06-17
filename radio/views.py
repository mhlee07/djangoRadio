from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .models import Show, Audio, Category
from .forms import ShowCreateForm, AudioCreateForm, ShowUpdateForm


# List of all shows
class IndexView(ListView):
    model = Show
    template_name = 'radio/index.html'

    def get_queryset(self):
        return Show.objects.all().order_by('-id')


# List of related category shows
def category_view(request, category_name):
    show_list = Show.objects.filter(category=category_name)
    return render(request, 'radio/category.html', {
        'category_name':category_name,
        'show_list':show_list
        })


# Detail of Show
class DetailView(DetailView):
    model = Show
    template_name = 'radio/detail.html'


# Create new show
class ShowCreate(CreateView):
    model = Show
    form_class = ShowCreateForm
    template_name = 'radio/show-add.html'

    # Associate user with new show
    def form_valid(self, form):
        form.instance.artist = self.request.user
        return super().form_valid(form)


# Create new category
class CategoryCreate(CreateView):
    model = Category
    fields = '__all__'
    template_name = 'radio/category-add.html'
    success_url = reverse_lazy('radio:index')


# Create new audio
class AudioCreate(CreateView):
    model = Audio
    form_class = AudioCreateForm
    template_name = 'radio/audio-add.html'

    # Associate show with new audio
    def form_valid(self, form):
        form.instance.show_id = self.kwargs['pk']
        return super().form_valid(form)


# Update show
class ShowUpdate(UpdateView):
    model = Show
    form_class = ShowUpdateForm
    template_name = 'radio/show-update.html'


# Delete show
class ShowDelete(DeleteView):
    model = Show
    success_url = reverse_lazy('radio:index')


# Delete audio
def audio_delete(request, show_id, audio_id):
    show = get_object_or_404(Show, pk=show_id)
    audio = Audio.objects.get(pk=audio_id)
    audio.delete()
    return render(request, 'radio/detail.html', {'show':show})


# Favorite show
def show_favorite(request, show_id):
    selected_show = get_object_or_404(Show, pk=show_id)
    if selected_show.favorite.filter(pk=request.user.id).exists():
        selected_show.favorite.remove(request.user)
    else:
        selected_show.favorite.add(request.user)  # Highlight which user likes the show
    return HttpResponseRedirect(reverse('radio:index'))


# Favorite audio
def audio_favorite(request, audio_id):
    selected_audio = get_object_or_404(Audio, pk=audio_id)
    if selected_audio.favorite.filter(pk=request.user.id).exists():
        selected_audio.favorite.remove(request.user)
    else:
        selected_audio.favorite.add(request.user)
    return HttpResponseRedirect(reverse('radio:detail', args=[selected_audio.show.id]))


# Search bar
def search_view(request):
    if request.method == 'GET':
        search_value = request.GET['q']
        search_result = Show.objects.filter(show_name__contains=search_value).order_by('-id')
        return render(request, 'radio/search.html', {
            'search_value': search_value,
            'search_result': search_result,
            })
    else:
        return reverse_lazy('radio:index')
