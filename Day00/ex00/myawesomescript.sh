#!/bin/bash
curl -I -s $1 | grep "Location" | cut -d' ' -f2
