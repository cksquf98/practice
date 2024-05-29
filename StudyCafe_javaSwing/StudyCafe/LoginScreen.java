package StudyCafe;

import StudyCafe.Admin.AdminPage;
import StudyCafe.Button.RoundedButton;
import StudyCafe.Seats.SeatReservation;

import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
import java.sql.SQLException;

public class LoginScreen extends JFrame {
    private UserDao userDao;
    private UserVO user;

    public LoginScreen() {
        userDao = new UserDao(); // UserDao 초기화

        setTitle("로그인");
        setSize(400, 600);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLocationRelativeTo(null);

        JPanel panel = new JPanel();
        panel.setLayout(null);

        JLabel loginLabel = new JLabel("로그인", SwingConstants.CENTER);
        loginLabel.setFont(new Font("", Font.BOLD, 24));
        loginLabel.setBounds(150, 100, 100, 30);
        panel.add(loginLabel);

        JTextField idField = new JTextField("Phone");
        idField.setBounds(100, 200, 200, 30);
        panel.add(idField);

        idField.addFocusListener(new FocusAdapter() {
            @Override
            public void focusGained(FocusEvent e) {
                if (idField.getText().equals("Phone")) {
                    idField.setText("");
                }
            }

            @Override
            public void focusLost(FocusEvent e) {
                if (idField.getText().isEmpty()) {
                    idField.setText("Phone");
                }
            }
        });

        JPasswordField pwField = new JPasswordField("PW");
        pwField.setBounds(100, 250, 200, 30);
        panel.add(pwField);

        pwField.setEchoChar((char) 0);
        pwField.addFocusListener(new FocusAdapter() {
            @Override
            public void focusGained(FocusEvent e) {
                String password = new String(pwField.getPassword());
                if (password.equals("PW")) {
                    pwField.setText("");
                    pwField.setEchoChar('●');
                }
            }

            @Override
            public void focusLost(FocusEvent e) {
                String password = new String(pwField.getPassword());
                if (password.isEmpty()) {
                    pwField.setText("PW");
                    pwField.setEchoChar((char) 0);
                }
            }
        });

        RoundedButton loginButton = new RoundedButton("확인");
        loginButton.setBounds(150, 300, 100, 30);
        loginButton.setBackground(Color.lightGray);
        panel.add(loginButton);

        RoundedButton signUpButton = new RoundedButton("회원가입");
        signUpButton.setBounds(150, 350, 100, 30);
        signUpButton.setBackground(Color.LIGHT_GRAY);
        panel.add(signUpButton);

        add(panel);

        loginButton.addActionListener(e -> {
            String idText = idField.getText();
            String pwText = new String(pwField.getPassword());

            if (idText.equals("") || idText.equals("Phone") || pwText.equals("") || pwText.equals("PW")) {
                JOptionPane.showMessageDialog(this, "제대로 입력해주세요.", "경고", JOptionPane.WARNING_MESSAGE);
            } else {
                try {
                    user = userDao.getUser(idText, pwText);
                    if(user == null) {
                        JOptionPane.showMessageDialog(this, "잘못된 입력입니다.", "경고", JOptionPane.WARNING_MESSAGE);
                    }
                    if(user.getReportCount(user.getUserIdx()) == 5) {
                        JOptionPane.showMessageDialog(this, "금일 5회 이상의 신고를 받아 좌석을 이용할 수 없습니다.\n관리자에게 문의 바랍니다.", "경고", JOptionPane.WARNING_MESSAGE);
                        dispose();
                    }
                    else if (user != null && user.getAdmin().equals("N")) {
                        JOptionPane.showMessageDialog(this, "로그인 성공", "알림", JOptionPane.INFORMATION_MESSAGE);
                        new SeatReservation(user);
                        dispose();
                    }
                    else if (user != null && user.getAdmin().equals("Y")) {
                        JOptionPane.showMessageDialog(this, "로그인 성공", "알림", JOptionPane.INFORMATION_MESSAGE);
                        new AdminPage();
                        dispose();
                    }
                    else {
                        JOptionPane.showMessageDialog(this, "잘못된 입력입니다.", "경고", JOptionPane.WARNING_MESSAGE);
                    }
                } catch (SQLException ex) {
                    JOptionPane.showMessageDialog(this, "로그인 실패:" +ex.getMessage(), "경고", JOptionPane.ERROR_MESSAGE);
                    ex.printStackTrace(); // 예외 세부 정보 출력
                }
            }
        });

        signUpButton.addActionListener(e -> {
            new SignUpScreen();
            dispose();
        });

        setVisible(true);
    }

    public static void main(String[] args) {
        new LoginScreen();
    }
}
