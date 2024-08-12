# -*- coding: shift_jis -*-

import random

def team_assignment():
    # 総人数を指定
    total_players = int(input("総人数を入力してください: "))

    # プレイヤー名の入力
    players = []
    for i in range(total_players):
        name = input(f"プレイヤー {i+1} の名前を入力してください: ")
        players.append(name)

    # 必要に応じて"unknown"プレイヤーを追加
    while len(players) < 5:
        players.append("unknown")

    # lane
    lane_names = ["TOP", "JG", "MID", "BOT", "SUP"]

    # プレイヤーをランダムにシャッフル
    random.shuffle(players)

    # チームにプレイヤーを割り当て
    teams = {team_name: [] for team_name in lane_names}

    for i, player in enumerate(players):
        team_index = i % len(lane_names)
        teams[lane_names[team_index]].append(player)

    # 結果を表示
    for lane_name, team_members in teams.items():
        print(f"\n{lane_name}:")
        for member in team_members:
            print(f"- {member}")

# プログラムを実行
team_assignment()
