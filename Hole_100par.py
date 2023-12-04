from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import pyautogui
from PIL import ImageGrab

def take_screenshot(file_path):
    # デスクトップ全体のスクリーンショットを取得
    screenshot = ImageGrab.grab()
    
    # スクリーンショットを保存
    screenshot.save(file_path)

def process_link(driver, link):

    try:
        # ウェブページごとの処理をここで記述
        driver.get(link)

        if "chofu-bunka" in link:
            click_coordinates = [
                (850, 450),
                (980, 300),
                #ホール選択
                (800, 480),
                (955, 405),
                #日付選択
                (794, 633),
                (783, 915),
                (903, 636),
                (892, 652),

                (1104, 672),
                (1171, 673),
                (900, 738),
            ]
            # 1つ目のウェブページの処理（例：タイトルを表示）
            for coordinates in click_coordinates:
                # クリック後に少し待つ（必要に応じて調整）
                time.sleep(1.5)
                # 指定された座標に移動して左クリック
                pyautogui.click(coordinates[0], coordinates[1])
            
            # スクリーンショットを保存するファイルのパスを指定してください
            file_path1 = "result/chofu-bunka12.png"

            time.sleep(2)
            # スクリーンショットを取得して保存
            take_screenshot(file_path1)   

            #11月分
            time.sleep(1.2)
            pyautogui.click(700,650)
            file_path2 = "result/chofu-bunka11.png"
            time.sleep(2)
            take_screenshot(file_path2)   



        elif "itabashi-shisetsu" in link:
            click_coordinates = [
                (1350, 210),
                (1200, 770),
                (700, 400),
                (286, 391),
                (286, 391),
                (286, 341),
                (286, 341),
                (1800, 200),
                (400, 484),

                # (903, 636),
                # (892, 652),
                #　月日選択
                (376, 438),
                (361, 724),
                (441, 435),
                (426, 463),

                (290, 540),
                (370, 540),
                (450, 540),
                (550, 540),
                (630, 540),

                (678,450),
                (800,450)
            ]
            # 1つ目のウェブページの処理（例：タイトルを表示）
            for coordinates in click_coordinates:
                # クリック後に少し待つ（必要に応じて調整）
                time.sleep(1.5)
                # 指定された座標に移動して左クリック
                pyautogui.click(coordinates[0], coordinates[1])

            # ページを下にスクロール
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            
            # スクリーンショットを保存するファイルのパスを指定してください
            file_path = "result/itabashi-bunka.png"

            time.sleep(1)
            # スクリーンショットを取得して保存
            take_screenshot(file_path)  


        elif "suginamikoukaidou" in link:
            click_coordinates1 = [
            
                (864, 750),
                (906, 750),
                (946, 750),
                (989, 750),
                (1032, 750),

                (950, 723),
                (920, 665),
                (960, 780),
            ]
            # 1つ目のウェブページの処理（例：タイトルを表示）
            for coordinates in click_coordinates1:
                # クリック後に少し待つ（必要に応じて調整）
                time.sleep(0.5)
                # 指定された座標に移動して左クリック
                pyautogui.click(coordinates[0], coordinates[1])
            
            # スクリーンショットを保存するファイルのパスを指定してください
            file_path1 = "result/suginamikoukaidou12.png"

            time.sleep(1)
            # スクリーンショットを取得して保存
            take_screenshot(file_path1)   

            #11月分

            click_coordinates2 = [
            
                (1259, 507),
                (1104, 776),
                (988, 571),
            ]
            # 1つ目のウェブページの処理（例：タイトルを表示）
            for coordinates in click_coordinates2:
                # クリック後に少し待つ（必要に応じて調整）
                time.sleep(0.5)
                # 指定された座標に移動して左クリック
                pyautogui.click(coordinates[0], coordinates[1])
            
            # スクリーンショットを保存するファイルのパスを指定してください
            file_path2 = "result/suginamikoukaidou11.png"

            time.sleep(1)
            # スクリーンショットを取得して保存
            take_screenshot(file_path2)   


        elif "nerima" in link:
            click_coordinates = [
            
                (700, 350),
                (750, 600),
                (1200, 545),
                (800, 300),
                (700, 375),
                (700, 300),
                
                #カレンダー　移行
                (1200, 350),
                (1200, 350),
                (1100, 350),
                (1100, 350),
                (1100, 350),
                (1100, 350),
                (1100, 350),

                # 曜日
                (812, 738),
                (1220, 742),
                (963, 876),
                (684, 544),
                

            ]

            click_count_threshold1 = 3  # 待機を追加する回数の閾値
            click_count_threshold2 = 7  # 待機を追加する回数の閾値

            # 1つ目のウェブページの処理（例：タイトルを表示）
            for click_count, coordinates in enumerate(click_coordinates, start=1):
                # クリック後に少し待つ（必要に応じて調整）
                time.sleep(1.5)
                # 指定された座標に移動して左クリック
                pyautogui.click(coordinates[0], coordinates[1])
                # 特定の回数目のときだけ待機
                if click_count ==  click_count_threshold1  or click_count ==  click_count_threshold2 :
                    time.sleep(2.5)  # 待機時間を適宜調整
            
            # スクリーンショットを保存するファイルのパスを指定してください
            file_path1 = "result/nerima11.png"

            time.sleep(1)
            # スクリーンショットを取得して保存
            take_screenshot(file_path1)   

            #12月分
            time.sleep(1)
            pyautogui.click(1108, 337)
            file_path2 = "result/nerima12.png"
            time.sleep(1)
            take_screenshot(file_path2)   

        elif "nakano" in link:
            click_coordinates = [
                (567, 535),
                (1152,292),
                (964, 778),
                (1098, 292),
                (976, 770),
                (790, 606),
                (707, 359),
                (950, 782),
                (1083, 287),
                (949, 776),

                # カレンダー
                (1300, 256),
                (805, 646),
                (1225, 649),
                (641,361),
                (951,790),
                (720,769),
        
            ]

            # 1つ目のウェブページの処理（例：タイトルを表示）
            for click_count, coordinates in enumerate(click_coordinates, start=1):
                # クリック後に少し待つ（必要に応じて調整）
                time.sleep(1)
                # 指定された座標に移動して左クリック
                pyautogui.click(coordinates[0], coordinates[1])
                # 特定の回数目のときだけ待機
                if click_count == 10:
                    time.sleep(2.5)  # 待機時間を適宜調整
            
            # スクリーンショットを保存するファイルのパスを指定してください
            file_path1 = "result/nakanoZERO12.png"

            time.sleep(2)
            # スクリーンショットを取得して保存
            take_screenshot(file_path1)   

            #11月分
            time.sleep(1)
            pyautogui.click(711,250)
            file_path2 = "result/nakanoZERO11.png"
            time.sleep(2)
            take_screenshot(file_path2)   

        elif "nishitokyo" in link:
            click_coordinates = [
                (780, 525),
                (963, 429),
                (820, 622),
                (1187, 415),
                (797, 740),
                (785, 704),
                (900, 733),
                (882, 406),
                (1105, 776),
                (1170, 781),
                (900, 850),

            ]
            # 1つ目のウェブページの処理（例：タイトルを表示）
            for click_count, coordinates in enumerate(click_coordinates, start=1):
                # クリック後に少し待つ（必要に応じて調整）
                time.sleep(1.2)
                # 指定された座標に移動して左クリック
                pyautogui.click(coordinates[0], coordinates[1])
                # 特定の回数目のときだけ待機
                if click_count == 2:
                    time.sleep(2.5)  # 待機時間を適宜調整
            
            # スクリーンショットを保存するファイルのパスを指定してください

            file_path1 = "result/komorebiGRAFARE12.png"

            time.sleep(2)
            # スクリーンショットを取得して保存
            take_screenshot(file_path1)   

            #11月分
            time.sleep(1)
            pyautogui.click(610,676)
            file_path2 = "result/komorebiGRAFAR11.png"
            time.sleep(2)
            take_screenshot(file_path2)   

        elif "bunkyo" in link:
            time.sleep(1)
            click_coordinates = [
                (633, 919),
                (740, 522),
                (1717, 1007),
                (295, 494),
                (200, 556),
                (172, 701),
                (292, 668),
                (153,608),
            
                (907, 555),
                (776, 688),
                (903, 682),
                (702, 510),
                (1136, 748),

        
            ]
            # 1つ目のウェブページの処理（例：タイトルを表示）
            for click_count, coordinates in enumerate(click_coordinates, start=1):
                # クリック後に少し待つ（必要に応じて調整）
                time.sleep(1)
                # 指定された座標に移動して左クリック
                pyautogui.click(coordinates[0], coordinates[1])
                # 特定の回数目のときだけ待機
                if click_count == 3:
                    time.sleep(2)  # 待機時間を適宜調整

            # ページを下にスクロール
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            
            # スクリーンショットを保存するファイルのパスを指定してください
            file_path1 = "result/bunkyo.png"

            time.sleep(2.5)
            # スクリーンショットを取得して保存
            take_screenshot(file_path1)   


        # elif "" in link:
        #     click_coordinates = [
        
        #     ]
        #     # 1つ目のウェブページの処理（例：タイトルを表示）
        #     for click_count, coordinates in enumerate(click_coordinates, start=1):
        #         # クリック後に少し待つ（必要に応じて調整）
        #         time.sleep(1)
        #         # 指定された座標に移動して左クリック
        #         pyautogui.click(coordinates[0], coordinates[1])
        #         # 特定の回数目のときだけ待機
        #         if click_count == 2:
        #           time.sleep(2.5)  # 待機時間を適宜調整
            
        #     # スクリーンショットを保存するファイルのパスを指定してください
        #     file_path1 = ".png"

        #     time.sleep(2)
        #     # スクリーンショットを取得して保存
        #     take_screenshot(file_path1)   

        #     #11月分
        #     time.sleep(1)
        #     pyautogui.click(700,650)
        #     file_path2 = ".png"
        #     time.sleep(2)
        #     take_screenshot(file_path2)   
    
    except KeyboardInterrupt:
        print("プログラムが中断されました。")
    except Exception as e:
        print(f"エラーが発生しました: {e}")
        



def open_multiple_links_in_chrome(links):
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")  # ウィンドウを最大化

    # ChromeのWebDriverを指定
    driver = webdriver.Chrome(options=chrome_options)

    try:
        for link in links:
            process_link(driver, link)
    except Exception as e:
        print(f"エラーが発生しました: {e}")
    finally:
        # プログラムが終了したときに手動でブラウザを閉じる必要があります
        driver.quit()
        print("プログラムを終了し、ブラウザも閉じられました。")

# ここに開きたいウェブリンクを追加してください
weblinks = [
    "https://web02.rsv.ws-scs.jp/chofu-bunka/web/",
    "https://www.itabashi-shisetsu-yoyaku.jp/eshisetsu/menu/Login.cgi#footer",
    "https://sst1.ka-ruku.com/suginamikoukaidou/month" ,
    "https://yoyaku.city.nerima.tokyo.jp/stagia/reserve/gin_menu",
    "https://yoyaku.nakano-tokyo.jp/stagia/reserve/grb_init",
    "https://rsvsys.city.nishitokyo.eprs.jp/web/",
    "https://www.shisetsu.city.bunkyo.lg.jp/user/Home",
]


open_multiple_links_in_chrome(weblinks)