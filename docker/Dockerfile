FROM python:3.11

RUN apt-get update
# RUN apt-get install -y libreoffice
RUN apt-get -y install libreoffice-nogui
RUN apt-get -y install wkhtmltopdf

RUN apt update
RUN apt -y install wkhtmltopdf

WORKDIR /code

RUN wget https://github.com/wkhtmltopdf/packaging/releases/download/0.12.6.1-2/wkhtmltox_0.12.6.1-2.jammy_amd64.deb
RUN dpkg -x wkhtmltox_0.12.6.1-2.jammy_amd64.deb .
RUN rm wkhtmltox_0.12.6.1-2.jammy_amd64.deb

COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY gunicorn.conf.py .
COPY main.py .

RUN mkdir -p templates
COPY templates/index.html templates/index.html
COPY templates/style.css templates/style.css

RUN mkdir -p files
COPY files/schema_template.json files/schema_template.json
COPY files/settings_template.json files/settings_template.json

# Make port available
EXPOSE 3100  

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "3100", "--proxy-headers"]

