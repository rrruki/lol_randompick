# -*- coding: shift_jis -*-

import random

def team_assignment():
    # ���l�����w��
    total_players = int(input("���l������͂��Ă�������: "))

    # �v���C���[���̓���
    players = []
    for i in range(total_players):
        name = input(f"�v���C���[ {i+1} �̖��O����͂��Ă�������: ")
        players.append(name)

    # �K�v�ɉ�����"unknown"�v���C���[��ǉ�
    while len(players) < 5:
        players.append("unknown")

    # lane
    lane_names = ["TOP", "JG", "MID", "BOT", "SUP"]

    # �v���C���[�������_���ɃV���b�t��
    random.shuffle(players)

    # �`�[���Ƀv���C���[�����蓖��
    teams = {team_name: [] for team_name in lane_names}

    for i, player in enumerate(players):
        team_index = i % len(lane_names)
        teams[lane_names[team_index]].append(player)

    # ���ʂ�\��
    for lane_name, team_members in teams.items():
        print(f"\n{lane_name}:")
        for member in team_members:
            print(f"- {member}")

# �v���O���������s
team_assignment()
