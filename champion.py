# リーグ・オブ・レジェンドのチャンピオンをロールごとにリストアップして保存するためのPythonスクリプトを作成します。

# 各ロールごとのチャンピオンリストを辞書形式で作成
lol_champions_by_role = {
    "Top": [
        "Aatrox", "Akali", "Camille", "Cho'Gath", "Darius", "Dr. Mundo", "Fiora",
        "Garen", "Gangplank", "Gnar", "Illaoi", "Irelia", "Jax", "Jayce",
        "Kayle", "Kennen", "Kled", "Malphite", "Maokai", "Mordekaiser", "Nasus",
        "Ornn", "Poppy", "Quinn", "Renekton", "Riven", "Rumble", "Sett",
        "Shen", "Singed", "Sion", "Sylas", "Teemo", "Tryndamere", "Urgot",
        "Vladimir", "Volibear", "Wukong", "Yorick"
    ],
    "Jungle": [
        "Amumu", "Diana", "Dr. Mundo", "Elise", "Evelynn", "Fiddlesticks", "Gragas",
        "Graves", "Hecarim", "Ivern", "Jarvan IV", "Jax", "Karthus", "Kayn", 
        "Kha'Zix", "Kindred", "Lee Sin", "Lillia", "Master Yi", "Nidalee", "Nocturne",
        "Nunu & Willump", "Olaf", "Pantheon", "Poppy", "Rammus", "Rek'Sai", 
        "Rengar", "Sejuani", "Shaco", "Shyvana", "Skarner", "Taliyah", 
        "Trundle", "Udyr", "Vi", "Viego", "Volibear", "Warwick", "Wukong", "Zac"
    ],
    "Mid": [
        "Ahri", "Akali", "Anivia", "Annie", "Aurelion Sol", "Azir", "Cassiopeia",
        "Corki", "Diana", "Ekko", "Fizz", "Galio", "Gragas", "Heimerdinger", "Irelia", 
        "Kassadin", "Katarina", "LeBlanc", "Lissandra", "Lux", "Malzahar", "Neeko", 
        "Orianna", "Pantheon", "Qiyana", "Ryze", "Seraphine", "Swain", "Sylas", 
        "Syndra", "Taliyah", "Talon", "Twisted Fate", "Veigar", "Vex", "Viktor", 
        "Vladimir", "Xerath", "Yasuo", "Yone", "Zed", "Ziggs", "Zoe", "Zyra"
    ],
    "Bot": [
        "Aphelios", "Ashe", "Caitlyn", "Draven", "Ezreal", "Jhin", "Jinx", 
        "Kai'Sa", "Kalista", "Kog'Maw", "Lucian", "Miss Fortune", "Samira", 
        "Senna", "Sivir", "Tristana", "Twitch", "Varus", "Vayne", "Xayah", "Zeri"
    ],
    "Support": [
        "Alistar", "Bard", "Blitzcrank", "Brand", "Braum", "Janna", "Karma", 
        "Leona", "Lulu", "Lux", "Morgana", "Nami", "Nautilus", "Pyke", 
        "Rakan", "Renata Glasc", "Rell", "Seraphine", "Sona", "Soraka", 
        "Swain", "Tahm Kench", "Taric", "Thresh", "Zilean", "Zyra"
    ]
}

# データをテキストファイルに書き込む
file_path = "C:\Users\rukit\makepro\lol_pick\lol_champions_by_role.txt"
with open(file_path, "w") as file:
    for role, champions in lol_champions_by_role.items():
        file.write(f"{role}:\n")
        for champion in champions:
            file.write(f"  - {champion}\n")
        file.write("\n")

file_path
