.. _chapter_simpleCode:

A Simple Program
================

Let's write a simple program to make the TurtleBot3 do the following tasks consecutively:

1. Move forward for two seconds
2. Wait for one second
3. Move backward for three seconds
4. Wait for one second

Drag and drop blocks
*********************

Launch the Blockly web interface and ensure that TurtleBot3 is connected to the master (your pc/laptop).

On the left sidebar of the Blockly web interface you will find ``Dabit-Turtlebot3`` icon. Click on it and drag a ``Move_Forward`` block onto the workspace.


.. image:: _static/simpCode1.png


Our task is to move the TurtleBot3 for two seconds, so change the seconds field to ``2`` and let's run it at a **NORMAL** speed.


.. image:: _static/simpCode2.png


The following figure shows the remaining steps to complete the program.
You can find the ``Wait 1 seconds`` block inside the ``Control`` icon on the left sidebar.


.. image:: _static/simpCode.gif


Launch the program
******************

After writing the program you should launch it to make the TurtleBot3 move.
Click once on the ``Launch`` icon on the far left of the Blockly web interface and you should see TurtleBot3 perform the tasks consecutively.


.. image:: _static/launchCode.png

