## 保存图片
### 1
```python
import requests
from bs4 import BeautifulSoup

r = requests.get("http://www.pythonscraping.com")
bs = BeautifulSoup(r.text， "lxml")
image = bs.find("a", {"id": "logo"}).find("img")["src"]
```
![20180102.png](http://upload-images.jianshu.io/upload_images/3146277-2c3d64e96bd5cbb5.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
```
ir = requests.get(image)
if ir.status_code == 200:
    open('logo.jpg', 'wb').write(ir.content)
```
### 2
```
import requests
import shutil

r = requests.get(settings.STATICMAP_URL.format(**data), stream=True)
if r.status_code == 200:
    with open(path, 'wb') as f:
        r.raw.decode_content = True
        shutil.copyfileobj(r.raw, f)        
```
http://stackoverflow.com/questions/13137817/how-to-download-image-using-requests