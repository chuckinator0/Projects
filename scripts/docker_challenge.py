# when you type the id of a docker container into a command like `docker exec` you can
# type just the "prefix" characters needed to uniquely identify the container name
# Challenge: write a function that takes a list of container ids and outputs the prefixes that
# would uniquely identify the an id in the list.

import sys

if not sys.stdin.isatty():
    # grab the list of containers from stdin
    # so you can use it from the command line like this:
    # docker ps -q | python3 docker_challenge.py
    containers = [line.strip() for line in sys.stdin]
else:
    # otherwise work with some test data
    containers = """870722647a89
18b334a69107
20300970f718
33a36ed98893
4595e8c0af01
5630d965b560
c1db502f346f
ab9e3f0c7bcc
af5409903166
4e94d97aff29
497860baeb29
60e26dc5c030
3be3920d68ca
ba7c80d50c82
bebdfc3c89b5
b370906111d7
702747cdef13
4877be1b8a0b
46d83135806a
99c60a9a1e44
97c3f19c63b2
thisisapreaa
thisisaprebb""".split("\n")

# assuming all container ids are the same length
if not containers or not all([len(c)==len(containers[0]) for c in containers]):
    print("expecting container ids lenths to be the same")
    sys.exit(1)

pos = 0
while len(containers) > 0:
    prefix_unique = {}
    # find which prefixes of length pos are unique
    for container in containers:
        prefix = container[:pos+1]
        if prefix in prefix_unique:
            prefix_unique[prefix] = False
        else:
            prefix_unique[prefix] = True

    # print and remove containers that have a unique prefix of length pos
    for container in containers.copy():
        for prefix in prefix_unique:
            if prefix_unique[prefix] and container.startswith(prefix):
                print(container[:pos+1], container)
                containers.remove(container)

    pos = pos + 1
