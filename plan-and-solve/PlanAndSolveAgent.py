from typing import List

from ReAct.llms import HelloAgentsLLM
from Planner import Planner
from Executor import Executor

class PlanAndSolveAgent():
    """
    初始化智能体，同时创建规划器和执行器实例。协调者角色
    """
    def __init__(self, llm_client: HelloAgentsLLM):
        self.llm_client = llm_client
        self.planner = Planner(self.llm_client)
        self.executor = Executor(self.llm_client)

    def run(self, question: str):
        """
                运行智能体的完整流程:先规划，后执行。
                """
        print(f"\n--- 开始处理问题 ---\n问题: {question}")

        plan = self.planner.plan(question)

        # 检查计划是否成功
        if not plan:
            print("\n--- 任务终止 --- \n无法生成有效的行动计划。")
            return

        final_answer = self.executor.execute(plan)

        print(f"\n--- 任务完成 ---\n最终答案: {final_answer}")


if __name__ == '__main__':
    question = "一个水果店周一卖出了15个苹果。周二卖出的苹果数量是周一的两倍。周三卖出的数量比周二少了5个。请问这三天总共卖出了多少个苹果？"
    llm_client = HelloAgentsLLM()
    plan_and_solve = PlanAndSolveAgent(llm_client)
    plan_and_solve.run(question)

