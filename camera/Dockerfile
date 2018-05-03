FROM python:alpine

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV VERKADA_CAMERA_API_URL http://api:5000
ENTRYPOINT [ "python" ]
CMD [ "-m", "camera" ]
