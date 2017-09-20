.. _chapter_softwareSetup:

Software Setup
==============

To program a TurtleBot3 with Blockly some software packages must be installed. 
This section on software setup is also helpful for those who would like to create custom blocks to either add new funtionalities or modify the existing ones.

TurtleBot3 + Remote PC + Blockly
********************************

Before we begin the software setup let's understand, on a high level, how the three things are connected.Also note that TurtleBot3 and Remote PC should be connected to the same WiFi network.

**Remote PC**

A Desktop PC or Laptop a.k.a Remote PC should have ``Ubuntu 16.04`` and ``ROS Kinetic Kame`` installed. Remote PC will run ROS and be the ``ROS_MASTER``. 

**TurtleBot3**

TurtleBot3 runs a custom Linux version called ``Ubuntu Mate`` and will need its own `setup <http://turtlebot3.robotis.com/en/latest/pc_software.html>`_. Once TurtleBot3 is up and running ROS, it should connect to the Remote PC and recognize it as the ``ROS_MASTER``. 

**Blockly**

Now that the Remote PC and TurtleBot3 are connected, you need to setup Blockly software package and launch it. This way, using ROS, Blockly can send commands to TurtleBot3.

The steps below will help you install and launch Blockly on the Remote PC. They are adapted from the instructions provided by `Erle Robotics <http://erlerobotics.com/blog/>`_.


Installation
************

Linux
~~~~~

.. NOTE::
  TurtleBot3s are tested on ``Ubuntu 16.04`` and ``ROS Kinetic Kame``. So, these are two prerequisites to setup Blockly and work with a TurtleBot3.

Open terminal and enter the following instructions to install and develop Blockly.
::

    $ mkdir -p ~/blockly_ws/src
    $ cd ~/blockly_ws/src
    $ git clone https://github.com/dabit-industries/turtlebot3_blockly
    $ cd turtlebot3_blockly/frontend/
    $ git submodule add https://github.com/dabit-industries/ace-builds.git ace-builds
    $ git submodule init
    $ git submodule update
    $ git submodule add https://github.com/dabit-industries/blockly.git blockly
    $ git submodule init
    $ git submodule update
    $ cd ~/blockly_ws/
    $ catkin_make_isolated -j2 --pkg turtlebot3_blockly --install

**or**
::

    $ mkdir -p ~/blockly_ws/src
    $ cd ~/blockly_ws/src
    $ git clone --recurse-submodules https://github.com/dabit-industries/turtlebot3_blockly
    $ cd ~/blockly_ws
    $ catkin_make_isolated -j2 --pkg turtlebot3_blockly --install

