import cv2
import cvlib
from cvlib.object_detection import draw_bbox

# ? الفيديو الأصلى
video = cv2.VideoCapture('./videos/highway-civil.mp4')
fps = video.get(cv2.CAP_PROP_FPS)
frame_width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))


# ? الفيديو الناتج
fourcc = cv2.VideoWriter_fourcc(*'MP4V')
output_video = cv2.VideoWriter(
    'output.mp4', fourcc, fps, (frame_width, frame_height))


# ? البدء فى إنتاج الفيديو
print('Writting...')

while True:
    ret, frame = video.read()
    if not ret:
        break

    #! لا تحول الصورة الى ابيض و أسود
    # grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #! yolov3 استخدم نموذج اصغر بدلا من ولكن الدقة ستصبح اقل بكثير
    #! yolov3 : دقائق 10
    #! yolov3-tiny : دقيقة

    bounding_box, label, conf = cvlib.detect_common_objects(
        frame, model='yolov3-tiny')  # , enable_gpu=True)

    # ? انظر السطر رقم 3
    frame = draw_bbox(frame, bounding_box, label, conf, write_conf=True)

    # ? المدة المستغرقة كبيرة جدا لأنى لا امتلك كارت شاشة
    # ? بوجود كارت شاشة ستتضاعف قوةالمعالجة بمقدار من 5 الى 10 أضعاف
    output_video.write(frame)

print('Done.')
