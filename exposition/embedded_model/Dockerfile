FROM python:3.11-slim
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 8091
ENV PYTHONPATH /app
CMD streamlit run embedded_model.py --server.port 8091
