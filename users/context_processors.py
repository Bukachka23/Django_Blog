from .forms import SearchForm

# Search form context processor
def search_form(request):
    return {'search_form': SearchForm()}