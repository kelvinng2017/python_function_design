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
不論是return或接續右邊的回傳值皆是可有可無，如果有回傳多個資料彼此需以逗號","間隔。
