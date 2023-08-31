package application;

import entities.Comments;
import entities.Post;

import java.text.ParseException;
import java.time.Instant;
import java.util.Date;

public class Main {
    public static void main(String[] args) throws ParseException {

        Date date = Date.from(Instant.now());

        Post post1 = new Post(date, "Traveling to New Zealand", "I'm going to visit this wonderful country!", 12);

        Comments comments = new Comments();
        comments.addComments("Have a nice trip");
        comments.addComments("Wow that's awesome!");

        post1.setComments(comments);
        post1.changeLikes(10);


        System.out.println("Data: " + post1.printMoment());
        System.out.println("Post: " + post1.getTitle());
        System.out.println("Content: " + post1.getContent());
        System.out.println("Likes: " + post1.getLikes());
        System.out.println("Comments: ");
        for (Comments comment : post1.getComments()) {
            for (String com : comment.getComments()) {
                System.out.println(com);
            }
        }
    }
}
