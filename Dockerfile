FROM public.ecr.aws/lambda/python:3.8

COPY requirements.txt .

RUN python3 -m pip install -r requirements.txt --target "${LAMBDA_TASK_ROOT}"

COPY  /src/property ${LAMBDA_TASK_ROOT}

ARG DB_HOST
ARG DB_NAME
ARG DB_USER
ARG DB_PASSWORD
ARG AWS_ACCESS_KEY_ID
ARG AWS_SECRET_ACCESS_KEY
ARG AWS_DEFAULT_REGION

ENV DB_HOST $DB_HOST
ENV DB_NAME $DB_NAME
ENV DB_USER $DB_USER
ENV DB_PASSWORD $DB_PASSWORD

CMD [ "handler.lambda_handler" ]
