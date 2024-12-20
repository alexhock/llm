#!/bin/bash
# fix git permissions on some machines
#git config --global --add safe.directory $1

#poetry config virtualenvs.in-project true
#poetry install --with dev -vv --no-ansi

# Configure git
#if ! git config user.name > /dev/null || ! git config user.email > /dev/null; then
#    echo "Git user name or email is not set."
#    echo "Please configure Git with your name and email:"
#    read -p "Enter your name: " user_name
#    git config user.name "$user_name"
#    read -p "Enter your email: " user_email
#    git config user.email "$user_email"
#fi
# Setup pre-commit
#poetry run pre-commit install

az extension add -n ml
