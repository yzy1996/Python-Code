
import easyocr

reader = easyocr.Reader(['ch_sim', 'en'], gpu=False) # this needs to run only once to load the model into memory
result = reader.readtext('test.jpg', detail = 0)

# 去掉空格
print(result)