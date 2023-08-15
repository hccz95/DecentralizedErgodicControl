Decentralized Ergodic Control
=============================

Create a ros melodic environment with this package in the src folder. 
First source the ros devel/setup file
To run use the following commands
```
python create_scene.py num_of_agents
```
where num_of_agents is replaced with the number of agents you 
want to see (dont set it high than 50).

then to visualize the environment run 
```
rosrun rviz rviz 
```
and open the default.rviz config in the rviz folder in this repo

# Run in docker

1. Start a container by `docker run -p 6080:80 hccz95/ros:noetic-dec`. Or you can build from `./Dockerfile`.
2. Open `localhost:6080` in browser.
3. Open a terminal and compile the workspace:
    ```bash
    cd /home/catkin_ws/
    catkin_make
    echo "source /home/catkin_ws/devel/setup.bash" >> ~/.bashrc
    ```
4. Open a terminal (I) and run:
    ```bash
    roscore
    ```
5. Open a terminal (II) and run:
    ```bash
    cd /home/catkin_ws/src/DecentralizedErgodicControl/
    python create_scene.py 5
    ```
6. Open a terminal (III) and run rviz to render:
    ```bash
    cd /home/catkin_ws/src/DecentralizedErgodicControl/
    rosrun rviz rviz -d ./rviz/default.rviz
    ```
