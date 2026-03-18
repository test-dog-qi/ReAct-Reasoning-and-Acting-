from dotenv import load_dotenv
from core.my_llm import MyLLM


# 加载环境变量
load_dotenv()

# 实例化我们重写的客户端，并指定provider
llm = MyLLM(provider="modelscope")

