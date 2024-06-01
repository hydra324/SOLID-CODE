package discount;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

interface PriceWord {
    boolean evaluate(String word);
    String applyDiscount(String word, float discount);
}

class DefaultPriceWord implements PriceWord {
    @Override
    public boolean evaluate(String word) {
        return word.charAt(0) == '$' && word.charAt(word.length()-1) != ','; //first char is $ and last char is not comma
    }

    @Override
    public String applyDiscount(String word, float discount) {
        String priceSubString = word.substring(1);
        float priceSubStringValue = Float.parseFloat(priceSubString);
        priceSubStringValue *= discount;
        return word.charAt(0) + String.valueOf(priceSubStringValue);
    }
}

public class Main {
    List<PriceWord> priceWords;
    public Main() {
        this.priceWords = new ArrayList<>();
        this.priceWords.add(new DefaultPriceWord());
    }
    public static void main(String[] args) {
        System.out.println("entry point");
    }

    public String applyDiscountToWords(String word, float discount) {
        //return true; // dummy return value for now
        for (PriceWord priceWord : this.priceWords) {
            if (!priceWord.evaluate(word)) continue;
            return priceWord.applyDiscount(word, discount);
        }
        return word;
    }

    public String[] parseString(String inputString, String separator) {
        return inputString.strip().split(separator);
    }

    // inputString will be of this format: "My wallet balance is $42.23 and I want to buy an ice cream"
    public String applyDiscount(String inputString){
        String[] parsedString = parseString(inputString, " ");
        return Arrays.stream(parsedString)
                .map(word -> this.applyDiscountToWords(word, (float) 0.85))
                .collect(Collectors.joining(", "));
    }


}
