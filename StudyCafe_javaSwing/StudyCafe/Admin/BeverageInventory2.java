package StudyCafe.Admin;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.HashMap;
import java.util.Map;

public class BeverageInventory2 extends JFrame {
    private JPanel mainPanel;
    private Map<String, Beverage> beverages;

    public BeverageInventory2() {
        setTitle("음료 재고 관리");
        setSize(700, 600);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        beverages = new HashMap<>();
        mainPanel = new JPanel();
        mainPanel.setLayout(new BoxLayout(mainPanel, BoxLayout.Y_AXIS));
        
        
        
        JScrollPane scrollPane = new JScrollPane(mainPanel);
        scrollPane.setVerticalScrollBarPolicy(JScrollPane.VERTICAL_SCROLLBAR_ALWAYS);
        add(scrollPane, BorderLayout.CENTER);

        addBeveragePanel("Hot 아메리카노", "Images/Americano.JPG", 3); 
        addBeveragePanel("Ice 아메리카노", "Images/IceAmericano.JPG", 5);
        addBeveragePanel("Hot 카페라떼", "Images/Latte.JPG", 10); 
        addBeveragePanel("Ice 카페라떼", "Images/IceLatte.JPG", 7);
        addBeveragePanel("생수", "Images/Water.PNG", 3); 
        addBeveragePanel("오렌지쥬스", "Images/Orange.JPG", 5);
        
        addBeveragePanel("레몬에이드", "Images/Lemonade.JPG", 5); 
        addBeveragePanel("자몽에이드", "Images/Grapefruit.JPG", 5);
        addBeveragePanel("딸기에이드", "Images/StrawJuice.JPG", 5); 
        addBeveragePanel("청포도에이드", "Images/GreenGrape.JPG", 5);
        
        addBeveragePanel("블루베리스무디", "Images/Blueberry.PNG", 5);
        addBeveragePanel("망고스무디", "Images/Mango.JPG", 5);
        addBeveragePanel("딸기스무디", "Images/StrawSmoothie.JPG", 5);
        addBeveragePanel("키위스무디", "Images/Kiwi.JPG", 5);
        
        
        
        JButton confirmButton = new JButton("확인");
        confirmButton.setAlignmentX(Component.CENTER_ALIGNMENT);
        confirmButton.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                // 확인 버튼을 눌렀을 때 수행할 작업
                JOptionPane.showMessageDialog(mainPanel, "확인 버튼이 클릭되었습니다.");
            }
        });

        JPanel bottomPanel = new JPanel();
        bottomPanel.setLayout(new BoxLayout(bottomPanel, BoxLayout.Y_AXIS));
        bottomPanel.add(Box.createRigidArea(new Dimension(0, 20)));
        bottomPanel.add(confirmButton);
        bottomPanel.add(Box.createRigidArea(new Dimension(0, 20)));

        add(bottomPanel, BorderLayout.SOUTH);
    }

    private void addBeveragePanel(String name, String imagePath, int stock) {
        Beverage beverage = new Beverage(name, imagePath, stock);
        beverages.put(name, beverage);

        JPanel panel = new JPanel(new GridBagLayout());
        GridBagConstraints gbc = new GridBagConstraints();
        gbc.insets = new Insets(5, 5, 5, 5);

        // Panel for image and name
        JPanel imageNamePanel = new JPanel();
        imageNamePanel.setLayout(new BoxLayout(imageNamePanel, BoxLayout.Y_AXIS));
        JLabel imageLabel = new JLabel(new ImageIcon(imagePath));
        JLabel nameLabel = new JLabel(name);
//        nameLabel.setAlignmentX(Component.CENTER_ALIGNMENT);
        nameLabel.setAlignmentX(Component.LEFT_ALIGNMENT);
        imageNamePanel.add(imageLabel);
        imageNamePanel.add(nameLabel);

        JLabel stockLabel = new JLabel("재고 수량: " + stock);
        beverage.setStockLabel(stockLabel);
        updateStockLabelColor(beverage);

        JButton orderButton = new JButton("주문하기");
        orderButton.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                orderBeverage(beverage);
            }
        });

        // 음료 위치와 이름 (왼쪽)
        gbc.gridx = 0;
        gbc.gridy = 0;
        gbc.gridheight = 2;
        gbc.anchor = GridBagConstraints.EAST;
        panel.add(imageNamePanel, gbc);

        // 재고 수량 위치 (가운데)
        gbc.gridx = 1;
        gbc.gridy = 1;
        gbc.gridheight = 1;
        gbc.anchor = GridBagConstraints.CENTER;
        panel.add(stockLabel, gbc);

        // 주문 버튼 위치 (오른쪽)
        gbc.gridx = 50;
        gbc.anchor = GridBagConstraints.WEST;
        panel.add(orderButton, gbc);

        panel.setMaximumSize(new Dimension(600, 150));
        mainPanel.add(panel);

        JSeparator separator = new JSeparator();
        separator.setMaximumSize(new Dimension(600, 1));
        mainPanel.add(separator);
        mainPanel.revalidate();
    }

    private void orderBeverage(Beverage beverage) {
        JDialog orderDialog = new JDialog(this, "주문하기 - " + beverage.getName(), true);
        orderDialog.setSize(300, 200);
        orderDialog.setLayout(new FlowLayout());

        JLabel orderLabel = new JLabel("주문 수량:");
        JTextField quantityField = new JTextField("5", 5);
        JButton plusButton = new JButton("+");
        JButton minusButton = new JButton("-");

        plusButton.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                int quantity = Integer.parseInt(quantityField.getText());
                quantityField.setText(String.valueOf(++quantity));
            }
        });

        minusButton.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                int quantity = Integer.parseInt(quantityField.getText());
                if (quantity > 1) {
                    quantityField.setText(String.valueOf(--quantity));
                }
            }
        });

        JButton confirmButton = new JButton("확인");
        confirmButton.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                int quantity = Integer.parseInt(quantityField.getText());
                beverage.setStock(beverage.getStock() + quantity);
                beverage.getStockLabel().setText("재고 수량: " + beverage.getStock());
                updateStockLabelColor(beverage);
                orderDialog.dispose();
            }
        });

        orderDialog.add(orderLabel);
        orderDialog.add(minusButton);
        orderDialog.add(quantityField);
        orderDialog.add(plusButton);
        orderDialog.add(confirmButton);

        orderDialog.setVisible(true);
    }

    private void updateStockLabelColor(Beverage beverage) {
        if (beverage.getStock() <= 5) {
            beverage.getStockLabel().setForeground(Color.RED);
        } else {
            beverage.getStockLabel().setForeground(Color.BLACK);
        }
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(new Runnable() {
            public void run() {
                new BeverageInventory2().setVisible(true);
            }
        });
    }

    class Beverage {
        private String name;
        private String imagePath;
        private int stock;
        private JLabel stockLabel;

        public Beverage(String name, String imagePath, int stock) {
            this.name = name;
            this.imagePath = imagePath;
            this.stock = stock;
        }

        public String getName() {
            return name;
        }

        public int getStock() {
            return stock;
        }

        public void setStock(int stock) {
            this.stock = stock;
        }

        public JLabel getStockLabel() {
            return stockLabel;
        }

        public void setStockLabel(JLabel stockLabel) {
            this.stockLabel = stockLabel;
        }
    }
}
