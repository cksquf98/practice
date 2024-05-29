package Customer;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.HashMap;
import java.util.Iterator;
import java.util.LinkedHashMap;
import java.util.Map;
import java.util.Map.Entry;

public class Kiosk extends JFrame {
    private JPanel mainPanel;
    private JPanel drinkPanel;
    private JPanel orderPanel;
    private JPanel bottomPanel;
    private JPanel orderListPanel;
    private JScrollPane orderScrollPane;
    private JLabel totalLabel;
    private JButton paymentButton;
    private JButton nextButton;

    private Map<String, Integer> drinkPrice;
    private Map<String, Integer> orderList;
    private int totalAmount;

    public Kiosk() {
        // GUI 초기화
        setTitle("음료 키오스크");
        setSize(700, 600);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLayout(new BorderLayout());

        // 음료 및 가격 초기화 (HashMap 사용)
        drinkPrice = new LinkedHashMap<>();
        drinkPrice.put("아메리카노", 2500);
        drinkPrice.put("카페라떼", 3000);
        drinkPrice.put("생수                   ", 1000);
        drinkPrice.put("오렌지쥬스       ", 3500);

        drinkPrice.put("레몬에이드       ", 4000);
        drinkPrice.put("자몽에이드       ", 4000);
        drinkPrice.put("딸기에이드       ", 4000);
        drinkPrice.put("청포도에이드   ", 4000);
        
        drinkPrice.put("블루베리스무디", 4500);
        drinkPrice.put("망고스무디       ", 4500);
        drinkPrice.put("딸기스무디       ", 4500);
        drinkPrice.put("키위스무디       ", 4500);
                

        String []imgName = {"Americano.JPG", "Latte.JPG", 
        					"Water.PNG", "Orange.JPG",
        					"Lemonade.JPG", "Grapefruit.JPG",
        					"StrawJuice.JPG", "GreenGrape.JPG",
        					"Blueberry.PNG", "Mango.JPG",
        					"StrawSmoothie.JPG", "Kiwi.JPG"

        					};

        orderList = new HashMap<>();
        totalAmount = 0;

        // 상단 음료 패널
        drinkPanel = new JPanel();
        drinkPanel.setLayout(new GridLayout(3, 4));

        int i = 0;
        for (String drink : drinkPrice.keySet()) {
            // 음료 버튼 생성
            JButton drinkButton = new JButton();
            drinkButton.setLayout(new BorderLayout());

            // 음료 이미지
            ImageIcon drinkIcon = new ImageIcon("Images/" + imgName[i++]);
            JLabel drinkImageLabel = new JLabel(drinkIcon);
            drinkImageLabel.setHorizontalAlignment(SwingConstants.CENTER);
            drinkButton.add(drinkImageLabel, BorderLayout.CENTER);

            // 음료 이름과 가격
            JLabel drinkLabel = new JLabel("<html>" + drink + "<br>" + drinkPrice.get(drink) + "원</html>", SwingConstants.CENTER);
            drinkButton.add(drinkLabel, BorderLayout.SOUTH);

            // 버튼에 액션 리스너 추가
            drinkButton.setActionCommand(drink);
            drinkButton.addActionListener(new ActionListener() {
                @Override
                public void actionPerformed(ActionEvent e) {
                    String selectedDrink = e.getActionCommand();
                    int price = drinkPrice.get(selectedDrink);
                    String[] options = {"Hot", "Ice"};
                    if (drink.equals("아메리카노") || drink.equals("카페라떼")) {
                    	int choice = JOptionPane.showOptionDialog(null, selectedDrink + " 종류를 선택해주세요.\n", "Drink Type",
                    			JOptionPane.DEFAULT_OPTION, JOptionPane.INFORMATION_MESSAGE, null, options, options[0]);

                    	if (choice >= 0) {
                    		String drinkType = options[choice];
                    		addOrderItem(selectedDrink + "(" + drinkType + ")", price);
                    	}
                    }
                    else 
                    	addOrderItem(selectedDrink, price);
                    totalAmount += price;
                    totalLabel.setText("음료 금액: " + totalAmount + " 원");
           
                }
            });

            drinkPanel.add(drinkButton);
        }

        add(drinkPanel, BorderLayout.NORTH);

        // 하단 주문 패널
        orderPanel = new JPanel();
        orderPanel.setLayout(new BorderLayout());

        orderListPanel = new JPanel();
        orderListPanel.setLayout(new BoxLayout(orderListPanel, BoxLayout.Y_AXIS));

        orderScrollPane = new JScrollPane(orderListPanel);
        orderPanel.add(orderScrollPane, BorderLayout.CENTER);

        add(orderPanel, BorderLayout.CENTER);

        // 하단 결제 패널
        bottomPanel = new JPanel();
        bottomPanel.setLayout(new FlowLayout());

        totalLabel = new JLabel("음료 금액: 0원", SwingConstants.CENTER);
        bottomPanel.add(totalLabel);

        paymentButton = new JButton("결제");
        paymentButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                if (!orderList.isEmpty()) {
                    JOptionPane.showMessageDialog(null, "결제화면으로 넘어갑니다\n" + totalAmount + "원");
                    orderList.clear();
                    orderListPanel.removeAll();
                    totalAmount = 0;
                    totalLabel.setText("음료 금액: 0원");
                    revalidate();
                    repaint();
                } else {
                    JOptionPane.showMessageDialog(null, "선택한 음료가 없습니다.");
                    // 선택한 음료가 없으면 이 페이지에 그냥 있을 것(추가 코드 없음)
                }
            }
        });
        bottomPanel.add(paymentButton);

        nextButton = new JButton("넘어가기");
        nextButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                if (orderList.isEmpty()) {
                    JOptionPane.showMessageDialog(null, "음료를 선택하지 않았습니다.\n  다음 화면으로 넘어갑니다.");
                    // 다음 단계로 넘어가기(좌석 결제 화면으로 이동) 
                }else {
                	JOptionPane.showMessageDialog(null, "  음료를 선택하지 않고\n다음 화면으로 넘어갑니다.");
                }
            }
        });
        bottomPanel.add(nextButton);

        add(bottomPanel, BorderLayout.SOUTH);
    }

    
   
    private void addOrderItem(String drink, int price) {
        if (orderList.containsKey(drink)) {
            int quantity = orderList.get(drink);
            orderList.put(drink, quantity + 1);
            updateOrderItem(drink);
        }
        else {
        	
            orderList.put(drink, 1);
            createOrderItem(drink, price);
        }
    }

    private void createOrderItem(String drink, int price) {
        JPanel orderItemPanel = new JPanel();
        orderItemPanel.setLayout(new FlowLayout(FlowLayout.LEFT));
        orderItemPanel.setPreferredSize(new Dimension(600, 50));
        orderItemPanel.setMaximumSize(new Dimension(600, 50));
        
        String whiteSpace = "               ";
        JLabel orderItemLabel = new JLabel(drink + whiteSpace + 1 + "잔" + whiteSpace + price + "원");
        orderItemLabel.setPreferredSize(new Dimension(300, 50));
        orderItemPanel.add(orderItemLabel);

        JPanel quantityPanel = new JPanel();
        quantityPanel.setLayout(new FlowLayout());

        JButton minusButton = new JButton("-");
        minusButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                int quantity = orderList.get(drink);
                if (quantity > 1) {
                    orderList.put(drink, quantity - 1);
                    totalAmount -= price;
                    updateOrderItem(drink);
                }
                if (quantity - 1 == 1) {
                    minusButton.setEnabled(false);
                }
                totalLabel.setText("음료 금액: " + totalAmount + "원");
            }
        });
        minusButton.setEnabled(false); // 초기 수량은 1이므로 비활성화
        quantityPanel.add(minusButton);

        JLabel quantityLabel = new JLabel("1");
        quantityPanel.add(quantityLabel);

        JButton plusButton = new JButton("+");
        plusButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                int quantity = orderList.get(drink);
                orderList.put(drink, quantity + 1);
                
                totalAmount += price;
                minusButton.setEnabled(true);
                
                updateOrderItem(drink);
               
                
                totalLabel.setText("음료 금액: " + totalAmount + "원");
            }
        });

        quantityPanel.add(plusButton);

        // 취소 버튼과 수량 조절 버튼 간 여백 주기
        JLabel spaceLabel = new JLabel("                           ");
        quantityPanel.add(spaceLabel);

        JButton cancelButton = new JButton("취소");
        cancelButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                int quantity = orderList.get(drink);
                totalAmount -= price * quantity;
                orderList.remove(drink);
                orderListPanel.remove(orderItemPanel);
                totalLabel.setText("음료 금액: " + totalAmount + "원");
                revalidate();
                repaint();
            }
        });
        quantityPanel.add(cancelButton);
        
        orderItemPanel.add(quantityPanel);
        
        orderListPanel.add(orderItemPanel);
        revalidate();
        repaint();
    }
    
    

    private void updateOrderItem(String drink) {
        for (Component component : orderListPanel.getComponents()) {
            if (component instanceof JPanel) {
                JPanel orderItemPanel = (JPanel) component;
                JLabel orderItemLabel = (JLabel) orderItemPanel.getComponent(0);
                String labelText = orderItemLabel.getText();
                if (labelText.startsWith(drink)) {
                	int quantity = orderList.get(drink);
                	String whiteSpace = "               ";
                	if (drink.equals("아메리카노(Hot)") || drink.equals("아메리카노(Ice)") || drink.equals("카페라떼(Hot)") || drink.equals("카페라떼(Ice)"))
                		orderItemLabel.setText(drink + whiteSpace + quantity + "잔" + whiteSpace + drinkPrice.get(drink.split("\\(")[0]) * quantity + "원");
                    else
                       	orderItemLabel.setText(drink + whiteSpace + quantity + "잔" + whiteSpace + drinkPrice.get(drink) * quantity + "원");
                    JPanel quantityPanel = (JPanel) orderItemPanel.getComponent(1);
                    JLabel quantityLabel = (JLabel) quantityPanel.getComponent(1);
                    quantityLabel.setText(String.valueOf(quantity));

                    JButton minusButton = (JButton) quantityPanel.getComponent(0);
                    minusButton.setEnabled(quantity > 1);
                        
                    break;
                }
            }
        }
        revalidate();
        repaint();
    }
    
    private void updateOrderItem2(String drink) {
    	for (Component component : orderListPanel.getComponents()) {
    		if (component instanceof JPanel) {
    			JPanel orderItemPanel = (JPanel) component;
    			JLabel orderItemLabel = (JLabel) orderItemPanel.getComponent(0);
    			int price = 2500;
    			if (drink.equals("카페라떼(Hot)") || drink.equals("카페라떼(Ice)"))
    				price = 3000;
    			int quantity = orderList.get(drink);
    			String whiteSpace = "               ";
    			orderItemLabel.setText(drink + whiteSpace + quantity + "잔" + whiteSpace + price * quantity + "원");
        
    			
    			JPanel quantityPanel = (JPanel) orderItemPanel.getComponent(1);
    			JLabel quantityLabel = (JLabel) quantityPanel.getComponent(1);
    			quantityLabel.setText(String.valueOf(quantity));
        
    			JButton minusButton = (JButton) quantityPanel.getComponent(0);
    			minusButton.setEnabled(quantity > 1);
        
        
    	}}
    	revalidate();
        repaint();
    }
    
    public static void main(String[] args) {
        SwingUtilities.invokeLater(new Runnable() {
            @Override
            public void run() {
                new Kiosk().setVisible(true);
            }
        });
    }
    
}


