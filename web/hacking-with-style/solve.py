import argparse
import os
import requests
import subprocess
import time

parser = argparse.ArgumentParser()
parser.add_argument('--connection-info', default='http://localhost:8080')
args = parser.parse_args()

subprocess.run(["docker", "compose", "up", "--detach"], cwd=os.path.dirname(__file__))
time.sleep(5)

# not actually a solve
requests.get(args.connection_info)

subprocess.run(["docker", "compose", "down"], cwd=os.path.dirname(__file__))
