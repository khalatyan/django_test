from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import DetailView

from first.models import DeliveryState


class FirstView(DetailView):
    # model = DeliveryState

    def get(self, request, *args, **kwargs):
        current = 'first'

        # print(DeliveryState.get_refused())
        print(DeliveryState.get_refused())
        # print("DDDDdf")
        #
        # print(DeliveryState.__dict__)
        # print('dfdf')
        # print(DeliveryState.hhh)
        # print(DeliveryState.objects.all().first().s)
        # print(getattr(DeliveryState, 'get_x'))

        # print(MyClass.Bar)
        # print(str(MyClass))

        return HttpResponse(200)