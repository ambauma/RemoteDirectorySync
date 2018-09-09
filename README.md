# RemoteDirectorySync
A utility to synchronize directories across a local network.

## Usage
TBD

## Development

### Virtual Enviornment
```bash
python3 -m venv rdsEnv
source rdsEnv/bin/activate
pip install pytest-cov
pip instal pylint
```

### Build
Run `setup.py sdist`

### Test
Run `python -m pytest --cov=rds --cov-fail-under=80 tests/ && coverage html`