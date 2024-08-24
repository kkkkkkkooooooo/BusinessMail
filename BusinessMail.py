import streamlit as st
import requests

def call_dify_api(q1, q2, q3, q4, q5):
    url = "https://api.dify.ai/v1/workflows/run"
    headers = {
        "Authorization": f"Bearer {"app-OhEQ1sJoljDHLEv2SJPajKLz"}",
        "Content-Type": "application/json"
    }
    data = {
        "inputs": {"q1": q1, 
                   "q2": q2, 
                   "q3": q3, 
                   "q4": q4, 
                   "level": q5},
        "response_mode": "blocking",
        "user": "test"
    }
    response = requests.post(url, json=data, headers=headers)
    return response.json()

def main():
    st.title("ビジネスメール作成")
    st.write("ビジネスメールの作成をAIがサポートいたします。返信したい元のメールを提供いただければ、適切な返信メールを作成することも可能です。")  
    st.subheader("以下の欄を記入してください")
        
    
    recipient_info = st.text_area("・『送信先(相手)の情報(企業名、役職名、人名など)』  #返信の場合、情報が元のメールに記載してあれば省略可")
    email_content = st.text_area("・『メールの内容の説明』(必須)   #書きたい内容を自由に説明してください。形式は問いません。")
    sender_info = st.text_area("・『送信主(自分)の情報(企業名、人名、メールアドレスなど)』 (必須)")
    email_type = st.radio(
        "・メールのタイプを選択してください",
        ("・新規メール作成", "・返信メール作成")
    )
    if email_type in ["・返信メール作成"]:
        original_email = st.text_area("・『元のメール』 #やり取りが複数ある際、全て入力OK")
    else:
        original_email = ""
    email_level = st.radio(
            "・メールのレベルを選択してください：",
            ("・フォーマル (上司、クライアント、初対面など)", "・セミフォーマル (同僚、よく知っているビジネスパートナーなど)", "・カジュアル (親しい同僚など)")
        )
    submit_btn = st.button("メール作成")

    if submit_btn:
        hold = st.empty()
        hold.write("少々お待ちください・・・")
        result = call_dify_api(recipient_info, email_content, original_email, sender_info, email_level)
        hold.empty()
        text = result["data"]["outputs"]["text"]
        st.write(text)

if __name__ == "__main__":
    main()
