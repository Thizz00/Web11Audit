import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from axe_selenium_python import Axe

logger = logging.getLogger(__name__)


class AccessibilityAuditor:
    def __init__(self, url):
        self.url = url
        self.driver = None

    def _setup_driver(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--remote-debugging-port=9222")

        options.add_argument("--disable-gpu")

        self.driver = webdriver.Chrome(options=options)

    def _close_driver(self):
        if self.driver:
            self.driver.quit()

    def _run_axe(self):
        axe = Axe(self.driver)
        axe.inject()
        return axe.run()

    def audit_accessibility(self):
        logger.info(f"Starting accessibility audit for the page: {self.url}")
        self._setup_driver()
        try:
            self.driver.get(self.url)

            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.TAG_NAME, "body"))
            )

            logger.info("Page loaded, starting accessibility audit.")
            results = self._run_axe()
            logger.info("Accessibility audit completed.")
        except Exception as e:
            logger.error(f"Error loading the page: {e}")
            results = {"violations": []}
        finally:
            self._close_driver()

        return results
