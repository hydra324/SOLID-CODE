package snakeAndLadders;

public class Player {
    public String name;

    private Cell currentCell;

    public Player(String name) {
        this.name = name;
    }

    public String getName() {
        return name;
    }

    public Move createMove(int diceRoll) {
        return new Move(diceRoll,this);
    }

    public Cell getCurrentCell() {
        return currentCell;
    }

    public void setCurrentCell(Cell currentCell) {
        this.currentCell = currentCell;
    }
}
