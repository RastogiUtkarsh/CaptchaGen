#pip install captcha ; Required Pre-requisite
from captcha.image import ImageCaptcha 

image=ImageCaptcha(width=250,height=100)
text='coderbuzz'
data=image.generate(text)
image.write(text,'captcha.png')
