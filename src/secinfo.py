import requests,json,os,markdown
from bs4 import BeautifulSoup

# 获取配置文件信息
def config():
    config_file_path = os.path.join(script_dir, '../config.json')
    with open(config_file_path, 'r') as f:
        config_info = json.load(f)
    return config_info
# 获取文章内容
def get_article_content():
    data_dir = os.path.join(script_dir, '../data')
    article_content_file = os.path.join(data_dir, f"{''.join(filter(str.isalnum, config()['web_content_url']))}.md")
    with open(article_content_file, 'r', encoding='utf-8') as f:
        article_content = f.read()
    # 1. 将 Markdown 转换为 HTML
    html = markdown.markdown(article_content)
    
    # 2. 使用 BeautifulSoup 优化 HTML
    soup = BeautifulSoup(html, 'html.parser')
    
    # 3. 注入微信公众号支持的样式
    for tag in soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6']):
        tag['style'] = 'font-weight: bold; margin: 20px 0 10px;'
    
    for tag in soup.find_all('p'):
        tag['style'] = 'font-size: 16px; line-height: 1.8; margin: 10px 0;'
    
    for tag in soup.find_all('img'):
        tag['style'] = 'max-width: 100%; height: auto; display: block; margin: 10px auto;'
    
    # 4. 返回优化后的 HTML
    return str(soup)
    # return article_content

# 获取access_token
def get_access_token(appid, appsecret):
    url = "https://api.weixin.qq.com/cgi-bin/token"
    params = {
        "grant_type": "client_credential",
        "appid": appid,
        "secret": appsecret
    }
    try:
        response = requests.get(url, params=params)
        return response.json()["access_token"]
    except Exception as e:
        print(e)
        return None

# 上传图片素材
def upload_image(access_token):
    picture_dir = os.path.join(script_dir, '../data')
    picture_file = os.path.join(picture_dir, f"{''.join(filter(str.isalnum, 'test'))}.png")
    url = f"https://api.weixin.qq.com/cgi-bin/material/add_material?access_token={access_token}&type=image"
    with open(picture_file, 'rb') as file:
        files = {
            'media': (os.path.basename(picture_file), file, "image/png")
        }
        response = requests.post(url, files=files)
    return response.json()["media_id"]


# 微信公众号上传草稿文章
def create_article(access_token, TITLE, DIGEST, CONTENT, THUMB_MEDIA_ID):
    url = f'https://api.weixin.qq.com/cgi-bin/draft/add?access_token={access_token}'
    data = {
        "articles": [
            {
                "article_type":"news",
                "title":TITLE,
                "author":'We12',
                "digest":DIGEST,
                "content":CONTENT,
                # "content_source_url":CONTENT_SOURCE_URL,
                "thumb_media_id":THUMB_MEDIA_ID,
                "need_open_comment":'Uint32',
                "only_fans_can_comment":0,
                # "pic_crop_235_1":X1_Y1_X2_Y2,
                # "pic_crop_1_1":X1_Y1_X2_Y2
            }
        ]
    }
    headers = {"Content-Type": "application/json"}
    response = requests.post(url, data=json.dumps(data, ensure_ascii=False), headers=headers)
    if response.json()["media_id"]:
        print("草稿发布成功")
    else:
        print("草稿发布失败:{response.json()}")

# 使用示例
if __name__ == "__main__":
    # 获取当前脚本的目录
    script_dir = os.path.dirname(os.path.realpath(__file__))
    APPID = config()["wx_appid"]
    APPSECRET = config()["wx_secret"]
    access_token = get_access_token(APPID, APPSECRET)
    # print(access_token)
    # 上传图片素材
    THUMB_MEDIA_ID = upload_image(access_token)
    # print(THUMB_MEDIA_ID)
    # 构建图文文章
    json_data = get_article_content()
    # print(json_data)
    # 内容清洗
    
    # TITLE = json_data["title"]
    # DIGEST = json_data["DIGEST"]
    TITLE = "测试标题"
    DIGEST = "测试摘要"
    CONTENT = json_data
    THUMB_MEDIA_ID = THUMB_MEDIA_ID
    create_article(access_token, TITLE, DIGEST, CONTENT, THUMB_MEDIA_ID)