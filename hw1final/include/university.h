#include "student.h"

// declaration of University class
class University {
public: 
    University(std::string, double, double, double, double, std::string)    // constructor
    University(std::string, double, double, double, double);    // constructor
    void evaluate_student(const Student&);  // evaluate method 

private:
    std::string m_uni_name = "";    // university name attribute
    double m_weight1;   // weight1 attribute
    double m_weight2;   // weight2 attribute
    double m_weight3;   // weight3 attribute
    double m_bias;  // bias attribute
    std::string m_country_name = "";    // country name attribute
};

