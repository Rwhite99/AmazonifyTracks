from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Grabs Liked song file
LIKED_SONG_FILE = r"ADD FILE LOCATION FOR SONGS HERE"


def fetch_liked_songs():
    with open(LIKED_SONG_FILE, "r", encoding="utf-8") as file:
        return [line.strip() for line in file.readlines()]


def search_and_add_song(driver, song):
    try:
        # Wait for the Search Bar to be clickable
        search_box = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@type='search']"))
        )

        # Clear Search Bar and enter Song
        search_box.send_keys(Keys.CONTROL + "a" )
        search_box.send_keys(Keys.DELETE)
        search_box.clear()
        search_box.send_keys(song)
        time.sleep(2)
        search_box.send_keys(Keys.RETURN)
        print(f"Searching for: {song}")

        # Wait for Search results to load
        first_song = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "music-horizontal-item"))
        )

        # Hover over the Song Section
        actions = ActionChains(driver)
        actions.move_to_element(first_song).perform()

        # Wait for Add button to appear

        add_button = WebDriverWait(first_song, 3).until(
            EC.element_to_be_clickable((
                By.XPATH,
                ".//music-button[@icon-name='more' and @role='button']"
            ))
        )

        # click the Add button
        add_button.click()

        play_list_button = WebDriverWait(add_button, 15).until(
            EC.element_to_be_clickable((
                By.XPATH,
                "//music-list-item[@primary-text='Add to Playlist']"
            ))
        )

        # click playlist button
        play_list_button.click()

        # add to liked songs
        liked_songs_button = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((
                By.XPATH,
                "//music-link[@title='My Likes']"
            ))
        )

        # click My likes
        liked_songs_button.click()
        print(f"added: {song}")

    except Exception as e:
        print (f"failed to add {song}: {e}")


def main():
    driver = webdriver.Chrome()

    try:
        # navigate to Amazon Music and login
        driver.get("https://music.amazon.com")
        input("Log in to Amazon Music and Press enter to continue...")

        # Load Liked Songs
        liked_songs = fetch_liked_songs()

        # Add each Song to My Music
        for song in liked_songs:
            print(f"Processing: {song}")
            search_and_add_song(driver, song)
    finally:
        driver.quit()


if __name__ == "__main__":
    main()