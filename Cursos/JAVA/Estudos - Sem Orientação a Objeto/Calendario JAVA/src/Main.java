import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.time.Instant;
import java.util.Calendar;
import java.util.Date;
import java.util.TimeZone;

public class Main {
    public static void main(String[] args) throws ParseException {
        SimpleDateFormat sdf1 = new SimpleDateFormat("dd/MM/yyyy");
        SimpleDateFormat sdf2 = new SimpleDateFormat("dd/MM/yyyy HH:mm:ss");
        SimpleDateFormat sdf3 = new SimpleDateFormat("dd/MM/yyyy HH:mm:ss");
        sdf3.setTimeZone(TimeZone.getTimeZone("GMT"));

        Date x1 = new Date();
        Date x2 = new Date(System.currentTimeMillis());
        Date x3 = new Date(0L);
        Date x4 = new Date(1000L * 60L * 60L * 5L);

        Date y1 = sdf1.parse("25/06/2023");
        Date y2 = sdf2.parse("25/06/2023 15:37:23");
        Date y3 = Date.from(Instant.parse("2018-06-25T15:45:07Z"));

        System.out.println(sdf2.format(y3));

        Calendar cal = Calendar.getInstance();
        cal.setTime(y3);
        cal.add(Calendar.HOUR_OF_DAY, 4);
        int minutes = cal.get(Calendar.MINUTE);
        int month = 1 + cal.get(Calendar.MONTH);
        int dia = cal.get(Calendar.DAY_OF_MONTH);
        int ano = cal.get(Calendar.YEAR);

        System.out.println(minutes);
        System.out.println(month);
        System.out.println(dia);
        System.out.println(ano);


        System.out.println("-----------------------------------------------");
        System.out.println("x1 = " + sdf2.format(x1));
        System.out.println("x2 = " + sdf2.format(x2));
        System.out.println("x3 = " + sdf2.format(x3));
        System.out.println("x4 = " + sdf2.format(x4));
        System.out.println("y1 = " + sdf2.format(y1));
        System.out.println("y2 = " + sdf2.format(y2));
        System.out.println("y3 = " + sdf2.format(y3));
        System.out.println("-----------------------------------------------");
        System.out.println("x1 = " + sdf3.format(x1));
        System.out.println("x2 = " + sdf3.format(x2));
        System.out.println("x3 = " + sdf3.format(x3));
        System.out.println("x4 = " + sdf3.format(x4));
        System.out.println("y1 = " + sdf3.format(y1));
        System.out.println("y2 = " + sdf3.format(y2));
        System.out.println("y3 = " + sdf3.format(y3));
    }
}