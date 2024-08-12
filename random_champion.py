# -*- coding: shift_jis -*-

import random
import yaml

def choose_random_champion():
    # YAML�t�@�C����ǂݍ���
    with open("selected_champions.yaml", "r", encoding="utf-8") as file:
        config = yaml.safe_load(file)

    # �L�����N�^�[�̃��X�g���擾
    champions = config.get("selected_champions", [])

    # ���X�g����łȂ����m�F
    if not champions:
        print("�`�����s�I���̃��X�g����ł��Bconfig.yaml���m�F���Ă��������B")
        return

    # ���X�g���烉���_���ɃL�����N�^�[��I��
    selected_champion = random.choice(champions)

    # ���ʂ�\��
    print(f"�I�΂ꂽ�L�����N�^�[��: {selected_champion} �ł��B")

# �v���O���������s
choose_random_champion()
