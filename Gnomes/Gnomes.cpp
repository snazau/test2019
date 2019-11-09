#include <iostream>
#include <vector>
#include <string>
#include <map>

using namespace std;

const int SOME_MAX = 205;

vector<string> get_properties_line() {
    char symbol;
    string property;
    vector<string> properties;
    while (true) {
        cin >> property;
        properties.push_back(property);

        symbol = cin.peek();
        if (symbol == '\n' || symbol == EOF) {
            break;
        }
    }
    return properties;
}

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    ios_base::sync_with_stdio(false);
    cin.tie(false);
    cout.tie(false);

    vector<string> security_properties = get_properties_line();
    vector<string> gnome_properties = get_properties_line();

    // parse gnome properties into map
    map<char, int> gnome;
    for (int i = 0; i < gnome_properties.size(); ++i) {
        string value;
        for (int j = 2; j < gnome_properties[i].size(); ++j) {
            value.push_back(gnome_properties[i][j]);
        }
        char code = gnome_properties[i][0];
        gnome[code] = stoi(value);
    }
    //

    for (int i = 0; i < security_properties.size(); ++i) {
        char code = security_properties[i][0];

        // property check based on another property
        if (security_properties[i][2] >= 'A' && security_properties[i][2] <= 'Z') {
            if (gnome[code] <= gnome[security_properties[i][2]]) {
                cout << "false" << endl;
                return 0;
            }
            continue;
        }
        //

        // property check based on numeric values
        int left_value = SOME_MAX, right_value = SOME_MAX;
        string value;
        bool is_interval = false;
        for (int j = 2; j < security_properties[i].size(); ++j) {
            if (security_properties[i][j] == '-') { // '-' means existence of second value of interval
                left_value = stoi(value);
                value.clear();
                is_interval = true;
                continue;
            }
            value.push_back(security_properties[i][j]);
        }
        if (is_interval == true) {
            right_value = stoi(value);
        }
        else {
            left_value = stoi(value);
        }
        //

        if (gnome[code] < left_value || gnome[code] > right_value) {
            cout << "false" << endl;
            return 0;
        }
    }

    cout << "true" << endl;

    return 0;
}
