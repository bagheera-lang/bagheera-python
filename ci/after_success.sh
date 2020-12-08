#!/bin/bash

if [[ $TRAVIS_BRANCH == 'main'  && $TRAVIS_PULL_REQUEST == 'false' ]] ;
  then
    git config --global user.email "bumpversion-after-ci@example.com"
    git config --global user.name "Bumpversion after CI"
    bumpversion --tag --verbose patch
    chmod 600 travis_deploy_key
    eval `ssh-agent -s`
    ssh-add travis_deploy_key
    git config --global push.default simple
    git remote add deploy $(git remote -v | sed -nre 's#^origin.*https://([^/]*)/([^ ]*) *.*push.*#git@\1:\2#p')
    git push deploy HEAD:refs/heads/main
    python setup.py sdist bdist_wheel
    pip3 install twine
    twine upload --config-file .pypirc-bot dist/*
else
  echo "Skipped because not main"
fi
