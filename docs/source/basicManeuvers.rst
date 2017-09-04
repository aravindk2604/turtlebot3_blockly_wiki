.. _chapter_basicManeuvers:

Basic Maneuvers
===============

How to make the Turtlebot3 do basic actions like moving forward, backward, turning right, left and stop?

It's quite simple in Blockly. You should use the appropriate block from the list of blocks available. Let's look at each of the basic actions and program the Turtlebot3 to move accordingly. 

Moving Forward
**************

.. image:: ystatic/mv_frwd.png


This block makes the turtlebot3 move forward in three preset speed values - **SLOW**, **NORMAL** and **FAST**. Behind this block is a short code in Python language that talks to the robot from this Blockly web interface and commands it to move forward with one of the preset values as programmed by the user. A GIF shows how the block is dragged into the workspace (intuitive) and changing the preset speed values. 


.. image:: ystatic/fwd_mv.gif


The other basic maneuver blocks of the turtlebot3 are shown below along with the GIFs.

Moving Backward
***************

.. image:: ystatic/mv_bk.png


.. image:: ystatic/bk_mv.gif



Turning Right
*************

.. image:: ystatic/right.png


.. image:: ystatic/right_turn.gif


Turning Left
************

.. image:: ystatic/left.png


.. image:: ystatic/left_turn.gif


Turn Left/Right in degrees
**************************

All the above commands move the Turtlebot3 with a preset amount of time. To turn the Turtlebot3 accurately you can use the **Turn Left/Right __ degrees** command. Left turn is counter-clockwise and right turn is clockwise direction. This block uses the data from an Inertial Measurement Unit (IMU) sensor. Hence the accurate turn with 1 degree resolution.

.. image:: ystatic/turn_lr_degrees.png


.. image:: ystatic/turn_lr_deg.gif



Stop
****

.. image:: ystatic/stop.png


.. image:: ystatic/stop_block.gif




