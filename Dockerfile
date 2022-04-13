FROM python:3.7.11

# Skip the configuration part
ENV DEBIAN_FRONTEND noninteractive

# Update and install depedencies
RUN apt-get update && \
    apt-get install -y wget unzip bc vim python3-pip libleptonica-dev git

# Packages to complie Tesseract
RUN apt-get install -y --reinstall make && \
    apt-get install -y g++ autoconf automake libtool pkg-config \
     libpng-dev libjpeg62-turbo-dev libtiff5-dev libicu-dev \
     libpango1.0-dev autoconf-archive

RUN apt-get install -y poppler-utils

WORKDIR /app

RUN mkdir src && cd /app/src && \
    wget https://github.com/tesseract-ocr/tesseract/archive/5.0.0-alpha-20201224.zip && \
	unzip 5.0.0-alpha-20201224.zip && \
    cd /app/src/tesseract-5.0.0-alpha-20201224 && ./autogen.sh && ./configure && make && make install && ldconfig && \
    make training && make training-install && \
    cd /usr/local/share/tessdata && wget https://github.com/tesseract-ocr/tessdata_best/raw/master/eng.traineddata

# Setting the data prefix
ENV TESSDATA_PREFIX=/usr/local/share/tessdata

RUN apt-get install -y poppler-utils

RUN tesseract --version

COPY . /app

RUN pip install -r requirements.txt

ENTRYPOINT ["python"]

CMD ["main.py"]