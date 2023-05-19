#include <string>

// declaration of Student class
class Student {
public:
    Student(std::string, double, double, double);   // constructor
    Student(const Student&);    // constructor 
    std::string get_name() const {return m_student_name;}   // getter for m_student_name
    double get_GPA() const {return m_GPA;}  // getter for m_GPA
    double get_GRE() const {return m_GRE;}  // getter for m_GRE
    double get_TOEFL() const {return m_TOEFL;}  // getter for m_TOEFL
    int get_noapps() const {return m_no_of_apps;}   // getter for m_no_of_apps
    void set_name(std::string); // setter for m_student_name
    void increment_apps() const;    // method for incrementing m_np_of_apps by 1
    ~Student(); // destructor
private:
    std::string m_student_name = "";    // name attribute
    double m_GPA {};    // GPA attribute
    double m_GRE {};    // GRE attribute
    double m_TOEFL {};  // TOEFL attribute
    mutable int m_no_of_apps {};    // number of attribute. mutable keyword is used because it is modifiable by a const method

};