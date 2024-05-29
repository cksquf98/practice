package StudyCafe;

import java.sql.SQLException;

public class UserVO {
    UserDao userDao = new UserDao();
    private int userIdx;
    private String userName;
    private String userPhone;
    private String userPw;
    private int reportCount;
    private String admin;

    // Getters and Setters
    public int getUserIdx() {
        return userIdx;
    }

    public void setUserIdx(int userIdx) {
        this.userIdx = userIdx;
    }

    public String getUserName() {
        return userName;
    }

    public void setUserName(String userName) {
        this.userName = userName;
    }

    public String getUserPhone() {
        return userPhone;
    }

    public void setUserPhone(String userPhone) {
        this.userPhone = userPhone;
    }

    public String getUserPw() {
        return userPw;
    }

    public void setUserPw(String userPw) {
        this.userPw = userPw;
    }

    public int getReportCount() {
        return reportCount;
    }

    public void setReportCount(int reportCount) {
        this.reportCount = reportCount;
    }

    public String getAdmin() {
        return admin;
    }

    public void setAdmin(String admin) {
        this.admin = admin;
    }

    public int getUsingUser(int userIdx) throws SQLException {
        return userDao.CheckUsingUser(userIdx);
    }
    public int getReportCount(int userIdx) throws SQLException {
        return userDao.CheckReportCount(userIdx);
    }
}