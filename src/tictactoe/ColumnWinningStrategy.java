package tictactoe;

public class ColumnWinningStrategy implements WinningStrategy{

    @Override
    public boolean evaluate(Board board, Move move){
        Cell lastChangedCell = board.getCell(move.getRow(), move.getCol());
        // we have to check if the same player has all the cells in this column has the same
        Player currentPlayer = lastChangedCell.getPlayer();
        if (currentPlayer==null) return false;
        for(int i=0;i<board.getSize();i++){
            if (board.getCell(i,lastChangedCell.getCol()).getPlayer() != currentPlayer){
                return false;
            }
        }
        return true;
    }
}
