FROM python
COPY . /var/app
WORKDIR /var/app
RUN pip install flask
RUN python3 file.py