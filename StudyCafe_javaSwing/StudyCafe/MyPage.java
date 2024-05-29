package StudyCafe;

import StudyCafe.Button.RoundedButton;
import StudyCafe.Order.OrderDAO;
import StudyCafe.Order.OrderVO;
import StudyCafe.Report.ReportDao;
import StudyCafe.Report.ReportVO;
import StudyCafe.Seats.SeatDao;
import StudyCafe.Seats.SeatReservation;
import StudyCafe.Seats.SeatVO;

import javax.swing.*;
import javax.swing.table.DefaultTableModel;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.sql.SQLException;
import java.util.ArrayList;

public class MyPage extends JFrame {
    private UserVO user = null;
    private SeatVO seat = null;
    private ReportVO reportVO = null;

    public MyPage(UserVO user) throws SQLException {
         this.user = user;

        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setSize(700, 600);
        setLayout(new BorderLayout());

        // 상단 타이틀
        JLabel titleLabel = new JLabel("마이페이지", SwingConstants.CENTER);
        titleLabel.setFont(new Font("맑은 고딕", Font.BOLD, 30));
        titleLabel.add(Box.createVerticalStrut(50));
        add(titleLabel, BorderLayout.NORTH);

        // 중앙 패널
        JPanel centerPanel = new JPanel();
        centerPanel.setLayout(new BoxLayout(centerPanel, BoxLayout.Y_AXIS));
        centerPanel.setAlignmentX(Component.CENTER_ALIGNMENT); // 중앙 정렬


        centerPanel.add(Box.createVerticalStrut(50)); // 여백 추가

        // 프로필 이미지
        ImageIcon profileIcon = new ImageIcon("images/profile.png"); // 이미지 파일 경로를 확인하세요
        Image profileImage = profileIcon.getImage().getScaledInstance(100, 100, Image.SCALE_SMOOTH);
        JLabel profileLabel = new JLabel(new ImageIcon(profileImage));
        profileLabel.setAlignmentX(Component.CENTER_ALIGNMENT); // 중앙 정렬
        centerPanel.add(Box.createVerticalStrut(50)); // 여백 추가
        centerPanel.add(profileLabel);

        centerPanel.add(Box.createVerticalStrut(50)); // 여백 추가

        // 로그아웃 버튼
        RoundedButton logoutButton = new RoundedButton("로그아웃");
        logoutButton.setPreferredSize(new Dimension(150, 40)); // 버튼 크기 설정
        logoutButton.setMaximumSize(logoutButton.getPreferredSize()); // 최대 크기 설정
        logoutButton.setAlignmentX(Component.CENTER_ALIGNMENT); // 중앙 정렬
        logoutButton.setBackground(Color.lightGray);
        logoutButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                new LoginScreen();
                dispose();
            }
        });

        centerPanel.add(logoutButton);

        centerPanel.add(Box.createVerticalStrut(20)); // 여백 추가

        // 주문내역 버튼
        RoundedButton orderButton = new RoundedButton("주문내역");
        orderButton.setPreferredSize(new Dimension(150, 40)); // 버튼 크기 설정
        orderButton.setMaximumSize(orderButton.getPreferredSize()); // 최대 크기 설정
        orderButton.setAlignmentX(Component.CENTER_ALIGNMENT); // 중앙 정렬
        orderButton.setBackground(Color.lightGray);
        orderButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                 try {
                          new showOrder(user);
                 } catch (SQLException ex) {
                     ex.printStackTrace();
                 }
            }
        });
        centerPanel.add(orderButton);
        centerPanel.add(Box.createVerticalStrut(20)); // 여백 추가

        // 신고내역 버튼
        RoundedButton reportButton = new RoundedButton("신고내역");
        reportButton.setPreferredSize(new Dimension(150, 40)); // 버튼 크기 설정
        reportButton.setMaximumSize(reportButton.getPreferredSize()); // 최대 크기 설정
        reportButton.setAlignmentX(Component.CENTER_ALIGNMENT); // 중앙 정렬
        reportButton.setBackground(Color.lightGray);
        reportButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                try {
                    new showReport(user);
                } catch (SQLException ex) {
                    ex.printStackTrace();
                }
            }
        });
        centerPanel.add(reportButton);

        add(centerPanel, BorderLayout.CENTER);

        // 하단 돌아가기 버튼
        RoundedButton backButton = new RoundedButton("돌아가기");
        backButton.setPreferredSize(new Dimension(150, 40)); // 버튼 크기 설정
        backButton.setMaximumSize(backButton.getPreferredSize()); // 최대 크기 설정
        backButton.setBackground(Color.lightGray);
        backButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                SeatReservation sr = new SeatReservation(user);
                sr.setVisible(true);
                dispose(); // 현재 창 닫기
            }
        });

        JPanel bottomPanel = new JPanel();
        bottomPanel.setLayout(new BoxLayout(bottomPanel, BoxLayout.Y_AXIS));
        bottomPanel.setAlignmentX(Component.CENTER_ALIGNMENT); // 중앙 정렬
        bottomPanel.add(backButton);
        bottomPanel.add(Box.createVerticalStrut(20)); // 여백 추가

        add(bottomPanel, BorderLayout.SOUTH);
    }
}
class showOrder extends JFrame{
    UserVO user = null;
    SeatVO seat = null;
    ArrayList<OrderVO> orderList = null;
    public showOrder(UserVO user) throws SQLException {
        this.user = user;
        JFrame frame = new JFrame();
        setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE);
        setSize(600, 500);
        setLayout(new BorderLayout());

        // 상단 타이틀
        JLabel titleLabel = new JLabel("좌석 정보", SwingConstants.CENTER);
        titleLabel.setFont(new Font("맑은 고딕", Font.BOLD, 20));
        add(titleLabel, BorderLayout.NORTH);

        SeatDao seatDao = new SeatDao();
        seat = seatDao.getUserSeat(user.getUserIdx());

        OrderDAO orderDao = new OrderDAO();
        orderList = orderDao.getOrder(user.getUserIdx());

        JPanel mainPanel = new JPanel();
        mainPanel.setLayout(new BoxLayout(mainPanel, BoxLayout.Y_AXIS));

        if (seat == null) {
            // 좌석 정보가 없을 때 하단에 문구 추가
            JLabel noSeatInfoLabel = new JLabel("금일 좌석 결제 내역이 없습니다.", SwingConstants.CENTER);
            noSeatInfoLabel.setFont(new Font("맑은 고딕", Font.PLAIN, 16));
            add(noSeatInfoLabel, BorderLayout.CENTER);
        } else {
            // 좌석 정보가 있을 때 테이블 설정
            DefaultTableModel seatModel = new DefaultTableModel();
            seatModel.addColumn("좌석 번호");
            seatModel.addColumn("사용 시작 시간");
            seatModel.addColumn("사용 종료 시간");
            seatModel.addColumn("좌석 금액");

            seatModel.addRow(new Object[]{seat.getSeatIdx(), seat.getSeatStartTime(),
                    seat.getSeatEndTime(), seat.getSeatPrice()+"원"});

            JTable seatTable = new JTable(seatModel);
            JScrollPane seatScrollPane = new JScrollPane(seatTable);
            mainPanel.add(seatScrollPane);

            // 두 테이블 사이에 여유 공간 추가
            mainPanel.add(Box.createRigidArea(new Dimension(0, 20)));

            // 주문 내역 설정
            DefaultTableModel orderModel = new DefaultTableModel();
            orderModel.addColumn("주문 일자");
            orderModel.addColumn("주문 음료");
            orderModel.addColumn("가격");

            // 데이터 모델에 데이터 추가
            for (OrderVO order : orderList) {
                orderModel.addRow(new Object[]{order.getOrderDate(), order.getDrinkName(), order.getDrinkPrice()+"원"});
            }

            JTable orderTable = new JTable(orderModel);
            orderTable.setDefaultEditor(Object.class, null); // 편집 비활성화

            JScrollPane orderScrollPane = new JScrollPane(orderTable);

            // 주문 내역 라벨과 스크롤 패널을 포함할 패널 생성
            JPanel orderPanel = new JPanel(new BorderLayout());
            JLabel orderLabel = new JLabel("주문 내역", SwingConstants.CENTER);
            orderLabel.setFont(new Font("맑은 고딕", Font.BOLD, 20));
            orderPanel.add(orderLabel, BorderLayout.NORTH);
            orderPanel.add(orderScrollPane, BorderLayout.CENTER);

            // 주문 내역 패널을 mainPanel에 추가
            mainPanel.add(orderPanel);
        }

        add(mainPanel, BorderLayout.CENTER);

        setVisible(true);
    }
}

class showReport extends JFrame {
    UserVO user = null;
    public showReport(UserVO user) throws SQLException {
        this.user = user;
        JFrame frame = new JFrame();
        setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE);
        setSize(600, 200);
        setLayout(new BorderLayout());

        // 상단 타이틀
        JLabel titleLabel = new JLabel("신고내역", SwingConstants.CENTER);
        titleLabel.setFont(new Font("맑은 고딕", Font.BOLD, 20));
        add(titleLabel, BorderLayout.NORTH);

        ReportDao reportDao = new ReportDao();
        ArrayList<ReportVO> reportList = reportDao.getUserReport(user.getUserIdx());

        if(reportList == null)  return;

        // 테이블에 추가할 데이터를 담을 모델 생성
        DefaultTableModel model = new DefaultTableModel();
        model.addColumn("신고 번호");
        model.addColumn("신고자");
        model.addColumn("신고 항목");
        model.addColumn("신고 일자");
        model.addColumn("처리 상태");



        // 데이터 모델에 데이터 추가
        for (ReportVO report : reportList) {
            model.addRow(new Object[]{report.getReportIdx(), report.getReportingUser(), report.getReportCategory(),
                    report.getReportDate(), report.getReportStatus()});
        }

        // JTable 생성 및 모델 설정
        JTable table = new JTable(model);
        table.setDefaultEditor(Object.class, null); //편집 비활

        // 테이블을 스크롤 가능한 패널에 추가
        JScrollPane scrollPane = new JScrollPane(table);

        // 패널을 프레임에 추가
        add(scrollPane, BorderLayout.CENTER);

        setVisible(true);
    }
}