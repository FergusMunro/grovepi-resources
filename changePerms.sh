#!/bin/bash

find ~/Desktop/ -name '*idle*' -type f -exec sed -i '/^exec.*idle/s/idle/sudo idle/' "$1" '{}' ';'
