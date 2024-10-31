from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import time
from sympy import sympify, SympifyError
import math  # 导入数学模块以便进行四舍五入操作

# 设置WebDriver，比如使用Edge
driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))

def get_question():
    driver.get("http://127.0.0.1/")
    time.sleep(1)  # 等待页面加载
    question_element = driver.find_element(By.CLASS_NAME, "question")
    if question_element:
        return question_element.text.strip()
    return None

def convert_to_python_expression(question):
    # 替换运算符，清洗字符
    question = question.replace("÷", "/")
    question = question.replace("×", "*")
    question = question.replace("x", "*")
    question = question.replace("是", "")
    question = question.replace("？", "")
    question = question.replace("=", "")
    question = question.strip()
    return question

def calculate_answer(question):
    question = convert_to_python_expression(question)

    # 解析表达式
    try:
        # 使用 sympy 解析表达式
        answer = sympify(question)

        # 根据操作类型调整结果
        if '/' in question:
            # 对于除法，进行四舍五入
            return round(answer)
        else:
            # 对于加法、减法和乘法，确保结果为整数
            return int(answer)
    except SympifyError as e:
        print(f"表达式解析错误: {e}")
        return None
    except ZeroDivisionError as e:
        print(f"计算错误: {e}")
        return None

def submit_answer(answer):
    input_box = driver.find_element(By.NAME, "answer")
    input_box.clear()
    input_box.send_keys(str(answer))
    submit_button = driver.find_element(By.XPATH, "//input[@type='submit']")
    submit_button.click()

def main():
    while True:
        question = get_question()
        if question:
            print(f"题目: {question}")
            answer = calculate_answer(question)
            if answer is not None:
                print(f"计算结果: {answer}")
                submit_answer(answer)  # 在这里提交答案
                time.sleep(1)
            else:
                print("无法计算答案")
        else:
            print("未能获取题目")

        time.sleep(5)

if __name__ == "__main__":
    try:
        main()
    finally:
        driver.quit()