package StudyCafe;

import StudyCafe.Button.RoundedButton;

import java.awt.*;
import java.awt.event.*;
import java.sql.SQLException;
import javax.swing.*;

//회원가입 화면
public class SignUpScreen extends JFrame {
    UserDao userDao = new UserDao();
    public SignUpScreen() {
        setTitle("회원가입");
        setSize(400, 600);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLocationRelativeTo(null);

        JPanel panel = new JPanel();
        panel.setLayout(null);

        JLabel signUpLabel = new JLabel("회원가입", SwingConstants.CENTER);
        signUpLabel.setFont(new Font("", Font.BOLD, 24));
        signUpLabel.setBounds(150, 100, 100, 30);
        panel.add(signUpLabel);

        JTextField nameField = new JTextField("Name");
        nameField.setBounds(100, 200, 200, 30);
        panel.add(nameField);

        // NameField FocusListener
        nameField.addFocusListener(new FocusAdapter() {
            @Override
            public void focusGained(FocusEvent e) {
                if (nameField.getText().equals("Name")) {
                    nameField.setText("");
                }
            }

            @Override
            public void focusLost(FocusEvent e) {
                if (nameField.getText().isEmpty()) {
                    nameField.setText("Name");
                }
            }
        });

        JTextField phoneField = new JTextField("Phone");
        phoneField.setBounds(100, 250, 200, 30);
        panel.add(phoneField);

        // PhoneField FocusListener
        phoneField.addFocusListener(new FocusAdapter() {
            @Override
            public void focusGained(FocusEvent e) {
                if (phoneField.getText().equals("Phone")) {
                    phoneField.setText("");
                }
            }

            @Override
            public void focusLost(FocusEvent e) {
                if (phoneField.getText().isEmpty()) {
                    phoneField.setText("Phone");
                }
            }
        });

        JPasswordField pwField = new JPasswordField("PW");
        pwField.setBounds(100, 300, 200, 30);
        panel.add(pwField);

        // PWField FocusListener
        pwField.setEchoChar((char) 0); // Initially display text
        pwField.addFocusListener(new FocusAdapter() {
            @Override
            public void focusGained(FocusEvent e) {
                String password = new String(pwField.getPassword());
                if (password.equals("PW")) {
                    pwField.setText("");
                    pwField.setEchoChar('●'); // Change to a bullet character
                }
            }

            @Override
            public void focusLost(FocusEvent e) {
                String password = new String(pwField.getPassword());
                if (password.isEmpty()) {
                    pwField.setText("PW");
                    pwField.setEchoChar((char) 0); // Display text
                }
            }
        });

        RoundedButton registerButton = new RoundedButton("가입");
        registerButton.setBounds(150, 350, 100, 30);
        registerButton.setBackground(Color.LIGHT_GRAY);
        panel.add(registerButton);

        RoundedButton gobackButton = new RoundedButton("돌아가기");
        gobackButton.setBounds(150, 400, 100, 30);
        gobackButton.setBackground(Color.LIGHT_GRAY);
        panel.add(gobackButton);

        // 가입 버튼 클릭 시 이벤트 처리
        registerButton.addActionListener(e -> {
            String nameText = nameField.getText();
            String phoneText = phoneField.getText();
            String pwText = new String(pwField.getPassword());
            
            
            if (nameText.equals("") || nameText.equals("Name") ||
                    phoneText.equals("") || phoneText.equals("Phone") ||
                    pwText.equals("") || pwText.equals("PW")) {
                JOptionPane.showMessageDialog(this, "제대로 입력해주세요.", "경고", JOptionPane.WARNING_MESSAGE);
            }
            else if(pwText.length() < 6) {
                JOptionPane.showMessageDialog(this, "비밀번호는 6자리 이상이여야 합니다.", "경고", JOptionPane.WARNING_MESSAGE);
            }
            else {
                int createResult = 0;
                try {
                    createResult = userDao.CreateUser(nameText, phoneText, pwText);
                    if (createResult == 1) {
                        JOptionPane.showMessageDialog(this, "가입 되었습니다.", "알림", JOptionPane.INFORMATION_MESSAGE);
                        new LoginScreen();
                        dispose();
                    }
                    else {
                        JOptionPane.showMessageDialog(this, "가입 실패", "경고", JOptionPane.WARNING_MESSAGE);
                    }
                } catch (SQLException ex) {
                    throw new RuntimeException(ex);
                }
            }
        });

        // 돌아가기 버튼 클릭 시 이벤트 처리
        gobackButton.addActionListener(e -> {
            new LoginScreen();
            dispose();
        });

        add(panel);
        setVisible(true);
    }

    public static void main(String[] args) {
        new SignUpScreen();
    }

}