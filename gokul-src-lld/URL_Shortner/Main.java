class URL{
	String shortURL;
	String longURL;
	String id;
}

Class Base64Convertor {
	private Base64Convertor();
	public Base64Convertor getInstance();
	String convert(String id);
}

interface DatabaseService {
	public URL getEntryFromShortURL(String shortURL);
	public URL getEntryFromLongURL(String longURL);
	public void updateShortURL(String id, String shortURL);
}

class DatabaseServiceImpl implements DatabaseService {
	private DatabaseServiceImpl();
	public DatabaseService getInstance();
}

interface LongURLService {
	String fetchShortURL(String longURL);
}

class LongURLServiceImpl implements LongURLService {
	DatabaseService dbs;
	
	private longURLServiceImpl();
	public longURLService getInstance();
}

interface ShortURLService {
	String fetchLongURL(String shortURL);
}

class ShortURLServiceImpl implements ShortURLService {
	DatabaseService dbs;

	private shortURLServiceImpl();
	public shortURLService getInstance();
}


class Controller {
	ShortURLService shortURLService = ShortURLServiceImpl.getInstance();
	LongURLService longURLService = LongURLServiceImpl.getInstance();

	public String shortenURL(String input) {
		return longURLService.shorten(input);
	}
	
	public String fetchShortURL(String input) {
		return shortURLService.getLongURL(input);
	}
}
