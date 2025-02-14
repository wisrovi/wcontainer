FROM python:3.10.14-bullseye


USER root

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


# Establecemos el directorio de trabajo en /app
WORKDIR /app

# Instalamos git y actualizamos dependencias
RUN apt-get update && apt-get install -y git && apt-get clean

# RUN curl -sSL https://get.docker.com | sh
# RUN usermod -a -G docker $USER
# RUN VERSION=$(curl --silent https://api.github.com/repos/docker/compose/releases/latest | grep -Po '"tag_name": "\K.*\d')
# RUN DESTINATION=/usr/local/bin/docker-compose
# RUN curl -L https://github.com/docker/compose/releases/download/${VERSION}/docker-compose-$(uname -s)-$(uname -m) -o $DESTINATION
# RUN chmod 755 $DESTINATION

# Establecer argumentos y entorno
ARG DEBIAN_FRONTEND=noninteractive
ENV PATH="/usr/local/bin:$PATH"
# Instalar dependencias necesarias
RUN apt-get update && apt-get install -y \
    ca-certificates \
    curl \
    gnupg \
    lsb-release \
    iproute2 \
    iputils-ping \
    net-tools \
    procps \
    && rm -rf /var/lib/apt/lists/*
# Agregar la clave GPG de Docker
RUN mkdir -p /etc/apt/keyrings && \
    curl -fsSL https://download.docker.com/linux/debian/gpg | \
    tee /etc/apt/keyrings/docker.asc | \
    gpg --dearmor -o /etc/apt/keyrings/docker.gpg
# Agregar el repositorio de Docker
RUN echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] \
    https://download.docker.com/linux/debian $(lsb_release -cs) stable" | \
    tee /etc/apt/sources.list.d/docker.list > /dev/null
# Instalar Docker y Docker Compose
RUN apt-get update && apt-get install -y \
    docker-ce \
    docker-ce-cli \
    containerd.io \
    docker-buildx-plugin \
    docker-compose-plugin \
    && rm -rf /var/lib/apt/lists/*
# Verificar versiones de Docker y Docker Compose
RUN docker --version && docker compose version



# ZSH
RUN apt-get update && apt-get install -y zsh
RUN apt-get install -y wget
# Uses "robbyrussell" theme (original Oh My Zsh theme), with no plugins
RUN sh -c "$(wget -O- https://github.com/deluan/zsh-in-docker/releases/download/v1.1.5/zsh-in-docker.sh)" -- \
    -t aussiegeek

# customizations
RUN apt-get install figlet -y
RUN echo "alias ll='ls -l'" >> ~/.zshrc





# Establece el directorio de trabajo en el contenedor
WORKDIR /app

RUN apt-get update && apt-get install -y ffmpeg

# Copia los archivos necesarios al contenedor
COPY . /app

# Instala las dependencias
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Expone el puerto de Gradio
EXPOSE 7860


RUN echo "figlet brain_register" >> ~/.zshrc
RUN echo "figlet brain_register" >> ~/.bashrc

# Comando para ejecutar la aplicación
CMD ["python", "app.py"]