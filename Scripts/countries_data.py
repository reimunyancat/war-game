from .enemy_country import EnemyCountry

enemy_countries = {
    0: EnemyCountry('몽골', 10, 5, 2, 1000),
    1: EnemyCountry('중국', 30, 10, 5, 3000),
    2: EnemyCountry('태국', 50, 20, 10, 5000),
    3: EnemyCountry('캄보디아', 100, 25, 30, 7000),
    4: EnemyCountry('필리핀', 200, 40, 50, 10000),
    5: EnemyCountry('일본', 500, 100, 100, 15000),
    6: EnemyCountry('호주', 1000, 150, 200, 30000),
    7: EnemyCountry('싱가포르', 3000, 250, 500, 50000),
    8: EnemyCountry('몰디브', 5000, 500, 1000, 75000),
    9: EnemyCountry('인도', 10000, 700, 2000, 100000),
    10: EnemyCountry('네팔', 20000, 1000, 5000, 200000),
    11: EnemyCountry('두바이', 40000, 3000, 8000, 500000),
    12: EnemyCountry('사우디아라비아', 75000, 5000, 10000, 750000),
    13: EnemyCountry('케냐', 100000, 8000, 15000, 1200000),
    14: EnemyCountry('마다가스카르', 150000, 10000, 20000, 1500000),
    15: EnemyCountry('남아프리카', 300000, 20000, 60000, 20000000),
    16: EnemyCountry('가나', 750000, 30000, 80000, 50000000),
    17: EnemyCountry('사하라사막', 1000000, 50000, 130000, 80000000),
    18: EnemyCountry('이집트', 1500000, 75000, 175000, 110000000),
    19: EnemyCountry('터키', 4000000, 100000, 240000, 150000000),
    20: EnemyCountry('러시아', 8000000, 150000, 270000, 200000000),
    21: EnemyCountry('그리스', 13000000, 200000, 330000, 230000000),
    22: EnemyCountry('이탈리아', 18000000, 300000, 370000, 260000000),
    23: EnemyCountry('모나코', 25000000, 500000, 400000, 300000000),
    24: EnemyCountry('스페인', 35000000, 700000, 500000, 400000000),
    25: EnemyCountry('프랑스', 50000000, 1000000, 750000, 800000000),
    26: EnemyCountry('독일', 75000000, 1500000, 1000000, 1500000000),
    27: EnemyCountry('덴마크', 100000000, 2000000, 1500000, 2000000000),
    28: EnemyCountry('노르웨이', 140000000, 3000000, 2000000, 2500000000),
    29: EnemyCountry('영국', 190000000, 4500000, 2500000, 3000000000),
    30: EnemyCountry('그린란드', 250000000, 6000000, 3000000, 3500000000),
    31: EnemyCountry('캐나다', 330000000, 10000000, 4000000, 4500000000),
    32: EnemyCountry('뉴욕', 440000000, 17000000, 5000000, 5000000000),
    33: EnemyCountry('버뮤다', 600000000, 25000000, 6000000, 5500000000),
    34: EnemyCountry('자메이카', 800000000, 35000000, 7000000, 6000000000),
    35: EnemyCountry('콜롬비아', 1000000000, 45000000, 8000000, 6500000000),
    36: EnemyCountry('브라질', 1300000000, 60000000, 9000000, 7000000000),
    37: EnemyCountry('아르헨티나', 1600000000, 80000000, 10000000, 7500000000),
    38: EnemyCountry('마추픽추', 2000000000, 100000000, 11000000, 8000000000),
    39: EnemyCountry('이스터 섬', 2500000000, 120000000, 12000000, 8500000000),
    40: EnemyCountry('멕시코', 3000000000, 150000000, 13000000, 9000000000),
    41: EnemyCountry('NASA', 3600000000, 180000000, 14000000, 9500000000),
    42: EnemyCountry('라스베가스', 4300000000, 220000000, 15000000, 10000000000),
    43: EnemyCountry('할리우드', 5000000000, 270000000, 16000000, 10500000000),
    44: EnemyCountry('알래스카', 5700000000, 330000000, 17000000, 11000000000),
    45: EnemyCountry('미국', 6400000000, 400000000, 18000000, 11500000000),
    46: EnemyCountry('하와이', 7100000000, 500000000, 19000000, 12000000000),
    47: EnemyCountry('북한', 10000000000, 600000000, 20000000, 12500000000),
    48: EnemyCountry('한국', 12000000000, 700000000, 21000000, 13000000000),
    49: EnemyCountry('달', 14000000000, 800000000, 22000000, 13500000000),
    50: EnemyCountry('화성', 16000000000, 900000000, 23000000, 14000000000),
    51: EnemyCountry('수성', 18000000000, 1000000000, 24000000, 14500000000),
    52: EnemyCountry('금성', 20000000000, 1200000000, 25000000, 15000000000),
    53: EnemyCountry('목성', 22000000000, 1500000000, 26000000, 15500000000),
    54: EnemyCountry('토성', 24000000000, 1800000000, 27000000, 16000000000),
    55: EnemyCountry('천왕성', 26000000000, 2200000000, 28000000, 16500000000),
    56: EnemyCountry('해왕성', 28000000000, 2700000000, 29000000, 17000000000),
    57: EnemyCountry('태양', 30000000000, 3300000000, 30000000, 17500000000),
    58: EnemyCountry('명왕성', 32000000000, 4000000000, 31000000, 18000000000),
    59: EnemyCountry('견우성', 34000000000, 5000000000, 32000000, 18500000000),
    60: EnemyCountry('천랑성', 36900000000, 6000000000, 33000000, 19000000000),
    61: EnemyCountry('직녀성', 37600000000, 7000000000, 34000000, 19500000000),
    62: EnemyCountry('알데바란', 38300000000, 8000000000, 35000000, 20000000000),
    63: EnemyCountry('베텔게우스', 39000000000, 9000000000, 36000000, 20500000000),
    64: EnemyCountry('디네프', 40000000000, 10000000000, 37000000, 21000000000),
    65: EnemyCountry('리겔', 40400000000, 12000000000, 38000000, 21500000000),
    66: EnemyCountry('시리우스', 41100000000, 15000000000, 39000000, 22000000000),
    67: EnemyCountry('안드로메다', 41800000000, 18000000000, 40000000, 22500000000),
    68: EnemyCountry('중성자별', 42500000000, 22000000000, 41000000, 23000000000),
    69: EnemyCountry('블랙홀', 500000000000, 500000000000, 10000000, 50000000000),
    70: EnemyCountry('빅뱅', 100000000000000, 5000000000000, None, None),
}