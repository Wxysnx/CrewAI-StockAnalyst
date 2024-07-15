import sys
import os
from crew import StockAnalysisCrew

def run():
    """
    运行股票分析Crew并生成分析报告。
    默认分析Amazon (AMZN)股票，除非指定其他股票代码。
    """
    # 检查是否提供了股票代码参数
    if len(sys.argv) > 1 and sys.argv[1] != "train":
        company_stock = sys.argv[1].upper()
    else:
        # 默认使用AMZN
        company_stock = 'AMZN'
    
    print(f"## 开始分析股票: {company_stock}")
    print('-------------------------------')
    
    inputs = {
        'query': f'分析{company_stock}股票',
        'company_stock': company_stock,
    }
    return StockAnalysisCrew().crew().kickoff(inputs=inputs)

def train():
    """
    训练crew指定次数的迭代。
    用法: python main.py train <迭代次数>
    """
    inputs = {
        'query': '分析去年的收入',
        'company_stock': 'AMZN',
    }
    try:
        iterations = int(sys.argv[2]) if len(sys.argv) > 2 else 1
        StockAnalysisCrew().crew().train(n_iterations=iterations, inputs=inputs)
    except Exception as e:
        raise Exception(f"训练crew时出错: {e}")
   
if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "train":
        train()
    else:
        print("## 欢迎使用股票分析AI系统")
        print('-------------------------------')
        result = run()
        print("\n\n########################")
        print("## 分析报告")
        print("########################\n")
        print(result)