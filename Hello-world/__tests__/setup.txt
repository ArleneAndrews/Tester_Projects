const { Builder, By, Key, until } = require('selenium-webdriver')
require('selenium-webdriver/chrome')
require('selenium-webdriver/firefox')
require('chromedriver')
require('geckodriver')

const rootURL = 'https://www.iceyarns.com/'
const d = new Builder().forBrowser('firefox').build()
const waitUntilTime = 20000
let driver, el, actual, expected
jasmine.DEFAULT_TIMEOUT_INTERVAL = 1000 * 60 * 5

async function getElementById(id) {
  const el = await driver.wait(until.elementLocated(By.id(id)), waitUntilTime)
  return await driver.wait(until.elementIsVisible(el), waitUntilTime)
}
async function getElementByXPath(xpath) {
  const el = await driver.wait(until.elementLocated(By.xpath(xpath)), waitUntilTime)
  return await driver.wait(until.elementIsVisible(el), waitUntilTime)
}


beforeEach((done) => {
    driver.quit();
  driver = new Builder().forBrowser('chrome').build();

  driver.get(rootURL).then(done);
});


afterEach((done) => {
  driver.quit().then(done);
});