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
