/**
 * Combines reviews of each product into 1 rview
 * inputs: data.txt (review data)
 * output: sorted_chips_data.txt (review data that's ready for adjective extraction)
 * Next program: adjectiveExtractor.py
 */
#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>

using namespace std;

int main()
{
    ifstream thing1;
    thing1.open("data.txt");

    ofstream thing2;
    thing2.open("sorted_chips_data.txt");

    string line;

    string asin = "9742894116";
    thing2 << asin << endl;
    string review;
    while(getline(thing1, line))
    {
        string asin1;
        stringstream sstream(line);
        sstream >> asin1;
        if(asin1 != asin)
        {
            thing2 << endl;
            asin = asin1;
            thing2 << asin << endl;
            getline(sstream, review);
            review = review.substr(1, review.size());
            thing2 << review << " ";
            //cout << endl;
        }
        else
        {
            //thing2 << asin << endl;
            getline(sstream, review);
            review = review.substr(1, review.size());
            thing2 << review << " ";
            //cout << endl;
        }
        //thing2 << endl;
    }
    return 0;
}
