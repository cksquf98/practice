package StudyCafe.Report;

import StudyCafe.DB.DBConnection;
import StudyCafe.UserVO;
import oracle.jdbc.*;

import java.sql.*;
import java.util.ArrayList;

public class ReportDao {
    Connection conn = null;
    PreparedStatement pstmt = null;
    CallableStatement cstmt = null;
    ResultSet rs = null;
    ReportVO reportVO = null;

    public ArrayList<ReportVO> getReportAll() throws SQLException {
        ArrayList<ReportVO> reportList = new ArrayList<>();

        conn = DBConnection.getConnection();
        String sql = "{call GETREPORTALL(?)}";

        try {
            cstmt = conn.prepareCall(sql);
            cstmt.registerOutParameter(1, OracleTypes.CURSOR);
            cstmt.execute();

            // ResultSet으로 변환
            rs = (ResultSet) cstmt.getObject(1);

            if (rs != null) {
                while (rs.next()) {
                    ReportVO reportVO = new ReportVO();
                    reportVO.setReportIdx(rs.getInt("report_idx"));
                    reportVO.setReportingUser(rs.getString("reporting_user"));
                    reportVO.setReportCategory(rs.getInt("report_category"));
                    reportVO.setReportDate(rs.getString("report_date"));
                    reportVO.setReportStatus(rs.getInt("report_status"));

                    reportList.add(reportVO);
                }
            }
            else {
                System.out.println("rs is null");
            }
        } catch (SQLException ex) {
            ex.printStackTrace(); // 예외 세부 정보 출력
        } finally {
            closeResources();
        }

        return reportList;
    }
    public ArrayList<ReportVO> getUserReport(int userIdx) throws SQLException {
        ArrayList<ReportVO> reportList = new ArrayList<>();

        conn = DBConnection.getConnection();
        String sql = "{call getUserReport(?, ?)}";

        try {
            cstmt = conn.prepareCall(sql);
            cstmt.setInt(1, userIdx);
            cstmt.registerOutParameter(2, OracleTypes.CURSOR);
            cstmt.execute();

            rs = (ResultSet) cstmt.getObject(2);

            if (rs != null) {
                while (rs.next()) {
                    ReportVO reportVO = new ReportVO();
                    reportVO.setReportIdx(rs.getInt("report_idx"));
                    reportVO.setReportingUserIdx(rs.getInt("reporting_user_idx"));
                    reportVO.setReportingUser(rs.getString("reporting_user"));
                    reportVO.setReportCategory(rs.getInt("report_category"));
                    reportVO.setReportDate(rs.getString("report_date"));
                    reportVO.setReportStatus(rs.getInt("report_status"));

                    reportList.add(reportVO);
                }
            } else {
                System.out.println("rs is null");
            }
        } catch (SQLException ex) {
            ex.printStackTrace(); // 예외 세부 정보 출력
        } finally {
            closeResources();
        }

        return reportList;
    }
    public void updateStatus(int reportIdx, int reportStatus) throws SQLException {
        conn = DBConnection.getConnection();
        String query = "UPDATE Reports SET report_status = ? WHERE report_idx = ?";
        try {
            pstmt = conn.prepareStatement(query);
            pstmt.setInt(1, reportStatus);
            pstmt.setInt(2, reportIdx);
            pstmt.executeUpdate();
            conn.commit();
            System.out.println("ReportStatus update successfully.");
        } catch (SQLException ex) {
            ex.printStackTrace();
            conn.rollback();
        } finally {
            closeResources();
        }
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
