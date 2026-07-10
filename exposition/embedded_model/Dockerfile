FROM python:3.14-slim
COPY . /app
WORKDIR /app
RUN pip install --no-deps formation_mlops_2-0.1.0-py3-none-any.whl
RUN pip install -r requirements.txt
EXPOSE 8091
ENV PYTHONPATH /app
CMD streamlit run embedded_model.py --server.port 8091
