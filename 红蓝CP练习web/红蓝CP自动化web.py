from appium import webdriver
from appium.webdriver.extensions.android.nativekey import AndroidKey
import time
import pytest

class Test_rbapp:

  desired_caps = {
    'platformName': 'Android', # 被测手机是安卓
    'platformVersion': '6', # 手机安卓版本
    'deviceName': 'xxx', # 设备名，安卓手机可以随意填写
    'appPackage': 'com.xiaoyu.rightone', # 启动APP Package名称
    'appActivity': '.features.launch.LaunchActivity', # 启动Activity名称
    'unicodeKeyboard': True, # 使用自带输入法，输入中文时填True
    'resetKeyboard': True, # 执行完程序恢复原来输入法
    'noReset': True,       # 不要重置App
    'newCommandTimeout': 6000,
    'automationName' : 'UiAutomator2'
    # 'app': r'd:\apk\bili.apk',
  }

  # 连接Appium Server，初始化自动化环境
  driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

  # 设置缺省等待时间
  driver.implicitly_wait(10)
  #点击注册/登录按钮
  driver.find_element_by_class_name('android.widget.Button').click()
  #点击清除手机号码
  driver.find_elements_by_class_name('android.widget.ImageView')[1].click()
  #输入手机号码
  driver.find_element_by_class_name('android.widget.EditText').send_keys('17858753967')


  """获取窗口大小"""
  def window_size():
    x = driver.get_window_size()['width']
    y = driver.get_window_size()['height']
    return x,y
  """下拉任务栏"""
  def task_bar():
    point = window_size()
    x1 = int(point[0]*0.5)
    y1 = int(point[1]*0.01)
    y2 = int(point[1]*0.9)
    driver.swipe(x1,y1,x1,y2)
  task_bar()
  time.sleep(1)
  #点击清除按钮清除消息
  try:
    driver.find_element_by_accessibility_id('清除所有通知。').click()
  except:
    print('没有消息可以清空')
    """"上滑任务栏"""
    def task_bar1():
      point1 = window_size()
      x1 = int(point1[0]*0.5)
      y1 = int(point1[1]*0.6)
      y2 = int(point1[1]*0.3)
      driver.swipe(x1,y1,x1,y2)
    task_bar1()
  else:
    print('消息已清空')


  #点击获取验证码
  driver.find_element_by_class_name('android.widget.Button').click()
  time.sleep(20)
  """下拉任务栏"""
  def task_bar2():
    point = window_size()
    x1 = int(point[0]*0.5)
    y1 = int(point[1]*0.01)
    y2 = int(point[1]*0.9)
    driver.swipe(x1,y1,x1,y2)
  task_bar2()
  #找到短信
  message = driver.find_elements_by_id('android:id/text')[1]
  idd = message.text

  #提取短信中的数字
  number = idd.split('：')[1].split('，')[0]
  print(number)
  """上滑任务栏"""
  def task_bar3():
    point1 = window_size()
    x1 = int(point1[0] * 0.5)
    y1 = int(point1[1] * 0.6)
    y2 = int(point1[1] * 0.3)
    driver.swipe(x1, y1, x1, y2)
  task_bar3()
  #填入验证码
  driver.find_element_by_class_name('android.widget.EditText').send_keys(number)
  driver.implicitly_wait(10)


  #点击消息按钮进入消息页面
  driver.find_element_by_xpath('//*[@resource-id="com.xiaoyu.rightone:id/bottom_layout"]'
                               '//android.widget.LinearLayout[2]').click()
  #点击消息框进入查看消息
  driver.find_element_by_xpath('//*[@resource-id="com.xiaoyu.rightone:id/chat_recycler_view"]'
                               '//android.widget.RelativeLayout[3]').click()
  #点击返回到消息页面
  driver.find_element_by_accessibility_id('转到上一层级').click()
  #进入第二个消息框
  driver.find_element_by_xpath('//*[@resource-id="com.xiaoyu.rightone:id/chat_recycler_view"]'
                               '//android.widget.RelativeLayout[4]').click()
  #点击返回到消息页面
  driver.find_element_by_accessibility_id('转到上一层级').click()

  #点击广场
  driver.find_element_by_xpath('//*[@resource-id="com.xiaoyu.rightone:id/bottom_layout"]'
                               '//android.widget.LinearLayout[4]').click()

  #循环操作
  i = 0
  while i < 10 :
    """获取界面大小"""
    def test_size():
      x = driver.get_window_size()['width']
      y = driver.get_window_size()['height']
      return x,y

    """向下滑动的封装"""
    def swip_down():
      size = test_size()
      x1 = int(size[0]*0.5) #获取X轴的中间点
      y1 = int(size[1]*0.9) #*0.9表示距离底部近
      y2 = int(size[1]*0.1)
      driver.swipe(x1,y1,x1,y2,1000)

    swip_down()
    i+=1


  #点击发布动态按钮
  driver.find_element_by_id('publish_button').click()
  #点击选择照片按钮
  driver.find_elements_by_class_name('android.widget.ImageView')[0].click()
  #点击选择图片
  driver.find_elements_by_class_name('android.widget.TextView')[0].click()
  #选择图片
  driver.find_elements_by_class_name('android.widget.CheckBox')[6].click()
  #点击原图
  driver.find_element_by_class_name('android.widget.RadioButton').click()
  #点击确定
  driver.find_elements_by_class_name('android.widget.TextView')[0].click()
  #点击发布
  driver.find_elements_by_class_name('android.widget.TextView')[0].click()
  #点击我的
  driver.find_element_by_xpath('//*[@resource-id="com.xiaoyu.rightone:id/bottom_layout"]'
                               '//android.widget.LinearLayout[5]').click()
  #点击我的
  driver.find_elements_by_class_name('android.widget.RelativeLayout')[2].click()
  #获取图片列表
  pitures = driver.find_elements_by_class_name('android.widget.ImageView')
  if len(pitures) >= 3:
    print('动态发布成功')

  else:
    print('动态没能正常发布')


  #返回主界面
  driver.find_element_by_class_name('android.widget.ImageButton').click()
  #滑动窗口
  swip_down()
  #点击设置
  driver.find_elements_by_class_name('android.widget.RelativeLayout')[6].click()
  #点击退出登录
  driver.find_element_by_id('icon_text_loading_button_icon_text').click()
  #点击确定
  driver.find_elements_by_class_name('android.widget.Button')[0].click()
  #获取文本
  reg_login = driver.find_element_by_class_name('android.widget.Button')
  print(reg_login.text)

  test_demo = '注册/登录'
  if reg_login.text == test_demo :
    print('本次回归测试完成，满足测试要求')

  else:
    print('本次回归测试完成，不满足测试要求')






