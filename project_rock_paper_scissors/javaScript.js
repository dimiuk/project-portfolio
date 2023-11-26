let userScore = 0;
let computerScore = 0;
const userScoreSpan = document.getElementById("user-score");
const computerScoreSpan = document.getElementById("computer-score");
const scoreBoardDiv = document.querySelector(".score-board");
const resultP = document.querySelector(".result > p");
const rockDiv = document.getElementById("r");
const scissorsDiv = document.getElementById("s");
const paperDiv = document.getElementById("p");

function getComputerChoice() {
  const choices = ["r", "p", "s"];
  const randomNumber = Math.floor(Math.random() * 3);
  return choices[randomNumber];
}

function convertTwoWords(letter) {
  if (letter === "r") return "Rock";
  if (letter === "p") return "Paper";
  return "Scissors";
}

function win(userChoice, computerChoice) {
  const userChoiceDive = document.getElementById(userChoice);
  userScore++;
  userScoreSpan.innerHTML = userScore;
  computerScoreSpan.innerHTML = computerScore;
  resultP.innerHTML = `${convertTwoWords(userChoice)} beats ${convertTwoWords(
    computerChoice
  )}. You win!`;
  userChoiceDive.classList.add("green-glow");
  setTimeout(() => userChoiceDive.classList.remove("green-glow"), 500);
}

function lose(userChoice, computerChoice) {
  const userChoiceDive = document.getElementById(userChoice);
  computerScore++;
  userScoreSpan.innerHTML = userScore;
  computerScoreSpan.innerHTML = computerScore;
  resultP.innerHTML = `${convertTwoWords(
    userChoice
  )} loses to ${convertTwoWords(computerChoice)}. You lost!`;
  userChoiceDive.classList.add("red-glow");
  setTimeout(() => userChoiceDive.classList.remove("red-glow"), 500);
}

function draw(userChoice, computerChoice) {
  const userChoiceDive = document.getElementById(userChoice);
  resultP.innerHTML = `${convertTwoWords(userChoice)} equals ${convertTwoWords(
    computerChoice
  )}. It's a draw`;
  userChoiceDive.classList.add("yellow-glow");
  setTimeout(() => userChoiceDive.classList.remove("yellow-glow"), 500);
}

function game(userChoice) {
  const computerChoice = getComputerChoice();
  // console.log("Comp choise" + computerChoice);
  // console.log("User choise" + userChoice);

  switch (userChoice + computerChoice) {
    case "rs":
    case "pr":
    case "sp":
      win(userChoice, computerChoice);
      break;
    case "rp":
    case "ps":
    case "sr":
      lose(userChoice, computerChoice);
      break;
    case "rr":
    case "pp":
    case "ss":
      draw(userChoice, computerChoice);
      break;
  }
}

function main() {
  rockDiv.addEventListener("click", function () {
    game("r");
  });
  scissorsDiv.addEventListener("click", function () {
    game("s");
  });
  paperDiv.addEventListener("click", function () {
    game("p");
  });
}
main();
