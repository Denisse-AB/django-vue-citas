from django.http import JsonResponse, HttpResponseBadRequest, HttpResponseNotAllowed
from django.template.loader import render_to_string
from django.core.mail import send_mail


from rest_framework import viewsets

from .serializers import PostSerializers
from .models import Post

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-date')
    serializer_class = PostSerializers

    def create(self, request):
        if request.method == 'POST':
            serializer = PostSerializers(data=request.data)
            if serializer.is_valid():
                input_email = request.data.get('email')
                input_name = request.data.get('name')
                input_date = request.data.get('date')
                input_time = request.data.get('time')
                q = Post.objects.filter(date=input_date, time=input_time)
                count = q.count()
                # Cuatro citas por hora, four appointments per hour.
                if count > 3:
                    return JsonResponse(request.data, status=200)
                else:
                    serializer.save()
                    # email
                    context = {
                        'name': input_name,
                        'date': input_date,
                        'time': input_time
                    }
                    subject = 'Tu Cita!'
                    html_message = render_to_string('citas\email.html', context)
                    from_email = 'from@example.com'
                    to = input_email

                    send_mail(subject, html_message, from_email, [to], html_message=html_message)

                    return JsonResponse(request.data, status=201)

            return HttpResponseBadRequest(serializer.errors)
        return HttpResponseNotAllowed()
