const messages = [
  "LOL",
  "ApexLegends",
  "Valorant",
  "Steamゲーム",
  "アニメをみよう！"
];

function popBalloon(element) {
  element.style.visibility = 'hidden';  // 風船を非表示にする
  const randomIndex = Math.floor(Math.random() * messages.length);
  document.getElementById('message').textContent = messages[randomIndex];
}

function addCustomMessage() {
  const customMessage = document.getElementById('customMessage').value;
  if (customMessage.trim()) {
      messages.push(customMessage);
      document.getElementById('customMessage').value = ''; 
      alert('メッセージを追加しました!');
  } else {
      alert('メッセージを入力してください。');
  }
}
