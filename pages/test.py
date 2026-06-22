import streamlit as st
import requests
import json

from datetime import date
from dateutil.relativedelta import relativedelta

#関数の定義部分

#サーバーファイルの読み込み 
def get_user_id(family_name, first_name):
    with open('./assets/known_people.json',"r",
encoding="utf-8") as f:
        people = json.loads(f.read())
    matched = filter(
        lambda d:d["first_name"] == first_name and d["family_name"] == family_name,
        people
    )
    matched = list(matched)
    if len(matched) > 0:
        return matched [0]["id"]
    else:
        return None
        
        
        
        
@st.cache_data
def agify(first_name):
    url = "https://api.agify.io/"
    params = {"name": first_name}
    response = requests.get(url, params=params)
    result = json.loads(response.content)
    age = result["age"]
    return age


@st.cache_data
def genderize(first_name):
    url = "https://api.genderize.io/"
    params = {"name": first_name}
    respones = requests.get(url, params=params)
    result = json.loads(respones.content)
    gender = result["gender"]
    return gender

@st.cache_data
def natioanalize(first_name):
    url = "https://api.nationalize.io/" 
    params = {"name": first_name}
    respones = requests.get(url, params=params)
    result = json.loads(respones.content)
    country = result["country"][0]["country_id"]
    return country

st.markdown("プロファイル予測アプリ")

family_name = st.text_input("名字を入力してください")
first_name = st.text_input("名前を入力してください")

if st.button("終了する"):
    user_id = get_user_id(family_name, first_name)
    user_id_text = f"ユーザーID: {user_id}" if user_id else "ゲスト"
    
    full_name = family_name + first_name
    
    age = agify(first_name)
    gender = genderize(first_name)
    country = natioanalize(first_name)
    
    st.text ( f"{full_name}({user_id_text})さんの予測結果" )
    st.table({
        "年齢": age,
        "性別": gender,
        "国籍": country
    })