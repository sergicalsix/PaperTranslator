"""
Driver: https://chromedriver.chromium.org/downloads

実行速度が遅すぎてお蔵入り->ローカルのアプリを使用する方針に変更
"""
from selenium import webdriver  
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import pyperclip 
import time 
import datetime

# import tkinter as tk


URL = "https://www.deepl.com/translator"
input_selector = "#panelTranslateText > div.lmt__sides_container > div.lmt__sides_wrapper > section.lmt__side_container.lmt__side_container--source > div.lmt__textarea_container > div.lmt__inner_textarea_container > d-textarea > div > p"
output_selector = "#panelTranslateText > div.lmt__sides_container > div.lmt__sides_wrapper > section.lmt__side_container.lmt__side_container--target > div.lmt__textarea_container.lmt__raise_alternatives_placement > div.lmt__inner_textarea_container > d-textarea > div"



def remove_newline(text):
    cleaned_text = text.replace("\n", "")
    return cleaned_text

def save_trans_result(message, file_name=None):
    """
    message: str, ex. "Hello"
    file_name: str, ex. trans1.txt
    """
    driver = webdriver.Chrome()
    driver.get(URL)

    ### 原文(英語)の入力
    wait = WebDriverWait(driver, 15)
    input_element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, input_selector)))
    input_element.send_keys(message)

    ### 翻訳結果(日本語)の取得
    wait = WebDriverWait(driver, 15)
    element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, output_selector)))
    css_value = element.get_attribute("textContent")


    print(css_value)
    ## ファイル書き込み
    if file_name is None:
        file_name = datetime.datetime.now().strftime("%y%m%d") + '.txt'
    
    with open(file_name, "a") as f:
        f.write(css_value + "\n")
        
    time.sleep(1)

message = "改\n行 \n"#pyperclip.paste()
message = remove_newline(message)
save_trans_result(message)
    