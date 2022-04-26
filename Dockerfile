FROM public.ecr.aws/lambda/python:3.9

COPY requirements.txt .

RUN python3 -m pip install -r requirements.txt --target "${LAMBDA_TASK_ROOT}"

COPY  /src/property ${LAMBDA_TASK_ROOT}

CMD [ "handler.lambda_handler" ]