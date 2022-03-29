"""
 * Project name(项目名称)：Python包
 * Package(包名): 
 * File(文件名): __init__.py
 * Author(作者）: mao
 * Author QQ：1296193245
 * GitHub：https://github.com/maomao124/
 * Date(创建日期)： 2022/3/29 
 * Time(创建时间)： 20:58
 * Version(版本): 1.0
 * Description(描述)： 
 """
from package.a import f1, str1
from package.b import f2

print("加载包")

__all__ = ["f1", "str1", "f2"]
