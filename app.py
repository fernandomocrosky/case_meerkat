from flask import Flask, jsonify
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

app = Flask(__name__)

@app.route('/scrap')
def index():
  options = Options()
  options.headless = True

  service = Service("./chromedriver.exe")
  driver = webdriver.Chrome(service=service, options=options)

  try:
    driver.get("http://www.bianca.com")
    element = driver.find_element(By.TAG_NAME, "h1")
    text = element.text
  finally:
    driver.quit()

  data = {
    "scrapped": text
  }
  return jsonify(data)


if __name__ == '__main__':
  app.run()