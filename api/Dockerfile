FROM python:alpine

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
RUN python create_db.py

EXPOSE 5000
ENTRYPOINT [ "python" ]
CMD [ "-m", "flask", "run", "--host=0.0.0.0" ]
