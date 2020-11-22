from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.template.context_processors import csrf
from django.views import View

from jobtest.settings import DEFAULT_FROM_EMAIL, RECIPIENTS_EMAIL
from main.forms import ContactForm
from main.models import Category, Product


class Index(View):

    def get(self, request):

        categories = Category.get_all_categories()
        categoryID = request.GET.get('category')

        if categoryID:
            products = Product.get_all_products_by_category_id(categoryID)
        else:
            products = Product.get_all_products()

        data = {'products': products, 'categories': categories}
        return render(request, 'index.html', data)


# def reservation_page(requests):
#     return render(requests, 'reservation.html')

def contact_view(request):
    # если метод GET, вернем форму
    if request.method == 'GET':
        form = ContactForm()
    elif request.method == 'POST':
        # если метод POST, проверим форму и отправим письмо
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = 'Reservation'
            from_email = form.cleaned_data['from_email']
            message = 'Phone: ' + form.cleaned_data['phone'] + '\nStolik: ' + form.cleaned_data['chill_time'] + '\nPojelania: ' + form.cleaned_data['delicion']

            try:
                send_mail(f'{subject} от {from_email}', message,
                          DEFAULT_FROM_EMAIL, RECIPIENTS_EMAIL)
            except BadHeaderError:
                return HttpResponse('Ошибка в теме письма.')
            return redirect('success')
    else:
        return HttpResponse('Неверный запрос.')
    return render(request, "reservation.html", {'form': form})


def success_view(request):
    return HttpResponse('Приняли! Спасибо за вашу заявку.')

