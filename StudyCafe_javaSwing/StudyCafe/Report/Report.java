package StudyCafe.Report;

import StudyCafe.Seats.SeatDao;
import StudyCafe.UserVO;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.sql.SQLException;

public class Report extends JFrame {
    private static UserVO user;
    private SeatDao seatDao = new SeatDao();
    public Report(int seatNumber,UserVO user) {
        this.user = user;

        setTitle("Report Issue");
        setSize(400, 300);
        setLayout(new BorderLayout());

        JLabel reportLabel = new JLabel("신고할 좌석: " + seatNumber);
        reportLabel.setHorizontalAlignment(SwingConstants.CENTER);
        reportLabel.setFont(new Font("맑은 고딕", Font.BOLD, 15));
        add(reportLabel, BorderLayout.NORTH);

        JPanel radioPanel = new JPanel();
        radioPanel.setLayout(new BoxLayout(radioPanel, BoxLayout.Y_AXIS));

        JRadioButton option1 = new JRadioButton("소음");
        JRadioButton option2 = new JRadioButton("냄새");
        JRadioButton option3 = new JRadioButton("음식물 섭취");

        ButtonGroup group = new ButtonGroup();
        group.add(option1);
        group.add(option2);
        group.add(option3);

        radioPanel.add(option1);
        radioPanel.add(option2);
        radioPanel.add(option3);

        add(radioPanel, BorderLayout.CENTER);

        JButton submitButton = new JButton("신고하기");
        submitButton.setFont(new Font("맑은 고딕", Font.BOLD, 15));
        submitButton.setBackground(Color.RED);
        submitButton.setForeground(Color.WHITE);
        submitButton.setOpaque(true);
        submitButton.setBorderPainted(false);
        submitButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                int selectedOption = 0;
                if (option1.isSelected()) {
                    selectedOption = 1;//소음
                } else if (option2.isSelected()) {
                    selectedOption = 2;//냄새
                } else if (option3.isSelected()) {
                    selectedOption =3;//음식물섭취
                }

                if (selectedOption == 1 || selectedOption == 2 || selectedOption == 3) {

                    int complete = -1;
                    try {
                        complete = seatDao.insertReport(user.getUserIdx(),seatNumber, selectedOption); //해서 디비로 넘어가게 해야겠다!!!
                        if(complete != -1) {
                            JOptionPane.showMessageDialog(Report.this, selectedOption + "항목으로 신고가 접수되었습니다.");
                        }
                        else {
                            JOptionPane.showMessageDialog(null, "해당 좌석은 비어있습니다. ", "경고", JOptionPane.ERROR_MESSAGE);

                        }
                    } catch (SQLException ex) {
                        JOptionPane.showMessageDialog(null, "해당 좌석 신고 실패:" +ex.getMessage(), "경고", JOptionPane.ERROR_MESSAGE);
                        ex.printStackTrace(); // 예외 세부 정보 출력
                    }

                    dispose(); // Close the report window
                } else {
                    JOptionPane.showMessageDialog(Report.this, "신고 항목을 선택하세요.");
                }
            }
        });

        add(submitButton, BorderLayout.SOUTH);

        setVisible(true);
    }
}
