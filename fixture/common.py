from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import random
import string


def wait_for(wd, element, value, timeout=5):
    wait = WebDriverWait(wd, timeout)
    return wait.until(EC.presence_of_element_located((element, value)))


def wait_for_elements(wd, element, value, timeout=5):
    wait = WebDriverWait(wd, timeout)
    return wait.until(EC.presence_of_all_elements_located((element, value)))


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " " * 10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(1, maxlen))])
