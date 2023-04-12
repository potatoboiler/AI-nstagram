FROM nvidia/cuda:11.8.0-devel-ubuntu22.04

WORKDIR /root/

# Install base utilities
RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get install -y wget build-essential git \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Conda
ENV CONDA_DIR /opt/conda
RUN wget --quiet https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda.sh && \
	/bin/bash ~/miniconda.sh -b -p /opt/conda
ENV PATH=$CONDA_DIR/bin:$PATH
RUN conda init bash \
	&& . /root/.bashrc \
	&& conda activate

# Install deps
RUN conda install pytorch torchvision torchaudio pytorch-cuda=11.8 -c pytorch -c nvidia
RUN pip install transformers diffusers invisible-watermark

RUN git clone --recurse-submodules -j8 https://github.com/potatoboiler/AI-nstagram.git \
	&& cd AI-nstagram/xformers \
	&& git submodule update --init --recursive \
	&& pip install -r requirements.txt \
	&& pip install -e .

RUN conda clean -af

WORKDIR /root/AI-nstagram

EXPOSE 80

# ENTRYPOINT ["/bin/bash"]
