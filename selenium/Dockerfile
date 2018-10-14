FROM selenium/standalone-firefox-debug:3.14.0-gallium

ENV SE_OPTS -role node -servlet org.openqa.grid.web.servlet.LifecycleServlet -registerCycle 0 -register false -port 4444

COPY start-selenium-standalone.sh /opt/bin/start-selenium-standalone.sh
