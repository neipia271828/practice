import java.io.*;

public class Typing {
    public static void main(String[] args) {
        try (BufferedReader br = new BufferedReader(new InputStreamReader(System.in))) {
            System.out.print("入力してください: ");
            String str = br.readLine();
            System.out.println("入力された文字列: " + str);
        } catch (IOException e) {
            System.err.println("エラーが発生しました: " + e.getMessage());
        }
    }
}
