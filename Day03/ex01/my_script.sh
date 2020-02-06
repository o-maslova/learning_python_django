#!/bin/bash
/usr/local/bin/python3 -m pip --version

if [[ ! -d "./local_lib" ]]
then
    mkdir "./local_lib"
fi

/usr/local/bin/python3 -m pip install --target=local_lib --upgrade git+https://github.com/jaraco/path.git > install.log