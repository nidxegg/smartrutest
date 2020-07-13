# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestCheckname():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def wait_for_window(self, timeout = 2):
    time.sleep(round(timeout / 1000))
    wh_now = self.driver.window_handles
    wh_then = self.vars["window_handles"]
    if len(wh_now) > len(wh_then):
      return set(wh_now).difference(set(wh_then)).pop()
  
  def test_checkname(self):
    """Переход должен быть на https://www.avtodispetcher.ru/distance/"""
    self.driver.get("https://yandex.kz/")
    self.driver.find_element(By.ID, "text").click()
    self.driver.find_element(By.ID, "text").send_keys("расчет расстояний между городами ")
    self.driver.find_element(By.CSS_SELECTOR, ".mini-suggest__button").click()
    self.vars["window_handles"] = self.driver.window_handles
    self.driver.find_element(By.LINK_TEXT,"Расчет расстояний между городами").click()
    window_name = self.driver.window_handles[1]    
    self.driver.switch_to.window(window_name)
    time.sleep(5)
    assert self.driver.current_url == 'https://www.avtodis1petcher.ru/distance/',  'Не верный адрес перехода'  


  def test_record(self):
    self.driver.get("https://www.avtodispetcher.ru/distance/")
    element=self.driver.find_element(By.CSS_SELECTOR, ".submit_button > input")
    element.location_once_scrolled_into_view
    self.driver.find_element(By.NAME, "from").send_keys("Тула")
    self.driver.find_element(By.NAME, "to").send_keys("Санкт-Петербург")
    self.driver.find_element(By.NAME, "fc").clear()
    self.driver.find_element(By.NAME, "fc").send_keys("9")
    self.driver.find_element(By.NAME, "fp").clear()
    self.driver.find_element(By.NAME, "fp").send_keys("46")    
    target = self.driver.find_element(By.CSS_SELECTOR, ".submit_button > input")
    target.location_once_scrolled_into_view
    self.driver.find_element(By.CSS_SELECTOR, ".submit_button > input").click()
    
    
    time.sleep(2)
    range_path = self.driver.find_element_by_xpath('//*[@id="totalDistance"]').text
    assert int(range_path) == 897, 'не верный километраж'
    s = self.driver.find_element_by_xpath('//*[@id="summaryContainer"]/form/p').text
    word_list = s.split()
    num_list = []

    for word in word_list:
        if word.isnumeric():
            num_list.append(int(word))

    assert num_list[-1] == 31726, 'не верная стоимость'
    time.sleep(1)

  
  def test_changeCity(self):
    self.driver.get("https://www.avtodispetcher.ru/distance/?from=%D0%A2%D1%83%D0%BB%D0%B0&to=%D0%A1%D0%B0%D0%BD%D0%BA%D1%82-%D0%9F%D0%B5%D1%82%D0%B5%D1%80%D0%B1%D1%83%D1%80%D0%B3&v=&vt=car&rm=110&rp=90&rs=60&ru=40&fc=9&fp=46&ov=&atn=&aup=&atr=&afd=&ab=&acb=")
    time.sleep(2)
    target =  self.driver.find_element(By.CSS_SELECTOR, ".anchor")
    target.location_once_scrolled_into_view
    self.driver.find_element(By.CSS_SELECTOR, ".anchor").click()
    self.driver.find_element(By.NAME, "v").send_keys("Великий Новгород")
    target =  self.driver.find_element(By.CSS_SELECTOR, ".submit_button > input")
    target.location_once_scrolled_into_view
    self.driver.find_element(By.CSS_SELECTOR, ".submit_button > input").click()
    
    time.sleep(20)
    target =  self.driver.find_element(By.CSS_SELECTOR, "p > input:nth-child(4)")
    target.location_once_scrolled_into_view
    self.driver.find_element(By.CSS_SELECTOR, "p > input:nth-child(4)").click()
    time.sleep(5)
    range_path = self.driver.find_element_by_xpath('//*[@id="totalDistance"]').text
    assert int(range_path) == 966, 'не верный километраж'
    s = self.driver.find_element_by_xpath('//*[@id="summaryContainer"]/form/p').text
    word_list = s.split()
    num_list = []

    for word in word_list:
        if word.isnumeric():
            num_list.append(int(word))

    assert num_list[-1] == 41002, 'не верная стоимость'
    time.sleep(1)

