% Facts: Students, Teachers, Subjects
student(vijay, csa1705).
student(raju, dsa1111).
student(mike, cs101).
student(lisa, phys301).

teacher(prof_smith, csa1705).
teacher(prof_jones, dsa1111).
teacher(prof_doe, phys301).

% Rules: Relationships
teaches(Teacher, Subject) :-
    teacher(Teacher, Subject).

enrolled(Student, Subject) :-
    student(Student, Subject).
