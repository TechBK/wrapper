FROM      python:3
MAINTAINER TechBK <quangbinh.nguyentrong@gmail.com>

RUN pip3 install aiohttp 
RUN apt-get update && apt-get install -y ncbi-blast+ clustalw 
RUN mkdir db

COPY myapp/ /

COPY refseq_rna.00.tar.gz db/

RUN tar zxvpf db/refseq_rna.00.tar.gz && rm db/refseq_rna.00.tar.gz

CMD blastn -version && python3 myapp/tuan4.py

EXPOSE 8080
