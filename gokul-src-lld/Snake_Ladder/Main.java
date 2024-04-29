Enum BoardDifficulty {
	EASY,
	MEDIUM,
	DIFFICULT
}

abstract class Board {
	private int m;
	private int n;
	
	public Board(int x);
	public Board(int x, int y);
	public abstract initBoard();
}

class BoardInstance extends Board {
	private int boardId;
	private BoardDifficulty difficulty;
	
	public BoardInstance(BoardDifficulty difficulty);
	public initBoard() {
		initBoard(difficulty);
	}
	public initBoard(BoardDifficulty difficulty);
}

####################################################################
Board b = new BoardInstance(BoardDifficulty.EASY);
####################################################################

class Dice {
	private int faces;
	
	Dice(int faces);
	public int roll();
}

class PlayerSession {
	private int playerId;
	private int playingBoardId;
	private int currX;
	private int currY;
	
	public void updatePos(int steps);
	public void getX();
	public void getY();
}

abstract class Game {
	private int gameId;
	private Board board;
	private List<PlayerSession> players;
	private int currentTurn; //Default initialized to 0, indicating player 1
	private Dice dice;

	public Game(Board b, int playersCount, int diceFaces);
	public abstract createGame(Board b, int playersCount, int diceFaces);
	public abstract createPlayerSessions();
	public abstract resetPlayerSessions();
	public abstract Dice createDice(int diceFaces);
	public abstract int getCurrentPlayer();
	public abstract int rollDice();
	public abstract int movePlayer(int steps);
	public abstract int printGame();
	public abstract boolean isWinner(int playerId);
}

class GameInstance extends Game {
	
}

####################################################################
GameInstance gameInstance = new GameInstance();
gameInstance.createGame(b, 2, 6);
####################################################################

class PlayService implements Runnable {
	public PlayService(GameInstance gameInstance);
	public void run() {
		while() {
			int d = gameInstance.rollDice();
			int p = gameInstance.getCurrentPlayer();
			gameInstance.move(d);
			if(gameInstance.isWinner(p)) {
				System.out.println("WINNER");
			}
		}
	}
}

class Driver {
	Board b = new BoardInstance(BoardDifficulty.EASY);
	GameInstance gameInstance = new GameInstance();
	gameInstance.createGame(b, 2, 6);
	Thread t = new Thread(new PlayService(gameInstance));
	t.start();
}

