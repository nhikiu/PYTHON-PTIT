package test.test2;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

public class DSICPC {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        ArrayList<Team> teams = new ArrayList<>();
        int nTeam = sc.nextInt();
        sc.nextLine();
        for (int i = 0; i < nTeam; i++) {
            teams.add(new Team(i + 1, sc.nextLine(), sc.nextLine()));
        }
        ArrayList<Student> students = new ArrayList<>();
        int nStudent = sc.nextInt();
        sc.nextLine();
        for (int i = 0; i < nStudent; i++) {
            students.add(new Student(i + 1, sc.nextLine()));
            String team = sc.nextLine();
            for (Team t : teams) {
                if (t.getId().equals(team)) {
                    students.get(i).setTeam(t);
                }
            }
        }
        Collections.sort(students);
        for (Student student : students) {
            System.out.println(student);
        }
    }
}

class Team {
    private int id;
    private String name;
    private String school;

    public Team() {
    }

    public Team(int id, String name, String school) {
        this.id = id;
        this.name = name;
        this.school = school;
    }

    public String getId() {
        return String.format("Team%02d", id);
    }

    public void setId(int id) {
        this.id = id;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getSchool() {
        return school;
    }

    public void setSchool(String school) {
        this.school = school;
    }
}

class Student implements Comparable<Student>{
    private int id;
    private String name;
    private Team team;

    public Student(int id, String name) {
        this.id = id;
        this.name = name;
    }

    public String getId() {
        return String.format("C%03d", id);
    }

    public void setId(int id) {
        this.id = id;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public Team getTeam() {
        return team;
    }

    public void setTeam(Team team) {
        this.team = team;
    }

    @Override
    public String toString() {
        return getId() + " " + name + " " + team.getName() + " " + team.getSchool();
    }

    @Override
    public int compareTo(Student o) {
        return this.name.compareTo(o.name);
    }
}

