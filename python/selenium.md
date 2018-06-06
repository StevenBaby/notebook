# selenium

selenium 是一个web自动化测试工具，他支持各种浏览器，包括chrome, safari,firefox 等主流浏览器。


## 安装

### pip 安装 selenium

    pip install selenium 

### 浏览器驱动

| 浏览器 | 地址 |
| - | - | 
| chrome | https://sites.google.com/a/chromium.org/chromedriver/downloads | 
| Edge | https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/ |
| FireFox | https://github.com/mozilla/geckodriver/releases |
| Safari | https://webkit.org/blog/6900/webdriver-support-in-safari-10/ |


### selenium server

## 开始

### 简单使用

如果已Python安装selenium，可以写一下下面的程序:

```python
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("http://www.python.org")
assert "Python" in driver.title
elem = driver.find_element_by_name("q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
driver.close()
```

### 单元测试

selenium很大概率上会被用在单元测试上，selenium自身并不提供测试工具和框架。可以使用python unittest 来写单元测试。

下面的例子演示了一个使用 selenium 的测试用例，自动搜索python.org。

```python
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("http://www.python.org")
        self.assertIn("Python", driver.title)
        elem = driver.find_element_by_name("q")
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)
        assert "No results found." not in driver.page_source


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
```

### 使用远程驱动

刨坑待填

## 导航

如果想让浏览器去某个连接，可以直接写

```python
driver.get("http://www.google.com")
```

在继续执行下面的代码之前，浏览器驱动将会等待页面完全加载（这说明，onload 事件不可用），如果你的页面使用了AJAX来加载页面，驱动可能不知道页面何时加载完毕。如果需要确保页面加载完成，你可以使用 waits.

### 与页面的交互

获取页面元素

```html
<input type="text" name="passwd" id="passwd-id" />
```

```python
element = driver.find_element_by_id("passwd-id")
element = driver.find_element_by_name("passwd")
element = driver.find_element_by_xpath("//input[@id='passwd-id']")
```

你同样可以使用链接的文本来获取元素，但是需要注意的是，文本必须完全匹配！同样需要注意的是在使用XPATH的时候，如果没有只有一个元素匹配，那么就只有这个元素返回。如果没有元素匹配，将会有异常 **NoSuchElementException** 抛出。

所以，得到了元素，能对他做些什么呢？首先，你可能会在输入框里输入一些文本。

```python
element.send_keys("some text")
```

你可以使用Keys来模仿键盘操作

```python
element.send_keys(" and some", Keys.ARROW_DOWN)
```

可以向所有的元素调用 send_keys，来测试键盘快捷键。如果想清除输入框的话，可以使用如下方法

```python
element.clear()
```

### 填写表单

我们已经知道了怎么向输入框里输入文本，但是其他的元素呢？你可以修改下拉框的状态，你可以使用 'setSelected' 来设置一些选项标签。用 SELECT 标签来操作不算很坏。

```python
element = driver.find_element_by_xpath("//select[@name='name']")
all_options = element.find_elements_by_tag_name("option")
for option in all_options:
    print("Value is: %s" % option.get_attribute("value"))
    option.click()
```

你将找到页面中第一个 SELECT 标签。然后将每个选项的值打印出来，然后点击。

可以看到，直接操作 SELECT 标签并不是特别高效。浏览器驱动支持一个叫 Select 的类，他提供了一些有用的方法来与之交互。

```python
from selenium.webdriver.support.ui import Select
select = Select(driver.find_element_by_name('name'))
select.select_by_index(index)
select.select_by_visible_text("text")
select.select_by_value(value)
```

驱动同样提供了取消选择的方法

```python
select = Select(driver.find_element_by_id('id'))
select.deselect_all()
```

假设我们有这样的测试，需要默认的已选的选项， Select 类提供了一个属性方法返回一个列表。

```language
select = Select(driver.find_element_by_xpath("//select[@name='name']"))
all_selected_options = select.all_selected_options
```

获取所有可用选项

```python
options = select.options
```

提交表单

```python
driver.find_element_by_id("submit").click()

element.submit() # from
```

### 拖放


### 移动窗口和frames


### 弹出框


### 历史记录和位置


### Cookies


## 定位元素

有多种方式可以从页面中定位元素，你可以根据你的情况使用最合适的。selenium 提供了下面的方法来定位页面中的元素：

- find_element_by_id
- find_element_by_name
- find_element_by_xpath
- find_element_by_link_text
- find_element_by_partial_link_text
- find_element_by_tag_name
- find_element_by_class_name
- find_element_by_css_selector

获取多个元素（返回一个列表）：


- find_elements_by_name
- find_elements_by_xpath
- find_elements_by_link_text
- find_elements_by_partial_link_text
- find_elements_by_tag_name
- find_elements_by_class_name
- find_elements_by_css_selector

除了上面公开的方法，还有两种特别有用的方法可以从页面中定位元素

- find_element
- find_elements

例如:

```python
from selenium.webdriver.common.by import By

driver.find_element(By.XPATH, '//button[text()="Some text"]')
driver.find_elements(By.XPATH, '//button')
```

这些属性定义再 By 类中：

```python
ID = "id"
XPATH = "xpath"
LINK_TEXT = "link text"
PARTIAL_LINK_TEXT = "partial link text"
NAME = "name"
TAG_NAME = "tag name"
CLASS_NAME = "class name"
CSS_SELECTOR = "css selector"
```

## 等待

现在大多数的web应用使用了AJAX技术，当一个浏览器加载页面的时候，页面中的元素可能在不同的时间段加载。这对定位元素造成了一定的困难：如果一个元素不再DOM中，定位的方法会抛出  
**ElementNotVisibleException** 异常，使用等待，我们可以解决这个问题。等待使得动作之前松懈了一些，使得定位元素更可能被找到。

selenium 提供了两种方式来等待，显示等待和隐式等待，显式等待要求浏览器等待一个确切的条件变量，然后再来执行其他操作。隐式等待让浏览器在没有定位到元素前，等待一段时间。

### 显式等待

式等待要求浏览器等待一个确切的条件变量，然后再来执行其他操作。极限的可能是直接执行 time.sleep() 方法，这里有一些方便的方法来让你写出代码，等待你需要的长度。浏览器等待和条件变量来组合可以达到这个需求。

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
driver.get("http://somedomain/url_that_delays_loading")
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "myDynamicElement"))
    )
finally:
    driver.quit()
```

上面的代码将会在10秒之内找到元素并返回，如果没有找到的话，将抛出 **TimeoutException** 异常。默认情况下 浏览器等待每隔500毫秒来尝试获取元素直到成功。

### 条件变量

这里是一些公用的条件变量，下面是一些方法，可以不用显式地写条件变量的类。

- title_is
- title_contains
- presence_of_element_located
- visibility_of_element_located
- visibility_of
- presence_of_all_elements_located
- text_to_be_present_in_element
- text_to_be_present_in_element_value
- frame_to_be_available_and_switch_to_it
- invisibility_of_element_located
- element_to_be_clickable
- staleness_of
- element_to_be_selected
- element_located_to_be_selected
- element_selection_state_to_be
- element_located_selection_state_to_be
- alert_is_present

```python
from selenium.webdriver.support import expected_conditions as EC

wait = WebDriverWait(driver, 10)
element = wait.until(EC.element_to_be_clickable((By.ID, 'someid')))
```

### 隐式等待

隐式等待是告诉驱动查找某个元素的时候，如果该元素没有立即可用，那么就等待一段时间，默认设置为0，一旦设置，隐式等待将对驱动器对象的整个生命周期可用。

## 浏览器驱动 API


当前url

```python
driver.current_url
```

关闭当前窗口

```python
driver.close()
```

### 异常

selenium.common.exceptions.MoveTargetOutOfBoundsException 提供给ActionChainsmovable()方法的目标无效时，异常将抛出，例如：超出文件外

### 动作链 ActionChains

ActionChains 可以用来做低级交互，比如鼠标移动，鼠标按钮点击，键盘点击和右键菜单交互，这对于实现复杂的动作比如悬停、拖拽和释放等非常有用。

当你调用ActionChains的一些方法的时候，这些动作将会存储在ActionChains对象的队列中。当你调用perform() 方法时。这些动作将会以队列中的顺序来依次执行。

ActionChains 可以使用链式模式

```python
menu = driver.find_element_by_css_selector(".nav")
hidden_submenu = driver.find_element_by_css_selector(".nav #submenu1")

ActionChains(driver).move_to_element(menu).click(hidden_submenu).perform()
```

也可以使用单步模式

```python
menu = driver.find_element_by_css_selector(".nav")
hidden_submenu = driver.find_element_by_css_selector(".nav #submenu1")

actions = ActionChains(driver)
actions.move_to_element(menu)
actions.click(hidden_submenu)
actions.perform()
```

| 方法 | 作用 | 
| - | - |
| click | 点击元素，如果元素为空，则点击当前鼠标位置 |
| click_and_hold | 在元素上按下鼠标 | 
| context_click |  |
| double_click |  |
| drag_and_drop |  |
| drag_and_drop_by_offset |  |
| key_down |  |
| key_up |  |
| move_by_offset |  |
| move_to_element |  |
| move_to_element_with_offset |  |
| pause |  |
| release |  |
| perform |  |
| reset_actions |  |
| send_keys |  |
| send_keys_to_element |  |


### Alert

### 特殊按键

### By

### Desired Capabilities

### 触屏事件

## firefox  火狐浏览器配置

### 代理 

```python
capabilities = webdriver.DesiredCapabilities.FIREFOX.copy()

proxy = webdriver.Proxy()
proxy.proxy_type = webdriver.common.proxy.ProxyType.MANUAL
proxy.http_proxy = "localhost:8080"
proxy.add_to_capabilities(capabilities)

driver = webdriver.Firefox(firefox_profile=profile, options=options, capabilities=capabilities)
```

### 配置

```python
profile = webdriver.FirefoxProfile()

# 使用TAB
profile.set_preference("browser.tabs.remote.autostart", False)
profile.set_preference("browser.tabs.remote.autostart.1", False)
profile.set_preference("browser.tabs.remote.autostart.2", False)

# 使用缓存
profile.set_preference("browser.cache.disk.enable", False)
profile.set_preference("browser.cache.memory.enable", False)
profile.set_preference("browser.cache.offline.enable", False)
profile.set_preference("network.http.use-cache", False)

# 默认激活flash插件
profile.set_preference("plugin.state.flash", 2)

```