FROM python:3.10-slim
 
WORKDIR /app
 
COPY requirements.txt requirements.txt
 
RUN pip install -r requirements.txt
 
COPY . .
 
ENV DJANGO_SETTINGS_MODULE=Atividade-Deploy.settings
 
RUN python manage.py collectstatic --noinput

# ARG DB_URL
# ENV DB_URL=${DB_URL}
 
RUN python manage.py mograte --noinput
 
EXPOSE 8000
 
CMD ["gunicon","--bind","0.0.0.0:8000","atividade_de_integracao:application"]