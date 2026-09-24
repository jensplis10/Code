#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    string a;
    cout <<"Du stehst vor einem Gegner.\nEr hat 5 Hp und macht 1 Damage.\nWähle eine Waffe: \n1. Pumpgun (2 Damage) \n2. Sigma (3 Damage)\n";
    cin >> a;
    int php = 10;
    int hp = 20;
    
    if (hp < 1)
        cout << "Der Gegner ist tot. Du hast noch " << php << " hp.";
    else
    {
        if (a == "1")
        {
            int dm = -2;
            cout << "Der Gegner hat jetzt " << hp + dm << " hp.\nDu hast " << php-1 << " hp.\n";
            hp += dm;
            php = php-1;
        }
        else if (a == "2")
        {
            int dm = -3;
            cout << "Der Gegner hat jetzt " << hp + dm << " hp.\nDu hast " << php-1 << " hp.\n";
            hp = hp + dm;
            php = php-1;
            
        }
        else
        {
            cout << "Wähle 1 oder 2.";
        } 
    }
    return 0;
}