package entities;

import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.Date;

public class Post {
    private Date moment;
    private String title;
    private String content;
    private Integer likes;
    private ArrayList<Comments> comments;

    public Post() {

    }
    public Post(Date moment, String title, String content, Integer likes){
        this.moment = moment;
        this.title = title;
        this.content = content;
        this.likes = likes;
        this.comments = new ArrayList<>();
    }

    public Date getMoment(){
        return moment;
    }

    public String printMoment() {
        SimpleDateFormat sdf = new SimpleDateFormat("dd/MM/yyyy HH:mm:ss");
        String formattedDate = sdf.format(Date.from(moment.toInstant()));
        return formattedDate;
    }

    public void setMoment(Date moment){
        this.moment = moment;
    }

    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }

    public String getContent() {
        return content;
    }

    public void setContent(String content) {
        this.content = content;
    }

    public Integer getLikes() {
        return likes;
    }

    public void changeLikes(Integer likes) {
        this.likes += likes;
    }

    public ArrayList<Comments> getComments() {
        return comments;
    }

    public void setComments(Comments comments) {
        this.comments.add(comments);
    }
}
