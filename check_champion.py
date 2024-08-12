# -*- coding: shift_jis -*-

import yaml

def load_champions_from_yaml(file_path, lane):
    """YAML�t�@�C������w�肳�ꂽ���[���̃`�����s�I�����X�g��ǂݍ���"""
    with open(file_path, 'r', encoding='utf-8') as file:
        config = yaml.safe_load(file)
        return config.get(lane, [])

def save_selected_champions_to_yaml(selected_champions, player, lane):
    """�I�����ꂽ�`�����s�I�����v���C���[����YAML�t�@�C���ɕۑ�����"""
    file_path = f"{player}_selected_champions.yaml"
    with open(file_path, 'w', encoding='utf-8') as file:
        yaml.dump({lane: selected_champions}, file, allow_unicode=True)

def create_checklist_for_players(champions, players, lane):
    """�v���C���[���ƂɃ��[�U�[���`�����s�I����I���ł���`�F�b�N���X�g���쐬����"""
    player_champions = {player: [] for player in players}

    for player in players:
        print(f"\n{player}�̃`�F�b�N���X�g:")
        selected_champions = []

        while True:
            print("\n�`�F�b�N���X�g:")
            for i, champion in enumerate(champions, 1):
                checked = "?" if champion in selected_champions else " "
                print(f"{i}. [{checked}] {champion}")

            print("\n�ԍ�����͂��č��ڂ�؂�ւ��邩�A'q'�������ďI�����܂��B")
            choice = input(f"{player}�̑I��: ")

            if choice.lower() == 'q':
                break
            elif choice.isdigit() and 1 <= int(choice) <= len(champions):
                index = int(choice) - 1
                if champions[index] in selected_champions:
                    selected_champions.remove(champions[index])
                else:
                    selected_champions.append(champions[index])
            else:
                print("�����ȓ��͂ł��B������x���������������B")

        player_champions[player] = selected_champions
        # �v���C���[���ƂɑI�����ꂽ�`�����s�I����YAML�t�@�C���ɕۑ�
        save_selected_champions_to_yaml(selected_champions, player, lane)

    return player_champions

if __name__ == "__main__":
    input_yaml_file = 'lol_champions_by_role.yaml'
    lanes = ["Top", "Jungle", "Mid", "Bot", "Support"]

    print("���[����I�����Ă�������:")
    for i, lane in enumerate(lanes, 1):
        print(f"{i}. {lane}")

    lane_choice = input("���[���̔ԍ�����͂��Ă�������: ")

    if lane_choice.isdigit() and 1 <= int(lane_choice) <= len(lanes):
        selected_lane = lanes[int(lane_choice) - 1]
        champions_to_check = load_champions_from_yaml(input_yaml_file, selected_lane)
        if not champions_to_check:
            print(f"{selected_lane}�̃`�����s�I����������܂���Blol_champions_by_role.yaml���m�F���Ă��������B")
        else:
            player = input("�v���C���[������͂��Ă�������: ")
            selected = create_checklist_for_players(champions_to_check, [player], selected_lane)
            print("\n�I�����ꂽ����:")
            for champion in selected[player]:
                print(f"- {champion}")

            print("\n�I�����ꂽ���ڂ��v���C���[��YAML�t�@�C���ɕۑ�����܂����B")
    else:
        print("�����ȃ��[���̔ԍ��ł��B�v���O�������I�����܂��B")
