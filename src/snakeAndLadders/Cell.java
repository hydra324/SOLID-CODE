package snakeAndLadders;

import java.util.Set;

public class Cell {
    private int row;
    private int col;

    private int number;

    private Set<Player> players = null;

    public Cell(int row, int col,int number) {
        this.row = row;
        this.col = col;
        this.number = number;
    }

    public int getRow() {
        return row;
    }

    public void setRow(int row) {
        this.row = row;
    }

    public int getCol() {
        return col;
    }

    public void setCol(int col) {
        this.col = col;
    }

    public int getNumber() {
        return number;
    }

    public void addPlayer(Player p){
        players.add(p);
    }

    public void removePlayer(Player p){
        if (!players.contains(p)) {
            throw new IllegalStateException("Player cannot be removed!");
        }
        players.remove(p);
    }
}
