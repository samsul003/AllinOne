from main_app.models import Category


def categories(request):

    return {'categories': Category.objects.all()}

def next_param(request, next_val=""):
    return {'next_param': next_val}