ARG var_name
from ${var_name}/docker-image-python-backend:latest

ENV FLASK_ENV=production
ENV PORT = "PORTA DA APLICACAO"
ENV APP = radix_challenge.app:create_app

COPY radix_challenge /app
WORKDIR /app

EXPOSE 'NUMERO DA PORTA'

CMD ["waitress-serve", "--port=[#numero da porta#]", "--call", "radix_challenge:create_app"]