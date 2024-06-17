import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Map;
import java.util.StringTokenizer;

public class Main {
    static Map<String, Integer> check = new HashMap<>();
    static int countCheck() {
        String[] alphabet = {"A", "C", "G", "T"};
        for(String s : alphabet) {
            if(check.get(s+s) > check.get(s)) return 0;
        }
        return 1;
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer tokens = new StringTokenizer(br.readLine(), " ");

        int totalLength = Integer.parseInt(tokens.nextToken());
        int windowLength = Integer.parseInt(tokens.nextToken());
        int count = 0;

        String str = br.readLine();
        char[] DNA = str.toCharArray();



        tokens = new StringTokenizer(br.readLine(), " ");

        //알파벳 조건
        check.put("AA", Integer.parseInt(tokens.nextToken())); //얘가 조건
        check.put("A", 0); //얘가 count

        check.put("CC", Integer.parseInt(tokens.nextToken()));
        check.put("C", 0);

        check.put("GG", Integer.parseInt(tokens.nextToken()));
        check.put("G",0);

        check.put("TT", Integer.parseInt(tokens.nextToken()));
        check.put("T", 0);

//        System.out.println("* check = "+ check.toString());

        for (int i = 0; i < windowLength; i++) {
            String c = String.valueOf(DNA[i]);
            check.put(c, check.get(c)+1);
        }
        count += countCheck();

//        System.out.println("First check = "+ check.toString());

        //윈도우 움직이기
        for (int i = 1; i+windowLength <= totalLength; i++) {
            String origin = String.valueOf(DNA[i - 1]);
            check.put(origin, check.get(origin)-1);

            String newChar = String.valueOf(DNA[i+windowLength-1]);
            check.put(newChar, check.get(newChar)+1);

//            System.out.println(i+"번째 check = "+ check.toString());
            count += countCheck();
        }
        System.out.println(count);
    }
}