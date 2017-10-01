# turtlebot3_blockly_wiki
Wiki for TurtleBot3 control using Blockly.
Hosted on readthedocs: https://turtlebot-3-blockly-wiki.readthedocs.io/en/latest/
## Build
```
cd docs
sudo pip install -r requirements.txt
make html
```

## Test
```
xdg-open build/html/index.html
```

## Notes
- Using `_themes/sphinx_rtd_themes` for line-height of .highlight>pre element
