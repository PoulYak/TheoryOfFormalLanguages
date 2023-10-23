%option noyywrap
%{
    #include<stdio.h>
    #include<locale.h>
%}
letter [a-z]
digit [0-9]

symbols [\{\}\[\]\,\:]
literals (true|false|null)
strings \"[^\"]*\"
numbers [\+\-]?{digit}*\.?{digit}+([eE][\+\-]?{digit}+)?

%%
{symbols} {printf("\n символ: %s\n",yytext);}
{literals} {printf("\n литерал: %s\n",yytext);}
{strings} {printf("\n строка: %s\n",yytext);}
{numbers} {printf("\n число: %s\n",yytext);}
%%
int main(int argc, char* argv[])
{
    printf("JSON file: %s\n", argv[1]);
    yyin = fopen(argv[1], "r");
    
    setlocale(LC_ALL, "Rus");

    yylex();
    //identifier {letter}({letter}|{digit})*
    //return 0;
}
