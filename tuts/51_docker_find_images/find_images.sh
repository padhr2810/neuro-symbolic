# Based on Technique 10: Find and Run a Docker Image

:'
Let’s say you’re interested in playing with Node.js. In the following example we
searched for images matching “node” with the docker search command:
'

docker search node


:'
Once you’ve chosen an image, you can download it by performing a docker pull
command on the name
'

docker pull node

:'
The -t flag creates a TTY
device (a terminal) for you, and the -i flag specifies that this Docker session is interactive
'

docker run -t -i node /bin/bash
process.version
