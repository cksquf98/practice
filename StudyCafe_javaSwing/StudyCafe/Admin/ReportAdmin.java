package StudyCafe.Admin;

import StudyCafe.Button.RoundedButton;
import StudyCafe.Report.ReportDao;
import StudyCafe.Report.ReportVO;

import javax.swing.*;
import javax.swing.table.DefaultTableModel;
import java.awt.*;
import java.awt.event.*;
import java.sql.SQLException;
import java.util.ArrayList;

public class ReportAdmin extends JFrame {
    private JTable reportTable;
    private JComboBox<String> statusComboBox; // 셀렉트 박스 추가
    private JButton confirmButton; // 확인 버튼
    private int selectedReportIdx = -1;
    public ReportAdmin() throws SQLException {
        setTitle("신고 내역 관리");
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setSize(500, 600);


        // 상단 패널 (상단 우측 버튼 포함)
        JPanel topPanel = new JPanel(new BorderLayout());
        JLabel titleLabel = new JLabel("신고 내역", SwingConstants.CENTER);
        titleLabel.setFont(new Font("맑은 고딕", Font.BOLD, 20));
        topPanel.add(titleLabel, BorderLayout.CENTER);

        JPanel bottomPanel = new JPanel(new FlowLayout(FlowLayout.RIGHT)); // 하단 패널 생성
        JLabel desc = new JLabel("처리 상태 변경 :");
        desc.setFont(new Font("맑은 고딕", Font.PLAIN, 14));
        bottomPanel.add(desc);
        statusComboBox = new JComboBox<>(new String[]{"접수완료", "처리중", "처리완료"});
        bottomPanel.add(statusComboBox);

        confirmButton = new JButton("확인");
        confirmButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                String selectedStatus = (String) statusComboBox.getSelectedItem();
                int reportStatus = 0;
                if (selectedStatus.equals("접수완료")) {
                    reportStatus = 0;
                } else if (selectedStatus.equals("처리중")) {
                    reportStatus = 1;
                } else if (selectedStatus.equals("처리완료")) {
                    reportStatus = 2;
                }

                if (selectedReportIdx != -1) {
                    ReportDao reportDao = new ReportDao();
                    try {
                        reportDao.updateStatus(selectedReportIdx, reportStatus);
                        new ReportAdmin();
                        dispose();
                    } catch (SQLException ex) {
                        ex.printStackTrace();
                    }
                }
            }
        });
        bottomPanel.add(confirmButton); // 확인 버튼 추가

        add(topPanel, BorderLayout.NORTH);
        add(bottomPanel, BorderLayout.SOUTH); // 하단 패널 추가
        // 테이블 모델 설정
        DefaultTableModel tableModel = new DefaultTableModel(new Object[]{"신고 번호", "신고자", "카테고리", "신고 날짜", "상태"}, 0);
        reportTable = new JTable(tableModel);
        reportTable.setSelectionMode(ListSelectionModel.SINGLE_SELECTION); // 행 단위 선택
        reportTable.setRowSelectionAllowed(true);
        reportTable.setColumnSelectionAllowed(false);
        reportTable.addMouseListener(new MouseAdapter() {
            @Override
            public void mouseClicked(MouseEvent e) {
                int selectedRow = reportTable.getSelectedRow();
                if (selectedRow != -1) {
                    selectedReportIdx = (int) reportTable.getValueAt(selectedRow, 0);
                    statusComboBox.setVisible(true); // 행을 클릭하면 버튼 보이기
                }
            }
        });

        ReportDao reportDao = new ReportDao();
        ArrayList<ReportVO> reportList = reportDao.getReportAll();


        // 데이터 모델에 데이터 추가
        for (ReportVO report : reportList) {
            tableModel.addRow(new Object[]{report.getReportIdx(), report.getReportingUser(),
                    report.getReportCategory(),report.getReportDate(), report.getReportStatus()});
        }

        // JTable 생성 및 모델 설정
        JTable table = new JTable(tableModel);
        table.setDefaultEditor(Object.class, null); //편집 비활

        // 스크롤 패널에 테이블 추가
        JScrollPane scrollPane = new JScrollPane(reportTable);
        add(scrollPane, BorderLayout.CENTER);

        setVisible(true);
    }
}
