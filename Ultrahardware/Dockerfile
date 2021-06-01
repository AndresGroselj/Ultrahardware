FROM python:3.7-buster
RUN pip install --upgrade pip && \
    pip install Django==3.0.2 && \
    pip install django-allauth==0.44.0 && \
    pip install django-pwa==1.0.10 && \
    pip install djangorestframework==3.12.2 && \
    pip install Pillow==7.2.0
    
COPY . /app
WORKDIR /app
EXPOSE 8000
CMD python manage.py runserver 0.0.0.0:8000