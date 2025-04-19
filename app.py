import streamlit as st
from PIL import Image

# ----- 卡片資料 ----- #
pokemon_1 = {
    'name': '尼多王',
    'image': 'nidoking.png',
    'hp': 143,
    'attack': 109,
    'defense': 83,
    'speed': 91,
    'type': '毒',
    'move': '緩步擊破'
}

pokemon_2 = {
    'name': '大比鳥',
    'image': 'pidgeot.png',
    'hp': 145,
    'attack': 76,
    'defense': 81,
    'speed': 108,
    'type': '飛行',
    'move': '空氣斬'
}

# ----- 屬性相剋倍率 ----- #
def get_type_multiplier(attacker_type, defender_type):
    if attacker_type == '飛行' and defender_type == '毒':
        return 1.0
    if attacker_type == '毒' and defender_type == '飛行':
        return 1.0
    return 1.0  # 其他情況一律 1 倍

# ----- 傷害計算 ----- #
def calculate_damage(attacker, defender):
    multiplier = get_type_multiplier(attacker['type'], defender['type'])
    damage = int(attacker['attack'] * multiplier - defender['defense'])
    return max(damage, 0)

# ----- Streamlit UI ----- #
st.title("寶可夢卡牌對戰模擬")

col1, col2 = st.columns(2)

with col1:
    st.image(pokemon_1['image'], width=250)
    st.subheader(pokemon_1['name'])
    st.text(f"HP: {pokemon_1['hp']}")
    st.text(f"攻擊: {pokemon_1['attack']}")
    st.text(f"防禦: {pokemon_1['defense']}")
    st.text(f"速度: {pokemon_1['speed']}")
    st.text(f"屬性: {pokemon_1['type']}")
    st.text(f"招式: {pokemon_1['move']}")

with col2:
    st.image(pokemon_2['image'], width=250)
    st.subheader(pokemon_2['name'])
    st.text(f"HP: {pokemon_2['hp']}")
    st.text(f"攻擊: {pokemon_2['attack']}")
    st.text(f"防禦: {pokemon_2['defense']}")
    st.text(f"速度: {pokemon_2['speed']}")
    st.text(f"屬性: {pokemon_2['type']}")
    st.text(f"招式: {pokemon_2['move']}")

if st.button("開始對戰"):
    st.subheader("對戰開始！")

    if pokemon_1['speed'] >= pokemon_2['speed']:
        first, second = pokemon_1.copy(), pokemon_2.copy()
    else:
        first, second = pokemon_2.copy(), pokemon_1.copy()

    damage = calculate_damage(first, second)
    second['hp'] -= damage
    st.write(f"{first['name']} 使用 {first['move']}！造成 {damage} 傷害！")

    if second['hp'] <= 0:
        st.success(f"{second['name']} 倒下了！{first['name']} 獲勝！")
    else:
        damage = calculate_damage(second, first)
        first['hp'] -= damage
        st.write(f"{second['name']} 反擊，使用 {second['move']}！造成 {damage} 傷害！")

        if first['hp'] <= 0:
            st.success(f"{first['name']} 倒下了！{second['name']} 獲勝！")
        elif first['hp'] > second['hp']:
            st.success(f"戰鬥結束！{first['name']} 保留更多 HP，獲勝！")
        else:
            st.success(f"戰鬥結束！{second['name']} 保留更多 HP，獲勝！")
