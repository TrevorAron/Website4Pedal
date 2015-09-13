from django.shortcuts import render
from .models import Effect
from .models import Twitter

# Create your views here.
def index(request):
    effect_list = Effect.objects.order_by('id')
    twitter = Twitter.objects.get(pk=1)
    num = len(effect_list)

    tuple_list = []
    master_tup = ()
    for i in range(num):
        temp_tup = (effect_list[i],)
        master_tup = master_tup + temp_tup
        if i % 3 == 2:
            tuple_list.append(master_tup)
            master_tup = ()
    context = {'effect_list': tuple_list, 'bird': twitter}
    return render(request, 'polls/index.html', context)

def submit(request):
    bird = Twitter.objects.get(pk=1)
    try:
        status = request.POST['twitter_status']
    except (KeyError, Choice.DoesNotExist):
        pass
    else:
        if status == "ON":
            b_status = True
        else
            b_status = False
        bird.status = b_status
        bird.save()

    for effect in Effects.objects.order_by('id'):
        range_string = "range" + str(effect.id)
        status_string = "status" + str(effect.id)
        try:
            slide_val = request.POST[range_string]
        except (KeyError, Choice.DoesNotExist):
            pass
        else:
            effect.param = int(slide_val)
            effect.save()

        try:
            status = request.POST[status_string]
        except (KeyError, Choice.DoesNotExist):
            pass
        else:
            if status == "ON":
                b_status = True
            else
                b_status = False

            effect.status = b_status
            effect.save()
