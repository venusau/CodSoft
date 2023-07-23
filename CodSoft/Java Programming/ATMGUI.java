import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

class BankAccount {
    private double balance;

    public BankAccount(double initialBalance) {
        this.balance = initialBalance;
    }

    public double getBalance() {
        return balance;
    }

    public void deposit(double amount) {
        balance += amount;
    }

    public boolean withdraw(double amount) {
        if (amount <= balance) {
            balance -= amount;
            return true;
        }
        return false;
    }
}

public class ATMGUI {
    private BankAccount bankAccount = new BankAccount(50000);

    public ATMGUI() {
        JFrame frame = new JFrame("ATM Machine");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(400, 200);
        frame.setResizable(false);

        JLabel balanceLabel = new JLabel("Balance: ₹" + bankAccount.getBalance());
        balanceLabel.setFont(new Font("Arial", Font.PLAIN, 20));

        JPanel inputPanel = new JPanel(new FlowLayout(FlowLayout.CENTER, 10, 10));
        JLabel amountLabel = new JLabel("Enter amount:");
        JTextField amountField = new JTextField(10);
        JButton withdrawButton = new JButton("Withdraw");
        JButton depositButton = new JButton("Deposit");

        ActionListener transactionListener = e -> {
            String amountStr = amountField.getText();
            try {
                double amount = Double.parseDouble(amountStr);
                if (amount <= 0) {
                    showErrorDialog("Invalid amount. Please enter a positive value.");
                } else {
                    if (e.getSource() == withdrawButton) {
                        if (bankAccount.withdraw(amount)) {
                            showInfoDialog("Withdrawal successful. New balance: ₹" + bankAccount.getBalance());
                        } else {
                            showErrorDialog("Insufficient balance.");
                        }
                    } else if (e.getSource() == depositButton) {
                        bankAccount.deposit(amount);
                        showInfoDialog("Deposit successful. New balance: ₹" + bankAccount.getBalance());
                    }
                    balanceLabel.setText("Balance: ₹" + bankAccount.getBalance());
                }
            } catch (NumberFormatException ex) {
                showErrorDialog("Invalid amount. Please enter a valid number.");
            }
        };

        withdrawButton.addActionListener(transactionListener);
        depositButton.addActionListener(transactionListener);

        inputPanel.add(amountLabel);
        inputPanel.add(amountField);
        inputPanel.add(withdrawButton);
        inputPanel.add(depositButton);

        frame.setLayout(new BorderLayout());
        frame.add(balanceLabel, BorderLayout.NORTH);
        frame.add(inputPanel, BorderLayout.CENTER);

        frame.setVisible(true);
    }

    private void showInfoDialog(String message) {
        JOptionPane.showMessageDialog(null, message, "Information", JOptionPane.INFORMATION_MESSAGE);
    }

    private void showErrorDialog(String message) {
        JOptionPane.showMessageDialog(null, message, "Error", JOptionPane.ERROR_MESSAGE);
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(ATMGUI::new);
    }
}
