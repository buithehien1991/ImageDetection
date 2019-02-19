import os
import requests
import shutil

ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}


def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def download_image_from_url(UPLOAD_FOLDER, image_url):
    filename = image_url.split('/')[-1]

    r = requests.get(image_url, stream=True, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'})
    with open(UPLOAD_FOLDER + '/' + filename, 'wb') as f:
        f.write(r.content)

    return filename


def save_upload_file(UPLOAD_FOLDER, file):
    filename = file.filename
    if file and allowed_file(filename):
        file.save(os.path.join(UPLOAD_FOLDER, filename))
        return filename
    else:
        return ''


if __name__ == "__main__":
    download_image_from_url("C:/Users/hienbt/PycharmProjects/ImageDetection/uploads", "https://hatgiongphuongnam.com/asset/upload/image/hat-giong-hoa-hong-1.jpg")
