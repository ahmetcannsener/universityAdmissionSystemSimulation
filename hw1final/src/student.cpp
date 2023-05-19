#include <string>
#include "student.h"
#include <iostream>


// constructor definition of Student class
Student::Student(std::string name, double gpa, double gre, double toefl) {
    set_name(name);
    m_GPA = gpa;
    m_GRE = gre;
    m_TOEFL = toefl;

    std::cout << get_name() << " logged in to the system." << std::endl;
}

// constructor definition of Student class
Student::Student(const Student& s1)
        : m_student_name{s1.m_student_name}, m_GPA{s1.m_GPA}, m_GRE{s1.m_GRE}, m_TOEFL{s1.m_TOEFL} 
 {
    std::cout << get_name() << " logged in to the system." << std::endl;
    m_no_of_apps = 0;
}

// setter method
void Student::set_name(std::string name) {
    m_student_name = name;
}

// destructor
Student::~Student() {
    std::cout << get_name() << " logged out of the system with " << get_noapps() << " application(s)." << std::endl;
}

// incerement method
void Student::increment_apps() const {
    m_no_of_apps++;
}