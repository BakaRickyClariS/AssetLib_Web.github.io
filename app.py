from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__, template_folder=os.path.dirname(__file__))

# 靜態文件夾路徑
MODEL_DIRECTORY = 'static/models'

@app.route('/')
def index():
    # 獲取所有模型文件列表
    model_files = []
    for root, dirs, files in os.walk(MODEL_DIRECTORY):
        for file in files:
            if file.endswith(('.glb', '.gltf', '.obj', '.babylon')):
                rel_dir = os.path.relpath(root, MODEL_DIRECTORY)  # 使用 '/' 作為路徑分隔符
                model_files.append(os.path.join(rel_dir, file).replace("\\", "/"))
    return render_template('index.html', model_files=model_files)

@app.route('/models/<path:filename>')
def download_file(filename):
    # 使用 '/' 作為路徑分隔符
    filename = filename.replace("/", os.path.sep)
    return send_from_directory(MODEL_DIRECTORY, filename)


if __name__ == '__main__':
    app.run(debug=True, port=7000)
