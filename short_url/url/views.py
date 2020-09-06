from django.shortcuts import render, get_object_or_404
from django.views import View
from url.models import AllUrl
from .forms import CreateNewURL
from .utils import new_url
from django.http import HttpResponseRedirect


class UrlView(View):
    def get(self, request):
        form = CreateNewURL()
        context = {
            "form": form,
        }
        return render(request, "home.html", context)

    def post(self, request):
        form = CreateNewURL(request.POST or None)
        if form.is_valid():
            obj = AllUrl()
            obj.long_url = form.cleaned_data.get("original_url")
            l_url = obj.long_url
            s_url = new_url()
            obj.short_url = s_url
            obj.save()
            context = {
                "l_url": l_url,
                "s_url": s_url,
            }
            return render(request, "new_short_url.html", context)
        else:
            form = CreateNewURL()
            context = {
                "form": form,
                'error': "Invalid URL!"
            }

            return render(request, "home.html", context)


def redirect_url(request, short_url=None):
    obj = get_object_or_404(AllUrl, short_url=short_url)
    return HttpResponseRedirect(obj.long_url)
