
function myFunction() { 
    document.getElementById("correct").innerHTML = "You are correct!";
    document.getElementById("correct").style.textAlign = "center";
    document.getElementById("correct").style.color = "Brown";
    document.getElementById("correct").style.fontFamily = "Arial Rounded MT";
    document.getElementById("correct").style.fontSize = "larger";
    }

  var scoreText = document.getElementById("num")
  var score = Number(scoreText.innerText)
  var submit_btn = document.getElementById("forsubmit")
  var next_btn = document.getElementById("next")
  
  function hintonClick(){
    if (score >= 2) {
      score -= 2;
      scoreText.innerText =  String(score)
    }
  }

  function nexttoPage() {
    document.getElementById("forsubmit").style.visibility = 'hidden';
    submit_btn.style.display="none";
    document.getElementById("next").style.visibility = 'visible';
    next_btn.display="block";
  }
