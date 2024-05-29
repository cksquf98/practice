package StudyCafe.Order;

import StudyCafe.DB.DBConnection;
import StudyCafe.Order.OrderVO;
import StudyCafe.Report.ReportVO;
import StudyCafe.Seats.SeatVO;
import StudyCafe.UserVO;

import java.sql.Connection;
import java.sql.Date;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;

public class OrderDAO {

    // 주문 및 좌석 예약 메서드
    public void placeOrderWithSeat(OrderVO order, SeatVO seat) {
        Connection conn = null;
        PreparedStatement pstmtOrder = null;
        PreparedStatement pstmtSeat = null;

        try {
            conn = DBConnection.getConnection();
            conn.setAutoCommit(false); // 트랜잭션 시작

            // 좌석 정보 삽입
            String sqlSeat = "INSERT INTO Seats (seat_idx, user_idx, seat_start_time, seat_end_time) VALUES (?, ?, ?, ?)";
            pstmtSeat = conn.prepareStatement(sqlSeat);
            pstmtSeat.setInt(1, seat.getSeatIdx());
            pstmtSeat.setInt(2, seat.getUserIdx());
            pstmtSeat.setString(3, seat.getSeatStartTime());
            pstmtSeat.setString(4, seat.getSeatEndTime());
            pstmtSeat.executeUpdate();

            // 주문 정보 삽입
            String sqlOrder = "INSERT INTO Orders (user_idx, drink_idx, order_date) VALUES (?, ?, ?)";
            pstmtOrder = conn.prepareStatement(sqlOrder);
            pstmtOrder.setInt(1, order.getUserIdx());
            pstmtOrder.setInt(2, order.getDrinkIdx());
            pstmtOrder.setString(3, order.getOrderDate());
            pstmtOrder.executeUpdate();

            conn.commit(); // 트랜잭션 커밋
        } catch (SQLException e) {
            if (conn != null) {
                try {
                    conn.rollback(); // 오류 발생 시 롤백
                } catch (SQLException ex) {
                    ex.printStackTrace();
                }
            }
            e.printStackTrace();
        } finally {
            close(conn, pstmtOrder, null);
            close(conn, pstmtSeat, null);
        }
    }

    public ArrayList<OrderVO> getOrder(int userIdx) {
        Connection conn = null;
        PreparedStatement pstmt = null;
        ResultSet rs = null;

        ArrayList<OrderVO> orderList = new ArrayList<>();
        String query = "SELECT order_idx,to_char(order_date,'YYYY-MM-DD HH24:MI:SS') as order_date, drink_name, drink_price " +
                "FROM Orders inner join Menu on (Orders.drink_idx = Menu.drink_idx)" +
                "WHERE users_user_idx = ?";

        try {
            conn = DBConnection.getConnection();
            pstmt = conn.prepareStatement(query);
            pstmt.setInt(1, userIdx);
            rs = pstmt.executeQuery();

            while(rs.next()) {
                OrderVO orderVO = new OrderVO();
                orderVO.setOrderIdx(rs.getInt("order_idx"));
                orderVO.setOrderDate(rs.getString("order_date"));
                orderVO.setDrinkName(rs.getString("drink_name"));
                orderVO.setDrinkPrice(rs.getInt("drink_price"));

                orderList.add(orderVO);

            }

        } catch (SQLException ex) {
            ex.printStackTrace();
        }  finally {
            close(conn, pstmt, rs);
        }
        return orderList;
    }

    // 자원 닫기 메서드
    private void close(Connection conn, PreparedStatement pstmt, ResultSet rs) {
        try {
            if (rs != null) rs.close();
            if (pstmt != null) pstmt.close();
            if (conn != null) conn.close();
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }
}