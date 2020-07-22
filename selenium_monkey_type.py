from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
import time


def main():
    # Global driver prevents the window from closing after main() runs
    global driver
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)
    driver.get('https://monkey-type.com/')

    try:
        # Wait to load
        aWord = wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, 'word'))
        )

        words = wait.until(
            EC.presence_of_element_located((By.ID, 'words'))
        )

        # Begin looping
        i = 0
        while(words.get_attribute('class') != 'hidden'):
            print('*** ITERATION {} ***'.format(i))
            actions = ActionChains(driver)

            word_arr = words.find_elements_by_class_name('word')

            for word_elem in word_arr[60 * i:]:

                # Construct word
                letter_arr = word_elem.find_elements_by_tag_name('letter')
                for letter_elem in letter_arr:
                    letter_to_type = letter_elem.get_attribute('innerHTML')
                    actions.send_keys(letter_to_type)

                # Type word
                actions.send_keys(' ')

            actions.perform()
            # time.sleep(10)
            i += 1

    except TimeoutException:
        print("Timed out")

    except:
        print("Done")
        result = wait.until(
            EC.presence_of_element_located((By.ID, 'result'))
        )

        wpm = result.find_element_by_class_name('wpm')
        wpm_text = wpm.find_element_by_class_name('bottom')
        print("{} WPM".format(wpm_text.get_attribute('innerHTML')))


if __name__ == '__main__':
    main()
