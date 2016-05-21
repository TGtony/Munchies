/**
 * Extracts desired parts of the review Part I
 *      (product id, review)
 * inputs: final_review_data.txt (review data)
 * output: data.txt (review data with desired parts)
 * Next program: review_parser2.cpp
 */
#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
using namespace std;

int main()
{
    ifstream chipreview;
    chipreview.open("final_review_data.txt");

    ofstream simplified;
    simplified.open("data.txt");

    string line;
    string asin;
    string reviewtext;


    while(getline(chipreview, line))
    {
        string dummy;
        stringstream sstream(line);
        while(sstream >> dummy)
        {
            if((dummy == "\"asin\":"))
            {
                sstream >> asin;
                asin = asin.substr(1, 10);
            }
            if((dummy == "\"reviewText\":"))
            {
                //sstream >> dummy;
                string thereview;
                sstream >> reviewtext;
                thereview = reviewtext;
                //cout << reviewtext;
                while(sstream >> reviewtext)
                {

                    //cout << reviewtext << endl;
                    if((reviewtext == "\"overall\":"))
                    {
                        //simplified << "asin:" << " " << asin << "reviewText:" << " " << thereview << endl;
                        break;
                    }
                    else
                        thereview = thereview + " " + reviewtext;
                }
                //cout << thereview;
                simplified << /*"asin:" << " " <<*/ asin << /*" reviewText:" <<*/ " " << thereview << endl;
            }
            //simplified << /*"asin:" << " " << asin << "reviewText:" << " " <<*/ thereview << endl;
        }
    }

    chipreview.close();
    simplified.close();
    return 0;
}
