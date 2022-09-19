# Pitchy
A small python script that allows you to register input with the pitch of a sound.


## Installation

Clone and use the package manager pip to install required packages.

```bash 
git clone https://github.com/elvodqa/pitchy
cd pitchy
pip install -r requirements.txt
```

## Usage

```bash 
python pitchy.py
```

### Setting up config

Setting up a config is really easy. For example, adding option to press K between 100 and 1000 pitch values is

```json
{
    "key_map": [
        {
            "key": "K",
            "min": 100,
            "max": 1000    
        }
    ]    
}
```


