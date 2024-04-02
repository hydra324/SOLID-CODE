package tictactoe;

public class RowWinningStrategy implements WinningStrategy{

    @Override
    public boolean evaluate(Board board, Move move) {
        Cell lastChangedCell = board.getCell(move.getRow(), move.getCol());
        // we have to check if the same player has all the cells in this row has the same
        Player currentPlayer = lastChangedCell.getPlayer();
        if (currentPlayer==null) return false;
        for(int j=0;j<board.getSize();j++){
            if (board.getCell(lastChangedCell.getRow(),j).getPlayer() != currentPlayer){
                return false;
            }
        }
        return true;
    }
}
