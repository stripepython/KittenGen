import os
import zipfile

import jinja2
from flask import Flask, request, send_file

from .lib import global_vars   # 默认变量

app = Flask(__name__)

GCC_PATH = 'g++.exe'   # 这里填写你的g++路径
DIR_PATH = os.path.join(os.path.dirname(__file__), 'templates')


def renders(file: str, **kwargs):
    with open(os.path.join(DIR_PATH, file), 'r', encoding='utf-8') as f:
        s = f.read()
    template = jinja2.Template(s)
    return template.render(**kwargs)


@app.route('/', methods=['GET', 'POST'])
def index():   # 主网页
    if request.method == 'GET':
        return renders('index.html', error=None)
    cwd = os.getcwd()  # 记录当前工作路径
    data_path = os.path.join(cwd, 'data')
    if not os.path.exists(data_path):
        os.mkdir(data_path)
    os.chdir(data_path)  # 进入数据工作路径

    form = request.form
    std, maker, num, options = form.get('std'), form.get('maker'), int(form.get('num')), form.get('options')
    try:
        maker_complied = compile(maker, 'maker.py', 'exec')   # 先编译生成器
    except (Exception, SystemExit) as err:
        os.chdir(cwd)  # 切换回原工作路径
        return renders('index.html', error=str(err))

    use_spj, use_cfg = form.get('useSpj'), form.get('useCfg')
    if use_spj:
        checker = form.get('checker')
        with open('checker.cpp', 'w', encoding='utf-8') as f:
            f.write(checker)
    if use_cfg:
        config = form.get('config')
        with open('config.yml', 'w', encoding='utf-8') as f:
            f.write(config)

    with open('std.cpp', 'w', encoding='utf-8') as f:
        f.write(std)   # 写入std.cpp
    os.system(f'{GCC_PATH} {options} -o std.exe std.cpp')    # 编译 std

    for i in range(1, num + 1):   # 循环并生成数据
        local_vars = global_vars.copy()
        in_file = open(f'{i}.in', 'w', encoding='utf-8')
        local_vars['num'], local_vars['print'] = i, lambda *args, **kwargs: print(*args, **kwargs, file=in_file)  # 设置变量
        try:
            exec(maker_complied, local_vars)
        except (Exception, SystemExit) as err:
            os.chdir(cwd)  # 切换回原工作路径
            return renders('index.html', error=str(err))
        finally:
            in_file.close()
        os.system(f'std.exe < {i}.in > {i}.out')   # 使用 std 生成答案

    with zipfile.ZipFile('data.zip', 'w', zipfile.ZIP_DEFLATED) as zf:   # 打包 zip 文件
        for i in range(1, num + 1):
            zf.write(f'{i}.in')
            zf.write(f'{i}.out')
        if use_spj:
            zf.write('checker.cpp')
        if use_cfg:
            zf.write('config.yml')

    os.chdir(cwd)   # 切换回原工作路径
    return send_file(os.path.join(data_path, 'data.zip'), as_attachment=True)   # 返回答案 zip 文件


@app.route('/help/')
def show_help():
    return renders('help.html')
