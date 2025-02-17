import os, sys,json,subprocess

# 获取配置文件信息
def config():
    config_file_path = os.path.join(script_dir, 'config.json')
    with open(config_file_path, 'r') as f:
        config_info = json.load(f)
    return config_info


if __name__ == '__main__':
    # 获取当前脚本的目录
    script_dir = os.path.dirname(os.path.realpath(__file__))
    script_file = os.path.join(script_dir,'src')
    script_app_file = config()["channel_type"]
    if script_app_file == "deepseek":
        deepseek_app_file = os.path.join(script_file, 'deepseek_app.py')
        subprocess.run(['python3', deepseek_app_file])
    elif script_app_file == "kimi":
        kimi_app_file = os.path.join(script_file, 'kimi_app.py')
        subprocess.run(['python3', kimi_app_file])
    else:
        print("暂不支持该渠道")
    secinfo_file = os.path.join(script_file, 'secinfo.py')
    subprocess.run(['python3', secinfo_file])

