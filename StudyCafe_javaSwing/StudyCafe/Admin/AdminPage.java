package StudyCafe.Admin;

import StudyCafe.Button.RoundedButton;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.sql.SQLException;

public class AdminPage extends JFrame {
    public AdminPage() {
        JFrame frame = new JFrame("Admin Page");

        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setSize(500, 600);

//        // 상단 타이틀
//        JLabel titleLabel = new JLabel("관리자 페이지", SwingConstants.CENTER);
//        titleLabel.setFont(new Font("맑은 고딕", Font.BOLD, 30));
//        add(titleLabel, BorderLayout.NORTH);

        // 중앙 패널
        JPanel centerPanel = new JPanel();
        centerPanel.setLayout(new BoxLayout(centerPanel, BoxLayout.Y_AXIS));
        centerPanel.setAlignmentX(Component.CENTER_ALIGNMENT); // 중앙 정렬


        centerPanel.add(Box.createVerticalStrut(50)); // 여백 추가

        // 프로필 이미지
        ImageIcon profileIcon = new ImageIcon("images/profile.png");
        Image profileImage = profileIcon.getImage().getScaledInstance(100, 100, Image.SCALE_SMOOTH);
        JLabel profileLabel = new JLabel(new ImageIcon(profileImage));
        profileLabel.setAlignmentX(Component.CENTER_ALIGNMENT); // 중앙 정렬
        centerPanel.add(Box.createVerticalStrut(50)); // 여백 추가
        centerPanel.add(profileLabel);

        centerPanel.add(Box.createVerticalStrut(50)); // 여백 추가

        // 신고 관리 이동 버튼
        RoundedButton Button1 = new RoundedButton("신고 관리");
        Button1.setPreferredSize(new Dimension(150, 40)); // 버튼 크기 설정
        Button1.setMaximumSize(Button1.getPreferredSize()); // 최대 크기 설정
        Button1.setAlignmentX(Component.CENTER_ALIGNMENT); // 중앙 정렬
        Button1.setBackground(Color.lightGray);
        Button1.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                ReportAdmin r = null;
                try {
                    r = new ReportAdmin();
                } catch (SQLException ex) {
                    ex.printStackTrace();
                }
                r.setVisible(true);
                dispose();
            }
        });

        centerPanel.add(Button1);

        centerPanel.add(Box.createVerticalStrut(20)); // 여백 추가

        // 재고 관리 이동 버튼
        RoundedButton Button2 = new RoundedButton("재고 관리");
        Button2.setPreferredSize(new Dimension(150, 40)); // 버튼 크기 설정
        Button2.setMaximumSize(Button2.getPreferredSize()); // 최대 크기 설정
        Button2.setAlignmentX(Component.CENTER_ALIGNMENT); // 중앙 정렬
        Button2.setBackground(Color.lightGray);
        Button2.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                BeverageInventory2 b = new BeverageInventory2();
                b.setVisible(true);
                dispose();
            }
        });
        centerPanel.add(Button2);
        centerPanel.add(Box.createVerticalStrut(20)); // 여백 추가

        add(centerPanel, BorderLayout.CENTER);
        setVisible(true);
    }

    public static void main(String[] args) {
        new AdminPage();
    }
}
