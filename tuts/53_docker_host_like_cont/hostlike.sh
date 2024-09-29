# Technique 12: A host-like container 
# Docker In Practice 2nd ed.

:'
Running a host-like image can be a good way to persuade Docker
refuseniks that Docker is useful. As they use it more, they’ll understand the
paradigm better and the microservices approach will make more sense to
them. At the company we introduced Docker into, we found that this mono-
lithic approach was a great way to move people from developing on dev serv-
ers and laptops to a more contained and manageable environment. From
there, moving Docker into testing, continuous integration, escrow, and
DevOps workflows was trivial.

This is considered bad form in parts of the Docker community. Containers are not
virtual machines—there are significant differences—and pretending there aren’t can
cause confusion and issues down the line.
For good or ill, this technique will show you how to run a host-like image and dis-
cuss some of the issues around doing this.

one of the more contentious areas of discussion within the
Docker community—running a host-like image, with multiple processes running from
the start.

Docker containers share an operating system with other Docker containers. In
contrast, VMs each have their own operating system managed by a hypervisor.

Docker containers are designed to run one principal process, not manage mul-
tiple sets of processes.

SOLUTION: Use a base container designed to run multiple processes.

For this technique you’re going to use an image designed to simulate a host, and
provision it with the applications you need. The base image will be the phusion/
baseimage Docker image, an image designed to run multiple processes.
The first steps are to start the image and jump into it with docker exec.

Although this can be useful in initial demos for engineers new to Docker or genuinely
useful for your particular circumstances, it’s worth being aware that it’s a somewhat
controversial idea.
The history of container use has tended toward using them to isolate workloads to
“one service per container.”

More recently, the growing popularity of both the Kubernetes’ pod and docker-
compose concepts has made the host-like container relatively redundant—separate
containers can be conjoined into a single entity at a higher level, rather than manag-
ing multiple processes using a traditional init service.
'

