import yaml
import sys
import pprint

with open(sys.argv[1], 'r') as f:
    pprint.pprint(yaml.safe_load(f))