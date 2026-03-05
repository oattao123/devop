FROM ubuntu:22.04

RUN apt-get update && apt-get install -y \
    openssh-server \
    python3 \
    sudo \
    && rm -rf /var/lib/apt/lists/*

RUN mkdir /var/run/sshd

# Create target user
RUN useradd -m -s /bin/bash target_user && \
    echo "target_user:password123" | chpasswd && \
    echo "target_user ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers

# Allow SSH access
RUN mkdir -p /home/target_user/.ssh && \
    chown target_user:target_user /home/target_user/.ssh && \
    chmod 700 /home/target_user/.ssh

EXPOSE 22

CMD ["/usr/sbin/sshd", "-D"]
