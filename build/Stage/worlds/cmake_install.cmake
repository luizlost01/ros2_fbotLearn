# Install script for directory: /home/luiz/ros2_fbot/src/Stage/worlds

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/home/luiz/ros2_fbot/install/Stage")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "RELEASE")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

# Is this installation the result of a crosscompile?
if(NOT DEFINED CMAKE_CROSSCOMPILING)
  set(CMAKE_CROSSCOMPILING "FALSE")
endif()

# Set default install directory permissions.
if(NOT DEFINED CMAKE_OBJDUMP)
  set(CMAKE_OBJDUMP "/usr/bin/objdump")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/stage/worlds" TYPE FILE FILES
    "/home/luiz/ros2_fbot/src/Stage/worlds/amcl-sonar.cfg"
    "/home/luiz/ros2_fbot/src/Stage/worlds/autolab.cfg"
    "/home/luiz/ros2_fbot/src/Stage/worlds/camera.cfg"
    "/home/luiz/ros2_fbot/src/Stage/worlds/everything.cfg"
    "/home/luiz/ros2_fbot/src/Stage/worlds/lsp_test.cfg"
    "/home/luiz/ros2_fbot/src/Stage/worlds/mbicp.cfg"
    "/home/luiz/ros2_fbot/src/Stage/worlds/nd.cfg"
    "/home/luiz/ros2_fbot/src/Stage/worlds/roomba.cfg"
    "/home/luiz/ros2_fbot/src/Stage/worlds/simple.cfg"
    "/home/luiz/ros2_fbot/src/Stage/worlds/test.cfg"
    "/home/luiz/ros2_fbot/src/Stage/worlds/uoa_robotics_lab.cfg"
    "/home/luiz/ros2_fbot/src/Stage/worlds/vfh.cfg"
    "/home/luiz/ros2_fbot/src/Stage/worlds/wavefront-remote.cfg"
    "/home/luiz/ros2_fbot/src/Stage/worlds/wavefront.cfg"
    "/home/luiz/ros2_fbot/src/Stage/worlds/wifi.cfg"
    "/home/luiz/ros2_fbot/src/Stage/worlds/SFU.world"
    "/home/luiz/ros2_fbot/src/Stage/worlds/autolab.world"
    "/home/luiz/ros2_fbot/src/Stage/worlds/camera.world"
    "/home/luiz/ros2_fbot/src/Stage/worlds/circuit.world"
    "/home/luiz/ros2_fbot/src/Stage/worlds/everything.world"
    "/home/luiz/ros2_fbot/src/Stage/worlds/fasr.world"
    "/home/luiz/ros2_fbot/src/Stage/worlds/fasr2.world"
    "/home/luiz/ros2_fbot/src/Stage/worlds/fasr_plan.world"
    "/home/luiz/ros2_fbot/src/Stage/worlds/large.world"
    "/home/luiz/ros2_fbot/src/Stage/worlds/lsp_test.world"
    "/home/luiz/ros2_fbot/src/Stage/worlds/mbicp.world"
    "/home/luiz/ros2_fbot/src/Stage/worlds/pioneer_flocking.world"
    "/home/luiz/ros2_fbot/src/Stage/worlds/pioneer_follow.world"
    "/home/luiz/ros2_fbot/src/Stage/worlds/pioneer_walle.world"
    "/home/luiz/ros2_fbot/src/Stage/worlds/roomba.world"
    "/home/luiz/ros2_fbot/src/Stage/worlds/sensor_noise_demo.world"
    "/home/luiz/ros2_fbot/src/Stage/worlds/sensor_noise_module_demo.world"
    "/home/luiz/ros2_fbot/src/Stage/worlds/simple.world"
    "/home/luiz/ros2_fbot/src/Stage/worlds/uoa_robotics_lab.world"
    "/home/luiz/ros2_fbot/src/Stage/worlds/wifi.world"
    "/home/luiz/ros2_fbot/src/Stage/worlds/beacons.inc"
    "/home/luiz/ros2_fbot/src/Stage/worlds/chatterbox.inc"
    "/home/luiz/ros2_fbot/src/Stage/worlds/hokuyo.inc"
    "/home/luiz/ros2_fbot/src/Stage/worlds/irobot.inc"
    "/home/luiz/ros2_fbot/src/Stage/worlds/map.inc"
    "/home/luiz/ros2_fbot/src/Stage/worlds/objects.inc"
    "/home/luiz/ros2_fbot/src/Stage/worlds/pantilt.inc"
    "/home/luiz/ros2_fbot/src/Stage/worlds/pioneer.inc"
    "/home/luiz/ros2_fbot/src/Stage/worlds/sick.inc"
    "/home/luiz/ros2_fbot/src/Stage/worlds/ubot.inc"
    "/home/luiz/ros2_fbot/src/Stage/worlds/uoa_robotics_lab_models.inc"
    "/home/luiz/ros2_fbot/src/Stage/worlds/walle.inc"
    "/home/luiz/ros2_fbot/src/Stage/worlds/cfggen.sh"
    "/home/luiz/ros2_fbot/src/Stage/worlds/test.sh"
    "/home/luiz/ros2_fbot/src/Stage/worlds/worldgen.sh"
    )
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for each subdirectory.
  include("/home/luiz/ros2_fbot/build/Stage/worlds/benchmark/cmake_install.cmake")
  include("/home/luiz/ros2_fbot/build/Stage/worlds/bitmaps/cmake_install.cmake")
  include("/home/luiz/ros2_fbot/build/Stage/worlds/wifi/cmake_install.cmake")

endif()

