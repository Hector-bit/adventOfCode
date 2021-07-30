#include <iostream>
#include <string>
#include <vector>
 
struct Content
{
    int id;
    int numberOf;
};
 
struct Bag
{
    int bagID;
    int parent=-1;
    std::string color;
    std::vector<Content> con;
    int visited=0;
};
 
bool allChildVisited(Bag b[], int accualID) {
    bool ans = true;
    int id = accualID;
    std::vector<Content> ch = b[id].con;
    
    for(int i=0; i<ch.size(); i++)
    {
        if (ch[i].numberOf > b[ch[i].id].visited) {
            ans = false;
            break;
        }
    }
    return ans;
}
 
int visitChild(Bag b[], int accualID) {
    int newID=0, id = accualID;
    std::vector<Content> ch = b[id].con;
    
    for(int i=0; i<ch.size(); i++)
    {
        if (ch[i].numberOf > b[ch[i].id].visited) {
            newID = ch[i].id;
            b[newID].parent = accualID;
            break;
        }
    }
    
    return newID;
}
 
int returnToParent(Bag b[], int accualID) {
    int id = accualID, newID=0;
    
    newID =b[id].parent;
    
    return newID;   
}
 
void resetChildVisit(Bag b[], int accualID) {
    int id = accualID;
    std::vector<Content> ch = b[id].con;
    
    for(int i=0; i<ch.size(); i++) {
        b[ch[i].id].visited = 0;
    }
}
 
int main() {
    int numOfInput=594, pA=0,pB=0, shineGoldId=0, currentID=0;
    std::string testInput[numOfInput];
    std::string txt;
    Bag b[numOfInput];
    Content cnt;
    std::vector<int> mult;
    long int sum=0;
    
    //Get colors 
    for(int i=0; i < numOfInput; i++)
    {
    std::getline(std::cin, testInput[i]);
        
        b[i].bagID = i;
        
        pA = testInput[i].find("contain")-6;
        
        b[i].color = testInput[i].substr(0,pA);
        
        testInput[i] = testInput[i].substr(pA+14);
    }
    
    //Get content of every bag
    for(int j=0; j<numOfInput; j++)
    {
        for(int i=0; i<numOfInput; i++)
        {
            if(testInput[j].find(b[i].color) != -1) {
                cnt.id = i;
                
                b[i].parent = j;
                pA = testInput[j].find(b[i].color)-2;
                cnt.numberOf = (int)testInput[j].at(pA)-48;
                b[j].con.push_back(cnt);
                }
        }
    }
    
    //Shiny Gold Id finding
    
    for(int i=0; i<numOfInput; i++)
    {
        if(b[i].color.compare("shiny gold")==0)
        {
            shineGoldId = i;
            break;
        }
    }
        
    //Needed because I had no better idea how to create while argument
        b[shineGoldId].con[b[shineGoldId].con.size()-1].numberOf++;
        sum=-1;
    currentID = shineGoldId;
        
    while(!allChildVisited(b, shineGoldId))
    {
        if(allChildVisited(b, currentID)&&currentID!=shineGoldId)
        {
            resetChildVisit(b, currentID);
            currentID = returnToParent(b, currentID);
        
        } else {
            currentID = visitChild(b, currentID);
            sum++;
            b[currentID].visited++;
        }
    }  
    
    std::cout << "\n\n\n Bags inside: " << sum;
}