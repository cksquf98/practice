package StudyCafe.DB;

import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.io.Reader;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
import java.util.Properties;

public class DBConnection {

    private DBConnection() {
    }

    public static Connection getConnection() throws SQLException {
        Properties properties = new Properties();
        Reader reader;
        try {
            reader = new FileReader("lib/oracle.properties");
            properties.load(reader);
        } catch (FileNotFoundException e1) {
            System.out.println("예외: 지정한 파일을 찾을 수 없습니다: " + e1.getMessage());
            e1.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        }

        String driverName = properties.getProperty("driver");
        String url = properties.getProperty("url");
        String user = properties.getProperty("user");
        String pwd = properties.getProperty("password");

        try {
            Class.forName(driverName);
        } catch (ClassNotFoundException e) {
            System.out.println("예외: 드라이버 로드 실패: " + e.getMessage());
            e.printStackTrace();
        }

        Connection conn = DriverManager.getConnection(url, user, pwd);
        conn.setAutoCommit(false);
        System.out.println("Connection success!");

        return conn;
    }
}
