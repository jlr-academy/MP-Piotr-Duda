#!/bin/bash
set -eu

project_dir="C:\Users\pduda1\OneDrive\OneDrive - JAGUAR LAND ROVER\Documents\course\MP-Piotr-Duda"

if [[ $(pwd) != ${project_dir} ]];
then
    echo -e "Not in project directory.Changing directory to ${project_dir}\n"
    cd ${project_dir}
fi

if pytest;
then
    git commit -am "${1}"
fi