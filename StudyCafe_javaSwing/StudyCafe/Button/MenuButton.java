//package StudyCafe.Button;
//
//import StudyCafe.BeverageKiosk;
//
//import javax.swing.*;
//import java.awt.*;
//import java.awt.event.*;
//
//public class MenuButton extends JButton implements ActionListener{
//    private ImageIcon image;
//    private String menuName;
//    private boolean isSelected = false;  // 음료가 선택되었는지 나타내는 상태변수
//    private BeverageKiosk kiosk; // BeverageKiosk에 접근하기 위한 변수
//
//    public MenuButton(ImageIcon image, String menuName, BeverageKiosk kiosk) {
//        this.image = image;
//        this.menuName = menuName;
//        this.kiosk = kiosk;
//
//        setPreferredSize(new Dimension(150, 200)); // 패널 크기 설정
//        setBackground(Color.WHITE);
//        //setLayout(new BorderLayout());
//
//        // 버튼 텍스트 설정
//        //setText(menuName);
//        //패널에 MouseListener 추가
//        addActionListener(this);
//    }
//
//    @Override
//    protected void paintComponent(Graphics g) {
//        super.paintComponent(g);
//
//        //패널 크기를 기준으로 둥근 사각형 테두리 그리기
//        int arcWidth = 10;
//        int arcHeight = 10;
//        g.drawRoundRect(0,  0,  getWidth()-1, getHeight() -1, arcWidth, arcHeight);
//        // 이미지를 패널에 그립니다.
//        if (image != null) {
//            int x = (getWidth() - image.getIconWidth()) / 2;
//            int y = 10;
//            image.paintIcon(this, g, x, y);
//        }
//
//        // 메뉴 이름을 패널 하단에 그립니다.
//        if (menuName != null) {
//            FontMetrics metrics = g.getFontMetrics();
//            int nameWidth = metrics.stringWidth(menuName);
//            int x = (getWidth() - nameWidth) / 2;
//            int y = getHeight() - 20;
//            g.drawString(menuName, x, y);
//        }
//    }
//
//    // 마우스 클릭 이벤트 처리
//    @Override
//    public void actionPerformed(ActionEvent e) {
//    	isSelected = !isSelected;  // 현재 선택 상태를 토글
//
//    	// 선택 상태에 따라 선택한 음료를 BeverageKiosk에 전달하여 주문 내역을 업데이트
//    	if (isSelected) {
//    		kiosk.addSelectedBeverage(menuName);
//    	}
//    	else {
//    		kiosk.removeSelectedBeverage(menuName);
//    	}
//    	// 주문 내역을 업데이트
//    	kiosk.updateOrderList();
//
//    	//JOptionPane.showMessageDialog(this, this.menuName + "가 선택 되었습니다.");
//    	repaint();  //패널을 다시 그려서 선택 상태를 반영
//    }
//
//
//    public boolean isSelected() {
//    	return isSelected;
//    }
//}
