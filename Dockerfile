FROM python:3.10-slim
RUN pip install --no-cache-dir jsbsim
WORKDIR /workspace
CMD ["python"]
