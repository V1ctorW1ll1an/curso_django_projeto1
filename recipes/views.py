from django.shortcuts import render

# Create your views here.


def home_recipes(request):
    context = {
        "logo_name": "Recipes"
    }

    return render(
        request=request,
        template_name='recipes/pages/home.html',
        context=context
    )
