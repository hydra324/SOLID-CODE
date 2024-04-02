package tictactoe;

public class Cell {
    private int row;
    private int col;

    private Player player=null;

    public Cell(int row, int col) {
        this.row = row;
        this.col = col;
    }

    public int getRow(){
        return row;
    }

    public int getCol(){
        return col;
    }

    public void setPlayer(Player player){
        this.player = player;
    }

    public Player getPlayer() {
        return this.player;
    }
}
