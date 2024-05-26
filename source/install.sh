#!/bin/bash
if ! mkdir core >/dev/null 2>&1
  then
    rm -rf core
    fi

mkdir core
cd core
git init
git clone https://github.com/calithos4136/PyCaliCore.git
cd PyCaliCore/
echo "Unpacking files"
if ! mv *.py ../ >/dev/null 2>&1
  then
    echo "Installation failed. Please make sure you are connected to the internet and have the latest version installed."
    cd ../../
    rm -rf core

else
  cd ../
  rm -rf PyCaliCore

  echo "Core files successfully installed."
fi