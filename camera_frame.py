from PyQt6.QtWidgets import QGridLayout, QFrame, QVBoxLayout, QSlider
from PyQt6.QtCore import Qt
from font import FontLabel
import vlc

"""

Toestandsvariabelen​                Commando’s​

#identificatie_code​                SetPan(p)​
#pan_stand​                         SetTilt(t)​
#tilt_stand​                        SetZoom(z)​
#zoom_stand​                        SetIdentificatiecode(ic)​
#focus_stand​                       SelectCameraActueelBeeld(k)​
#diafragma_stand​                   UnselectCameraActueelBeeld(k)​
"""

#TODO 
#Data halen van simulatie
#Data sturen naar de simulatie 

#Echte video beelden tonen
#http://77.173.76.238:8090/Camera_01.webm
#http://77.173.76.238:8090/Camera_02.webm
#http://77.173.76.238:8090/Camera_03.webm

class Slider(QSlider):
    def __init__(self, min, max, tick):
        super(Slider, self).__init__()
        self.setOrientation(Qt.Orientation.Horizontal)
        self.setMinimum(min)
        self.setMaximum(max)
        self.setTickInterval(tick)
        self.setTickPosition(QSlider.TickPosition.TicksBelow)

class CameraPanel(QFrame):
    def __init__(self, camera_number):
        super().__init__()
        self.setStyleSheet("QFrame {color : #b2b2b2; background-color: #30393c;border : 1px solid black;}")
        self.setContentsMargins(20,10,20,10)
        self.layout = QVBoxLayout()
        self.layout.setSpacing(10)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.layout)

        self.camera_label = FontLabel(camera_number, 20, True)
        self.camera_label.setStyleSheet("QLabel {color : #b2b2b2; background-color: #30393c; border : none}")
        self.camera_label.setMaximumHeight(30)
        self.options_frame = QFrame()
        self.options_frame.setContentsMargins(0,0,0,0)
        self.options_layout = QGridLayout()
        self.options_layout.setSpacing(0)
        self.options_layout.setContentsMargins(0,0,0,0)
        self.options_frame.setLayout(self.options_layout)
        self.options_frame.setStyleSheet("QFrame {color : #b2b2b2; background-color: #30393c; border : none}")
        
        self.option_slider_pan = Slider(0, 360, 10)
        self.option_label_pan = FontLabel(f'Pan { self.option_slider_pan.value() }', 12, False)
        self.option_slider_pan.valueChanged.connect(self.updateLabel)
        
        self.option_slider_tilt = Slider(-90, 90, 10)
        self.option_label_tilt = FontLabel(f'Tilt { self.option_slider_tilt.value() }', 12, False)
        self.option_slider_tilt.valueChanged.connect(self.updateLabel)
        
        self.option_slider_zoom = Slider(10, 45 , 1)
        self.option_label_zoom = FontLabel(f'Zoom { self.option_slider_zoom.value() }', 12, False)
        self.option_slider_zoom.valueChanged.connect(self.updateLabel)
        
        self.option_slider_preset = Slider(0, 8, 1)
        self.option_label_preset = FontLabel(f'Preset { self.option_slider_preset.value() }', 12, False)
        self.option_slider_preset.valueChanged.connect(self.updateLabel)

        self.options_layout.addWidget(self.option_label_pan,0,0)
        self.options_layout.addWidget(self.option_slider_pan,0,1)
        self.options_layout.addWidget(self.option_label_tilt,1,0)
        self.options_layout.addWidget(self.option_slider_tilt,1,1)
        self.options_layout.addWidget(self.option_label_zoom,2,0)
        self.options_layout.addWidget(self.option_slider_zoom,2,1)
        self.options_layout.addWidget(self.option_label_preset,3,0)
        self.options_layout.addWidget(self.option_slider_preset,3,1)

        self.layout.addWidget(self.camera_label)
        self.layout.addWidget(self.options_frame)

    def updateLabel(self):
        self.option_label_pan.setText(f'Pan { self.option_slider_pan.value() }')
        self.option_label_tilt.setText(f'Tilt { self.option_slider_tilt.value() }')
        self.option_label_zoom.setText(f'Zoom { self.option_slider_zoom.value() }')
        self.option_label_preset.setText(f'Preset { self.option_slider_preset.value() }')
    
class ControlPanel(QFrame):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("QFrame {color : #b2b2b2; background-color: #000000;border-radius: 5px;}")
        self.setContentsMargins(0, 0, 0, 0)
        self.layout = QGridLayout()
        self.layout.setSpacing(10)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.layout)
        self.addFrames()

    def addFrames(self):
        self.panel_camera1 = CameraPanel("Camera 1")
        self.panel_camera1.setFixedSize(400,400)
        #self.panel_camera2 = CameraPanel("Camera 2")	
        #self.panel_camera3 = CameraPanel("Camera 3")

        self.layout.addWidget(self.panel_camera1,0,0)
        #self.layout.addWidget(self.panel_camera2,0,1)
        #self.layout.addWidget(self.panel_camera3,1,0)


class VideoFrame(QFrame):
    def __init__(self, camera, url):
        super().__init__()
        self.setStyleSheet("QFrame {color : #b2b2b2; background-color: #2c2c2c;}")
        self.setContentsMargins(0, 0, 0, 0)
        self.layout = QVBoxLayout()
        self.layout.setSpacing(0)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.layout)
        self.camera_label = FontLabel(camera, 20, True)
        self.camera_label.setMaximumHeight(50)
        self.camera = VideoPlayer(url)
        self.layout.addWidget(self.camera_label)
        self.layout.addWidget(self.camera)

class VideoPlayer(QFrame):
    def __init__(self, url):
        super(VideoPlayer, self).__init__()
        # Create a basic vlc instance
        self.setStyleSheet("QFrame {color : #b2b2b2; background-color: #000000;border-radius: 5px;}")
        self.instance = vlc.Instance('--verbose 2'.split())
        self.mediaplayer = self.instance.media_player_new()
        self.mediaplayer.set_mrl(url)
        self.mediaplayer.set_hwnd(int(self.winId()))
        self.mediaplayer.play()
        self.mediaplayer.audio_set_volume(0)
        

class CameraFrame(QFrame):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("QFrame {color : #b2b2b2; background-color: #000000;}")
        self.setContentsMargins(10,10,10,10)
        self.layout = QGridLayout()
        self.layout.setSpacing(10)
        self.layout.setContentsMargins(0,0,0,0)
        self.setLayout(self.layout)
        self.addFrames()

    def addFrames(self):
        self.camera1 = VideoFrame("Camera 1", "https://dl6.webmfiles.org/elephants-dream.webm")
        #self.camera2 = VideoFrame("Camera 2", "https://dl6.webmfiles.org/big-buck-bunny_trailer.webm")
        #self.camera3 = VideoFrame("Camera 3", "https://dl6.webmfiles.org/elephants-dream.webm")
        self.controlpanel = ControlPanel()

        self.layout.setColumnStretch(0,1)
        #self.layout.setColumnStretch(1,1)
        #self.layout.setRowStretch(0,1)
        #self.layout.setRowStretch(1,1)

        self.layout.addWidget(self.camera1,0,0)
        #self.layout.addWidget(self.camera2,0,1)
        #self.layout.addWidget(self.camera3,1,0)
        self.layout.addWidget(self.controlpanel,0,1)