# -*- coding: shift_jis -*-

import random
import yaml

def choose_random_champion():
    # YAMLファイルを読み込む
    with open("selected_champions.yaml", "r", encoding="utf-8") as file:
        config = yaml.safe_load(file)

    # キャラクターのリストを取得
    champions = config.get("selected_champions", [])

    # リストが空でないか確認
    if not champions:
        print("チャンピオンのリストが空です。config.yamlを確認してください。")
        return

    # リストからランダムにキャラクターを選択
    selected_champion = random.choice(champions)

    # 結果を表示
    print(f"選ばれたキャラクターは: {selected_champion} です。")

# プログラムを実行
choose_random_champion()
