Selenium One-Shot
=================

A simplified approach to running Selenium for one-shot scripts/tools in
containers.

Install
=======

    git clone https://github.com/jflemer/selenium-oneshot.git

Build
=====

    ./build.sh

Run
===

    ./docker-compose up

Customize
=========

    vim runner/runner.py
    ./build.sh && ./docker-compose up
