/**
 * Extracts desired parts of the meta data
 * inputs: meta_data.txt (meta data of desired snacks)
 * output: database.csv (file to be converted by json)
 * Next program: csvtojson.py
 */
#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <algorithm>
using namespace std;

struct Chip
{
    string asin_;
    string descrition_;
    string title_;
    string url_;
};

int main()
{
    ifstream datafile;
    datafile.open("final_meta_data.txt");
    ofstream outfile;
    outfile.open("database.csv");
    string line;
    string title = "";
    string desc = "";
    string asin;
    string url;

    vector <Chip> chips;
    int counter = 0;
    while (getline(datafile, line))
    {
        Chip product;
        chips.push_back(product);
    }
    datafile.close();

    datafile.open("final_meta_data.txt");
    while (getline(datafile, line))
    {
        string dummy;
        stringstream sstream1(line);
        while(sstream1 >> dummy)
        {
            if((dummy == "{'asin':"))
            {
                sstream1 >> asin;
                asin = asin.substr(1,10);
                chips[counter].asin_ = asin;
                //outfile << asin << " ";
            }
        }
        counter++;
    }
    datafile.close();
    counter = 0;

    datafile.open("final_meta_data.txt");
    while (getline(datafile, line))
    {
        string dummy;
        stringstream sstream1(line);
        while(sstream1 >> dummy)
        {
            if((dummy == "'description':"))
            {
                string thedesc;
                sstream1 >> desc;
                thedesc = desc;
                while((sstream1 >> desc))
                {
                    if((desc[0] == '\'')&&(desc[desc.size()-1] == ':'))
                    {
                        dummy = desc;
                        break;
                    }
                    else
                        thedesc = thedesc+" "+desc;
                }
                thedesc.erase(std::remove(thedesc.begin(), thedesc.end(), '"'), thedesc.end());
                thedesc.erase(std::remove(thedesc.begin(), thedesc.end(), '\\'), thedesc.end());
                //thedesc.erase(std::remove(thedesc.begin(), thedesc.end(), '\''), thedesc.end());
                thedesc.erase(std::remove(thedesc.begin(), thedesc.end(), '}'), thedesc.end());
                thedesc.erase(std::remove(thedesc.begin(), thedesc.end(), '{'), thedesc.end());
                if(thedesc[thedesc.size()-1] == ',')
                    thedesc = thedesc.substr(0, thedesc.size()-1);
                if(thedesc[0] == '\'')
                    thedesc = thedesc.substr(1, thedesc.size());
                if(thedesc[thedesc.size()-1] == '\'')
                    thedesc = thedesc.substr(0, thedesc.size()-1);
                //thedesc = thedesc.substr(1, thedesc.size()-3);
                chips[counter].descrition_ = thedesc;
            }
        }
        counter++;
    }
    datafile.close();
    counter = 0;

    datafile.open("final_meta_data.txt");
    while (getline(datafile, line))
    {
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
                    {
                        dummy = title;
                        break;
                    }
                    else
                        thetitle = thetitle+" "+title;
                }
                thetitle.erase(std::remove(thetitle.begin(), thetitle.end(), '"'), thetitle.end());
                thetitle.erase(std::remove(thetitle.begin(), thetitle.end(), '\\'), thetitle.end());
//                thetitle.erase(std::remove(thetitle.begin(), thetitle.end(), '\''), thetitle.end());
                thetitle.erase(std::remove(thetitle.begin(), thetitle.end(), '}'), thetitle.end());
                thetitle.erase(std::remove(thetitle.begin(), thetitle.end(), '{'), thetitle.end());
                if(thetitle[thetitle.size()-1] == ',')
                    thetitle = thetitle.substr(0, thetitle.size()-1);
                if(thetitle[0] == '\'')
                    thetitle = thetitle.substr(1, thetitle.size());
                if(thetitle[thetitle.size()-1] == '\'')
                    thetitle = thetitle.substr(0, thetitle.size()-1);
                //thetitle = thetitle.substr(1, thetitle.size()-3);
                chips[counter].title_ = thetitle;
            }
        }
        counter++;
    }
    datafile.close();
    counter = 0;

    datafile.open("final_meta_data.txt");
    while (getline(datafile, line))
    {
        string dummy;
        stringstream sstream1(line);
        while(sstream1 >> dummy)
        {
            if((dummy == "'imUrl':"))
            {
                sstream1 >> url;
                //asin = asin.substr(1,10);
                //product.url_ = url;
                //outfile << url << " ";
                url = url.substr(1, url.size()-3);
                chips[counter].url_ = url;
            }
        }
        counter++;
    }
    datafile.close();
    counter = 0;
for(int i = 0; i < chips.size(); i++)
{

            if(!chips[i].asin_.empty())
                outfile << "\"" << chips[i].asin_ << "\",";
            else
                outfile << ",";
                //outfile << "\"" << "" << "\",";
            if(!chips[i].descrition_.empty())
                outfile << "\"" << chips[i].descrition_ << "\",";
            else
            {
                if(!chips[i].title_.empty())
                    outfile << "\"" << chips[i].title_ << "\",";
                else
                    outfile << ",";
            }
                //outfile << "\"" << "" << "\",";
            if(!chips[i].title_.empty())
                outfile << "\"" << chips[i].title_ << "\",";
            else
                outfile << ",";
                //outfile << "\"" << "" << "\",";
            if(!chips[i].url_.empty())
                outfile << "\"" << chips[i].url_ << "\"";
            else
                outfile << ",";
                //outfile << "\"" << "" << "\"";
            outfile << endl;

}
//    datafile.close();
    outfile.close();

    return 0;
}
