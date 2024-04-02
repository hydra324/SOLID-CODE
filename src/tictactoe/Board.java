package tictactoe;

import java.util.ArrayList;
import java.util.List;

public class Board {
    private int size;

    List<List<Cell>> cells;

    public Board(int size){
        this.size = size;
        for(int i=0;i<this.size;i++){
            List<Cell> row = new ArrayList<>();
            for(int j=0;j<this.size;j++){
                row.add(new Cell(i,j));
            }
            cells.add(row);
        }
    }

    public Cell getCell(int row,int col){
        return cells.get(row).get(col);
    }

    public int getSize() {
        return size;
    }
}
