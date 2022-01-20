from selenium.common.exceptions import ElementNotVisibleException, ElementNotSelectableException, \
    NoSuchElementException
from selenium.webdriver import Opera
from selenium.webdriver.opera.options import Options
from selenium.webdriver.opera.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

from tkinter import Tk

from time import sleep


def reload_page(page):
    print('Caja inactiva')


new_options = Options()
driver: WebDriver = Opera(executable_path=r'C:/Users/Benjamin/Documents/operadriver/operadriver.exe',
                          options=new_options)

wait = WebDriverWait(driver, 20, poll_frequency=1,
                     ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException,
                                         NoSuchElementException])
driver.maximize_window()

locations = [
    "25°04\'03.63\"N 107°40\'05.61\"W",
    "25°19\'22.10\"N 107°27\'09.34\"W",
    "25°19\'21.20\"N 107°27\'18.88\"W",
    "25°19\'23.31\"N 107°27\'15.86\"W",
    "25°19\'18.35\"N 107°27\'11.27\"W",
    "25°19\'27.10\"N 107°27\'07.12\"W",
    "25°14\'48.97\"N 107°26\'32.90\"W",
    "25°14\'50.85\"N 107°26\'30.84\"W",
    "25°14\'36.80\"N 107°26\'16.19\"W",
    "25°14\'35.74\"N 107°26\'20.55\"W",
    "25°14\'46.78\"N 107°26\'32.66\"W",
    "25°14\'48.20\"N 107°26\'24.72\"W",
    "25°14\'46.78\"N 107°26\'23.97\"W",
    "25°14\'40.70\"N 107°26\'26.84\"W",
    "25°14\'47.71\"N 107°26\'26.02\"W",
    "25°14\'34.70\"N 107°26\'17.29\"W",
    "25°14\'46.21\"N 107°26\'28.66\"W",
    "25°14\'54.20\"N 107°26\'27.64\"W",
    "25°21\'08.50\"N 107°33\'19.10\"W",
    "25°18\'39.29\"N 107°22\'14.86\"W",
    "25°18\'42.22\"N 107°22\'16.13\"W",
    "25°18\'40.27\"N 107°22\'15.75\"W",
    "25°18\'42.95\"N 107°22\'16.62\"W",
    "25°18\'37.22\"N 107°22\'13.32\"W",
    "25°18\'36.46\"N 107°22\'16.98\"W",
    "25°18\'34.03\"N 107°22\'16.38\"W",
    "25°18\'38.24\"N 107°22\'17.79\"W",
    "25°17\'38.95\"N 107°21\'09.09\"W",
    "25°17\'37.95\"N 107°21\'13.02\"W",
    "25°17\'34.77\"N 107°21\'04.81\"W",
    "25°17\'26.03\"N 107°21\'07.86\"W",
    "25°17\'31.42\"N 107°21\'06.12\"W",
    "25°17\'37.19\"N 107°21\'08.53\"W",
    "25°17\'37.61\"N 107°21\'08.44\"W",
    "25°17\'29.44\"N 107°21\'13.84\"W",
    "25°17\'35.13\"N 107°21\'09.80\"W",
    "25°18\'14.98´´N 107°21\'36.60\"W",
    "25°17\'32.57\"N 107°21\'07.13\"W",
    "25°17\'36.36\"N 107°21\'11.46\"W",
    "25°17\'27.41\"N 107°21\'12.36\"W",
    "25°17\'36.96\"N 107°21\'09.46\"W",
    "25°17\'32.94\"N 107°21\'06.99\"W",
    "25°17\'37.34\"N 107°21\'09.44\"W",
    "25°17\'26.26\"N 107°21\'06.82\"W",
    "25°17\'30.29\"N 107°21\'08.77\"W",
    "25°17\'31.29\"N 107°21\'07.48\"W",
    "25°13\'52.54\"N 107°20\'00.23\"W",
    "25°20\'23.06\"N 107°23\'07.22\"W",
    "25°20\'24.12\"N 107°23\'06.58\"W",
    "25°20\'21.37\"N 107°23\'04.16\"W",
    "25°19\'53.57\"N 107°19\'55.70\"W",
    "25°23\'27.15\"N 107°20\'16.95\"W",
    "25°23\'03.36\"N 107°20\'00.60\"W",
    "25°23\'21.53\"N 107°20\'16.55\"W",
    "25°23\'12.50\"N 107°20\'23.78\"W",
    "25°23\'20.77\"N 107°20\'16.90\"W",
    "25°24\'05.87\"N 107°18\'18.21\"W",
    "25°24\'05.62\"N 107°18\'16.27\"W",
    "25°24\'22.28\"N 107°16\'06.71\"W",
    "25°21\'10.01\"N 107°33\'14.72\"W",
    "25°21\'48.82\"N 107°33\'14.57\"W",
    "25°21\'36.14\"N 107°32\'42.41\"W",
    "25°21\'37.00\"N 107°33\'4.83\"W",
    "25°20\'53.05\"N 107°33\'6.77\"W",
    "25°20\'53.17\"N 107°33\'8.08\"W",
    "25°20\'53.15\"N 107°33\'7.24\"W",
    "25°20\'56.91\"N 107°33\'14.10\"W",
    "25°22\'6.08\"N 107°33\'6.00\"W",
    "25°31´19.01\"N 107°27\'28.54\"W",
    "25°20\'53.21\"N 107°33\'8.66\"W",
    "25°21\'0.92\"N 107°33\'10.48\"W",
    "25°21\'40.35\"N 107°33\'17.60\"W",
    "25°19\'53.35\"N 107°27\'27.03\"W",
    "25°21\'55.06\"N 107°33\'14.91\"W",
    "25°21\'54.80\"N 107°33\'15.06\"W",
    "25°20\'48.55\"N 107°33\'37.76\"W",
    "25°35\'32.73\"N 107°34\'33.17\"W",
    "25°35\'33.62\"N 107°34\'34.68\"W",
    "25°37\'12.96\"N 107°31\'51.43\"W",
    "25°37\'07.96\"N 107°32\'50.24\"W",
    "25°37\'09.85\"N 107°31\'55.98\"W",
    "25°37\'06.94\"N 107°31\'50.48\"W",
    "25°37\'18.52\"N 107°31\'44.47\"W",
    "25°37\'15.23\"N 107°31\'44.16\"W",
    "25°37\'03.14\"N 107°31\'45.98\"W",
    "25°37\'08.84\"N 107°31\'55.24\"W",
    "25°48\'30.11\"N 107°33\'03.08\"W",
    "25°48\'31.91\"N 107°33\'03.31\"W",
    "25°48\'25.13\"N 107°11\'17.28\"W",
    "24°52\'46.9\"N 107°21\'26.9\"W",
    "24°51\'16.1\"N 107°22\'13.3\"W",
    "24°51\'03.7\"N 107°22\'16.1\"W",
    "24°51\'13.1\"N 107°22\'19.3\"W",
    "24°52\'47.1\"N 107°21\'27.5\"W",
    "24°52\'47.6\"N 107°21\'27.0\"W",
    "24°52\'46.9\"N 107°21\'26.9\"W",
    "24°52\'46.60\"N 107°21\'26.9\"W",
    "24°50\'54.7\"N 107°22\'15.6\"W",
    "24°52\'47.1\"N 107°21\'27.5\"W",
    "25°17\'28.07\"N 107°21\'3.80\"W",
    "25°28\'5.29\"N 107°37\'9.57\"W",

]

for location in locations:
    if location != "":
        driver.get('https://www.google.com/maps/place/' + location)
        sleep(4)
        ActionChains(driver).move_by_offset(200, 450).click().perform()
        ActionChains(driver).move_by_offset(-200, -450).perform()

        Direction = Tk().clipboard_get()
        sleep(1)
        print(Direction)
    else:
        print("---no data---")
