/**
 * Parses the main meta data file for desired snacks
 * inputs: finalist.txt (list of desired snacks)
 *         meta_Grocery_and_Gourmet_Food.txt (the main meta data)
 * output: final_meta_data.txt (target meta data)
 * Next Program: getreviews.cpp
 *               getdatabasefile.cpp
 */
#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
using namespace std;

int main()
{
    vector<string> notWanted = { "Chocolate", "Cookie", "Truffles", "Chips Ahoy", "Dip" };

    vector<string> brands;
    ifstream listofitems;
    listofitems.open("finalist.txt");
    string listline;
    while (getline(listofitems, listline))
    {
        brands.push_back(listline);
    }

    ifstream datafile;
    datafile.open("meta_Grocery_and_Gourmet_Food.txt");
    ofstream outfile;
    outfile.open("final_meta_data.txt");
    string line;
    string title = "";

    while (getline(datafile, line))
    {
        string line2;
        string dummy;
        stringstream sstream1(line);
        while(sstream1 >> dummy)
        {
            if((dummy == "'title':"))
            {
                string thetitle;
                sstream1 >> title;
                thetitle = title;
                while((sstream1 >> title))
                {
                    if((title[0] == '\'')&&(title[title.size()-1] == ':'))
                        break;
                    else
                        thetitle = thetitle+" "+title;
                }

                bool flag = true;

                for(int j = 0; j < notWanted.size(); j++)
                {
                    string query = notWanted[j];
                    string lowercasequery = query;
                    lowercasequery[0] = tolower(lowercasequery[0]);
                    if((thetitle.find(query) != string::npos)||(thetitle.find(lowercasequery) != string::npos))
                    {
                        flag = false;
                        break;
                    }
                }

                if(flag == true)
                {
                    for(int i = 0; i < brands.size(); i++)
                    {
                        string temp = brands[i];
                        string temp2 = temp;
                        temp2[0] = tolower(temp2[0]);
                        if((thetitle.find(temp) != string::npos)||(thetitle.find(temp2) != string::npos))
                        {
                            //outfile << thetitle << endl;
                            outfile << line << endl;
                            break;
                        }
                    }
                }
            }
        }
    }
    datafile.close();
    outfile.close();

    return 0;
}
