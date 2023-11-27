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

# Run without ROS

地图大小为$[0,1]^2$

agent的state有4维，前两维是横纵坐标，后两维目前不确定，判断依据是`obs_space`中，前两维是$[0,1]$区间，后两维是$[-\inf,+\inf]$区间。

目前干了这么一些工作，把代码中涉及`publish`、`rospy.Rate(1)`、`rospy.init_node`调用的都删掉，暂时不再依赖`roscore`

但是发现一个问题，agent并没有按照预期分组，去覆盖不同目标；可能是因为去掉了rospy通信，导致agent各自为战，需要自己覆盖所有目标？

`ergodic_controller.py`里的`self._ck_dict`记录了ck的通信记录，用来算平均值的，可以从这里着手改进
