package entities;

import java.util.ArrayList;

public class Comments{
    private ArrayList<String> comments;

    public Comments() {
        this.comments = new ArrayList<>();
    }

    public ArrayList<String> getComments() {
        return comments;
    }

    public void addComments(String comment) {
        comments.add(comment);
    }

    public void removeComments(Comments comment) {
        if(comments.contains(comment)) {
            comments.remove(comment);
        }
    }

    private String getComment(int index) {
        return comments.get(index);
    }

    public void printComments() {
        for (int i = 0; i < comments.size(); i++) {
            System.out.println(comments.get(i));
        }
    }
}
