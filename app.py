from flask import Flask, request, jsonify, render_template
import common.utils as utils
import common.tf_classify as image_classifier
import tensorflow as tf

LABELS_FILE = './tf_files/flowers_labels.txt'
MODEL_FILE = './tf_files/flowers_retrained_graph.pb'
UPLOAD_FOLDER = 'C:/Users/hienbt/PycharmProjects/ImageDetection/uploads'

app = Flask(__name__)


# Loads label file, strips off carriage return
label_lines = [line.rstrip() for line in tf.gfile.GFile(LABELS_FILE)]

# Unpersists graph from file
with tf.gfile.FastGFile(MODEL_FILE, 'rb') as f:
    graph_def = tf.GraphDef()
    graph_def.ParseFromString(f.read())
    _ = tf.import_graph_def(graph_def, name='')

sess = tf.Session()


@app.route('/', methods=['POST', 'GET'])
def index():
    try:
        if request.method == 'POST' and request.form.get('image', '') != '':
            print(request.form)
            if 'image' not in request.files:
                return jsonify({
                    'message': "No file part"
                }), 400
            file = request.files['image']
            if file.filename == '':
                return jsonify({
                    'message': 'No selected file'
                }), 400
            filename = utils.save_upload_file(UPLOAD_FOLDER, file)
        elif request.method == 'POST' and request.form.get('image_url', '') != '':
            image_url = request.form.get('image_url', '')
            filename = utils.download_image_from_url(UPLOAD_FOLDER, image_url)
        else:
            return render_template('index.html')
        if filename != '':
            output = image_classifier.label_image(image_path=UPLOAD_FOLDER+"/"+filename, label_lines=label_lines, sess=sess)
            return render_template('index.html', labels=output)
        else:
            return render_template('index.html', error="'Something when wrong'")
    except Exception as e:
        print(e)
        return repr(e), 500


if __name__ == '__main__':
    app.run(debug=True)
