import java.util.*;

import javax.swing.JOptionPane;

public class WordCounterMinimalGUI {
    private static final Set<String> STOP_WORDS = new HashSet<>(Arrays.asList(
            "a", "an", "the", "in", "on", "at", "of", "to", "and", "or", "for", "is", "are", "was", "were", "has", "have"
    ));

    public static void main(String[] args) {
        String inputText = getInputText();
        if (inputText.isEmpty()) {
            showMessage("Input text is empty.");
        } else {
            String[] words = inputText.split("\\W+");
            int totalWordCount = words.length;
            int uniqueWordCount = getUniqueWordCount(words);
            Map<String, Integer> wordFrequencyMap = getWordFrequencyMap(words);

            StringBuilder result = new StringBuilder();
            result.append("Total word count: ").append(totalWordCount).append("\n");
            result.append("Unique word count: ").append(uniqueWordCount).append("\n");

            if (!wordFrequencyMap.isEmpty()) {
                result.append("Word frequency:\n");
                wordFrequencyMap.forEach((word, frequency) -> result.append(word).append(": ").append(frequency).append("\n"));
            }
            showMessage(result.toString());
        }
    }

    private static String getInputText() {
        return JOptionPane.showInputDialog(null, "Enter the text:");
    }

    private static int getUniqueWordCount(String[] words) {
        Set<String> uniqueWords = new HashSet<>(Arrays.asList(words));
        uniqueWords.removeIf(STOP_WORDS::contains);
        return uniqueWords.size();
    }

    private static Map<String, Integer> getWordFrequencyMap(String[] words) {
        Map<String, Integer> wordFrequencyMap = new HashMap<>();
        for (String word : words) {
            if (!STOP_WORDS.contains(word.toLowerCase())) {
                wordFrequencyMap.put(word.toLowerCase(), wordFrequencyMap.getOrDefault(word.toLowerCase(), 0) + 1);
            }
        }
        return wordFrequencyMap;
    }

    private static void showMessage(String message) {
        JOptionPane.showMessageDialog(null, message);
    }
}
