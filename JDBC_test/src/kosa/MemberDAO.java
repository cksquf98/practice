package kosa;

import java.sql.Connection;
import java.sql.ResultSet;
import java.sql.Statement;
import java.util.ArrayList;

public class MemberDAO {

    private Connection conn = DBConnection.getConnection();
    private Statement stmt;
    private ResultSet rs;

    //호출 시 멤버VO 객체가 select된 리스트 반환
//    public ArrayList<MemberVO> list(String _name) {
//        ArrayList<MemberVO> list = new ArrayList<MemberVO>();
//        try {
            String query = "select * from member";
//            if (_name != null) // 인자로 넘어온 값이 있으면 where 조건문을 추가한다.
//                query += " where name='" + _name + "'";
//
//            System.out.println(query);
//            stmt = conn.createStatement();
//            rs = stmt.executeQuery(query);



        //동적쿼리문
        public ArrayList<MemberVO> list(MemberVO vo) {
            String _name = vo.getName();
            int _age = vo.getAge();

            ArrayList<MemberVO> list = new ArrayList<MemberVO>();

            try {
                String query = "select * from member";
                if (_name != null && _age != 0) {
                    query += " where name='" + _name + "' and age=" + _age;
                } else if (_name != null && _age == 0) {
                    query += " where name='" + _name + "'";
                } else if (_name == null && _age != 0) {
                    query += " where age=" + _age;
                }

                System.out.println(query);
                stmt = conn.createStatement();
                ResultSet rs = stmt.executeQuery(query);

            while (rs.next()) {
                String id = rs.getString("id");
                String name = rs.getString("name");
                int height = rs.getInt("height");
                int weight = rs.getInt("weight");
                int age = rs.getInt("age");

                MemberVO data = new MemberVO();

                data.setId(id);
                data.setName(name);
                data.setHeight(height);
                data.setWeight(weight);
                data.setAge(age);

                list.add(data);
            }
            rs.close();
            stmt.close();
            conn.close();
        } catch (Exception e) {
            e.printStackTrace();
        }
        return list;
    }

}
