.. _chapter_blockCreation:

Block Creation
==============

By now you have an idea that ``blocks`` are the fundamental elements in this drag and drop Blockly sofware. We will discuss how to create new blocks and/or to edit the existing ones.

This guide is adapted from Erle Robotics documentation on Block Creation and we focus on the block creation pertaining to Turtlebot3's functionalities.

Understanding the file structure
********************************

First let's get into the **blockly/** directory
::

    $ cd turtlebot3_blockly/frontend/blockly/

.. NOTE::
  ``blockly`` was one of the submodules we cloned during the software setup.

The directories **blocks/** and **generators/** contain a few files that we must edit.
We can start with the python script that is the backend of the blocks. Let's look into the **generators/python/scripts/turtlebot3/**  directory.
::

    $ cd generators/python/scripts/turtlebot3/

Each block that you see on the Blockly web interface has its own python script that provides the block's functionality. This directory should contain a few python scripts already. We'll go over the ``move_forward.py`` script.

.. literalinclude:: pyfiles/move_forward.py
    :linenos:
    :language: python
