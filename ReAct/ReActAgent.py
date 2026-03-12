# ReAct 提示词模板
from typing import List

from ReAct.llms import HelloAgentsLLM
from ReAct.tools import ToolExecutor

REACT_PROMPT_TEMPLATE = """
请注意，你是一个有能力调用外部工具的智能助手。

可用工具如下:
{tools}

请严格按照以下格式进行回应:

Thought: 你的思考过程，用于分析问题、拆解任务和规划下一步行动。
Action: 你决定采取的行动，必须是以下格式之一:
- `{{tool_name}}[{{tool_input}}]`:调用一个可用工具。
- `Finish[最终答案]`:当你认为已经获得最终答案时。
- 当你收集到足够的信息，能够回答用户的最终问题时，你必须在Action:字段后使用 Finish[最终答案] 来输出最终答案。

现在，请开始解决以下问题:
Question: {question}
History: {history}
"""

class ReactAgent:
    def __init__(self, llm_clinet: HelloAgentsLLM, toolExecutor: ToolExecutor, max_steps: int):
        self.llm_clinet = llm_clinet
        self.toolExecutor = toolExecutor
        self.max_steps = max_steps
        self.history: List[str] = []

    def run(self, question: str) -> str:
        """
        运行ReAct智能体来回答一个问题。
        """
        self.history = [] # 每次运行时重置历史记录
        current_step = 0

        with current_step < self.max_steps:
            current_step += 1
            print(f"--- 第 {current_step} 步 ---")

            # 1.格式化提示词


            # 2.调用llm进行思考

