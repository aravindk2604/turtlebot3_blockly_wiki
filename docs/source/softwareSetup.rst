.. _chapter_softwareSetup:

Software Setup
==============

To use a TurtleBot3 with Blockly some software packages must be installed. 
This section on software setup is also necessary for those who would like to create custom blocks to either add new funtionalities or modify the existing ones.

The following steps were adapted from the instructions provided by `Erle Robotics <http://erlerobotics.com/blog/>`_.


Installation
************

Linux
~~~~~

.. NOTE::
  TurtleBot3s are tested on ``Ubuntu 16.04`` and ``ROS Kinetic Kame``. So, these are two prerequisites to setup Blockly and work on a TurtleBot3.

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

.. NOTE::
  There are submodules in this repo so ensure to update (pull, add. commit, push) them appropriately.
  
