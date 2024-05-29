package StudyCafe.Order;

import java.sql.Date;

public class OrderVO {
    OrderDAO orderDao = new OrderDAO();

    private int orderIdx;
    private int userIdx;
    private int drinkIdx;
    private String orderDate;
    private String drinkName;
    private int drinkPrice;

    public OrderDAO getOrderDao() {
        return orderDao;
    }

    public void setOrderDao(OrderDAO orderDao) {
        this.orderDao = orderDao;
    }

    public int getOrderIdx() {
        return orderIdx;
    }

    public void setOrderIdx(int orderIdx) {
        this.orderIdx = orderIdx;
    }

    public int getUserIdx() {
        return userIdx;
    }

    public void setUserIdx(int userIdx) {
        this.userIdx = userIdx;
    }

    public int getDrinkIdx() {
        return drinkIdx;
    }

    public void setDrinkIdx(int drinkIdx) {
        this.drinkIdx = drinkIdx;
    }

    public String getOrderDate() {
        return orderDate;
    }

    public void setOrderDate(String orderDate) {
        this.orderDate = orderDate;
    }

    public String getDrinkName() {
        return drinkName;
    }

    public void setDrinkName(String drinkName) {
        this.drinkName = drinkName;
    }

    public int getDrinkPrice() {
        return drinkPrice;
    }

    public void setDrinkPrice(int drinkPrice) {
        this.drinkPrice = drinkPrice;
    }
}
