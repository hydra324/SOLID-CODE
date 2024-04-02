package tictactoe;

public class Player {
    private String name;
    private String character;

    public Player(String name, String character){
        this.name = name;
        this.character = character;
    }

    public String getName(){
        return name;
    }

    public String getCharacter(){
        return character;
    }

    public Move createMove(int row, int col){
        return new Move(row,col,this);
    }
}
