package kosa;


import java.util.ArrayList;

public class MemberTest {

    public static void main(String[] args) {
//        MemberDAO dao = new MemberDAO();
//        String _name = "Peter";
//
//        ArrayList<MemberVO> list = dao.list(_name); // Peter인 행만 불러옴

            MemberDAO dao = new MemberDAO();
            String _name = "Peter";
            int _age = 24;

            MemberVO vo = new MemberVO(_name, _age);
            ArrayList<MemberVO> list = dao.list(vo);

        for (int i = 0; i < list.size(); i++) {
            MemberVO data = (MemberVO) list.get(i);

            System.out.println("아이디는>>" + data.getId() +
                    " 이름은>>" + data.getName() +
                    " 키는>>" + data.getHeight() +
                    " 몸무게는>>" + data.getWeight() +
                    " 나이는>>" + data.getAge());
        }
    }

}