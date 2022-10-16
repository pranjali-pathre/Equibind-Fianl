FROM ubuntu:18.04
ENV PATH="/root/miniconda3/bin:${PATH}"
ARG PATH="/root/miniconda3/bin:${PATH}"
RUN apt-get update

RUN apt-get install -y wget && rm -rf /var/lib/apt/lists/*

RUN apt-get update && apt-get upgrade -y && apt-get install git python-pip -y
RUN apt-get install wget curl -y

RUN apt-get update --fix-missing && apt-get install -y wget bzip2 ca-certificates libglib2.0-0 libxext6 libsm6 libxrender1 git mercurial subversion

RUN wget \
    https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh \
    && mkdir /root/.conda \
    && bash Miniconda3-latest-Linux-x86_64.sh -b \
    && rm -f Miniconda3-latest-Linux-x86_64.sh
RUN conda --version
# RUN pip install torcheck
# RUN pip install pytest

RUN conda create -n equibind python=3.7 -y
# RUN conda env create -f environment_cpuonly.yml

WORKDIR /opt/
RUN activate equibind
RUN pip install psutil
# RUN pip install -r /opt/requirements.txt --no-cache-dir
RUN pip install torch==1.10.0 --no-cache-dir
RUN pip install torchvision --no-cache-dir
RUN pip install torchaudio --no-cache-dir
RUN pip install dgl --no-cache-dir
RUN pip install rdkit --no-cache-dir
RUN pip install biopython --no-cache-dir
RUN pip install biopandas --no-cache-dir
RUN pip install pot --no-cache-dir
RUN pip install dgllife --no-cache-dir
RUN pip install joblib --no-cache-dir
RUN pip install pyaml --no-cache-dir
RUN pip install icecream --no-cache-dir
RUN pip install matplotlib --no-cache-dir
RUN pip install tensorboard --no-cache-dir
RUN pip install tensorboard --no-cache-dir
RUN pwd
COPY openbabel-3.1.1-cp310-cp310-win32.whl /opt/
RUN ls
RUN apt-get install openbabel -y
RUN pip install fastapi --no-cache-dir
RUN pip install uvicorn --no-cache-dir
RUN pip install python-multipart

COPY EquiBind /opt/
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "800"]
# CMD ["uvicorn", "/opt/main:app"]
