# mechanics = [ Puzzle猜謎, Political政治, Racing競賽, Real-time時間限制, Spies/Secret Agents間諜, Sports運動, Territory Building領土建設, Trains火車,Travel旅行, Trivia瑣碎問答, Video Game Theme電玩題材, Vietnam War越戰, Wargame戰爭, Word Game單字, World War I一次大戰 ,World War II二次大戰, Zombies殭屍, Modern Warfare現代戰爭, Movies/TV/Radio theme	影視, Murder/Mystery謀殺, Music音樂, Mythology神話, Napoleonic拿破崙, Nautical航海, Negotiation談判, Novel-based小說題材, Number數字, Party Game派對, Pike n Shot阻絕與投射, Pirates	海盜, Political政治
# "Animals動物", "Arabian阿拉伯", "Aviation/Flight航空飛行", "Bluffing嚇唬欺騙", "Book紙本", "Card Game卡牌", "City Building都市建設", "Civilization文明", "Collectible Components集換","Comic Book/Strip漫畫題材",  "Deduction推理", "Dice骰子", "Economic經濟", "Educational教育", "Electronic	電子", "Environmental環境","Expansion for Base-game擴展包", "Exploration探險", "Fantasy奇幻", "Farming農業", "Fighting戰鬥", "Game System遊戲系統", "Horror	驚悚", "Humor幽默","Industry/Manufacturing	工業", "Mafia黑手黨", "Math數學", "Mature/Adult成人", "Maze迷宮", "Medical醫療", "Medieval中古時期", "Memory	記憶","Miniatures	微縮模型","Modern Warfare	現代戰爭",

import random

# mylist = ["apple", "banana", "cherry"]

# print(random.choice(mylist))

mechanics = [ "Animals動物", "Arabian阿拉伯", "Aviation/Flight航空飛行", "Bluffing嚇唬欺騙", "Book紙本", "Card Game卡牌", "City Building都市建設", "Civilization文明", "Collectible Components集換","Comic Book/Strip漫畫題材",  "Deduction推理", "Dice骰子", "Economic經濟", "Educational教育", "Electronic電子", "Environmental環境","Expansion for Base-game擴展包", "Exploration探險", "Fantasy奇幻", "Farming農業", "Fighting戰鬥", "Game System遊戲系統", "Horror驚悚", "Humor幽默","Industry/Manufacturing工業", "Mafia黑手黨", "Math數學", "Mature/Adult成人", "Maze迷宮", "Medical醫療", "Medieval中古時期", "Memory記憶","Miniatures微縮模型","Modern Warfare現代戰爭","Territory Building領土建設", "Trains火車", "Travel旅行", "Trivia瑣碎問答", "Video Game Theme電玩題材", "Wargame戰爭", "Word Game單字","Puzzle", "Political", "Racing", "Real-time", "Mythology神話", "Napoleonic拿破崙", " Nautical航海", "Negotiation談判", "Novel-based小說題材", "Number數字", "Modern Warfare現代戰爭", "Murder/Mystery謀殺", ]

choice1 = (random.choice(mechanics))
choice2 =(random.choice(mechanics))
choice3 =(random.choice(mechanics))
choice4 =(random.choice(mechanics))
choice5 =(random.choice(mechanics))


print(f"you will make a game with {choice1}+ {choice2}+ {choice3}+ {choice4}+ {choice5}")


