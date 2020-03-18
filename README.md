# BlueRov2 SLAM

![Heriot Watt](https://www.google.co.uk/url?sa=i&url=https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FHeriot-Watt_University&psig=AOvVaw27FTzzX9Y5zyaOmgmClZKh&ust=1584638885439000&source=images&cd=vfe&ved=0CAIQjRxqFwoTCPDvhYHGpOgCFQAAAAAdAAAAABAD)

## Related Packages

* UUV-simulator:

  https://github.com/uuvsimulator/uuv_simulator

* Octomap_server :
  
  https://github.com/OctoMap/octomap
  
* Desistek SAGA ROV vehicle:

  https://github.com/uuvsimulator/desistek_saga.git
  
* Point cloud Converter:
  
  https://github.com/pal-robotics-forks/point_cloud_converter.git

* AMCL3:
  
  https://github.com/fada-catec/amcl3d.git
  
  
  
  
To install every packages needed run the commands:

```
cd ~/catkin_ws/src
git clone https://github.com/uuvsimulator/uuv_simulator
git clone https://github.com/OctoMap/octomap
git clone https://github.com/uuvsimulator/desistek_saga.git
git clone https://github.com/pal-robotics-forks/point_cloud_converter.git
git clone https://github.com/fada-catec/amcl3d.git
cd ~/catkin_ws
catkin_make
```

## Installation

```
cd ~/catkin_ws/src
git clone https://github.com/Bluerov2/MASTER.git
cd ~/catkin_ws
catkin_make # or <catkin build>, if you are using catkin_tools
```
## List of Task

- [x] UUV simulation senario
- [x] IMU & DLV fused (/odom)
- [x] 3D Mapping (octomap)
- [x] 2D SLAM using Particle Filter
- [ ] 3D SLAM using Particle Filter
