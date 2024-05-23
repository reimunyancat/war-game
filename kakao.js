const scriptName = "전쟁 게임";

let users = {};

function registerUser(sender) {
  if (!users[sender]) {
      users[sender] = {
          name: sender,
          money: 1000,
          soldier: 0,
          weapon: 0,
          weaponPower: 1,
          currentWeaponName: weaponNames[0],
          enemyCountryIndex: 0
      };
      console.log(`${sender}님, 새로운 사용자로 등록되었습니다.`);
  } else {
      console.log(`${sender}님은 이미 등록된 사용자입니다.`);
  }
  return users[sender];
}

function response(room, msg, sender, isGroupChat, replier, imageDB, packageName) {
  let user = getUser(sender);

  switch (msg) {
    case "/돈벌기":
      earnMoney(user, replier);
      break;
    case "/무기강화":
      upgradeWeapon(user, replier);
      break;
    case "/군인모집":
      recruitSoldiers(user, replier);
      break;
    case "/전쟁":
      conductWar(user, replier);
      break;
    default:
      replier.reply("알 수 없는 명령입니다. 사용 가능한 명령: /돈벌기, /무기강화, /군인모집, /전쟁");
  }
}

function earnMoney(user, replier) {
  let earnedMoney = Math.floor(Math.random() * 500 + 100);
  user.money += earnedMoney;
  replier.reply(`${user.name}님, ${earnedMoney}원을 벌었습니다! 현재 돈: ${user.money}원`);
}

function upgradeWeapon(user, replier) {
  if (user.money >= 100) {
    user.money -= 100;
    user.weapon += 1;
    user.weaponPower += 5;
    replier.reply(`${user.name}님, 무기 강화 성공! 현재 무기 레벨: ${user.weapon}, 무기 파워: ${user.weaponPower}, 남은 돈: ${user.money}원`);
  } else {
    replier.reply("돈이 부족합니다. 무기 강화에 필요한 돈: 100원");
  }
}

function recruitSoldiers(user, replier) {
  if (user.money >= 500) {
    user.soldier += 1;
    user.money -= 500;
    replier.reply(`${user.name}님, 군인을 모집했습니다! 현재 군인 수: ${user.soldier}, 남은 돈: ${user.money}원`);
  } else {
    replier.reply("돈이 부족합니다. 군인 모집에 필요한 돈: 500원");
  }
}

function conductWar(user, replier) {
  let enemy = enemyCountries[user.enemyCountryIndex];
  if (user.soldier > enemy.defence) {
      user.money += enemy.moneyReward;
      user.soldier += enemy.soldierReward;
      replier.reply(`전쟁 승리! ${enemy.name}을/를 정복했습니다. 보상: ${enemy.moneyReward}원, ${enemy.soldierReward}명의 군인`);
      user.enemyCountryIndex += 1;
  } else {
      replier.reply(`전쟁 패배... ${enemy.name}에게 패배했습니다.`);
      user.soldier = 0; // 패배 시 모든 군인을 잃습니다.
  }
}

const enemyCountries = [
  { name: "몽골", defence: 10, attack: 5, soldierReward: 2, moneyReward: 1000 },
  { name: "중국", defence: 30, attack: 10, soldierReward: 5, moneyReward: 3000 },
  { name: "태국", defence: 50, attack: 20, soldierReward: 10, moneyReward: 5000 },
  { name: "캄보디아", defence: 100, attack: 25, soldierReward: 30, moneyReward: 7000 },
  { name: "필리핀", defence: 200, attack: 40, soldierReward: 50, moneyReward: 10000 },
  { name: "일본", defence: 500, attack: 100, soldierReward: 100, moneyReward: 15000 },
  { name: "호주", defence: 1000, attack: 150, soldierReward: 200, moneyReward: 30000 },
  { name: "싱가포르", defence: 3000, attack: 250, soldierReward: 500, moneyReward: 50000 },
  { name: "몰디브", defence: 5000, attack: 500, soldierReward: 1000, moneyReward: 75000 },
  { name: "인도", defence: 10000, attack: 700, soldierReward: 2000, moneyReward: 100000 },
  { name: "네팔", defence: 20000, attack: 1000, soldierReward: 5000, moneyReward: 200000 },
  { name: "두바이", defence: 40000, attack: 3000, soldierReward: 8000, moneyReward: 500000 },
  { name: "사우디아라비아", defence: 75000, attack: 5000, soldierReward: 10000, moneyReward: 750000 },
  { name: "케냐", defence: 100000, attack: 8000, soldierReward: 15000, moneyReward: 1200000 },
  { name: "마다가스카르", defence: 150000, attack: 10000, soldierReward: 20000, moneyReward: 1500000 },
  { name: "남아프리카", defence: 300000, attack: 20000, soldierReward: 60000, moneyReward: 20000000 },
  { name: "가나", defence: 750000, attack: 30000, soldierReward: 80000, moneyReward: 50000000 },
  { name: "사하라사막", defence: 1000000, attack: 50000, soldierReward: 130000, moneyReward: 80000000 },
  { name: "이집트", defence: 1500000, attack: 75000, soldierReward: 175000, moneyReward: 110000000 },
  { name: "터키", defence: 4000000, attack: 100000, soldierReward: 240000, moneyReward: 150000000 },
  { name: "러시아", defence: 8000000, attack: 150000, soldierReward: 270000, moneyReward: 200000000 },
  { name: "그리스", defence: 13000000, attack: 200000, soldierReward: 330000, moneyReward: 230000000 },
  { name: "이탈리아", defence: 18000000, attack: 300000, soldierReward: 370000, moneyReward: 260000000 },
  { name: "모나코", defence: 25000000, attack: 500000, soldierReward: 400000, moneyReward: 300000000 },
  { name: "스페인", defence: 35000000, attack: 700000, soldierReward: 500000, moneyReward: 400000000 },
  { name: "프랑스", defence: 50000000, attack: 1000000, soldierReward: 750000, moneyReward: 800000000 },
  { name: "독일", defence: 75000000, attack: 1500000, soldierReward: 1000000, moneyReward: 1500000000 },
  { name: "덴마크", defence: 100000000, attack: 2000000, soldierReward: 1500000, moneyReward: 2000000000 },
  { name: "노르웨이", defence: 140000000, attack: 3000000, soldierReward: 2000000, moneyReward: 2500000000 },
  { name: "영국", defence: 190000000, attack: 4500000, soldierReward: 2500000, moneyReward: 3000000000 },
  { name: "그린란드", defence: 250000000, attack: 6000000, soldierReward: 3000000, moneyReward: 3500000000 },
  { name: "캐나다", defence: 330000000, attack: 10000000, soldierReward: 4000000, moneyReward: 4500000000 },
  { name: "뉴욕", defence: 440000000, attack: 17000000, soldierReward: 5000000, moneyReward: 5000000000 },
  { name: "브라질", defence: 1300000000, attack: 60000000, soldierReward: 9000000, moneyReward: 7000000000 },
  { name: "아르헨티나", defence: 1600000000, attack: 80000000, soldierReward: 10000000, moneyReward: 7500000000 },
  { name: "마추픽추", defence: 2000000000, attack: 100000000, soldierReward: 11000000, moneyReward: 8000000000 },
  { name: "이스터 섬", defence: 2500000000, attack: 120000000, soldierReward: 12000000, moneyReward: 8500000000 },
  { name: "멕시코", defence: 3000000000, attack: 150000000, soldierReward: 13000000, moneyReward: 9000000000 },
  { name: "NASA", defence: 3600000000, attack: 180000000, soldierReward: 14000000, moneyReward: 9500000000 },
  { name: "라스베가스", defence: 4300000000, attack: 220000000, soldierReward: 15000000, moneyReward: 10000000000 },
  { name: "할리우드", defence: 5000000000, attack: 270000000, soldierReward: 16000000, moneyReward: 10500000000 },
  { name: "알래스카", defence: 5700000000, attack: 330000000, soldierReward: 17000000, moneyReward: 11000000000 },
  { name: "미국", defence: 6400000000, attack: 400000000, soldierReward: 18000000, moneyReward: 11500000000 },
  { name: "하와이", defence: 7100000000, attack: 500000000, soldierReward: 19000000, moneyReward: 12000000000 },
  { name: "북한", defence: 10000000000, attack: 600000000, soldierReward: 20000000, moneyReward: 12500000000 },
  { name: "한국", defence: 12000000000, attack: 700000000, soldierReward: 21000000, moneyReward: 13000000000 },
  { name: "달", defence: 14000000000, attack: 800000000, soldierReward: 22000000, moneyReward: 13500000000 },
  { name: "화성", defence: 16000000000, attack: 900000000, soldierReward: 23000000, moneyReward: 14000000000 },
  { name: "수성", defence: 18000000000, attack: 1000000000, soldierReward: 24000000, moneyReward: 14500000000 },
  { name: "금성", defence: 20000000000, attack: 1200000000, soldierReward: 25000000, moneyReward: 15000000000 },
  { name: "목성", defence: 22000000000, attack: 1500000000, soldierReward: 26000000, moneyReward: 15500000000 },
  { name: "토성", defence: 24000000000, attack: 1800000000, soldierReward: 27000000, moneyReward: 16000000000 },
  { name: "천왕성", defence: 26000000000, attack: 2200000000, soldierReward: 28000000, moneyReward: 16500000000 },
  { name: "해왕성", defence: 28000000000, attack: 2700000000, soldierReward: 29000000, moneyReward: 17000000000 },
  { name: "태양", defence: 30000000000, attack: 3300000000, soldierReward: 30000000, moneyReward: 17500000000 },
  { name: "명왕성", defence: 32000000000, attack: 4000000000, soldierReward: 31000000, moneyReward: 18000000000 },
  { name: "견우성", defence: 34000000000, attack: 5000000000, soldierReward: 32000000, moneyReward: 18500000000 },
  { name: "천랑성", defence: 36900000000, attack: 6000000000, soldierReward: 33000000, moneyReward: 19000000000 },
  { name: "직녀성", defence: 37600000000, attack: 7000000000, soldierReward: 34000000, moneyReward: 19500000000 },
  { name: "알데바란", defence: 38300000000, attack: 8000000000, soldierReward: 35000000, moneyReward: 20000000000 },
  { name: "베텔게우스", defence: 39000000000, attack: 9000000000, soldierReward: 36000000, moneyReward: 20500000000 },
  { name: "디네프", defence: 40000000000, attack: 10000000000, soldierReward: 37000000, moneyReward: 21000000000 },
  { name: "리겔", defence: 40400000000, attack: 12000000000, soldierReward: 38000000, moneyReward: 21500000000 },
  { name: "시리우스", defence: 41100000000, attack: 15000000000, soldierReward: 39000000, moneyReward: 22000000000 },
  { name: "안드로메다", defence: 41800000000, attack: 18000000000, soldierReward: 40000000, moneyReward: 22500000000 },
  { name: "중성자별", defence: 42500000000, attack: 22000000000, soldierReward: 41000000, moneyReward: 23000000000 },
  { name: "블랙홀", defence: 50000000000, attack: 50000000000, soldierReward: 10000000, moneyReward: 50000000000 },
  { name: "빅뱅", defence: 10000000000000, attack: 5000000000000, soldierReward: None, moneyReward: None }
];

const weaponNames = {
  0: '손', 1: '모래', 2: '돌', 3: '나무검', 4: '돌검', 5: '낫', 6: '망치', 7: '도끼', 8: '칼', 9: '노트북', 10: '톱',
  11: '쇠사슬', 12: '쇠막대기', 13: '철퇴', 14: '장궁', 15: '화살', 16: '창', 17: '방패', 18: '총', 19: '폭탄', 20: '미사일',
  21: '레이저건', 22: '수류탄', 23: '화염방사기', 24: '전기톱', 25: '레이저칼', 26: '독침', 27: '순간이동기', 28: '로켓런처', 29: '드론', 30: '자동소총',
  31: '저격총', 32: '기관총', 33: '핵폭탄', 34: 'EMP', 35: '가스폭탄', 36: '바이러스', 37: '생화학무기', 38: '사이버공격', 39: '위성무기', 40: '레일건',
  41: '플라즈마건', 42: '에너지 방패', 43: '얼음 방사기', 44: '초음파 무기', 45: '자기장 발생기', 46: '중력 폭탄', 47: '마이크로봇', 48: '나노머신', 49: '안개를 가르는 회광', 50: '시간 정지기',
  51: '블랙홀 생성기', 52: '양자 무기', 53: '메타 물질', 54: '암흑 물질', 55: '플라즈마 방패', 56: '안티 물질', 57: '태양 에너지 총', 58: '감마선 빔', 59: '중성자 폭탄', 60: '바이오 해킹', 
  61: '나노 로봇', 62: '인공 지능', 63: '가상 현실', 64: '홀로그램', 65: '레이저 드론', 66: '스팀펑크 메카', 67: '사이보그', 68: '유전자 조작', 69: '클론 군대', 70: '엑스칼리버',
  71: '오비탈 캐논', 72: '우주선', 73: '인공 블랙홀', 74: '우주 레이저', 75: '행성 파괴기', 76: '우주 방사기', 77: '다차원 포탈', 78: '양자 컴퓨터', 79: '인공태양', 80: '우주 정거장',
  81: '인공 웜홀', 82: '우주 전함', 83: '인공 지능 로봇', 84: '사이버네틱 파워 슈트', 85: '양자 폭탄', 86: '우주 드론', 87: '인공 중력', 88: '우주 미사일', 89: '항성간 미사일', 90: '우주 폭탄',
  91: '우주 레이저 건', 92: '우주 EMP', 93: '우주 가스폭탄', 94: '우주 바이러스', 95: '우주 생화학무기', 96: '우주 사이버공격', 97: '우주 위성무기', 98: '우주 레일건', 99: '우주 플라즈마건',
  100: '심판의 검'
};