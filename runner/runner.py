import click
import click_log
import logging
import os
import time
from urllib3.exceptions import HTTPError
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

logger = logging.getLogger(__name__)

click_log.basic_config(logger)

@click.command()
@click_log.simple_verbosity_option(logger)
def main():
    base_url = 'http://{0}:{1}'.format(
        os.environ['HUB_HOST'],
        os.environ['HUB_PORT'])
    hub_url = '{0}/wd/hub'.format(base_url)

    logger.info('Connecting to selenium: %s ...', hub_url)
    for try_num in range(30):
        if try_num > 1:
            logger.debug('Connecting to selenium: %s (try %n)', hub_url, try_num)
        try:
            driver = webdriver.Remote(command_executor=hub_url,
                    desired_capabilities=DesiredCapabilities.FIREFOX)
            break
        except HTTPError as e:
            logger.debug('Failed to connect: %s', e)
            pass
        time.sleep(1)

    if not driver:
        raise HTTPError

    logger.info('Connected to selenium: %s', hub_url)

    run(driver)

    driver.quit()

    time.sleep(1)

    try:
        import urllib3
        urllib3.PoolManager().request('GET', '{0}/extra/LifecycleServlet?action=shutdown'.format(base_url))
    except:
        logger.debug('Failed to shutdown selenium', exc_info=True)
        pass

def run(driver):
    driver.get("http://www.python.org")
    assert "Python" in driver.title
    elem = driver.find_element_by_name("q")
    elem.clear()
    elem.send_keys("pycon")
    elem.send_keys(Keys.RETURN)
    assert "No results found." not in driver.page_source
    logger.debug('Content: %s', driver.page_source)

if __name__ == '__main__':
    main()
