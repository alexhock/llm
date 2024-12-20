FROM pytorch/pytorch:2.4.1-cuda12.1-cudnn9-devel
ARG USERNAME=vscode

WORKDIR /

# Install common tools
RUN apt-get update && apt-get -y install git procps curl libicu-dev build-essential libssl-dev libffi-dev wget libgl1 libsecret-1-0

RUN useradd -ms /bin/bash $USERNAME

# Install Azure CLI
RUN curl -sL https://aka.ms/InstallAzureCLIDeb | bash

#WORKDIR /home/$USERNAME
USER $USERNAME

