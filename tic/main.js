//simple tictac game
//GRID PLAYERS
//UPDATE

let grid = [
  [" ", " ", " "],
  [" ", " ", " "],
  [" ", " ", " "],
];

function displayGrid() {
  console.log(
    grid.map((row) => row.join("|")).join("\n" + "-".repeat(5) + "\n"),
  );
}
