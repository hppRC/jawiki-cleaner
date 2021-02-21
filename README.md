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
</doc>


<doc id="11" url="?curid=11" title="日本語">
日本語

...

学校図書を除く四社の教科書では、単文節でできているものを「主語」のように「－語」と呼び、連文節でできているものを「主部」のように「－部」と呼んでいる。それに対し学校図書だけは、文節/連文節どうしの関係概念を「－語」と呼び、いわゆる成分（文を構成する個々の最大要素）を「－部」と呼んでいる。
種類とその役割.
以下、学校文法の区分に従いつつ、それぞれの文の成分の種類と役割とについて述べる。
主語・述語.
文を成り立たせる基本的な成分である。ことに述語は、文をまとめる重要な役割を果たす。「雨が降る。」「本が多い。」「私は学生だ。」などは、いずれも主語・述語から成り立っている。教科書によっては、述語を文のまとめ役として最も重視する一方、主語については修飾語と併せて説明するものもある（前節「主語廃止論」参照）。
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
アンパサンドと同じ役割を果たす文字に「のet」と呼ばれる、数字の「7」に似た記号があった(U+204A)。
この記号は現在もゲール文字で使われている。
記号名の「アンパサンド」は、ラテン語まじりの英語「& はそれ自身 "and" を表す」(& per se and)のくずれた形である。
英語以外の言語での名称は多様である。
日常的な手書きの場合、欧米でアンパサンドは「ε」に縦線を引く単純化されたものが使われることがある。
また同様に、「t」または「+(プラス)」に輪を重ねたような、無声歯茎側面摩擦音を示す発音記号のようなものが使われることもある。

学校図書を除く四社の教科書では、単文節でできているものを「主語」のように「-語」と呼び、連文節でできているものを「主部」のように「-部」と呼んでいる。
それに対し学校図書だけは、文節/連文節どうしの関係概念を「-語」と呼び、いわゆる成分(文を構成する個々の最大要素)を「-部」と呼んでいる。
以下、学校文法の区分に従いつつ、それぞれの文の成分の種類と役割とについて述べる。
文を成り立たせる基本的な成分である。
ことに述語は、文をまとめる重要な役割を果たす。
「雨が降る。」「本が多い。」「私は学生だ。」などは、いずれも主語・述語から成り立っている。
教科書によっては、述語を文のまとめ役として最も重視する一方、主語については修飾語と併せて説明するものもある(前節「主語廃止論」参照)。
```