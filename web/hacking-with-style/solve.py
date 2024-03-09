import argparse
import os
import requests
import subprocess

parser = argparse.ArgumentParser()
parser.add_argument('--connection-info', default='http://localhost:8080')
args = parser.parse_args()

subprocess.run(["docker", "compose", "up", "--detach"], cwd=os.path.dirname(__file__))

# not actually a solve
requests.get(args.connection_info)

subprocess.run(["docker", "compose", "down"], cwd=os.path.dirname(__file__))
