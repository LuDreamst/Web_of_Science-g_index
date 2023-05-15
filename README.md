# Web_of_Science-g_index
Web of Science 作者G_index计算
## 程序实现什么？ 
因g指数无法直观显示，手动计算又十分麻烦，故用selenium+chrome计算并输出web of science作者的g指数（顺带输出h指数） 
## 我所使用的配置 
1.python3.9+selenium(建议3.6以上)  
2.google_chrome+chromedriver(二者的版本号须一致)  
3.windows10(11亦可)  
## 如何操作？ 
## 更新于2023/5/15：感谢计算机科学的进步与相关人员的付出，如果您连接的网络无需登录可直接使用“文献库”功能，您可以直接运行g_index2.py，而不必进行繁琐的设置  
*下文为g_index.py的使用说明*  
1.chromedriver.exe（[下载连接](https://registry.npmmirror.com/binary.html?path=chromedriver/)）分别放置在chrome.exe和python.exe所在目录下，如下所示：  
![image](https://github.com/LuDreamst/WebofScience-g_index/assets/53106447/de9768ce-9b44-4211-b3b6-3efbb38953d9)  
![image](https://github.com/LuDreamst/WebofScience-g_index/assets/53106447/1ee48d8d-ab93-4c6d-86cf-81bbfcdac78c)  
**图中展示的皆是默认安装路径，具体路径视个人情况**  
  
2.在终端输入如下指令以调用程序可识别的浏览器：`chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\Workspace\Code\selenium\ChromeProfile"`  
**指令中的路径视个人情况，附图如下**  
![image](https://github.com/LuDreamst/WebofScience-g_index/assets/53106447/3c6b60ad-3eb5-41eb-a83b-4f421425f884)  
  
3.使用浏览器进入web of science的作者的**引文报告界面**，附图如下：  
![image](https://github.com/LuDreamst/WebofScience-g_index/assets/53106447/972b8c3a-a227-423f-8849-9d607b6e526c)  
  
4.运行g_index.py即可输出结果  
## 注意事项！  
1.chromedriver**必须**与chrome的版本一致，因为没有正常的手段停止chrome的自动更新，chrome的版本号一变，chromedriver**必须**也跟着变  
2.如未来网站重构，程序可能失效
