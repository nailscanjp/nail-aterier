
import streamlit as st
from PIL import Image, ImageDraw
import io
from streamlit_image_coordinates import streamlit_image_coordinates

st.markdown("""
<style>

/* 保存ボタン */
.stButton > button {
    background-color: #D9A6AC;
    color: white;
    border: none;
    border-radius: 24px;
    padding: 10px 24px;
    font-weight: 600;
    transition: all 0.2s ease;
}

/* マウスを乗せたとき */
.stButton > button:hover {
    background-color: #B97884;
    color: white;
    border: none;
    transform: translateY(-2px);
}

/* スマホ向けレイアウト */
@media (max-width: 600px) {
    .stApp .block-container {
        padding-left: 16px;
        padding-right: 16px;
        padding-top: 20px;
    }

    h1 {
        font-size: 26px !important;
        line-height: 1.4 !important;
    }

    h2 {
        font-size: 22px !important;
    }

    h3 {
        font-size: 19px !important;
    }

    .stButton > button {
        width: 100%;
        min-height: 48px;
        font-size: 16px;
    }
}

</style>
""", unsafe_allow_html=True)

st.markdown("""
<style>
/* アプリ全体の背景 */
.stApp {
    background-color: #FFFAF7;
    color: #514641;
}

/* メイン画面の余白 */
.block-container {
    max-width: 850px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}

/* 見出し */
h1, h2, h3 {
    color: #795C60 !important;
    letter-spacing: 0.03em;
}

/* ボタン */
.stButton > button {
    background-color: #D9A6AC;
    color: white;
    border: none;
    border-radius: 18px;
    padding: 0.55rem 1.2rem;
    font-weight: 600;
    transition: all 0.2s ease;
}

/* ボタンにカーソルを合わせたとき */
.stButton > button:hover {
    background-color: #BD858D;
    color: white;
    border: none;
}

/* 数値カード */
[data-testid="stMetric"] {
    background-color: #FFFFFF;
    border: 1px solid #F0DFDF;
    border-radius: 18px;
    padding: 20px;
    box-shadow: 0 3px 12px rgba(121, 92, 96, 0.06);
}

/* 数値 */
[data-testid="stMetricValue"] {
    color: #B97884;
    font-weight: 700;
}

/* 区切り線 */
hr {
    border-color: #F0DFDF;
}
</style>
""", unsafe_allow_html=True)

st.set_page_config(
    page_title="わたしのネイル計測",
    page_icon="💅",
    layout="centered"
)


st.markdown("""
<div style="text-align:center; padding: 10px 0 24px;">
    <div style="font-size: 14px; letter-spacing: 5px; color: #B97884;">
        N A I L   A T E L I E R
    </div>
    <h1 style="font-size: 34px; margin-bottom: 6px;">
        Nail Size Studio ♡
    </h1>
    <p style="color: #9D8585; font-size: 14px;">
        あなたの爪に、ぴったりのサイズを。
    </p>
</div>
""", unsafe_allow_html=True)

st.write("自分にぴったりのネイルチップを見つけよう！")

st.divider()

st.subheader("📏 爪のサイズを測ってみよう")

st.write(
    "まずは爪の横幅を入力してみよう。"
    "これからカメラを使った計測機能も作っていくよ！"
)

finger = st.selectbox(
    "測りたい指を選んでね",
    ["親指", "人差し指", "中指", "薬指", "小指"]
)

width = st.number_input(
    "爪の横幅（mm）",
    min_value=0.0,
    max_value=40.0,
    value=10.0,
    step=0.5
)

if st.button("サイズを確認する"):
    st.success(f"{finger}の爪の横幅は {width} mm だよ！")

st.divider()

st.subheader("📷 カメラで爪を撮影しよう")

st.write(
    "測りたい爪と100円玉を一緒にカメラに映して撮影してね。"
    "100円玉は爪のすぐ横に、同じ平面になるように置いてね！"
)

st.markdown("""
<div style="
    background-color: #FFFFFF;
    border: 1px solid #F0DFDF;
    border-radius: 18px;
    padding: 20px;
    margin: 12px 0;
">
    <p style="color: #B97884; font-size: 12px; letter-spacing: 2px;">
        STEP 01
    </p>
    <h3 style="margin: 0; color: #795C60;">
        📷 爪を撮影しよう
    </h3>
    <p style="color: #9D8585; font-size: 14px;">
        爪と100円玉を一緒に写してね。
        100円玉は爪のすぐ横に、同じ平面で置くのがポイント。
    </p>
</div>
""", unsafe_allow_html=True)

photo = st.camera_input("爪を撮影する")

if photo is not None:
    st.image(
        photo,
        caption="撮影した爪",
        use_container_width=True
    )


if photo is not None:
    st.subheader("📏 爪の横幅ガイド")

    guide_width = st.slider(
        "ガイドの幅を調整してね",
        min_value=20,
        max_value=300,
        value=100,
        step=5
    )

    st.write(f"ガイド幅：{guide_width}")

    
    image = Image.open(io.BytesIO(photo.getvalue())).convert("RGB")

    draw = ImageDraw.Draw(image)

    image_width, image_height = image.size

    st.write(f"写真のサイズ：横 {image_width} px × 縦 {image_height} px")

    guide_x = st.slider(
        "ガイドの位置を左右に調整してね",
        min_value=0,
        max_value=image_width - 1,
        value=image_width // 2,
        step=1
    )


    guide_y = st.slider(
        "ガイドの位置を上下に調整してね",
        min_value=0,
        max_value=image_height - 1,
        value=image_height // 2,
        step=1
    )




    
    nail_guide_width = st.slider(
        "爪用ガイドの幅を調整してね",
        min_value=10,
        max_value=300,
        value=100,
        step=1,
        key="nail_guide_width"
    )

    nail_guide_y = st.slider(
        "爪用ガイドの位置を上下に調整してね",
        min_value=0,
        max_value=image_height - 1,
        value=image_height // 2 + 50,
        step=1,
        key="nail_guide_y"
    )

    nail_guide_x = st.slider(
        "爪用ガイドの位置を左右に調整してね",
        min_value=0,
        max_value=image_width - 1,
        value=image_width // 2,
        step=1,
        key="nail_guide_x"
    )

    green_left = max(0, guide_x - guide_width // 2)
    green_right = min(image_width - 1, guide_x + guide_width // 2)

    draw.line(
        (green_left, guide_y, green_right, guide_y),
        fill="lime",
        width=5
    )

    red_left = max(0, nail_guide_x - nail_guide_width // 2)
    red_right = min(image_width - 1, nail_guide_x + nail_guide_width // 2)

    draw.line(
        (red_left, nail_guide_y, red_right, nail_guide_y),
        fill="red",
        width=5
    )

    st.image(image, caption="緑：100円玉用 / 赤：爪用", use_container_width=True)
    st.write("📍 写真をクリックしてみてね")

    clicked_point = streamlit_image_coordinates(image)

    if clicked_point is not None:
        st.write(f"クリックした位置：X={clicked_point['x']}, Y={clicked_point['y']}")
       
    st.subheader("💅 爪の幅を測ってみよう")

   
    if st.button("🔄 測定をやり直す"):
        for key in [
            "left_point",
            "right_point",
            "coin_left",
            "coin_right",
            "left_click",
            "right_click",
            "coin_left_click",
            "coin_right_click",
        ]:
            if key in st.session_state:
                del st.session_state[key]

        st.session_state["measurement_reset"] = True
        st.rerun()



    if "left_point" not in st.session_state:
        st.session_state.left_point = None
    if "right_point" not in st.session_state:
        st.session_state.right_point = None
    if "coin_left" not in st.session_state:
        st.session_state.coin_left = None
    if "coin_right" not in st.session_state:
        st.session_state.coin_right = None

    st.markdown("""
    <div style="
        background-color: #FFFFFF;
        border: 1px solid #F0DFDF;
        border-radius: 18px;
        padding: 18px;
        margin: 20px 0 12px;
    ">
        <p style="color: #B97884; font-size: 12px; letter-spacing: 2px;">
            STEP 02
        </p>
        <h3 style="margin: 0; color: #795C60;">
            📏 測定する場所を選ぼう
        </h3>
        <p style="color: #9D8585; font-size: 14px;">
            爪の左右の端と、100円玉の左右の端を順番にクリックしてね。
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.write("① 爪の左端をクリックしてね")
    left_click = streamlit_image_coordinates(image, key="left_click")
    if left_click is not None:
        st.session_state.left_point = left_click

    st.write("② 爪の右端をクリックしてね")
    right_click = streamlit_image_coordinates(image, key="right_click")
    if right_click is not None:
        st.session_state.right_point = right_click

    st.write("③ 100円玉の左端をクリックしてね")
    coin_left_click = streamlit_image_coordinates(image, key="coin_left_click")
    if coin_left_click is not None:
        st.session_state.coin_left = coin_left_click

    st.write("確認：④の表示処理まで来たよ")
    st.write("④ 100円玉の右端をクリックしてね")
    coin_right_click = streamlit_image_coordinates(image, key="coin_right_click")
    if coin_right_click is not None:
        st.session_state.coin_right = coin_right_click

    left_point = st.session_state.left_point
    right_point = st.session_state.right_point
    coin_left_point = st.session_state.coin_left
    coin_right_point = st.session_state.coin_right

    marker_draw = ImageDraw.Draw(image)

    # 爪の左右を赤い線でつなぐ
    if left_point is not None and right_point is not None:
        marker_draw.line(
            (
                int(left_point["x"]),
                int(left_point["y"]),
                int(right_point["x"]),
                int(right_point["y"]),
            ),
            fill="red",
            width=4,
        )

    # 100円玉の左右を緑の線でつなぐ
    if coin_left_point is not None and coin_right_point is not None:
        marker_draw.line(
            (
                int(coin_left_point["x"]),
                int(coin_left_point["y"]),
                int(coin_right_point["x"]),
                int(coin_right_point["y"]),
            ),
            fill="lime",
            width=4,
        )

    points_to_draw = [
        (left_point, "red"),
        (right_point, "red"),
        (coin_left_point, "lime"),
        (coin_right_point, "lime"),
    ]

    for point, color in points_to_draw:
        if point is not None:
            x = int(point["x"])
            y = int(point["y"])
            marker_draw.ellipse(
                (x - 6, y - 6, x + 6, y + 6),
                fill=color,
                outline="white",
                width=2
            )

    st.image(
        image,
        caption="🔴 赤：爪の端 / 🟢 緑：100円玉の端",
        use_container_width=True
    )

    if left_point is not None and right_point is not None:
        nail_pixels = abs(right_point["x"] - left_point["x"])
        st.write(f"爪の幅：約 {nail_pixels} px")

    if coin_left_point is not None and coin_right_point is not None:
        coin_pixels = abs(coin_right_point["x"] - coin_left_point["x"])
        st.write(f"100円玉の直径：約 {coin_pixels} px")

        if coin_pixels > 0 and left_point is not None and right_point is not None:
            nail_mm = 22.6 * nail_pixels / coin_pixels

            
            st.markdown("""
            <div style="
                background-color: #FFFFFF;
                border: 1px solid #F0DFDF;
                border-radius: 18px;
                padding: 18px;
                margin: 20px 0 10px;
            ">
                <p style="color: #B97884; font-size: 12px; letter-spacing: 2px;">
                    YOUR RESULT
                </p>
                <h3 style="margin: 0; color: #795C60;">
                    ✨ 測定結果
                </h3>
            </div>
            """, unsafe_allow_html=True)

            st.metric(
                label="💅 爪の横幅（目安）",
                value=f"{nail_mm:.1f} mm",
                help="100円玉の直径22.6mmを基準に計算しています"
            )

            
            if "measurement_history" not in st.session_state:
                st.session_state.measurement_history = []

            if st.button("💾 この測定結果を保存"):
                st.session_state.measurement_history.append(
                    round(nail_mm, 1)
                )
                st.success("測定結果を保存したよ！")
                
            st.subheader("📋 測定履歴")

            
            if st.session_state.measurement_history:
                for i, result in enumerate(
                    st.session_state.measurement_history, start=1
                ):
                    st.markdown(f"""
                    <div style="
                        background-color: #FFFFFF;
                        border: 1px solid #F0DFDF;
                        border-radius: 16px;
                        padding: 14px 18px;
                        margin: 8px 0;
                        display: flex;
                        justify-content: space-between;
                        align-items: center;
                    ">
                        <span style="
                            color: #9D8585;
                            font-size: 14px;
                        ">
                            ♡ MEASUREMENT {i:02d}
                        </span>
                        <span style="
                            color: #795C60;
                            font-size: 22px;
                            font-weight: 600;
                        ">
                            {result:.1f} mm
                        </span>
                    </div>
                    """, unsafe_allow_html=True)

