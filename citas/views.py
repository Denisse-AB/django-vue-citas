import datetime
from django.template.loader import render_to_string
from django.core.mail import send_mail

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import PostSerializers

from .models import Post


class CreateAppointment(APIView):

    def post(self, request, format=None):
        if request.method == 'POST':
            serializer = PostSerializers(data=request.data)
            if serializer.is_valid():
                email = request.data.get('email')
                name = request.data.get('name')
                date = request.data.get('date')
                time = request.data.get('time')
                check = Post.objects.filter(date=date, time=time)
                count = check.count()
                # Cuatro citas por hora
                # four appointments per hour.
                if count > 3:
                    return Response(data=request.data, status=status.HTTP_200_OK)
                else:
                    obj = serializer.save()
                    # email
                    context = {
                        'name': name,
                        'date': obj.date,
                        'time': obj.time
                    }
                    subject = 'Tu Cita!'
                    html_message = render_to_string('citas/email.html', context)
                    from_email = 'from@example.com'
                    to = email

                    send_mail(subject, html_message, from_email, [to], html_message=html_message)
                    
                    date = datetime.datetime.strptime(str(obj.date),'%Y-%m-%d').strftime('%d/%m/%Y')
                    time = datetime.datetime.strptime(str(obj.time),'%H:%M:%S').strftime('%I:%M %p')

                    return Response(
                        data={
                            'date': date,
                            'time': time
                        }, status=status.HTTP_201_CREATED)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
