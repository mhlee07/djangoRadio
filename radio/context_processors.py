from .models import Category

def category_dropdown(request):
    category_list = Category.objects.all()
    return {'category_list': category_list}


