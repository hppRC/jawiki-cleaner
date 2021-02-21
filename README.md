# Japanese Wikipedia Cleaner

- Split sentences at the proper position taking parentheses into account.
- Normalize Unicode characters by NFKC.
- Extract text from wiki links
- Remove of unnecessary symbols.

Apply this tool for a extracted text by WikiExtractor.

```
$ jawiki-cleaner --input ./wiki.txt --output ./cleaned-wiki.txt
$ jawiki-cleaner -i ./wiki.txt -o ./cleaned-wiki.txt
$ jawiki-cleaner -i ./wiki.txt # output path will be `./cleaned-wiki.txt`
```



## Example

### Before

```txt:wiki.txt
<doc id="5" url="?curid=5" title="アンパサンド">
アンパサンド

アンパサンド (&amp;、英語名：) とは並立助詞「…と…」を意味する記号である。ラテン語の の合字で、Trebuchet MSフォントでは、と表示され "et" の合字であることが容易にわかる。ampersa、すなわち "and per se and"、その意味は"and [the symbol which] by itself [is] and"である。
歴史.
その使用は1世紀に遡ることができ、5世紀中葉から現代に至るまでの変遷がわかる。
Z に続くラテン文字アルファベットの27字目とされた時期もある。
アンパサンドと同じ役割を果たす文字に「のet」と呼ばれる、数字の「7」に似た記号があった(, U+204A)。この記号は現在もゲール文字で使われている。
記号名の「アンパサンド」は、ラテン語まじりの英語「&amp; はそれ自身 "and" を表す」(&amp; per se and) のくずれた形である。英語以外の言語での名称は多様である。
手書き.
日常的な手書きの場合、欧米でアンパサンドは「ε」に縦線を引く単純化されたものが使われることがある。
また同様に、「t」または「+（プラス）」に輪を重ねたような、無声歯茎側面摩擦音を示す発音記号「」のようなものが使われることもある。
プログラミング言語.
プログラミング言語では、C など多数の言語で AND 演算子として用いられる。以下は C の例。
PHPでは、変数宣言記号（$）の直前に記述することで、参照渡しを行うことができる。
BASIC 系列の言語では文字列の連結演算子として使用される。codice_4 は codice_5 を返す。また、主にマイクロソフト系では整数の十六進表記に codice_6 を用い、codice_7 （十進で15）のように表現する。
SGML、XML、HTMLでは、アンパサンドを使ってSGML実体を参照する。

</doc>
```

### Run `jawiki-cleaner -i wiki.txt`

### After

```
アンパサンド(&、英語名)とは並立助詞「...と...」を意味する記号である。
ラテン語の の合字で、Trebuchet MSフォントでは、と表示され "et" の合字であることが容易にわかる。
ampersa、すなわち "and per se and"、その意味は"and [the symbol which] by itself [is] and"である。
その使用は1世紀に遡ることができ、5世紀中葉から現代に至るまでの変遷がわかる。
Z に続くラテン文字アルファベットの27字目とされた時期もある。
アンパサンドと同じ役割を果たす文字に「のet」と呼ばれる、数字の「7」に似た記号があった(U-204A)。
この記号は現在もゲール文字で使われている。
記号名の「アンパサンド」は、ラテン語まじりの英語「& はそれ自身 "and" を表す」(& per se and)のくずれた形である。
英語以外の言語での名称は多様である。
日常的な手書きの場合、欧米でアンパサンドは「ε」に縦線を引く単純化されたものが使われることがある。
また同様に、「t」または「-(プラス)」に輪を重ねたような、無声歯茎側面摩擦音を示す発音記号のようなものが使われることもある。
プログラミング言語では、C など多数の言語で AND 演算子として用いられる。
PHPでは、変数宣言記号($)の直前に記述することで、参照渡しを行うことができる。
BASIC 系列の言語では文字列の連結演算子として使用される。
codice_4 は codice_5 を返す。
また、主にマイクロソフト系では整数の十六進表記に codice_6 を用い、codice_7(十進で15)のように表現する。
SGML、XML、HTMLでは、アンパサンドを使ってSGML実体を参照する。
```