# caps
崩坏の大小写  
池塘の英文 iS vErY gOoD !  
仿池塘的大小写崩坏写的程序。  

## 干嘛用的？  
输入一个字符串，输出一个大小写崩坏的字符串。  

## 依赖

- Python 3.x
- pypinyin

您可以使用 `pip install pypinyin` 来安装 `pypinyin` 。
## 操作
### 终端
```bash
python caps.py -h 要转换的字符串
```  
### Python 脚本内导入
本脚本提供了一个继承了 `str` 基本类型的类 `str_of_chitang`。该类提供了一个成员函数 `str_of_chitang.chitang(self)` 。
要使用此类，请添加一行代码：
```python
from caps import str_of_chitang
```

然后，您可以定义一个实例：
```python
test = str_of_chitang('windows is a piece of shit')
```

并且使用 `str_of_chitang.chitang(self)` :
```python
test.chitang()
```

输出：
```
wInDoWs Is A pIeCe Of ShIt
```

