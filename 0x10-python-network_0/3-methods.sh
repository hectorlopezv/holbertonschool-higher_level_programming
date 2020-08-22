#!/bin/bash
#curl only methods
res=$(curl -is 0.0.0.0:5000/route_4 | awk '{if (NR == 3) print $0}');echo "${res[@]:7}"
