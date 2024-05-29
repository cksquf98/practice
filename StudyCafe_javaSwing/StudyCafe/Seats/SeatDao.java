package StudyCafe.Seats;

import StudyCafe.DB.DBConnection;
import StudyCafe.UserVO;
import oracle.jdbc.OracleTypes;

import java.sql.*;

public class SeatDao {
    Connection conn = null;
    PreparedStatement pstmt = null;
    CallableStatement cstmt = null;
    ResultSet rs = null;
    SeatVO seat;

    public SeatVO getUserSeat (int userIdx) throws SQLException {
        conn = DBConnection.getConnection();
        String sql = "{call getUserSeat(?, ?)}";
        SeatVO seat = null;

        try {
            cstmt = conn.prepareCall(sql);
            cstmt.setInt(1, userIdx);
            cstmt.registerOutParameter(2, OracleTypes.CURSOR);
            cstmt.execute();

            rs = (ResultSet) cstmt.getObject(2);

            if (rs != null && rs.next()) {
                seat = new SeatVO();
                seat.setSeatIdx(rs.getInt("seat_idx"));
                seat.setSeatStartTime(rs.getString("seat_start_time"));
                seat.setSeatEndTime(rs.getString("seat_end_time"));
                seat.setSeatPrice(rs.getInt("seat_price"));
                seat.setWaitingUser(rs.getInt("waiting_user"));
                seat.setUserIdx(rs.getInt("user_idx"));
            }
        } catch (SQLException ex) {
            ex.printStackTrace(); // 예외 세부 정보 출력
        } finally {
            closeResources();
        }

        return seat;
    }

    public int getUserIdx(int selectedSeatNumber) throws SQLException {
        conn = DBConnection.getConnection();
        String sql = "{? = call getUserIdx(?)}";
        int userIdx = -1;

        try {
            cstmt = conn.prepareCall(sql);
            cstmt.registerOutParameter(1, OracleTypes.NUMBER);
            cstmt.setInt(2, selectedSeatNumber);
            cstmt.execute();

            userIdx = cstmt.getInt(1);
        } catch (SQLException ex) {
            ex.printStackTrace(); // 예외 세부 정보 출력
        } finally {
            closeResources();
        }

        return userIdx;
    }
    public int insertReport(int userIdx, int seatNumber, int selectedOption) throws SQLException {
        conn = DBConnection.getConnection();
        int result = -1;
        try {
            CallableStatement cstmt = conn.prepareCall("{call InsertReport(?, ?, ?, ?)}");
            cstmt.setInt(1, userIdx);
            cstmt.setInt(2, seatNumber);
            cstmt.setInt(3, selectedOption);
            cstmt.registerOutParameter(4, Types.INTEGER); // 결과
            cstmt.execute();
            result = cstmt.getInt(4); //결과를 변수에 저장
        } catch (SQLException ex) {
            ex.printStackTrace();
        } finally {
            closeResources();
        }
        return result;
    }
    private void closeResources() {
            try {
                if (rs != null) rs.close();
                if (pstmt != null) pstmt.close();
                if (conn != null) conn.close();
            } catch (SQLException e) {
                e.printStackTrace();
            }
        }
}

