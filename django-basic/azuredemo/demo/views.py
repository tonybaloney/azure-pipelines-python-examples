from django.shortcuts import render
from django.http import HttpResponse, Http404

# Create your views here.
def index(request):
    if 'person' in request.POST:
        if request.POST['person'] == 'ground_control' \
         and request.POST['message'] == 'Ground Control to Major Tom':
            return HttpResponse(
                """<p>This is Major Tom to Ground Control,
                I'm stepping through the door,
                And I'm floating in a most peculiar way,
                And the stars look very different today.</p>""")
    raise Http404("Huh?")
