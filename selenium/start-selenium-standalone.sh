#!/usr/bin/env bash

java ${JAVA_OPTS} -jar /opt/selenium/selenium-server-standalone.jar \
    ${SE_OPTS}

test -e /run/supervisor/supervisord.pid && kill -15 `cat /run/supervisor/supervisord.pid`
