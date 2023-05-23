from django.shortcuts import render, redirect
from .forms import HotelBillForm
from .models import HotelBill



def input_data(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        address = request.POST.get('address')
        cindate = request.POST.get('cindate')
        coutdate = request.POST.get('coutdate')
        rno = int(request.POST.get('rno', 101))
        bill = HotelBill(name=name, address=address, cindate=cindate, coutdate=coutdate, rno=rno)
        bill.save()
        return render(request, 'hotel/room_rent.html', {'bill': bill})
    else:
        return render(request, 'hotel/input_data.html')

def room_rent(request):
    bill = HotelBill.objects.latest('id')
    if request.method == 'POST':
        x = int(request.POST.get('room_type'))
        n = int(request.POST.get('num_nights'))
        if x == 1:
            bill.s = 6000 * n
        elif x == 2:
            bill.s = 5000 * n
        elif x == 3:
            bill.s = 4000 * n
        elif x == 4:
            bill.s = 3000 * n
        else:
            return render(request, 'hotel/room_rent.html', {'bill': bill, 'error': 'Invalid room type'})
        
        bill.save()
        return render(request, 'hotel/restaurant_bill.html', {'bill': bill})
    else:
        return render(request, 'hotel/room_rent.html', {'bill': bill})
    

    
def hotel_bill_create(request):
    if request.method == 'POST':
        form = HotelBillForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('hotel_bill_success')  # Redirect to the success URL or template
    else:
        form = HotelBillForm()
    
    return render(request, 'hotel/hotel_bill_create.html', {'form': form})

def hotel_bill_success(request):
    return render(request, 'hotel_bill_success.html')


def restaurant_bill(request):
    bill = HotelBill.objects.latest('id')
    if request.method == 'POST':
        c = int(request.POST.get('choice'))
        if c == 6:
            return render(request, 'hotel/laundry_bill.html', {'bill': bill})
        
        if c < 1 or c > 6:
            return render(request, 'hotel/restaurant_bill.html', {'bill': bill, 'error': 'Invalid option'})
        
        d = int(request.POST.get('quantity'))
        if c == 1:
            bill.r += 20 * d
        elif c == 2:
            bill.r += 10 * d
        elif c == 3:
            bill.r += 90 * d
        elif c == 4:
            bill.r += 110 * d
        elif c == 5:
            bill.r += 150 * d
        
        bill.save()
    
    return render(request, 'hotel/restaurant_bill.html', {'bill': bill})

def laundry_bill(request):
    bill = HotelBill.objects.latest('id')
    if request.method == 'POST':
        e = int(request.POST.get('choice'))
        if e == 6:
            return render(request, 'hotel/game_bill.html', {'bill': bill})
        
        if e < 1 or e > 6:
            return render(request, 'hotel/laundry_bill.html', {'bill': bill, 'error': 'Invalid option'})
        
        f = int(request.POST.get('quantity'))
        if e == 1:
            bill.t += 3 * f
        elif e == 2:
            bill.t += 4 * f
        elif e == 3:
            bill.t += 5 * f
        elif e == 4:
            bill.t += 6 * f
        elif e == 5:
            bill.t += 8 * f
        
        bill.save()
    
    return render(request, 'hotel/laundry_bill.html', {'bill': bill})

def game_bill(request):
    bill = HotelBill.objects.latest('id')
    if request.method == 'POST':
        g = int(request.POST.get('choice'))
        if g == 6:
            return render(request, 'hotel/display.html', {'bill': bill})
        
        if g < 1 or g > 6:
            return render(request, 'hotel/game_bill.html', {'bill': bill, 'error': 'Invalid option'})
        
        h = int(request.POST.get('num_hours'))
        if g == 1:
            bill.p += 60 * h
        elif g == 2:
            bill.p += 80 * h
        elif g == 3:
            bill.p += 70 * h
        elif g == 4:
            bill.p += 90 * h
        elif g == 5:
            bill.p += 50 * h
        
        bill.save()
    
    return render(request, 'hotel/game_bill.html', {'bill': bill})

def display(request):
    bill = HotelBill.objects.latest('id')
    bill.rt = bill.s + bill.t + bill.p + bill.r
    bill.save()
    return render(request, 'hotel/display.html', {'bill': bill})
