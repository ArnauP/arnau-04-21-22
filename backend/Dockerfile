FROM python:3.6
WORKDIR /backend
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
VOLUME ["/data/db"]
ENV PYTHONPATH "${PYTHONPATH}:/backend"
EXPOSE 5000
CMD ["python", "controller/app.py"]
