package snakeAndLadders;

import java.util.ArrayList;
import java.util.List;

public class Board {
    private int rows;
    private int cols;

    private List<List<Cell>> cells;

    public int maxNumber;

    public Board(int rows, int cols) {
        this.rows = rows;
        this.cols = cols;

        this.initialize();

        this.maxNumber = rows*cols;

    }

    private void initialize(){
        for(int i=0;i<rows;i++){
            List<Cell> currentRow = new ArrayList<>();
            for(int j=0;j<cols;j++){
                currentRow.add(new Cell(i,j,getIndex(i,j)));
            }
            cells.add(currentRow);
        }
    }

    // utility fn,converts from i,j to number
    private int getIndex(int i, int j){
        // 0,0 -> 0+1
        // 0,5 -> 5+1
        // 1,5 -> 6+1
        // 1,0 -> 11
        return i*cols + (i%2==0 ? j : cols-1-j) + 1;
    }

    // utility fn, converts index to row,col
    private List<Integer> getRowAndCol(int index) {
        int row =  (index-1)/cols;
        int col = row%2==0 ? (index-1)%cols : cols-1-(index-1)%cols;
        return List.of(row,col);
    }

    public int getRows() {
        return rows;
    }

    public int getCols() {
        return cols;
    }

    public Cell getCell(int index) {
        List<Integer> rowAndCol = getRowAndCol(index);
        return cells.get(rowAndCol.get(0)).get(rowAndCol.get(1));
    }
}
