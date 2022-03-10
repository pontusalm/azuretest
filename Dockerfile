FROM python3.9
WORKDIR /Python/azuretest/app
COPY './requirements.txt' .
RUN pip install -r requirements.txt
COPY . .
RUN flask db init
RUN flask db migrate
RUN flask db upgrade
ENTRYPOINT ["python","app.py"]


