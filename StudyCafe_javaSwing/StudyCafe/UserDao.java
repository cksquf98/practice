package StudyCafe;

import StudyCafe.DB.DBConnection;
import oracle.jdbc.*;

import java.sql.*;


public class UserDao {
    Connection conn = null;
    CallableStatement cstmt = null;
    ResultSet rs = null;
    UserVO user = null;

    public UserVO getUser(String phone, String password) throws SQLException {
        conn = DBConnection.getConnection();
        String sql = "{call UserManagementPackage.getUser(?, ?, ?)}";

        try {
            cstmt = conn.prepareCall(sql);
            cstmt.setString(1, phone);
            cstmt.setString(2, password);
            cstmt.registerOutParameter(3, OracleTypes.CURSOR);
            cstmt.execute();

            rs = (ResultSet) cstmt.getObject(3);

            if (rs != null && rs.next()) {
                user = new UserVO();
                user.setUserIdx(rs.getInt(1));
                user.setUserName(rs.getString(2));
                user.setUserPhone(rs.getString(3));
                user.setReportCount(rs.getInt(4));
                user.setAdmin(rs.getString(5));
            }
        } catch (SQLException ex) {
            ex.printStackTrace(); // 예외 세부 정보 출력
        } finally {
            closeResources();
        }

        return user;
    }

    public int CreateUser(String name, String phone, String pw) throws SQLException {
        conn = DBConnection.getConnection();
        String sql = "{call UserManagementPackage.CreateUser(?, ?, ?, ?)}";

        try {
            cstmt = conn.prepareCall(sql);
            cstmt.setString(1, name);
            cstmt.setString(2, phone);
            cstmt.setString(3, pw);
            cstmt.registerOutParameter(4, Types.INTEGER);
            cstmt.execute();

            int result = cstmt.getInt(4);
            if (result == 1) {
                System.out.println("User inserted successfully.");
            } else if (result == -1) {
                System.out.println("Phone number already exists. Cannot create user.");
            } else {
                System.out.println("Failed to insert user.");
            }
            return result;
        } catch (SQLException ex) {
            ex.printStackTrace(); // 예외 세부 정보 출력
        } finally {
            closeResources();
        }

        return -1;
    }
    public int CheckUsingUser(int userIdx) throws SQLException {
        conn = DBConnection.getConnection();
        String sql = "{? = call UserManagementPackage.CheckUsingUser(?)}";
        int seatIdx = -1;

        try {
            cstmt = conn.prepareCall(sql);
            cstmt.registerOutParameter(1, Types.INTEGER);
            cstmt.setInt(2, userIdx);
            cstmt.execute();

            seatIdx = cstmt.getInt(1);
            } catch (SQLException ex) {
                ex.printStackTrace(); // 예외 세부 정보 출력
            } finally {
                closeResources();
            }
        return seatIdx;
    }

    public int CheckReportCount(int userIdx) throws SQLException {
        conn = DBConnection.getConnection();
        String sql = "{? = call UserManagementPackage.CheckReportCount(?)}";
        int reportCount = -1;

        try {
            cstmt = conn.prepareCall(sql);
            cstmt.registerOutParameter(1, Types.INTEGER);
            cstmt.setInt(2, userIdx);
            cstmt.execute();

            reportCount = cstmt.getInt(1);
        } catch (SQLException ex) {
            ex.printStackTrace(); // 예외 세부 정보 출력
        } finally {
            closeResources();
        }

        return reportCount;
    }
    private void closeResources() {
        try {
            if (rs != null) rs.close();
            if(cstmt != null) cstmt.close();
            if (conn != null) conn.close();
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }
}

