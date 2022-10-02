import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

public class LuyenTapLapTrinh {
    public static void main(String[] args) throws FileNotFoundException {
        Scanner sc = new Scanner(new File("LUYENTAP.in"));
        int t = Integer.parseInt(sc.nextLine());
        ArrayList<Student> students = new ArrayList<>();
        for (int i = 0; i < t; i++) {
            String name = sc.nextLine();
            String[] tmp = sc.nextLine().split(" ");
            students.add(new Student(name, Integer.parseInt(tmp[0]),
                    Integer.parseInt(tmp[1])));
        }
        Collections.sort(students);
        for (Student student : students) {
            System.out.println(student);
        }
    }
}


class Student implements Comparable<Student>{
    private String name;
    private int correctSubmit;
    private int totalSubmit;

    public Student() {
    }

    public Student(String name, int correctSubmit, int totalSubmit) {
        this.name = name;
        this.correctSubmit = correctSubmit;
        this.totalSubmit = totalSubmit;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public int getCorrectSubmit() {
        return correctSubmit;
    }

    public void setCorrectSubmit(int correctSubmit) {
        this.correctSubmit = correctSubmit;
    }

    public int getTotalSubmit() {
        return totalSubmit;
    }

    public void setTotalSubmit(int totalSubmit) {
        this.totalSubmit = totalSubmit;
    }

    @Override
    public String toString() {
        return name + " " + correctSubmit + " " + totalSubmit;
    }

    @Override
    public int compareTo(Student o) {
        if (this.correctSubmit == o.correctSubmit) {
            if (this.totalSubmit == o.totalSubmit) {
                return this.name.compareTo(o.name);
            }
            return this.correctSubmit > o.totalSubmit ? 1 : -1;
        }
        return this.correctSubmit < o.correctSubmit ? 1 : -1;
    }
}