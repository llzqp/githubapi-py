import os
from openai import OpenAI

# 直接在代码中指定 GitHub 访问令牌
token = "你的token"

endpoint = "https://models.inference.ai.azure.com"
model_name = "gpt-4o"


# 初始化 OpenAI 客户端
client = OpenAI(
    base_url=endpoint,
    api_key=token,
)

# 设置系统角色
messages = [
    {
        "role": "system",
        "content": "You are a helpful assistant.",
    }
]

while True:
    # 接收用户输入的问题
    user_input = input("请输入你的问题（输入 'exit' 退出）：")

    # 检查是否退出
    if user_input.lower() == 'exit':
        print("退出程序")
        break

    # 将用户输入的问题添加到对话历史
    messages.append({
        "role": "user",
        "content": user_input,
    })

    # 发送请求到 GPT-4 模型
    response = client.chat.completions.create(
        messages=messages,
        model=model_name,
        temperature=1.0,
        max_tokens=1000,
        top_p=1.0
    )

    # 获取模型的回答
    assistant_response = response.choices[0].message.content

    # 将模型的回答添加到对话历史
    messages.append({
        "role": "assistant",
        "content": assistant_response,
    })

    # 输出模型的回答
    print("助手:", assistant_response)
