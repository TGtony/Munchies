/**
 * Gets reviews that matches the meta data
 * inputs: meta_data.txt (meta data of desired snacks)
 *         review_Grocery_and_Gourmet_Food.txt (the main review data, converted into txt)
 * output: final_review_data.txt (target meta data)
 * Next Program: review_parser.cpp
 */
#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
using namespace std;

int main()
{
    ifstream chipfile;
    chipfile.open("final_meta_data.txt");

    ifstream reviewdata;
    reviewdata.open("reviews_Grocery_and_Gourmet_Food.txt");

    ofstream reviewfile;
    reviewfile.open("final_review_data.txt");

    string line;
    string asin;

    vector<string> asinvec;

    while(getline(chipfile, line))
    {
        string dummy;
        stringstream sstream1(line);
        while(sstream1 >> dummy)
        {
            if((dummy == "{'asin':"))
            {
                sstream1 >> asin;
                asin = asin.substr(1,10);
                asinvec.push_back(asin);
            }
        }
    }
    chipfile.close();

    string reviewline;
    while(getline(reviewdata, reviewline))
    {
        string dummy;
        stringstream sstream1(reviewline);
        while(sstream1 >> dummy)
        {
            if((dummy == "\"asin\":"))
            {
                sstream1 >> asin;
                asin = asin.substr(1, 10);
                for(int i = 0; i < asinvec.size(); i++)
                {
                    if(asinvec[i] == asin)
                        reviewfile << reviewline << endl;
                }
            }
        }
    }
    reviewdata.close();
    reviewfile.close();

    return 0;
}
