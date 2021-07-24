from django.views.decorators.csrf import ensure_csrf_cookie
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.template.loader import render_to_string
from django.core.mail import send_mail


from rest_framework import viewsets, status
from rest_framework.response import Response

from .serializers import PostSerializers
from .models import Post


@method_decorator(login_required, name='serializer_class')
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-date')
    serializer_class = PostSerializers


    @method_decorator(ensure_csrf_cookie)
    def create(self, request):
        if request.method == 'POST' and request.data['csrftoken']:
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
                    return Response(data=request.data, status=status.HTTP_200_OK)
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

                    return Response(data=request.data, status=status.HTTP_201_CREATED)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
