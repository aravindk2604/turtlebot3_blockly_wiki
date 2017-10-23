# turtlebot3_blockly_wiki
Wiki for TurtleBot3 control using Blockly.
Hosted on readthedocs: https://turtlebot-3-blockly-wiki.readthedocs.io/en/latest/
## Build (Instructions for the wiki)
```
cd docs
sudo pip install -r requirements.txt
make html
```

## Test (Instructions for the wiki)
```
xdg-open build/html/index.html
```


# Quickstart instructions for TurtleBot3 + Blockly interface
Follow the instructions below after cloning the wiki repo
```
cd ~/turtlebot3_blockly_wiki/
mkdir tb3_blockly
cd tb3_blockly/ 
wstool init src ~/turtlebot3_blockly_wiki/.rosinstall
catkin_make
```

# Launch TurtleBot3 + Blockly
```
source devel/setup.bash
roslaunch turtlebot3_blockly turtlebot3_blockly.launch
```



## Notes
- Using `_themes/sphinx_rtd_themes` for line-height of .highlight>pre element
