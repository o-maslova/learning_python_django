#!/bin/bash
echo "PIP VERSION"
python3 -m pip --version
echo -e
if [[ ! -d "./local_lib" ]]
then
    mkdir "./local_lib"
fi

/usr/local/bin/python3 -m pip install -q --target=local_lib --log install.log --upgrade git+https://github.com/jaraco/path.git
echo -e
echo "----my_program.py----"
python3 my_program.py