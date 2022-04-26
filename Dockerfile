FROM public.ecr.aws/lambda/python:3.9

COPY requirements.txt .

RUN python3 -m pip install -r requirements.txt --no-cache-dir

COPY  /src/property .

CMD [ "handler.lambda_handler" ]