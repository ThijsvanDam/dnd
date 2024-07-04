# Use the official Python image as the base image
FROM python:3.10-slim

# Install Node.js and npm
RUN apt-get update && \
    apt-get install -y curl git zsh && \
    curl -fsSL https://deb.nodesource.com/setup_21.x | bash - && \
    apt-get install -y nodejs
    
# Install oh-my-zsh
RUN sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)" "" --unattended

# Install Powerlevel10k theme
RUN git clone --depth=1 https://github.com/romkatv/powerlevel10k.git /root/.oh-my-zsh/custom/themes/powerlevel10k

# Set zsh as the default shell
RUN chsh -s $(which zsh) root

# Configure .zshrc
RUN echo 'export ZSH="/root/.oh-my-zsh"' >> /root/.zshrc && \
    echo 'ZSH_THEME="powerlevel10k/powerlevel10k"' >> /root/.zshrc && \
    echo 'plugins=(git)' >> /root/.zshrc && \
    echo 'source $ZSH/oh-my-zsh.sh' >> /root/.zshrc && \
    echo 'POWERLEVEL9K_DISABLE_CONFIGURATION_WIZARD=true' >> /root/.zshrc

# Install Svelte dependencies
RUN npm install -g degit

# Set the working directory
WORKDIR /workspace

# Copy the backend requirements file into the container
COPY backend/requirements.txt /workspace/backend/

# Install Python dependencies
RUN pip install --no-cache-dir -r /workspace/backend/requirements.txt

# Expose the application port
EXPOSE 5000

# Copy the rest of the application code into the container
COPY . /workspace/

# Command to run the application
CMD ["zsh"]