# OXY
### 医学处理应用软件设计 
\t\t现目前已有血氧软件是国外的Oxymap,主界面为英文，结合软件界面交互性不够完善，同时功能性不够强大，对眼底图像的计算主要为原软件提供的算法，处理方式单一。基于以上特点，现考虑自己设计一个血氧软件平台，在解决上述缺点的同时，能够拥有一个充分考虑医院使用者需求及算法开发者实践的实验室软件。

\t\t经调研及结合自身情况充分考虑，本软件平台应具有如下特性：
   1.开发周期相对快一点较好，现目前图像实现的算法大多是基于MATLAB是实现，后期将转为python或c++，以dll或sdk方式添加进软件，该软件设计时需考虑留出接口，方便后期实现算法添加；
   2.软件代码要易于维护，及设计软件应考虑模块化编程；
 - 3.考虑软件涉及病人隐私，后期数据库应考虑一定的安全性和保密性；
 
### 结合以上，对该软件语言平台设计级参考资源如下：
 1．语言：python3
 2．软件界面设计：PyQt5
 3．代码编辑平台：eric6、PyCharm
 4．开发平台环境配置：
\t\t http://blog.csdn.net/weiaitaowang/article/details/52045360
\t\t http://blog.csdn.net/a359680405/article/details/45074761
  
### 网上参考资源：
 1.《PyQt5快速开发与实战》
 * GitHub地址：https://github.com/cxinping/PyQt5.git
 2．PyQt5官方案例中文解析
 * GitHub地址：https://github.com/maicss/PyQt5-Chinese-tutoral
 
 ### 软件设计界面界面
![main_Window](./image/main_Window.png)
![result_Window](./image/result_Window.png)
