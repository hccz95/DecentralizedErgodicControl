FROM tiryoh/ros-desktop-vnc:noetic

RUN sudo apt-get update && \
    DEBIAN_FRONTEND=noninteractive sudo apt-get install -y ros-noetic-grid-map && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

ARG WS=/home/catkin_ws
RUN mkdir -p $WS/src && \
    cd $WS/src && \
    git clone https://github.com/hccz95/DecentralizedErgodicControl.git && \
    chmod -R 777 $WS
RUN echo "source $WS/devel/setup.bash" >> ~/.bashrc

RUN sudo apt-get update && \
    DEBIAN_FRONTEND=noninteractive sudo apt-get install -y x11-apps openssh-server python3-pip && \
    apt-get clean && rm -rf /var/lib/apt/lists/* && \
    sed -i "s/.*PermitRootLogin.*/PermitRootLogin yes/g" /etc/ssh/sshd_config && \
    sed -i 's/^#X11UseLocalhost yes/X11UseLocalhost no/' /etc/ssh/sshd_config
RUN pip3 install pygame && echo "root:sim812" | chpasswd && \
    mkdir -p ~/.pip && echo "[global]" > ~/.pip/pip.conf && \
    echo "index-url = https://pypi.tuna.tsinghua.edu.cn/simple/" >> ~/.pip/pip.conf && \
    echo "trusted-host = pypi.tuna.tsinghua.edu.cn" >> ~/.pip/pip.conf
# RUN sudo apt-get update && \
#     DEBIAN_FRONTEND=noninteractive sudo apt-get install -y \
#     alsa-base alsa-utils && \
#     apt-get clean && rm -rf /var/lib/apt/lists/*
