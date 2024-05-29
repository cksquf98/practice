package StudyCafe.DB;

import oracle.jdbc.pool.OracleDataSource;
import java.sql.Connection;
import java.sql.SQLException;

public class Jdbc_Connection {

    @SuppressWarnings("unused")
    public static void main(String args[]) throws SQLException {

        OracleDataSource ods = new OracleDataSource();


        /* Thin driver */

//        // 1 직접 계정 입력해서 연결하는 방법
//        ods.setURL("jdbc:oracle:thin:@localhost:1521/xe");
//        ods.setUser("hr");
//        ods.setPassword("199498");
//        Connection conn1 = ods.getConnection();
//
//        DatabaseMetaData meta = conn1.getMetaData();
//        System.out.println("JDBC driver version is " + meta.getDriverVersion());
//
//        // 2 직접 계정 입력해서 연결하는 방법
//        ods.setURL("jdbc:oracle:thin:hr/hr@localhost:1521/xe");
//        Connection conn2 = ods.getConnection();
//        System.out.println("2 성공");
//

        /* 설정 파일 + 싱글턴 패턴 활용 접속 -> DBConnection.java에서 연결된 것 이용 */
         Connection conn5 = DBConnection.getConnection();
    }

}