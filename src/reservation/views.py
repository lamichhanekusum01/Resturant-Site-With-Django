from .models import Reservation
from django.shortcuts import render
from .forms import ReserveTableForm

from reservation.models import Reservation

def reserve_table(request):
    isReserved = False
    reserve_form = ReserveTableForm()

    if request.method == 'POST' :
        reserve_form = ReserveTableForm(request.POST)

        if reserve_form.is_valid():
            reserve_form.save()
            reserve_form = ReserveTableForm()
            isReserved = True

    context = {'form' : reserve_form, 'isReserved': isReserved}

    return render(request , 'Reservation/reservation.html' , context)

