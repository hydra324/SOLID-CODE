package snakeAndLadders;

// move is the contract between player and game controller
public class Move {
    private int diceRoll;
    private Player player;

    public Move(int diceRoll, Player player) {
        this.diceRoll = diceRoll;
        this.player = player;
    }

    public int getDiceRoll() {
        return diceRoll;
    }

    public Player getPlayer() {
        return player;
    }
}
