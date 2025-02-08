
import os
from PIL import Image, ImageTk
import requests
from io import BytesIO
from dotenv import load_dotenv

# 정보 불러오기

def get_path_env():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    env_path = os.path.join( BASE_DIR, ".env.development.txt")
    return env_path

def get_character_ocid(character_name):
    load_dotenv(get_path_env())
    url = "https://open.api.nexon.com/maplestory/v1/id"
    headers = {
        "x-nxopen-api-key" : os.getenv("NEXON_API_KEY")
    }
    params = {
        "character_name" : character_name
    }

    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def get_character_info(character_name, ocid):
    load_dotenv(get_path_env())
    url = "https://open.api.nexon.com/maplestory/v1/character/basic"
    headers = {
        "x-nxopen-api-key" : os.getenv("NEXON_API_KEY")
    }
    params = {
        "character_name" : character_name,
        "ocid" : ocid,
        "date" : "2024-02-06"
    }

    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return None
    
def load_default_image():
    base_path = os.path.dirname(os.path.abspath(__file__)) # 현재 파일
    image_path = os.path.join(base_path, "mushroom.png") # os에 맞게 경로 설정
    image = Image.open(image_path)
    image = image.resize((150, 150))
    photo = ImageTk.PhotoImage(image)
    return photo

def show_character_image(url, character_image):
    image = load_image(url)
    if image:
        character_image.config(image=image)
        character_image.image = image

# 정보 처리

def load_image(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        image_data = BytesIO(response.content)
        image = Image.open(image_data)
        image = image.resize((200, 200))
        return ImageTk.PhotoImage(image)
    except Exception as e:
        print("이미지를 불러오는 중 오류 발생:", e)
        return None

def search_character_ocid(character_name):
    character_data = get_character_ocid(character_name)

    if character_data and "ocid" in character_data:
        return character_data["ocid"]
    else:
        return "존재하지 않는 이름입니다."

def search_character(character_name, ocid):
    character_info = get_character_info(character_name, ocid)

    if character_info:
        return character_info
    else:
        return "정보를 찾을 수 없습니다."
    
# 이밴트 처리
    
def show_result(character_image, label_name, label_world, label_gender, label_class, label_level, state_label ,character_info):
    image = load_default_image()
    if isinstance(character_info, str):
        character_image.config(image = image)
        character_image.image = image
        label_name.config(text="None")
        label_world.config(text="None")
        label_gender.config(text="None")
        label_class.config(text="None")
        label_level.config(text="None")
        state_label.config(text="None")
        return 
    
    character_image_url = character_info.get("character_image", None)
    if character_image_url:
        show_character_image(character_image_url, character_image)
    else :
        character_image.config(image = image)
        character_image.image = image
        label_name.config(text="None")
        label_world.config(text="None")
        label_gender.config(text="None")
        label_class.config(text="None")
        label_level.config(text="None")
        label_level.config(text="이미지 URL이 없습니다.")

    label_name.config(text=character_info.get("character_name",""))
    label_world.config(text=character_info.get("world_name",""))
    label_gender.config(text=character_info.get("character_gender",""))
    label_class.config(text=character_info.get("character_class",""))
    label_level.config(text=character_info.get("character_level",""))
    state_label.config(text="")


def on_search_button_click(entry_name, character_image, label_name, label_world, label_gender, label_class, label_level, state_label):
    character_name = entry_name.get()
    ocid = search_character_ocid(character_name)
    result = search_character(character_name, ocid)

    if result is None:
        label_name.config(text="정보를 찾을 수 없습니다.")
        return

    show_result(character_image, label_name, label_world, label_gender, label_class, label_level, state_label, result)