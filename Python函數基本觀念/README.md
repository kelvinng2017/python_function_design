# python_function_design
python函數設計

## 函數定義
函數的語法格式如下:

def 函數名稱(參數值1[,參數值2,...]):
    """函數註解(docstring)"""
    程式碼區塊  #需要內縮
    return [回傳值1,回傳值2,...] #中跨號可有可無

### 函數名稱
名稱必須是唯一的，程式未來可以呼叫引用，它的名稱規則與一般變數相同，不過在PEP 8 的Python 風格下建議英文字母小寫。

### 參數值
這是可有可無，完全視函數設計需要，可以接受呼叫函數傳來的變數，各參數值之間是用逗號","間隔。

### 函數註解
這是可有可無，不過如果是參與大型程式設計計畫，當負責一個小程式時，建議所設計的函數需要加上註解，除了自己需要也是方便他人閱讀。主要是註明此函數的功能，由於可能是有多行註解所以可以用3個雙引號(或單引號)包夾。許多英文Python資料將此稱docstring(document string 的縮寫)

### return[回傳值1，回傳值2，。。。。]
<font color=#FF0000>不論是**return**或*接*續右邊的回傳值皆是可有可無，如果有回傳多個資料彼此需以逗號","間隔。</font>

<hr>

# 沒有傳入參數也沒有傳回值的函數

建立greeting.py寫一個函數

可以將greeting的第8行以後的程式碼稱主程式，可以在greeting_no_function.py查看沒有函數功能的程式設計。

可以發現greeting.py和greeting_no_function.py執行結果是一樣

雖然greeting_no_function.py可以完成工作,但是可以發現重複的語句太多了，這不是一個好的設計。如果將"Python 歡迎你" 改成 "Python歡迎你們",程式必須修改5次相同語句。經過greeting_no_function.py和greeting.py的實做比對可以了解函數對程式設計的好處

<hr>

# 函數的參數(Parameter)設計

greeting.py沒有傳遞任何參數，在真實的函數設計與應用中大多是需要傳遞一些參數的。例如:呼叫Python內建函數時，例如:len()、print()....等，皆需要輸入參數，在下面會講解這方面的應用與設計。

執行pass_a_parameter時在第9行呼叫函數greeting()時,所放的參數是Nelson,這個字串將傳遞給函數括號內的name參數,所以程式第6行會將Nelson字串透過name參數列印出來。

在Pythony應用中，有時候也常會將第6行寫成下列語法

```python
print("Hi, "+ name + "Good Morning")
```
<hr>

# 多個參數傳遞

當所設計的函數需要傳遞多個參數時，呼叫此函數時就需要特別留意傳遞參數的位置需要正確，最後才可以獲得正確的結果。最常見的傳遞參數是數值或字串資料，在進階的程式應用中有時也會有需要傳遞串列、元組、字典或函數

在pass_more_parameter.py設計減法的函數 subtract(),第一個參數會減去第二個參數，然後列出執行結果。

pass_more_paramete.py函數功能是減去運算，所以需要傳遞2個參數，然後執行第一個數值減去第二個數值。呼叫這裡的函數時，就必須留意參數的位置，否則會有錯誤訊息產生。在pass_more_paramete.py程式而言，變數a和b皆是從螢幕輸入，執行第12行呼叫subtract()函數時，a將傳遞給x1,b將傳給x2。

在pass_more_string.py第9行呼叫interest()時,'<font color="#1e90ff">旅遊</font>'會傳給<font color="#1e90ff">interest_type</font>、'<font color="#00fa9a">敦煌</font>'會穿給<font color="#00fa9a">subject</font>。第10行呼叫interest()時,'<font color="#1e90ff">程式設計</font>'會傳給<font color="#1e90ff">interest_type</font>、'<font color="#00fa9a">Python</font>'會傳給</font>'會穿給<font color="#00fa9a">subject</font>'。經過pass_more_string.py程式，我已經了解呼叫需要傳遞多個參數的函數時，所傳遞參數的位置很重要否則有不可預期的錯誤，可以參考pass_more_string_interstet.py第11行參考

<hr>

# 關鍵字參數 參數名稱=值

<font color="#1e90ff">關鍵字參數</font>(keyword arguments)是指呼叫函數時，參數是用參數名稱=值配對方式呈現。Python 也允許在呼叫需傳遞多個參數的函數時，直接將參數名稱 = 值 用配對方式傳送，這個時候參數的位置就不重要了。

在pass_more_string_interest_parameter keyword arguments.py的第9和第10行的"<font color="#1e90ff">interest_type=</font>'<font color="#1e90ff">旅遊</font>'",當呼叫函數用配對方式傳送參數時，即使參數位置不同，程式執行結果也會不相同，因為在呼叫時已經明確指出所傳遞的值是要給哪一個參數了。

<hr>

# 參數預設值處理

在設計函數時也可以給參數<font color="#4169e1">預設值</font>，如果呼叫這個函數沒有給參數值時，函數的預設值將派上用場。<font color="#ff000">特別需留意</font>:函數設計時含有預設值的參數，<font color="#ff000">必須放置在參數列的最右邊</font>，請參考下列程式第2行，如果將"subject = '<font color="#4169e1">敦煌</font>'"與"<font color="#7fffd4">interest_type</font>"位置對調，程式會有錯誤產生。

在argument_default_value_processing.py,這個程式會將subject的預設值設為"敦煌"。程式將用不同方式呼叫，可以從中體會程式參數預設值的意義。在第11行和第12行只傳遞一個參數，所以subject就會使用預設值"敦煌"，第13行、14行和12行傳送遞2個參數，其中第14行和第15行主要說明使用不同類型的參數一樣可以獲得正確語意的結果。

<hr>

# 函數傳回值

在前面的章節實例我們有執行呼叫許多內建的函數，有時會傳回一些有意義的資料，例如:len()回傳元素數量。有些沒有回傳值。此時Python會自動傳回None，例如:clear()。為何會如此？下面會完整解說函數回傳值的知識。

## 傳回None
前2個小節所設計的函數全部沒有"<font color="#4169e1">return[回傳值]</font>"，相當於回傳None。在一些程式語言，例如:C語言這個None 就是NULL,None在Python中獨立成為一個資料形態NoneType，下列是實例觀察。

在argument_value_none.py,這個程式沒有做傳回值設計，不過筆者將列出Python回傳greeting()函數的資料是否是None，同時列出傳回值的資料形態,經過執行函數greeting()沒有return,Python 講自動處理成return None。其實即使函數設計時有return但是沒有回傳值,Python也將自動處理成return None可以參考argument_value_none_has_return.py，並發現和argument_value_none.py執行結果一樣

None 在python中是一個特殊的值，如果將它當作布林值使用，可將它視為是False,可以參考none_is_flase.py

在none_is_false.py val 是none,可以將之視為False,所以可以得到執行第6行，輸出字串"I love Python"。其實雖然None是被視為False,可是False並不是None，其實<font color="#4169e1">空串列、空元祖、空字典、空集合</font>雖然是False 可是他們也不是None。

也可以簡化用1行程式取代上述3-6行。可以參考none_is_false_one_line.py。

<hr>

# 簡單回傳資料
參數具有回傳值的功能，將可以大大增加程式的可讀性，回傳的基本方式可以參考11_11.py

return <font color="#4169e1">result</font> #result就是回傳的值

一個程式常常是由許多函數所組成，11_12.py含2個函數的應用

<hr>

# 傳回多筆資料的應用 - 實質是回傳tuple

使用return回傳函數資料時，也允許回傳多筆資料，各筆資料間只要以逗號隔開即可，可以參考11_13.py第8行

11_13.py函數mutifunction()第8行回傳了加法、減法、乘法與除法的運算結果，其實Python會將此打包為元組(tuple)物件，所以真正的回傳值只有一個，在11_13_1.py第11行則是Python將回傳的元祖(tuple)解包，從第12行我們可以知道回傳的資料形態是<font color="#4169e1">元組(tuple)</font>，所以在第13-16行可以用輸出<font color="#4169e1">元組(tuple)索引</font>方式列出運算結果。

<hr>

# 簡單回傳字串資料

回傳字串的方式與11_11.py回傳數值的方式相同

<font color="#8B4513">11_14.py</font>：一般中午姓名是三個字，將中午姓名拆解為第一個字是姓lastname,第二個字是中間名middlename,第三個字是firstname。這個程式內有一個函數guest_info()，參數意義分別是名firstname、中間名middlename和姓lastname，以及性別gender組織起來，同時加上問候回傳。如果是處理外國人的名字，則須在lastname、middlename和firstname之間加上空格，同時外國人名字處理方式循序是firstname middlename lastname

<hr>

# 再談參數預設值

雖然大多數國人的名字是3個字所組成，但是偶爾也會遇上2個字的狀況，例如:著名影星劉濤。其實外國人的名字中，有些人也只有2個字，因為沒有中間名 middlename。如果要讓11_14.py更完美，可以在函數設計時將middlename預設為空字串，這樣就可以處理沒有中間名的問題，設計時必須將預設放在最右邊

在11_15.py第10行呼叫guest_info()函數時只有3個參數，middlename就會使用預設的空字串。第11行呼叫guest_info()函數時只有4個參數，middlename就會使用呼叫函數是所預設的字串'冰'。

<hr>

# 函數回傳字典資料
函數除了可以回傳數值或字串資料外，也可以回傳比較複雜的資料，例如:字典或串列。。。等

11_16.py字典資料只是一個簡單的應用，在真正的企業建立VIP資料的案例中，可能需要<font color="#4169e1">性別、電話號碼、年齡、電子郵件、地址....</font>等資訊。在建立VIP資料過程，也許有些人會樂意提供手機號碼，有些人不樂意提供，函數設計時我們也可以將Tel電話號碼當作預設為空字串，但是如果有提供電話號碼時，程式也可以將納入字典內容。

11_17.py程式第10行呼叫build_vip()函數時，由於有提供電話號碼欄位，所以上述程式第5行會得到if敘述的tel 是True，所以在第6行會將此欄位增加到字典中。

<hr>

# 將迴圈應用在建立VIP會員字典

可以將迴圈的觀念應用在VIP會員字典的建立

<hr>

# 基本函數時參數是串列

在呼叫函數時，也可以將串列(此串列可以是由<font color="#4169e1">數值、字串、或字典所組成</font>)當參數傳遞給函數的，然後函數可以遍歷串列內容，然後執行更進一步的運作。

<hr>

# 觀察傳遞一般變數與串列變數至函數的區別

在解釋修訂串列內容前，先用2個簡單的程式說明傳遞整數變數與傳遞串列變數至函數的差別。如果傳遞的是一般整數變數，其實只是將此變數值傳給函數，此變數內容在函數更改時原先主程式的變數值不會改變

在程式11_19_1.py金額以發現主程式在呼叫mudata()函數時傳遞了參數x，在mudata()函數中將變數設為n。當第4行變數n內容更改為5時，這個變數在記憶體的地址也更改了，所以函數mydata()執行結束時回到主程式，第10行可以得到原先主程式的變數x仍然是1

如果主程式呼叫函數所傳遞的是串列變數，其實是將此串列變數位置參照的內容更改時，原先主程式串列變數內容會隨著改變。

從11_12_2.py執行結果可以看到，串列變數的位址不論是在主程式或是函數皆保持一致，所以第4行函數mydata()內串列內容改變時，函數執行結束回到主程式可以看到主程式串列內容也更改了。

<hr>

# 在函數內容修訂串列的內容

由前一小節可以知道Python允許主程式呼叫函數時，傳遞的參數是串列名稱，這時在函數內直接修訂串列的內容，同時串列經過修正後，主程式的串列也將隨著永久性更改的結果。






