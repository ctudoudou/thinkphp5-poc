# ThinkPHP5 Remote Command Execution Vulnerability

ThinkPHP officially released an important security update on December 9, 2018, fixing a serious remote code execution vulnerability. Use this vulnerability to get the shell directly, the scope of influence: v5.1.0 < 5.1.31, and <= 5.0.23.

Upload two scripts here, one for batch detection scripts and one for an attack script.

# How to use

```shell
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt 
python batch_scan.py [options: -i] <input file root>
python attack.py [options: -u] <url>
```

