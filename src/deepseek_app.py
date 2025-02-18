import os,json,requests,datetime
from openai import OpenAI

# 获取配置文件信息
def config():
    config_file_path = os.path.join(script_dir, '../config.json')
    with open(config_file_path, 'r') as f:
        config_info = json.load(f)
    return config_info

def get_web_content(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        # print(response.text)
        return response.text
    else:
        return None

def get_markdown_article(web_content):
    client = OpenAI(api_key=config()["api_key"], base_url="https://api.deepseek.com")
    response = client.chat.completions.create(
        model=config()["get_markdown_article_model"],
        messages=[
            {"role": "system", "content": config()["get_markdown_article_prompt"]},
            {"role": "user", "content": web_content},
        ],
        max_tokens=1024,
        temperature=0.7,
        stream=False
    )
    result = response.choices[0].message.content
    # print(result)
    return result   
# 调用deepseek API进行文章改写
def rewrite(markdown_article):
    client = OpenAI(api_key=config()["api_key"], base_url="https://api.deepseek.com")
    response = client.chat.completions.create(
        model=config()["rewrite_article_model"],
        messages=[
            {"role": "system", "content": config()["rewrite_article_prompt"]},
            {"role": "user", "content": markdown_article},
        ],
        max_tokens=1024,
        temperature=0.7,
        stream=False
    )
    result = response.choices[0].message.content
    return result

def save_markdown_article(rewrite_article):
    data_dir = os.path.join(script_dir, '../data')
    markdown_file = os.path.join(data_dir, f"{''.join(filter(str.isalnum, config()['web_content_url']))}.md")
    # 保存到本地文件
    with open(markdown_file, 'w', encoding='utf-8') as file:
        file.write(rewrite_article)
    print(f"article has been saved to {markdown_file}")


if __name__ == '__main__':
    # 获取当前脚本的目录
    script_dir = os.path.dirname(os.path.realpath(__file__))
    web_content_url = config()["web_content_url"]
    web_content = get_web_content(web_content_url)
    print("网页内容获取完成！")
    markdown_article = get_markdown_article(web_content)
    print("文章内容通过deepseek提取完成！")
    # 调用deepseek API进行文章改写
    rewrite_article = rewrite(markdown_article)
    print("文章内容改写完成！")
    # 保存到本地 .md 文件
    save_markdown_article(rewrite_article)



    