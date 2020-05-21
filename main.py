from flask import Flask, render_template, Response, send_file
import cv2

#from display_depth_frame import rgb_frame


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

def gen():
    filename = r'C:\Users\User\Desktop\New folder\Savedimg.jpg'
    image = cv2.VideoCapture(filename)

    while(image.isOpened()):
        ret,img = image.read()
        if ret == True:
        #    img = cv2.resize(img, (0,0), fx=0.5, fy=0.5)
        #filename = r'C:\Users\User\Desktop\New folder\Savedimg.jpg'
            img = cv2.imread("Savedimg.jpg")
            img = cv2.resize(img, (0,0), fx=0.5, fy=0.5) 
            frame = cv2.imencode('.jpg', img)[1].tobytes()
            yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
        else:
            break
    

@app.route('/video_feed')
def video_feed():
    return Response(gen(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')
   
   # filename = r'C:\Users\User\Desktop\New folder\Savedimg.jpg'
    #return send_file(filename, mimetype='image/jpg')
    #Response(gen(rgb_frame()),
    #                mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=True)

