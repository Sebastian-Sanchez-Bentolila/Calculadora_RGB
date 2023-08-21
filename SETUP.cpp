//Intalación de las libreras necesarias

/*
@Author: Sebastian Sanchez Bentolila
GitHub: https://github.com/Sebastian-Sanchez-Bentolila
Intagram: @sebas.code_crypto
*/

//Modules
#include<iostream>
#include<stdlib.h>
using namespace std;

//Variables
char pillow[19]= "pip install Pillow", pyperclip[23]= "pip install pyperclip";

void cmd(){
    system(pillow);
    system(pyperclip);
}

int main(){
    cmd();
    cout<<"Intalacion finalizada. Puede cerrar la ventana\n";
    system("pause");
    return 0;
}