import java.time.*;
import java.time.format.DateTimeFormatter;
import java.time.temporal.ChronoUnit;
import java.util.Date;

public class Main {
    public static void main(String[] args) {

        //Estudos de LocalDate e com o link:
        //https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/time/format/DateTimeFormatter.html

        //DateTimeFormatter fmt1= DateTimeFormatter.ofPattern("dd/MM/yyyy");
        //DateTimeFormatter fmt2= DateTimeFormatter.ofPattern("dd/MM/yyyy HH:mm");

        //LocalDate d01 = LocalDate.now();
        //LocalDateTime d02 = LocalDateTime.now();
        //Instant d03 = Instant.now();

        //Instant d07 = Instant.parse("2023-07-20T01:30:36-03:00");

        //LocalDate d08 = LocalDate.parse("20/07/2023", fmt1 /*ou DateTimeFormatter.ofPattern("dd/MM/yyyy")*/);
        //LocalDateTime d09 = LocalDateTime.parse("20/07/2023 01:30", fmt2);

        //LocalDate d10 = LocalDate.of(2023, 7, 20);
        //LocalDateTime d11 = LocalDateTime.of(2023, 7, 20, 1, 30);

        //System.out.printf("d01 = %s\n", d01.toString());
        //System.out.printf("d02 = %s\n", d02.toString());
        //System.out.printf("d03 = %s\n", d03.toString());
        //System.out.printf("d04 = %s\n", d04.toString());
        //System.out.printf("d05 = %s\n", d05.toString());
        //System.out.printf("d06 = %s\n", d06.toString());
        //System.out.printf("d07 = %s\n", d07.toString());
        //System.out.printf("d08 = %s\n", d08.toString());
        //System.out.printf("d09 = %s\n", d09.toString());
        //System.out.printf("d10 = %s\n", d10.toString());
        //System.out.printf("d11 = %s\n", d11.toString());

        //LocalDate r1 = LocalDate.ofInstant(d06, ZoneId.systemDefault());
        //LocalDate r2 = LocalDate.ofInstant(d06, ZoneId.of("Portugal"));
        //LocalDateTime r3 = LocalDateTime.ofInstant(d06, ZoneId.systemDefault());
        //LocalDateTime r4 = LocalDateTime.ofInstant(d06, ZoneId.of("Portugal"));

        //DateTimeFormatter fmt1= DateTimeFormatter.ofPattern("dd/MM/yyyy");
        //DateTimeFormatter fmt2= DateTimeFormatter.ofPattern("dd/MM/yyyy HH:mm");
        //DateTimeFormatter fmt3 = DateTimeFormatter.ofPattern("dd/MM/yyyy HH:mm").withZone(ZoneId.systemDefault());
        //DateTimeFormatter fmt4 = DateTimeFormatter.ISO_DATE_TIME;
        //DateTimeFormatter fmt5 = DateTimeFormatter.ISO_INSTANT;

        //System.out.printf("d04 = %s\n", d04.format(fmt1));
        //System.out.printf("d04 = %s\n", fmt1.format(d04));
        //System.out.printf("d04 = %s\n", DateTimeFormatter.ofPattern("dd/MM/yyyy").format(d04));
        //System.out.printf("d04 = %s\n", d04.format(DateTimeFormatter.ofPattern("dd/MM/yyyy")));

        //System.out.printf("d05 = %s\n", fmt2.format(d05));
        //System.out.printf("d05 = %s\n", fmt4.format(d05));

        //System.out.printf("d06 = %s\n", fmt3.format(d06));
        //System.out.printf("d06 = %s\n", fmt5.format(d06));

        //System.out.printf("r1 = %s\n", r1);
        //System.out.printf("r2 = %s\n", r2);
        //System.out.printf("r3 = %s\n", r3);
        //System.out.printf("r4 = %s\n", r4);

        //System.out.printf("d04 dia = %s\n", d04.getDayOfMonth());
        //System.out.printf("d04 mês = %s\n", d04.getMonthValue());
        //System.out.printf("d04 ano = %s\n", d04.getYear());

        //System.out.printf("d05 horas = %s\n", d05.getHour());
        //System.out.printf("d05 minutos = %s\n", d05.getMinute());
        //System.out.printf("d05 segundos = %s\n", d05.getSecond());

        LocalDate d04 = LocalDate.parse("2023-07-20");
        LocalDateTime d05 = LocalDateTime.parse("2023-07-20T01:30:36");
        Instant d06 = Instant.parse("2023-07-20T01:30:36Z");

        LocalDate pastWeekLocalDate = d04.minusDays(7);
        LocalDate nextWeekLocalDate = d04.plusDays(7);

        System.out.println("Past Week Local Date = " + pastWeekLocalDate);
        System.out.println("Next Week Local Date = " + nextWeekLocalDate);

        LocalDateTime pastWeekLocalDateTime = d05.minusDays(7);
        LocalDateTime nextWeekLocalDateTime = d05.plusDays(7);

        System.out.println("Past Week Local Date = " + pastWeekLocalDateTime);
        System.out.println("Next Week Local Date = " + nextWeekLocalDateTime);

        Instant pastWeekInstant = d06.minus(7, ChronoUnit.DAYS);
        Instant nextWeekInstant = d06.plus(7, ChronoUnit.DAYS);

        System.out.println("pastWeekInstant = " + pastWeekInstant);
        System.out.println("nextWeekInstant = " + nextWeekInstant);

        Duration t1 = Duration.between(pastWeekLocalDate.atStartOfDay(), d04.atStartOfDay());
        Duration t2 = Duration.between(pastWeekLocalDateTime, d05);
        Duration t3 = Duration.between(pastWeekInstant, d06);
        Duration t4 = Duration.between(d06, pastWeekInstant);

        System.out.println("t1 dias = " + t1.toDays());
        System.out.println("t2 dias = " + t2.toDays());
        System.out.println("t3 dias = " + t3.toDays());
        System.out.println("t4 dias = " + t4.toDays());
    }
}