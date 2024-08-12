# -*- coding: shift_jis -*-

import yaml

def load_champions_from_yaml(file_path, lane):
    """YAMLファイルから指定されたレーンのチャンピオンリストを読み込む"""
    with open(file_path, 'r', encoding='utf-8') as file:
        config = yaml.safe_load(file)
        return config.get(lane, [])

def save_selected_champions_to_yaml(selected_champions, player, lane):
    """選択されたチャンピオンをプレイヤー名のYAMLファイルに保存する"""
    file_path = f"{player}_selected_champions.yaml"
    with open(file_path, 'w', encoding='utf-8') as file:
        yaml.dump({lane: selected_champions}, file, allow_unicode=True)

def create_checklist_for_players(champions, players, lane):
    """プレイヤーごとにユーザーがチャンピオンを選択できるチェックリストを作成する"""
    player_champions = {player: [] for player in players}

    for player in players:
        print(f"\n{player}のチェックリスト:")
        selected_champions = []

        while True:
            print("\nチェックリスト:")
            for i, champion in enumerate(champions, 1):
                checked = "?" if champion in selected_champions else " "
                print(f"{i}. [{checked}] {champion}")

            print("\n番号を入力して項目を切り替えるか、'q'を押して終了します。")
            choice = input(f"{player}の選択: ")

            if choice.lower() == 'q':
                break
            elif choice.isdigit() and 1 <= int(choice) <= len(champions):
                index = int(choice) - 1
                if champions[index] in selected_champions:
                    selected_champions.remove(champions[index])
                else:
                    selected_champions.append(champions[index])
            else:
                print("無効な入力です。もう一度お試しください。")

        player_champions[player] = selected_champions
        # プレイヤーごとに選択されたチャンピオンをYAMLファイルに保存
        save_selected_champions_to_yaml(selected_champions, player, lane)

    return player_champions

if __name__ == "__main__":
    input_yaml_file = 'lol_champions_by_role.yaml'
    lanes = ["Top", "Jungle", "Mid", "Bot", "Support"]

    print("レーンを選択してください:")
    for i, lane in enumerate(lanes, 1):
        print(f"{i}. {lane}")

    lane_choice = input("レーンの番号を入力してください: ")

    if lane_choice.isdigit() and 1 <= int(lane_choice) <= len(lanes):
        selected_lane = lanes[int(lane_choice) - 1]
        champions_to_check = load_champions_from_yaml(input_yaml_file, selected_lane)
        if not champions_to_check:
            print(f"{selected_lane}のチャンピオンが見つかりません。lol_champions_by_role.yamlを確認してください。")
        else:
            player = input("プレイヤー名を入力してください: ")
            selected = create_checklist_for_players(champions_to_check, [player], selected_lane)
            print("\n選択された項目:")
            for champion in selected[player]:
                print(f"- {champion}")

            print("\n選択された項目がプレイヤーのYAMLファイルに保存されました。")
    else:
        print("無効なレーンの番号です。プログラムを終了します。")
