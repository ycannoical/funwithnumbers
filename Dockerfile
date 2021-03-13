FROM python:3
WORKDIR /usr/src/app
COPY . .
CMD ["thenoendprogram.py"]
ENTRYPOINT ["python3"]