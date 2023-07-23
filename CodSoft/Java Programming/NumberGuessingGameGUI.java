import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.Random;

public class NumberGuessingGameGUI extends JFrame {
    private int generatedNumber;
    private int attemptsLeft;
    private JLabel messageLabel;
    private JTextField guessTextField;
    private JButton guessButton;

    public NumberGuessingGameGUI() {
        generatedNumber = generateRandomNumber(1, 100);
        attemptsLeft = 5;

        messageLabel = new JLabel("Make a guess (1-100):");
        guessTextField = new JTextField(10);
        guessButton = new JButton("Submit");

        guessButton.addActionListener(e -> checkGuess());

        JPanel panel = new JPanel();
        panel.setLayout(new BoxLayout(panel, BoxLayout.Y_AXIS));
        panel.add(messageLabel);
        panel.add(guessTextField);
        panel.add(guessButton);

        add(panel);
        pack();
        setTitle("Number Guessing Game");
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLocationRelativeTo(null);
        setResizable(false);
    }

    private int generateRandomNumber(int min, int max) {
        return new Random().nextInt(max - min + 1) + min;
    }

    private void checkGuess() {
        String guessString = guessTextField.getText();

        try {
            int guess = Integer.parseInt(guessString);

            if (guess == generatedNumber) {
                JOptionPane.showMessageDialog(this, "Wow! You got it right!",
                        "Correct Guess", JOptionPane.INFORMATION_MESSAGE);
                restartGame();
            } else {
                attemptsLeft--;

                if (attemptsLeft > 0) {
                    String message = guess < generatedNumber ? "Nope, too low!" : "Oops, too high!";
                    messageLabel.setText(message + " Attempts left: " + attemptsLeft);
                } else {
                    JOptionPane.showMessageDialog(this,
                            "Game Over! The number was " + generatedNumber,
                            "Game Over", JOptionPane.ERROR_MESSAGE);
                    restartGame();
                }
            }
        } catch (NumberFormatException ex) {
            JOptionPane.showMessageDialog(this, "Invalid input. Please enter a number.",
                    "Invalid Input", JOptionPane.ERROR_MESSAGE);
        }

        guessTextField.setText("");
        guessTextField.requestFocus();
    }

    private void restartGame() {
        int option = JOptionPane.showConfirmDialog(this, "Play again?", "Play Again",
                JOptionPane.YES_NO_OPTION);

        if (option == JOptionPane.YES_OPTION) {
            generatedNumber = generateRandomNumber(1, 100);
            attemptsLeft = 5;
            messageLabel.setText("Make a guess (1-100):");
        } else {
            dispose();
        }
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> new NumberGuessingGameGUI().setVisible(true));
    }
}
