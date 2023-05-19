#include "university.h"
#include <string>
#include <iostream>


// constructor definition of University class
University::University(std::string name, double w1, double w2, double w3, double b,std::string country) {
    m_uni_name = name;
    m_weight1 = w1;
    m_weight2 = w2;
    m_weight3 = w3;
    m_bias = b;
    m_country_name = country;
}

// constructor definition of University class
University::University(std::string name, double w1, double w2, double w3, double b) {
    m_uni_name = name;
    m_weight1 = w1;
    m_weight2 = w2;
    m_weight3 = w3;
    m_bias = b;
}

// evalute_student method
void University::evaluate_student(const Student& s1) {
    double z;
    z = s1.get_GPA() * m_weight1 + s1.get_GRE() * m_weight2 + s1.get_TOEFL() * m_weight3 + m_bias;

    if(z >= 0) 
        std::cout << s1.get_name() << " is admitted to " << m_uni_name <<std::endl;
    else
        std::cout << s1.get_name() << " is rejected from " << m_uni_name <<std::endl;

    s1.increment_apps();
        
}