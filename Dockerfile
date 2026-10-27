FROM python:3.11-slim
WORKDIR /workspace
COPY requirements.txt .
RUN pip install \
    -i https://pypi.tuna.tsinghua.edu.cn/simple \
    --trusted-host pypi.tuna.tsinghua.edu.cn \
    --timeout 120 \
    --retries 5 \
    -r requirements.txt pytest
COPY . .
