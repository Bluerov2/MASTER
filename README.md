# BlueRov2 SLAM

![Heriot Watt](https://www.google.co.uk/url?sa=i&url=https%3A%2F%2Fwww.scotland.org%2Fstudy%2Fscottish-universities%2Fheriot-watt-university&psig=AOvVaw0FqS4zfgh83a-uElM-nA31&ust=1584639087271000&source=images&cd=vfe&ved=0CAIQjRxqFwoTCNCa6-LGpOgCFQAAAAAdAAAAABAD)

The aim of this project is to provide a start of a 3D SLAM for underwater ROV. this project uses UUV simulation to fufill this objectif. The model is simulated using Deskitek Saga but you can use your own as well. we modified the sonar to be se same as the [Micron Sonar](https://www.tritech.co.uk/product/small-rov-mechanical-sector-scanning-sonar-tritech-micron) from Tritech.

![sonar](https://github.com/Bluerov2/MASTER/blob/master/images/Screenshot%20from%202020-03-02%2015-56-21.png)


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
$ cd ~/catkin_ws/src
$ git clone https://github.com/uuvsimulator/uuv_simulator
$ git clone https://github.com/OctoMap/octomap
$ git clone https://github.com/uuvsimulator/desistek_saga.git
$ git clone https://github.com/pal-robotics-forks/point_cloud_converter.git
$ git clone https://github.com/fada-catec/amcl3d.git
$ cd ~/catkin_ws
$ catkin_make
```

## Installation

```
$ cd ~/catkin_ws/src
$ git clone https://github.com/Bluerov2/MASTER.git
$ cd ~/catkin_ws
$ catkin_make # or <catkin build>, if you are using catkin_tools
```
## List of Task

- [x] UUV simulation senario
- [x] IMU & DLV fused (/odom)
- [x] 3D Mapping (octomap)
- [x] 2D SLAM using Particle Filter
- [ ] 3D SLAM using Particle Filter
