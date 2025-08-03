import time
import streamlit as st
import numpy as np
import pandas as pd

st.set_page_config(
    page_title = 'DnD 半神的試煉模組',
    page_icon = ':classical_building:',
    layout = 'centered'
)

st.markdown("""
    <style>
    header {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

st.markdown("""
    <style>
    /* 隱藏右上角 GitHub 連結與選單 */
    #MainMenu {visibility: hidden;}
    header {visibility: hidden;}
    
    /* 隱藏右下角 "Made with Streamlit" 與使用者頭像 */
    footer {visibility: hidden;}

    /* 隱藏 Streamlit 登入區域（頭像） */
    [data-testid="stToolbar"] {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

st.markdown(
    """
    <style>
    html, body, [class*="css"]  {
        font-family: "Noto Sans TC", "Microsoft JhengHei", "PingFang TC", "Heiti TC", sans-serif;
    }
    </style>
    """,
    unsafe_allow_html=True
)

#tabs_config = [
    #("模組簡介", None),  # 無密碼
    #("雅典城", ["烏伊伊阿伊 瑞斯", "伊菲婭‧凱拉斯", "卯咪米咪咪", "艾佛瑞‧梅莉安涅"]),  # 多組密碼
    #("獅子", "Lion"),
    #("九頭蛇", "九頭蛇"),
    #("牝鹿", "南方蒼林間"),
    #("野豬", "Erymanthian"),
    #("牛廄", "潔淨"),
    #("怪鳥", "災"),
    #("公牛", "Maze"),
    #("牝馬", "hearts"),
    #("亞馬遜", "希波呂忒"),
    #("牛群", "Geryon"),
    #("聖園", "Golden Apples"),
    #("冥界", "地獄三頭犬"),
    #("成就表", None),
#]

tabs_config = [
    ("模組簡介", None),  # 無密碼
    ("雅典城", None),  # 多組密碼
    ("涅墨亞獅子", None),
    ("九頭蛇海德拉", None),
    ("克列尼亞牝鹿", "2348"),
    ("厄律曼托斯山野豬", None),
    ("奧格阿斯牛廄", None),
    ("斯廷法利斯湖怪鳥", None),
    ("克里特公牛", None),
    ("狄俄墨得斯牝馬", None),
    ("亞馬遜王國", "9274"),
    ("格律翁牛群", "6893"),
    ("聖園", None),
    ("冥界", "4830"),
    ("成就表", None),
]


# 各 tab 的內容函數
def content_tab1():
    st.header("半神的試煉")
    st.image("DND 照片/封面照.jpeg", use_container_width=True)

    expander = st.expander("世界觀：")
    expander.write("這是一個英雄輩出的時代，亦是神祇意志交織的世紀。無數冒險者、戰士與航海家穿梭於地中海，試圖在神話與歷史的洪流中刻下自身的名號。然而，當凡人讚頌榮耀之時，神祇的恩寵亦可轉為詛咒。在這片受神掌管的土地上，凡人雖可選擇道路，卻無法逃離神話。每一個誓言、每一次冒險、每一場戰役，無不映照出神祇的意志。這是凡人試圖掌握命運，卻不知命運早已寫就的時代。")

    expander = st.expander("天后希拉（Hera）")
    expander.write("希拉是奧林匹斯的天后，象徵忠誠、婚姻與尊嚴。她庇佑那些忠誠的配偶、王室貴族與誓約之人，厭惡背叛與欺瞞。她的信徒通常是高貴而堅定的領袖、守護家庭的戰士，或是維護傳統與秩序的宗教人士。儘管她以威嚴著稱，但她的祝福能賦予忠誠者無與倫比的庇護，使他們在誓約與責任的重壓下仍能堅持到底。")

    expander.image("DND 照片/希拉護符.jpeg", caption="孔雀翎墜飾（Peacock Plume Pendant）", use_container_width=True)
    expander.write(
        "以白銀精雕成孔雀羽毛的形狀，"
        "中央嵌著一顆閃耀的藍綠寶石，如神聖之眼窺探世間忠貞與背叛。"
        "墜飾時而流轉柔和光輝，似在默默見證持有者的誓約與榮耀，"
        "庇佑其維繫盟約，守護不容褻瀆的忠誠。"
    )

    expander = st.expander("太陽之神阿波羅（Apollo）")
    expander.write("阿波羅是知識、藝術與醫術之神，象徵真理與和諧。他的信徒包括學者、醫者、音樂家與預言者，追求智慧、創造與生命的美好。他的光芒能照亮黑暗，指引迷失的靈魂，也能驅散疾病與絕望。他的信徒通常冷靜而理性，喜愛追求完美，並努力在混亂之中尋找秩序與平衡。")

    expander.image("DND 照片/阿波羅護符.jpeg", caption="黃金豎琴別針（Golden Lyre Brooch）", use_container_width=True)
    expander.write(
        "形似一架小巧的金色豎琴，琴弦雖無形，卻於指尖輕觸時泛起幽微共鳴，彷彿來自太陽神的旋律。別針中央浮雕著旭日初升，象徵著光明與啟迪，使佩戴者的言語更具韻律與影響力，能以詩歌與樂聲安撫動蕩的心靈。"
    )

    expander = st.expander("月亮女神阿提密斯（Artemis）")
    expander.write("阿蒂蜜絲是荒野的守護者，代表純粹、獨立與自然的力量。她的信徒多為遊俠、獵人與流浪者，他們擁抱自由，不受世俗束縛，並在黑暗中為弱者提供庇護。她崇尚直覺與純粹的戰技，而非陰謀詭計。她的祝福賜予信徒無聲的步伐、敏銳的直覺與夜視的恩惠，使他們能在黑夜中無聲地狩獵，成為大自然真正的守護者。")

    expander.image("DND 照片/阿提密斯護符.jpeg", caption="銀月弓墜（Silver Crescent Bow）", use_container_width=True)
    expander.write(
        "一枚細緻的銀弓墜飾，弓弦似隱似現，宛如夜空中一抹新月，弓身雕刻著飛奔的鹿影，流露著荒野與自由的氣息。當月光灑落，墜飾將閃爍微光，庇佑持有者身手輕盈如夜行獵者，使其在林間與山谷中行動如風，難以被察覺。"
    )

    expander = st.expander("神使荷米斯（Hermes）")
    expander.write("荷米斯是速度與機智的象徵，掌管貿易、旅行與詭計。他的信徒多為商人、信使、探險家與竊賊，他們行動迅捷，善於應對變化，總能在危機中找到機會。荷米斯崇尚自由與靈活，認為僵化的規則是用來被突破的。他的祝福讓信徒的腳步更輕盈，反應更敏捷，使他們能在瞬間做出最佳決策，無論是談判桌上，還是危險的密道中。")

    expander.image("DND 照片/荷米斯護符.jpeg", caption="飛翼足環（Winged Anklet）", use_container_width=True)
    expander.write(
        "是一只纖細的銀色足環，兩側雕刻著微小的翅膀圖案，當佩戴者行走時，足環仿若輕微振動，如風輕拂。持有者的步伐將變得迅捷靈巧，能迅速穿越人群與險境，甚至於最緊要關頭閃避災厄，如神使荷米斯般在天地間自由來去。"
    )

    expander = st.expander("供奉流程")
    expander.header("祭壇說明：")
    expander.write("在古希臘時代，各處皆會有奧林帕斯十二眾神的祭壇，讓各神的信奉子民可以獻上供品，有時你的神祇會回應你的請求祝福，提供你一些可能需要的物品。但有時，祂們事務繁忙，不一定會有空理你...。而唯一不變的是始終保持虔誠和跟隨你所信奉的神祇的作風過生活...")
    
    expander.write("祭壇出現的地方通常會與你所信奉的神祇所管轄的區域相關：")

    expander.write("1. 整個地中海地區皆有人信奉希拉")
    expander.write("2. 阿提密斯的祭壇由荒野獵人或長居野外之信徒建造")
    expander.write("3. 阿波羅是醫藥之神")
    expander.write("4. 荷米斯掌管旅行")

    expander.write("你身為該神祇的子民，每當你認為和神祇似乎感應到某種連結時可以嘗試對周圍環境發起調查，DM 會告訴你你是否成功找到祭壇")

    expander.header("供奉流程：")

    expander.write("1. 在祭壇前點火")
    expander.write("2. 你可以以 5 青銅幣或是 2 磅的食物進行供奉")
    expander.write("3. 將欲供奉之物投入火中")
    expander.write("4. 默念你的名字和所求之事")
    expander.write("5. 你會看到火焰燃燒變得旺盛，代表神祇已收到你的供品")
    expander.write("6. 如果火焰持續燃燒，不久後從中會有神祇給你的回應；若火焰熄滅，則供奉結束")

    expander.header("備註：")

    expander.write("若你非常虔誠的和你的神交流一陣子後，祂有可能會給你護符，擁有護符象徵著你被這位信奉的神祇永久地祝福，當祂無暇協助你時，這個護符的效果能夠在你需要時提供你幫助。")

    expander.header("祭壇樣貌：")

    expander.write("以下是你們所信奉神祇的祭壇長相：")

    expander.write(
        "希拉祭壇由潔白大理石建成，柱面刻有孔雀羽與蓮花紋飾。中央置放一頂黃金冠冕，象徵女神的主權與婚姻的權柄。"
    )
    expander.image("DND 照片/希拉祭壇.jpeg", caption="希拉祭壇", use_container_width=True)

    expander.write(
        "阿波羅祭壇以金色石英堆砌而成，四邊雕飾太陽放射線與月桂枝。中央豎立一具無弦琴，琴身光滑，反射上方光柱。牆面刻有詩文與箭矢圖騰，整體充滿秩序與光明的氛圍。"
    )
    expander.image("DND 照片/阿波羅祭壇.jpeg", caption="阿波羅祭壇", use_container_width=True)

    expander.write(
        "阿提密斯祭壇以蒼灰石搭建，邊緣飾有野鹿奔馳與彎弓圖樣。上方懸掛一圈乾燥銀葉編織的花冠。地面布有繁星與林葉樣式的淺刻紋，周遭氣溫偏冷，空氣中有乾淨土壤與林木的氣息。"
    )
    expander.image("DND 照片/阿提密斯祭壇.jpeg", caption="阿提密斯祭壇", use_container_width=True)

    expander.write(
        "荷米斯祭壇採用磨光青銅與銀飾混構，表面鑲有飛翼涼鞋、雙蛇杖的徽記。兩側懸掛銅鈴與收納袋。地面紋飾呈現流動與曲線形，整體結構不對稱但動感十足。"
    )
    expander.image("DND 照片/荷米斯祭壇.jpeg", caption="荷米斯祭壇", use_container_width=True)



def content_tab2():
    st.header("雅典城")
    st.image("DND 照片/雅典城.jpeg", use_container_width=True)
    
    expander = st.expander("執政官辦公室")
    expander.write("在城邦中央，巍峨的大理石建築聳立於人潮之上，其門前刻有雅典的法律條文，象徵著這座城邦的秩序與理性。執政官辦公室內，陽光透過高聳的石柱灑落，映照在牆上懸掛的橄欖枝飾與黃金雕刻的雷霆徽記。這裡是雅典的決策中樞，執政官梭倫正於此召見來訪者。")
    expander.image("DND 照片/執政官辦公室.jpeg", caption="執政官辦公室", use_container_width=True)
    expander.subheader("執政官梭倫")
    expander.write("梭倫身披白色長袍，衣緣鑲有金線，象徵著執政官的尊貴。他年約中年，雙眼銳利而深思熟慮，額上刻滿歲月留下的皺紋，顯示他經歷無數政治鬥爭與城邦變革。胸前垂掛著一枚雷雲徽印，表明他對宙斯的信仰，而一旁書架上則擺放著智慧女神雅典娜的青銅雕像，象徵他對理性與公平的追求。")
    expander.image("DND 照片/梭倫.jpeg", caption="執政官梭倫", use_container_width=True)

    expander = st.expander("帕拉斯雜貨店")
    expander.write("在雅典城喧囂的市集邊緣，有一條隱秘的小巷，巷尾矗立著一間外表樸實卻又隱含神秘氣息的雜貨店。店面正楣上斑駁的銘牌上刻著「帕拉斯雜貨店」六字，字跡雖隱約卻透著古韻，彷彿訴說著歷經千年的傳奇。推開那扇沉重的橡木門，冒險者們便會置身於一個仿若時光倒流的空間。室內陳設極具古典風範：木製貨架上排列著各式奇珍異寶，牆角懸掛的青銅燈飾柔和地映出斑駁光影，而最引人注目的，則是那牆上密密麻麻、各異風格的地圖——從古老海圖到秘境遺跡的卷軸，無不昭示著隱藏於整個地中海的未知奇蹟。")
    expander.image("DND 照片/帕拉斯雜貨店.jpeg", caption="帕拉斯雜貨店", use_container_width=True)
    expander.subheader("帕拉斯")
    expander.write("坐在櫃檯後的中年婦人身著樸實但裁剪得體的麻布長裙，額上隱隱可見的細紋，卻難掩那雙深邃、明澈且洞悉一切的眼眸。")
    expander.image("DND 照片/帕拉斯.jpeg", caption="帕拉斯", use_container_width=True)

    expander = st.expander("赫菲斯托斯鐵匠鋪")
    expander.write("這座鐵匠鋪位於中央廣場的一角，門口高掛著一塊鑄鐵招牌，上頭刻著燃燒的鐵鎚與鐵砧。鍛爐熊熊燃燒，熱浪從開放的門窗湧出，火光映照著鋼鐵與銅器的輪廓，迴盪著沉穩的敲擊聲。架上陳列著各式各樣的武器、工具與護具，從簡單的匕首到華麗的青銅胸甲，每一件作品都展現了工匠的精湛技藝。")
    expander.image("DND 照片/鐵匠鋪.jpeg", caption="赫菲斯托斯鐵匠鋪", use_container_width=True)
    expander.subheader("卡力克斯")
    expander.write("卡力克斯是一名身形魁梧的鐵匠，肌膚因長年鍛造而染上銅紅色，手臂強壯如鋼。他的左眼因鍛造意外失明，如今戴著一片青銅眼罩。他崇敬赫菲斯托斯，認為技藝與毅力才是鑄造真正強大武器的關鍵。卡力克斯沉默寡言，但對於尋求良兵利器的客人，他總會仔細端詳對方的雙手，然後給出建議——無論是戰士、工匠，或只是尋找一把可靠短劍的旅人。")
    expander.image("DND 照片/卡力克斯.jpeg", caption="卡力克斯", use_container_width=True)

    expander = st.expander("狄蜜特麵包店")
    expander.write("這間麵包店散發著溫暖的麥香，門前擺放著幾籃剛出爐的麵包，黃金色的外皮閃爍著微光。店內擺滿各式各樣的烘焙食品，從簡單的黑麥麵包到摻有蜂蜜與無花果的甜餅，吸引著路人駐足。店裡不時傳來笑聲與交談聲，讓人忍不住停下腳步，買上一塊剛烤好的熱麵包。")
    expander.image("DND 照片/狄蜜特麵包店.jpeg", caption="狄蜜特麵包店", use_container_width=True)
    expander.subheader("瑪爾西婭")
    expander.write("瑪爾西婭是一名中年婦人，圓潤的臉上總是掛著親切的微笑。她熱愛大地女神狄蜜特，認為糧食是神祇的恩賜，理應與所有人分享。因此，流浪者與窮人總能在她這裡獲得一小塊麵包，帶著溫暖離開。她身上總是沾著些許麵粉，雙手布滿了長年揉麵的痕跡。當她提起擀麵杖時，甚至能夠驅散惡棍——曾有一次，兩名地痞試圖搶劫時，她用擀麵杖敲得對方連滾帶爬。")
    expander.image("DND 照片/瑪爾西婭.jpeg", caption="瑪爾西婭", use_container_width=True)

    expander = st.expander("荷米斯馬場")
    expander.write("這座馬場座落於廣場邊緣，周圍圍著一圈木欄，內部寬敞且井然有序。馬匹來回奔跑，訓練有素，時而有信使或旅人來此租借快馬。馬場內還設有簡單的競技場，供人們測試馬匹的速度與耐力。荷米斯的雕像立於馬場入口，象徵著速度與旅程的庇護。")
    expander.image("DND 照片/荷米斯馬場.jpeg", caption="荷米斯馬場", use_container_width=True)
    expander.subheader("尼克昂")
    expander.write("尼克昂是一名身手敏捷的年輕人，擁有一雙如鷹般銳利的眼睛，總是充滿好奇與機智。他身形精瘦，走路帶風，無論是牽馬、訓練，甚至是閃避潑濺的泥水，他的動作都像風一樣迅速。他信仰荷米斯，認為世界的機遇來自於速度與決斷，因此他經營馬場時，總是鼓勵客人挑選最快的坐騎，並時不時分享關於信使與旅人的故事。他總是能嗅出廣場上的最新消息，因此除了馬匹租賃，許多冒險者也會向他打聽情報。")
    expander.image("DND 照片/尼克昂.jpeg", caption="尼克昂", use_container_width=True)

def content_tab3():
    st.header("斬殺侵亂小鎮之涅墨亞獅子")

    st.subheader("涅墨亞小鎮")
    st.write("涅墨亞坐落於黑松林的邊緣，一條蜿蜒的石徑貫穿全鎮。這裡的建築以厚重的岩石堆砌而成，牆面經過長年的煙火洗禮，顯現出深褐與鐵灰交錯的色澤。鎮內到處可見鐵匠鋪與工坊，炙熱的爐火終日不熄，金屬敲擊的聲音混雜著工匠們的低語與怒吼，充斥著空氣中的每一個角落。他們的手掌佈滿繭痕，眼神堅定而專注，這座城鎮的靈魂深植於烈焰與鋼鐵之中，每一次鍛造的聲響，彷彿都是對赫菲斯托斯的讚頌。城鎮中央矗立著一座鍛造之神赫菲斯托斯高舉巨鎚的雕像，眼神炯炯，彷彿隨時準備將意志灌注於熾熱的鐵砧之上。")
    st.image("DND 照片/涅墨亞小鎮.jpeg", caption="涅墨亞小鎮", use_container_width=True)

    st.subheader("里昂")
    st.write("里昂是一位年輕且精緻的巧匠，身形瘦小，靈活且迅速。他的頭髮是深褐色，總是略顯凌亂。他胸前掛著赫菲斯托斯的信物熔岩鍛鎚墜。他的皮膚白皙，雙手纖細，並且總是帶著些許細小的傷痕和燙傷，這些都是長年與銳利的工具和小巧機械打交道的證據。里昂總是穿著一件褐色的工匠外衣，外衣上滿是油漬和泥土。他的腰間總掛著各種工具，從微小的螺絲刀到小型的焊接設備，一應俱全。每當他工作時，他會駐足細看每一個齒輪、每一塊零件，仿佛每一個部件對他來說都是一個複雜的謎題。他的工作台上滿是精緻的機械裝置、複雜的裝飾物品、手工製作的精巧盒子，所有物品都顯示出他對工藝的無限熱情與堅持。雖然里昂並不擅長鍛造武器，但他卻能製作出各種機關、精巧的工具、或是用來解謎的機械裝置。他的作品可能不是暴力的力量，而是智慧和巧思的結晶，這讓他在那些需要精密裝置和解謎能力的場合中，總是成為一位不可或缺的角色。")
    st.image("DND 照片/里昂.jpeg", caption="里昂", use_container_width=True)

    st.subheader("法蘭克")
    st.write("法蘭克是一位年老而精瘦的鍛造大師，身穿灰色的粗布工作服，肩膀上披著厚重的皮革，雙手布滿了因長年操刀鐵器所留下的厚繭和疤痕。他的鬍鬚灰白，眉頭濃密，臉上帶著經年累月鍛造火爐所留下的燒灼痕跡，胸前掛著赫菲斯托斯的信物熔岩鍛鎚墜。當他在鍛爐旁忙碌時，沉默而專注，但與他交涉時，他會顯得話語鋒利、但卻富有見地，儘管語氣總帶著一絲堅定的冷酷。")
    st.image("DND 照片/法蘭克.jpeg", caption="法蘭克", use_container_width=True)

    st.subheader("涅墨亞獅子")
    st.write("涅墨亞獅子是一頭龐大無比的野獸，比凡間的獅子巨大三倍，渾身覆蓋著閃爍琥珀色光芒的毛皮，堅不可摧，。牠的眼睛宛如燃燒的熔爐，瞳孔中閃爍著殘忍與憤怒的光芒。牠的利爪如同神匠鍛造的短劍，能夠撕裂岩石與青銅盔甲，而獠牙則比獵刀更加鋒利，能一口咬碎敵人的骨骼。牠的血液暗紅如熔岩，帶有詛咒，凡人若沾染到這些血液，將陷入劇痛與瘋狂。牠的咆哮震撼天地，足以震裂地面，使敵人站立不穩，甚至短暫失聰。")
    st.image("DND 照片/涅墨亞獅子.png", caption="涅墨亞獅子", use_container_width=True)

def content_tab4():
    st.header("沼澤中斬盡九頭蛇海德拉")

    st.subheader("沼澤")
    st.write("當冒險者踏入沼澤，一股腐爛與硫磺混雜的氣味迎面撲來。黃色與紫黑色的霧氣盤旋在沼澤之上，陽光難以穿透，使整個環境如同墮入無盡的黃昏。毒霧會隨著風勢流動，吸入過多者會感到喉嚨灼熱、視線模糊，甚至產生幻覺，聽見耳邊傳來無形的低語。地面佈滿腐爛的植物與深不見底的泥潭，樹葉枯黃、土地濕潤而發黑。每走一步，腳下的土地便會發出詭異的咕嚕聲，似乎整片大地都是活著的，伺機將闖入者吞沒。偶爾，黑色的水泡自水面冒起，破裂時釋放出令人作嘔的惡臭氣體，讓人感覺每一次呼吸都是對生命的消耗。水中漂浮著不知何時沉沒的戰車與鏽蝕的武器，地上散落著骸骨，顯示過去曾有勇士試圖挑戰此地的統治者，但無人生還。偶爾，一些骨骼上仍殘存著被強酸侵蝕的痕跡，甚至有的仍緊握著劍柄，顯示他們直到最後一刻仍在奮戰。")
    st.image("DND 照片/沼澤.jpeg", caption="沼澤", use_container_width=True)

    st.subheader("羊男地下洞窟")
    st.write("在剛進入沼澤時，一旁有一塊佈滿歲月痕跡的石碑立在岔路旁。上頭刻著一個扭曲的羊頭符號，彷彿以銳利的爪痕劃出，深深嵌入石面之中，久經風雨卻仍清晰可見。石碑旁有一條向下延伸的狹窄通道，邊緣長滿黑色的苔蘚，幾道泛著腐朽氣味的藤蔓懸掛其上。沿著石階往下，空氣逐漸變得陰冷而沉悶，儘管這裡隔絕了地表上毒霧的侵襲，但空氣中仍瀰漫著一種潮濕與霉味交織的味道。洞窟內由粗糙的岩壁圍繞，壁面刻滿了古老的羊角紋路與奇異的符號。洞窟中央有一處略微開闊的空間，數根簡陋的石柱支撐著低矮的頂部，地面上散落著殘破的陶器與獸皮，顯示這裡曾有人居住。靠近深處，擺放著一具殘舊的木製長椅，椅旁是一個石雕製成的羊頭像，羊的眼窩深陷，流淌出乾涸的黑色液體。")
    st.image("DND 照片/羊男地下洞窟.jpeg", caption="羊男地下洞窟", use_container_width=True)

    st.subheader("羊男潘波斯")
    st.write("當冒險者進入這片幽閉的空間時，一道低沉的嘆息聲從角落傳來。那裡蜷縮著一名羊男，他的身軀消瘦，雙腿像山羊般覆滿毛皮，頭上長著一對捲曲的犄角，雙眼暗淡無光，似乎早已接受自己的命運。")
    st.image("DND 照片/羊男潘波斯.jpeg", caption="羊男潘波斯", use_container_width=True)

    st.subheader("九頭蛇海德拉")
    st.write("隨著冒險者逐漸深入，一陣低沉的咆哮自霧中傳來，隨即，水面劇烈翻騰，一道龐然的黑影浮現。九對猩紅的雙眼在黑霧中閃爍，粗壯的鱗甲隱藏在沼澤的污泥裡，九頭蛇海德拉緩緩地升起，毒液從牠的獠牙滴落，落地之處燃起不祥的青黑色火焰，腐蝕著一切生機。")
    st.image("DND 照片/九頭蛇海德拉.png", caption="九頭蛇海德拉", use_container_width=True)

def content_tab5():
    st.header("捕獲月光映照下的馳騁克列尼亞牝鹿")

    st.subheader("克列尼亞草原")
    st.write("一片綿延無際的草原在晨曦中閃爍著金綠色的光輝。微風輕拂，帶動著一望無際的野草，如波浪般輕輕搖曳。偶爾幾朵白色的野花點綴其中，散發出淡雅的芳香，與遠處森林裡的濕潤泥土氣息形成對比。這片草原似乎不曾受到時間的侵蝕，歲月靜靜流淌，彷彿這裡的每一根草、每一縷風都存於天地初開之時。")
    st.image("DND 照片/克列尼亞草原.jpeg", caption="克列尼亞草原", use_container_width=True)

    #st.subheader("獵人黛安娜營區")
    #st.write("一座隱匿於高草之間的營地，四周豎立著幾根粗壯的木樁，綁著風乾的野獸骨飾，這些骨片在夜風中輕微晃動，發出宛如狩獵之歌的低吟。中央，一頂簡樸卻堅固的帳篷由獸皮與樹枝搭建而成，帳篷外懸掛著幾張風乾的狼皮與鹿角，象徵著狩獵的榮耀與敬畏。帳篷內部陳設極為簡單，地上鋪著厚實的毛皮，角落擺放著削得銳利的箭矢與一張銀弓，箭袋整齊排列，顯示出主人的謹慎與紀律。帳篷旁邊，一排低矮的石台上擺放著以月光為祭的獵物——新鮮的野兔與水鳥，依照古老的狩獵儀式處理，獻給那位在夜幕之下注視著萬物的女神。")
    #st.image("DND 照片/黛安娜營區.jpeg", caption="獵人黛安娜營區", use_container_width=True)

    #st.subheader("月光獵人黛安娜")
    #st.write("她如月影般神秘，腳步無聲，唯有當皎潔的月光灑落樹梢時，人們才能隱約瞥見她的身影。黛安娜身披一襲月白色的輕甲，光滑如銀，卻如夜霧般輕盈，使她能在森林間迅捷無聲地穿梭。她的披風宛如夜空，點綴著銀色的星屑，隨著微風飄動，彷彿群星在黑暗中閃爍。她的雙眼如冷月之輝，透著沉靜與威嚴，能洞悉任何潛伏於黑暗中的生靈。一年之中有一半的日子代替她的信奉神祇阿提密斯維持這片森林的秩序。")
    #st.image("DND 照片/月光獵人黛安娜.jpeg", caption="月光獵人黛安娜", use_container_width=True)

    st.subheader("克列尼亞牝鹿")
    st.write("這頭牝鹿的雙眼如琥珀般透亮，充滿靈性，蹄子輕盈無聲，能以不可思議的速度穿梭於森林之間。傳說牠可奔馳如疾風，甚至能踏浪過河，沒有人能輕易追上它。牠不懼生人，但也絕不輕易被捕捉。")
    st.image("DND 照片/克列尼亞牝鹿.png", caption="克列尼亞牝鹿", use_container_width=True)

def content_tab6():
    st.header("活捉厄律曼托斯山雪峰中野豬")

    st.subheader("厄律曼托斯山脈")
    st.write("厄律曼托斯山脈山勢陡峭，松林遍佈，地勢崎嶇，時有濃霧瀰漫。夜間溫度驟降，適合潛伏與設伏。野豬棲息之地，終年積雪，地面藏有裂縫與冰河暗流。呼吸吐霧，腳步聲在雪地回響。此處偶爾可見巨大蹄印與折斷的松木，顯示牠的力量。針葉林蔓延於山地斜坡，冷風穿梭松柏之間，枝葉低垂覆雪，地面鋪滿厚厚的松針與斷枝。")
    st.image("DND 照片/厄律曼托斯山.jpeg", caption="厄律曼托斯山脈", use_container_width=True)

    st.subheader("厄律曼托斯山野豬")
    st.write("體型如牛，渾身覆蓋深棕與鐵灰交錯的粗硬毛髮，雙目泛紅如火，獠牙彎曲粗長。蹄聲沉重，奔行如雷，每次呼吸皆吐出白霧與低鳴，身上隱有古老符紋般的傷痕，散發殘暴與原始怒意。")
    st.image("DND 照片/厄律曼托斯山野豬.jpeg", caption="厄律曼托斯山野豬", use_container_width=True)

    st.subheader("盜賊傭兵團")
    st.write("多人組成，身著舊戰甲與毛皮，皮膚曬黑斑駁，武器混雜但上手純熟，臉上或帶戰紋，或蒙布遮面。他們行事粗暴，彼此少語但動作協調，眼神警惕，行蹤如狼群般悄然逼近。")
    st.image("DND 照片/盜賊傭兵團.jpeg", caption="盜賊傭兵團", use_container_width=True)

def content_tab7():
    st.header("清洗污穢積年奧格阿斯牛廄")

    st.subheader("沉音花園")
    st.write("一座靜默無聲的幽暗花園，滿布罪惡玫瑰，每一朵皆如閉合的耳語，在風中不搖不曳。中央有一道石徑蜿蜒，路旁刻有模糊難辨的名字與片語，似是遺忘者的記憶殘痕。花香清淡卻異常銳利，嗅入鼻中便如割裂心神，一段記憶將在腦海中悄然消退。無鳥鳴、無風聲、無回音，彷彿整座世界在此屏住了呼吸，只等旅人決定該放下什麼，才能繼續前行。")
    st.image("DND 照片/沉音花園.jpeg", caption="沉音花園", use_container_width=True)

    st.subheader("逆律殿堂")
    st.write("一座矗立於灰白天幕與鏡面大地之間的殿堂，建築本身彷彿被上下顛倒般倒懸於半空。水自天花板傾流而上，火焰冷凝於石柱之中，陰影照亮空間而光線深陷黑暗。走入其中，時間感扭曲，言語一出口便迴盪成實體，思想在空氣中顫動如絲。牆面上嵌著無名者的祈語與倒寫的神文，每一步都像踏入自己記憶的錯層。這裡不是建築，而是信仰與罪的回音。")
    st.image("DND 照片/罪潮裂口.jpeg", caption="逆律殿堂", use_container_width=True)

    st.subheader("王宮侍女薇拉")
    st.write("滿頭灰白蓬亂長髮覆住半邊臉孔，瘦小駝背，披著染有牛血與灰燼的舊僕衣，眼神沉靜如枯井。喉頸上留有舊創，聲帶早被割除，只以斑駁石板與細炭書寫溝通。她手中總握著斷裂的鐵匙，一手拄著裂痕累累的拐杖，行動緩慢卻堅定。儘管無法言語，她凝視時卻仿若能看透過往之重，心中承載著牛廄昔日的全部罪與痛。")
    st.image("DND 照片/王宮侍女薇拉.jpeg", caption="王宮侍女薇拉", use_container_width=True)

    st.subheader("奧格阿斯王")
    st.write("蒼老而枯槁的男子，披著殘破的王袍，指節如枯枝，雙眼混濁卻時而閃現神智的火光。他滿身塵垢與牛糞味，頭戴傾斜的破冠，神智游移不定，語句跳躍反覆。肩背微駝，步履不穩，時常爆發出異常狂熱，聲如雷吼，氣如火發，彷彿仍是王座上的掌權者。")
    st.image("DND 照片/奧格阿斯王.jpeg", caption="奧格阿斯王", use_container_width=True)

def content_tab8():
    st.header("殺死鋼羽掠空斯廷法利斯湖怪鳥")

    st.subheader("斯廷法利斯湖")
    st.write("斯廷法利斯湖怪鳥，其形如夜鷹與鷲鷹混種，羽毛呈現金屬質地，銅銳如刃，微風拂動便能嗆聲如刃鳴。雙翅扇動時捲起鐵鏽與羽刃風暴。牠們的喙可裂甲啄骨，利爪則鋒利如鐵鉤，能輕易撕裂護甲與盾牌。當群鳥齊飛，宛如鐵雨傾瀉，片甲不留。")
    st.image("DND 照片/斯廷法利斯湖.jpeg", caption="斯廷法利斯湖", use_container_width=True)

    st.subheader("湖中遺跡")
    st.write("半沉於湖中的一座古老神殿。現在堆滿了鋒利金屬羽毛與半融化的盔甲。")
    st.image("DND 照片/湖中遺跡.jpeg", caption="湖中遺跡", use_container_width=True)

    st.subheader("幽靈女戰士梅麗瑟")
    st.write("梅麗瑟的幽魂在湖畔的濃霧中時隱時現，身披斷裂破碎的胸甲。她的長髮隨靈氣無風而舞，雙眼泛著冷光，如同湖水下未解的怒意。她的身體半透明、散發微光，她說話時聲音低沉空靈，彷彿從水底傳出，語氣中充滿不甘與執著。")
    st.image("DND 照片/斯廷法利斯湖女戰士.jpeg", caption="幽靈女戰士梅麗瑟", use_container_width=True)

def content_tab9():
    st.header("制服克里特島狂暴公牛")

    st.subheader("迷宮入口")
    st.write("迷宮的入口坐落於克里特島北端，一座嶙峋岩石圍繞的峽谷盡頭。遠望之時，僅見斷垣殘壁與古老祭壇的遺跡，唯有走近，才能發現那扇半掩於地表之下的巨大青銅門。在迷宮入口的側牆上，有一座由青銅與黑曜石構成的圓形石盤，分別刻著兩個圖案：一卷繩索、一幅迷宮地圖，看起來像是大門的開關。")
    st.image("DND 照片/迷宮入口.jpeg", caption="迷宮入口", use_container_width=True)

    st.subheader("祭壇")
    st.write("一處方形大殿靜靜矗立，與四周蜿蜒幽暗的通道截然不同。大殿的圓頂高聳，以銀白與赤金交織鑄成，中央鏤空讓一道永不熄滅的光柱從天而降，彷彿來自星界深處。地面則鋪著漆黑玄岩，上鑲十道放射狀的金線，各通往一座等距排列的祭壇，每座祭壇象徵一位奧林帕斯主神。每座祭壇下皆刻有古老的銘文。祭壇之間懸浮著細微的星塵與火光，當有人靠近時，地面金線隨之微光閃爍，仿若某種古老神力甦醒。")
    st.image("DND 照片/神殿.jpeg", caption="祭壇", use_container_width=True)

    expander = st.expander("帕西淮遊蕩處")
    expander.write("這個隱秘空間是帕西淮殘影遊蕩之地。四周牆壁由冷灰色的石塊砌成，卻佈滿如藤蔓般的龜裂與被撕裂的古老咒文，似乎曾經被某種神力灼燒又強行封印。天花板垂下的蔓藤已枯黃焦黑，空氣中瀰漫著微弱的香草與血氣混合的氣息。")
    expander.image("DND 照片/帕西淮遊蕩處.jpeg", caption="帕西淮遊蕩處", use_container_width=True)
    expander.subheader("帕西淮")
    expander.write("一位身披墨綠長袍的中年女子，銀白髮絲如海浪般垂落，眉宇之間隱藏著深重的悲傷與古老的神秘。她的雙眼彷彿映著夜海，幽深而迷離，時而可見月光般的微光流動其中。身上散發淡淡的花香與藥草氣息。雖為幻靈形體，但舉手投足仍具母性的溫柔與無法言說的遺憾。")
    expander.image("DND 照片/帕西淮.jpeg", caption="帕西淮", use_container_width=True)

    expander = st.expander("代達羅斯工作室")
    expander.write("代達羅斯的工作室深藏於迷宮腹地。走過曲折石階與機關暗道後，冒險者將抵達一扇厚重的銅門，其上刻有錯綜複雜的齒輪與星象圖紋。當銅門緩緩開啟，映入眼簾的是一間寬敞卻雜亂無章的空間，瀰漫著金屬、油脂與炙熱石灰的氣味。四面牆壁皆嵌滿活動式的工具架，排列著古老又陌生的器械。一張龐大的石製工作桌橫亙中央，桌上堆著發光的礦石、未完成的自走機偶。屋內一處平台上有個微光流動的半球狀觀測儀，正無聲轉動，投影出迷宮結構的動態全貌，迷宮的轉動與陷阱變化可在此即時顯示。牆角堆滿草圖與設計書卷。書架上則放有數本以鯨皮裝訂、用古希臘文與神祇語混寫的筆記。天花板懸掛著各種尚未完成的機械創造，有的彷彿鳥翼、有的像人臉、有的則完全無法辨識用途。這個空間儘管混亂，卻充滿一種強烈的秩序與智慧痕跡，每一件物品都似乎處於正確的位置。這是一座不屬於時代的工坊，亦是一間牢籠。")
    expander.image("DND 照片/代達羅斯工作室.jpeg", caption="代達羅斯工作室", use_container_width=True)
    expander.subheader("代達羅斯")
    expander.write("一位身形高瘦的中年男子，披著刻有黃銅與象牙紋飾的長袍，衣角掛滿卷軸、齒輪與鐘擺零件。他的雙手骨節粗大，指節滿是工具長年磨出的痕跡，掌心總沾著些微油漬與碳粉。臉上刻滿歲月與天才的孤傲，深陷的眼窩裡燃著冷靜且急躁的火光——那是無數創作與失敗後仍不肯熄滅的求知之焰。")
    expander.image("DND 照片/代達羅斯.jpeg", caption="代達羅斯", use_container_width=True)

    st.subheader("房間 A")
    st.write("房間四面牆壁高聳而不規則，由一種黯紅色的火山岩構成，其上刻滿了被劍刃與蹄爪劃出的痕跡，地板由龜裂的大理石拼合而成，中央陷落成一個粗糙的鬥技場般凹陷區，周圍布有破碎的鎖鍊與生鏽的銅柱。空氣中帶有濃重的汗水、鐵鏽與獸皮混合的氣味，並隱約聽見沉重呼吸與腳蹄踱地聲，在幽深回音中倍增其震懾力。四周石柱傾斜倒塌，一些甚至被撞碎成粉。天花板上垂掛著乾枯的藤蔓與古代掛飾，如今蒙塵褪色。當冒險者踏入時，沉睡的咆哮將自深處響起，伴隨踏地之震，牆面浮現溫熱的氣浪，彷彿整座迷宮都在喚醒牠的怒意與記憶。")
    st.image("DND 照片/房間 A.jpeg", caption="房間 A", use_container_width=True)

    st.subheader("房間 B")
    st.write("迷宮的一翼深處，有一間與整座迷宮陰暗潮濕的氛圍截然不同的房間。當冒險者接近這裡時，空氣變得乾燥灼熱，地面轉為淺白與淡金交錯的石材；天花板極高。牆面以大理石雕飾出奔牛與太陽的浮雕圖騰，已因歲月風化而模糊不清。這裡不是戰場，而是一座獻祭神牛的祕殿")
    st.image("DND 照片/房間 B.jpeg", caption="房間 B", use_container_width=True)

    st.subheader("???")
    st.write("牠如神祇親手雕鑄的野性化身，全身潔白無瑕，肌理分明，毛髮宛如絲綢覆雪，閃爍淡金色的光澤。雙眼如兩枚燃燒的琥珀，蘊含怒火與神性的意志。四蹄踏地會在石板上留痕，背脊之上浮現如雷電閃爍般的靈紋，象徵其非凡的血脈。其鼻間吐息灼熱，踩踏之地留下焦土與灼痕，咆哮聲能撕裂迷宮之牆。牠非惡，卻不受控，牠無言，卻仿若試圖控訴天命的殘酷。")
    st.image("DND 照片/克里特公牛.jpeg", caption="???", use_container_width=True)

    st.subheader("???")
    st.write("半牛半人的高大身影，擁有宛如鐵塔般的身軀與覆蓋苔蘚的暗紅獸皮。兩隻巨大彎角像古老樹枝般向後延展，臉上獸性與人性交織，時而咆哮，時而沉默。他雙眼泛著黃銅色光芒，閃爍如迷宮中無盡的燈火，語言困頓，情感卻真切。胸前綁著斷裂的鏈索，那是帕西淮留下的最後安撫之物。若靠近細看，可見其左肩上刻有赫菲斯托斯所鑄的封印符文，微微閃動，似在壓制其失控的本能。")
    st.image("DND 照片/彌諾陶.jpeg", caption="???", use_container_width=True)

def content_tab10():
    st.header("降伏狄俄墨得斯食人牝馬")

    st.subheader("空蕩城邦")
    st.write("這座空蕩的城邦正對著宮殿。城邦毫無人聲。鳥類不棲、野獸不近，唯有風聲穿梭於建築之間，宛如回音在對空無低語。進入城邦後，街道兩旁的房屋皆完好如初，門戶緊閉，窗簾輕掀，彷彿人們只是瞬間消失，生活痕跡仍在：乾裂的麵包、尚未冷卻的爐灶、灑落地面的骨骰。夜幕降臨後，城中會浮現模糊的身影，在街角、窗後、屋頂默立，無聲注視入侵者。沒有攻擊，只有持續的凝視與逐漸逼近的不安感。")
    st.image("DND 照片2/空蕩城邦.jpeg", caption="空蕩城邦", use_container_width=True)

    #expander = st.expander("王國宮殿")
    #expander.subheader("宮殿大廳")
    #expander.write("宮殿的大廳內常常舉行盛大的宴會與儀式，地板由大理石鋪就，上面刻有複雜的圖騰和家族徽章。牆壁上掛著由大師畫家創作的油畫，描繪著國家歷史上的重要事件和戰爭勝利。此地氣氛隆重，長桌兩旁擺放著美味的食物與金杯，偶爾會有賓客和貴族們在此會面。")
    #expander.image("DND 照片2/宮殿大廳.jpeg", caption="宮殿大廳", use_container_width=True)
    #expander.subheader("皇家馬廄")
    #expander.write("馬廄四周被古老的石牆包圍，這裡的空間大而寬敞，廄內放著許多精緻的馬具與武器，木地板上鋪著厚厚的乾草。")
    #expander.image("DND 照片2/皇家馬廄.jpeg", caption="皇家馬廄", use_container_width=True)
    #expander.subheader("王宮文件室")
    #expander.write("這間文件室收藏著王國所有珍貴的卷軸和手稿。高高的書架上擺滿了知識與智慧的結晶，空氣中彌漫著老舊書本的味道。此地不僅是知識的寶庫，也是王國政府謀劃與計劃的重要場所。")
    #expander.image("DND 照片2/文件室.jpeg", caption="王宮文件室", use_container_width=True)
    #expander.subheader("王宮地下室")
    #expander.write("位於宮殿深處的地下室，常常用來儲存王國的珍寶與秘密文件。這裡陰暗潮濕，走廊中燈光昏暗，牆上長滿了青苔和藤蔓。地下室裡有許多密室，存放著各式各樣的文物、古籍以及貴金屬。曾經有傳聞稱，地下室深處還藏著不為人知的秘密與禁忌物品，只有極少數的宮廷高層才有權利接觸這些神秘物品。")
    #expander.image("DND 照片2/王宮地下室.jpeg", caption="王宮地下室", use_container_width=True)
    #expander.subheader("秘密花園")
    #expander.write("王宮後方有一座隱秘的花園，這裡種植著奇異的花卉與草藥，四季如春。花園中有一條蜿蜒的小徑，通向一座小型的池塘，水面上漂浮著各式各樣的荷花。花園四周被高高的竹籬圍繞，外界很難窺見其中的動靜。")
    #expander.image("DND 照片2/秘密花園.jpeg", caption="秘密花園", use_container_width=True)
    #expander.subheader("宮殿露台")
    #expander.write("宮殿最頂層有一個開放的露台，從這裡可以俯瞰整個王國。露台四周圍著鐵製欄杆，並有裝飾性的雕塑。這裡的風景壯麗，常是國王或貴族觀察國土、監視局勢的地方。隨著日落時分，露台上會充滿柔和的光線，是國王與賓客進行重要談話或放鬆的理想場所。")
    #expander.image("DND 照片2/宮殿露台.jpeg", caption="宮殿露台", use_container_width=True)

    st.subheader("煙霧林地")
    st.write("這是一片幽暗的森林，空氣中總是彌漫著一層薄薄的煙霧，彷彿隨時會有火焰爆發。這裡的樹木高大而茂密，枝葉交織，讓陽光無法穿透，營造出一個陰森的氛圍。樹木上的藤蔓像是盤踞的巨蛇，時不時會聽見遠處傳來的馬蹄聲與低吼，這是牝馬們徘徊在邊界的警告聲音。")
    st.image("DND 照片2/煙霧林地.jpeg", caption="煙霧林地", use_container_width=True)

    st.subheader("牝馬")
    st.write("由左至右分別是：")
    st.write("-- 恐怖（Deinos）")
    st.write("-- 閃耀（Lampon）")
    st.write("-- 迅疾（Podagros )")
    st.write("-- 金黃（Xanthos）")
    st.image("DND 照片2/牝馬.jpeg", caption="牝馬", use_container_width=True)

def content_tab11():
    st.header("奪取亞馬遜女王之榮耀腰帶")

    expander = st.expander("亞馬遜王國")
    expander.write("亞馬遜王國位於遼闊的沙漠中，只有最勇敢與智慧的冒險者才能穿越重重沙漠，找到這片女戰士的聖地。當你走進這片王國的邊境，首先感受到的是一股力量的氣息，似乎空氣中每一個分子都帶著強大的生命力，沙漠的每一個角落都充滿了無聲的警覺。沿著粗糙的石板路走去，逐漸可見到一些精緻的石製建築，它們與周圍的自然景觀完美融合。亞馬遜王國的建築多以石材與木材為主，設計簡潔而實用，外觀粗獷中帶有優雅。進入王宮的核心區域，空氣中充滿了藥草的香氣和來自火焰的熾熱。王宮內部的設計簡潔而莊重，牆壁上懸掛著女戰士的徽章、古老的戰旗與勝利的紀念品，每一件物品都訴說著一段段激烈的戰鬥與英雄的傳奇。這裡的每一個角落都彷彿承載著女王希波呂忒的威嚴與亞馬遜戰士的勇氣。")
    expander.image("DND 照片2/亞馬遜王國.jpeg", caption="亞馬遜王國", use_container_width=True)
    #expander.subheader("王國監獄")
    #expander.write("亞馬遜王國的監獄像一個被遺忘的陰影，默默存在於古老的岩洞之中。這座監獄並非建造於平凡的土地，而是依靠天然的地下岩層與隱蔽的巖洞構成，它的入口隱蔽且狹窄，只有經過精心設計的標記和指引，才能找到通往這片禁錮之地的路。進入監獄，首先映入眼簾的是陰沉的光線，只有稀疏的火把散發出微弱的光芒，映照在石牆上，創造出扭曲的陰影。這些火把的光芒似乎無法驅散周圍的黑暗，反而讓一切更加沉重。空氣中瀰漫著潮濕的氣息，岩壁上渗透著水珠。監獄的結構錯綜複雜，走廊彎曲迂回，像迷宮一般，讓人難以逃脫。每個囚室都用厚重的鐵欄杆或石門隔開，裡面只有簡陋的床鋪與粗糙的石地，沒有任何奢華。囚犯的呼吸聲、腳步聲和偶爾的低語，回響在狹窄的空間中，打破了這裡的死寂。監獄的守衛並非普通的士兵，而是亞馬遜王國最精銳的女戰士，她們對囚犯毫不留情。她們穿著簡潔而堅固的盔甲，手持長矛，目光銳利，時刻警戒著任何試圖越獄的行為。")
    #expander.image("DND 照片2/王國監獄.jpeg", caption="王國監獄", use_container_width=True)
    expander.subheader("亞馬遜女王希波呂忒")
    expander.write("身穿以獸皮與黃銅鑄成的戰鎧，眼神堅毅、話語簡潔有力。她是亞馬遜部族的精神與軍事領袖，冷靜而不輕信外人。她佩戴的腰帶是一件神祕神器，相傳由戰神阿瑞斯贈予，能加強持有者的戰鬥與領導能力。")
    expander.image("DND 照片2/希波呂忒.jpeg", caption="亞馬遜女王希波呂忒", use_container_width=True)
    #expander.subheader("女王副官伊法恩")
    #expander.write("個性激進，極不信任外來者，總認為冒險者圖謀不軌。主張直接逐出或審判入侵者。她是玩家在部族內最可能遇到的阻礙。")
    #expander.image("DND 照片2/伊法恩.jpeg", caption="女王副官伊法恩", use_container_width=True)

    #expander = st.expander("聖火工坊")
    #expander.write("隱藏於一片陰影中的石洞內，聖火工坊的入口幾乎與周圍的自然環境融為一體。洞口由一塊巨大的岩石擋住，只有在夕陽的最後光芒照射時，才隱約可見一條狹窄的縫隙，似乎刻意隱匿在密林深處。走進這個隱秘之地，空氣中充斥著香木煙與金屬的味道，洞內的光線昏暗，依靠一些石雕的神秘符號所釋放的微弱光芒照亮四周。洞壁上雕刻著許多古老的圖騰與符文，這些圖案彷彿訴說著遠古的故事與秘法，它們似乎是由某種未知的工匠所刻，表現出人類與神祇、自然界的深刻聯繫。每當火光閃爍，這些圖騰便會投下奇異的陰影，彷彿有生命般隨著火光跳動。")
    #expander.image("DND 照片2/聖火工坊.jpeg", caption="聖火工坊", use_container_width=True)
    #expander.subheader("塞瑞薇")
    #expander.write("塞瑞薇身形纖細結實，膚色帶著陽光曬過的健康古銅色。她的雙眼明亮如琥珀，總帶著好奇與警覺，彷彿在時刻觀察這個她熱愛卻質疑的世界。她綁著一頭蓬鬆的深褐色捲髮，髮間插著製作腰帶用的銀針與銅簪，就像戰士插羽那般自然。與其他亞馬遜戰士不同，塞瑞薇身穿的是簡化式皮甲與編織布料混合的衣著，上面繡有代表家族與工坊的幾何圖紋，腰間掛滿製繩、鉤環與小刀等工具。她的手指佈滿長年製作皮革時留下的繭與刮痕，卻總是細緻地觸摸每一根線，每一塊獸皮，彷彿在與材料對話。她行動快速，語速輕快，但在長輩或衛士面前仍保留傳統敬語。她相信傳承，但更想改變。對於外來者，她抱持保留但不敵意的態度——若他們願意學習，她會是最誠實的老師；若他們只想奪取，她寧願將知識一同埋葬在獸皮下。")
    #expander.image("DND 照片2/塞瑞薇.jpeg", caption="塞瑞薇 – 年輕的亞馬遜學者與製帶工匠", use_container_width=True)

def content_tab12():
    st.header("牽回迷途之革律翁牛群")

    expander = st.expander("格律翁的堡壘")
    expander.write("巨人格律翁的堡壘位於險峻山脈之中，堡壘建在一座高大的懸崖上，從這裡俯瞰整片草原。堡壘內的設計以冷鋼和黑岩為主，散發著陰暗且沉重的氣息。這座堡壘充滿了危險的陷阱和防衛機制，並且由巨人與神秘的守衛所把守。")
    expander.image("DND 照片2/格律翁堡壘.jpeg", caption="格律翁的堡壘", use_container_width=True)
    expander.subheader("巨人格律翁")
    expander.write("巨人格律翁好戰且嫉妒，對任何侵入自己領土的人懷有強烈的敵意。巨人格律翁非常自信，覺得自己所擁有的東西無人能奪走。")
    expander.image("DND 照片2/格律翁.jpeg", caption="巨人格律翁", use_container_width=True)

    expander = st.expander("海岸線")
    expander.write("一片長長的金色沙灘和藍色的大海交織，海風清新，海浪不斷拍打著岸邊。這片海岸線被稱為“英雄的海”，因為過去許多傳奇的冒險者曾在此起航。沿岸有一些廢棄的漁村，這些村莊曾經被海上怪物摧毀，現在已被大自然重新吞噬。這片海岸常受猛烈的海風與突如其來的暴風侵襲。")
    expander.image("DND 照片2/海岸線.jpeg", caption="海岸線", use_container_width=True)
    #expander.subheader("卡利斯")
    #expander.write("卡利斯是一位年輕且充滿魅力的海盜首領，精明、機智且不容小覷，具有非常強的領導能力。他善於交涉，並且在戰鬥中充滿動力。對他來說，報仇與金錢的誘惑是無法抗拒的。")
    #expander.image("DND 照片2/卡利斯.jpeg", caption="卡利斯", use_container_width=True)

    expander = st.expander("葡萄園與橄欖樹林")
    expander.write("這片地區擁有豐富的土地，葡萄藤在地中海的陽光下茂盛生長，而橄欖樹則提供了一片陰影，為這片土地帶來安逸與靜謐。葡萄園之中，有些隱秘的地下通道，可以通往古老的祭壇和祭司的洞窟。")
    expander.image("DND 照片2/葡萄園與橄欖樹林.jpeg", caption="葡萄園與橄欖樹林", use_container_width=True)
    #expander.subheader("麥格諾")
    #expander.write("麥格諾是一位年輕的獨臂獵人，沉默寡言、警覺，他信奉的是「智謀勝於力量」的信條，他經常保持冷靜，並且能在困境中提供關鍵的建議。他對牛群有著極深的了解。")
    #expander.image("DND 照片2/麥格諾.jpeg", caption="麥格諾", use_container_width=True)
    #expander.subheader("亞娜")
    #expander.write("亞娜是來自地中海沿岸小村落的年輕祭司，她的家族世代與神祇有著深厚的聯繫，並以守護神殿為生。她的神殿位於海岸的懸崖上，能俯瞰整個大海。她謹慎且具有神秘氣質並深信神的旨意，而且擁有強烈的直覺能力。她對任何未經神許可的冒險都心存疑慮，但也不會拒絕有信念的挑戰者。")
    #expander.image("DND 照片2/亞娜.jpeg", caption="亞娜", use_container_width=True)

    expander = st.expander("岩石峭壁")
    expander.write("這些峭壁直插雲霄，從高處俯瞰下去，可以看到整個地中海的壯麗景觀。岩壁上有許多由自然力量形成的奇異洞窟，風力強烈，常常使得這些峭壁成為危險的障礙。這些岩壁的登攀是一次極大的挑戰，任何失誤都可能掉入深不見底的深谷。")
    expander.image("DND 照片2/岩石峭壁.jpeg", caption="岩石峭壁", use_container_width=True)
    #expander.subheader("無名英雄")
    #expander.write("這五位無名英雄身形高大、肌肉結實，面容棱角分明，眼神堅毅，透露著無畏的勇氣。臉上有著戰鬥的疤痕與深深的皺紋，皮膚顯得粗糙而結實。")
    #expander.image("DND 照片2/無名英雄.jpeg", caption="無名英雄", use_container_width=True)

    expander = st.expander("牛群草原")
    expander.write("牛群所在的領地是一片寬廣的草原。每一頭牛都有強烈的領地意識，它們對異物的氣息極為敏感。")
    expander.image("DND 照片2/牛群草原.jpeg", caption="牛群草原", use_container_width=True)

def content_tab13():
    st.header("摘取極西赫斯珀裡得斯聖園之果")

    expander = st.expander("流浪商人的帳篷")
    expander.write("帳篷立於聖園外的一片寂靜草原，帳篷本身由古老的獸皮與黑色絲綢拼接而成，邊緣綴著銅製的鈴鐺，隨風搖曳時發出低沉的聲響。頂部懸掛著數串奇異的乾燥草藥與動物骨飾，每當微風吹拂，便散發出一股混雜著香料與煙草的氣息。帳篷內部昏暗而神秘，唯有幾盞懸掛的藍色燭火微微照亮擺滿奇異物品的木架與地毯上的低矮桌案。")
    expander.image("DND 照片2/流浪商人帳篷.jpeg", caption="流浪商人的帳篷", use_container_width=True)
    expander.subheader("流浪商人卡呂普索")
    expander.write("一名神秘的流浪商人，她的臉部幾乎被深紫色的頭巾與斗篷遮掩，露出的僅是一雙如琥珀般的雙眼，總是閃爍著難以捉摸的光芒。她的膚色帶有一絲古銅色，手指纖長而靈巧，指節上帶著各式各樣的戒指，每一枚戒指的寶石似乎都蘊藏著不同的故事。她的身上總是披著一件深藍色的長袍，袖口繡著難以辨識的古老文字，偶爾隨步伐晃動，隱約可見暗金色的紋路浮現。")
    expander.image("DND 照片2/卡呂普索.jpeg", caption="流浪商人卡呂普索", use_container_width=True)

    expander = st.expander("赫斯珀里得斯聖園")
    expander.write("聖園是一個靜謐而神聖的地方。整個區域被一層神秘的薄霧所籠罩，四周環繞著高聳的青翠樹木，樹枝盤結如同天然的圍牆，阻擋了外界的視線。每棵果樹上都有閃耀著無比迷人光澤的金蘋果，散發著一股誘人的香氣。每一顆蘋果都充滿神秘的力量。果樹的根部深深地扎入土地，周圍的土壤豐饒而滋潤，使得這片土地如同永恆的樂土。整個聖園被一片祥和與神聖的氛圍籠罩。整個聖園彷彿是遠離人世塵囂的桃源，時間在這裡緩慢流逝，空氣中充滿了神秘與寧靜，讓人一旦踏入便無法自拔，彷彿進入了一個不屬於凡人的世界。")
    expander.image("DND 照片2/聖園.jpeg", caption="聖園", use_container_width=True)
    expander.subheader("仙女赫斯珀里得斯")
    expander.write("仙女赫斯珀里得斯是天后希拉親選的守護者，同時也是黃昏與暮光的化身，彷彿夕陽最後一縷餘暉凝聚而成的女神。她的雙眼深邃如暮色星辰，藏著古老智慧與不可測的神秘，每一次凝視都彷彿能讀透來者的意圖。她身披輕紗，步履輕盈，行走於花園時，腳下會綻放金色花朵。")
    expander.subheader("巨龍拉頓")
    expander.write("拉頓（Ladon）是一條盤踞在赫斯珀里得斯花園中的金龍，牠的身軀猶如鑄金般閃耀，每一片鱗甲都映照著日光，彷彿由神火鍛造，散發著神聖而不可侵犯的威嚴。牠擁有一顆巨大的龍首，雙眼猶如琥珀，深邃而銳利，凝視入侵者時，彷彿能直視靈魂深處。拉頓的身軀蜿蜒盤踞於園中的金蘋果樹，長尾如鎖鏈般纏繞樹幹，爪痕刻印於土地與岩石之上，顯示出牠作為守護者的無可動搖。每當風掠過，牠的金色鱗片便映射出如日落般的餘暉，使整座花園籠罩在一片神秘而靜謐的光輝中。當有不速之客靠近，拉頓將緩緩抬起頭顱，金光自瞳孔閃耀，伴隨低沉的龍吟，如古老的誓言迴蕩在天地間，警告世人——這裡是神聖之地，凡人勿近。")
    expander.image("DND 照片2/仙女與巨龍.jpeg", caption="仙女赫斯珀里得斯與巨龍拉頓", use_container_width=True)


def content_tab14():
    
    st.markdown("""
        <style>
        .dark-box {
            background-color: #1e1e1e;
            color: white;
            padding: 20px;
            border-radius: 10px;
        }
        </style>
        """, unsafe_allow_html=True)

        # 把內容包在 .dark-box 中
    st.markdown("""
        <div class="dark-box">
            <h2>入冥府降伏三頭犬克爾柏洛斯</h2>
            <p>測試</p>
        </div>
        """, unsafe_allow_html=True)


def content_tab15():
    st.header("英雄事蹟")

    st.write("一、神諭的無上加冕")
    st.checkbox("天選之人：完成所有的神諭指示")
    st.checkbox("權宜之計：在一項神諭中不與任何 NPC 進行互動（怪物除外）")
    st.checkbox("醉翁之意：透過非常規手段完成一項神諭（DM 判斷）")
    st.checkbox("強弩之末：在僅有兩位（含）以下英雄的參與下完成一項神諭")

    st.write("二、英雄的自我救贖")
    st.checkbox("不敗之地：團隊在一次神諭任務中至少一半的成員未失去生命值")
    st.checkbox("君子之交：在冥界中遇到三個團隊曾經在人界擊殺的生物")
    st.checkbox("身外之物：團隊中有英雄曾經獲得護符後又失去護符")
    st.checkbox("害群之馬：團隊中有英雄曾經在戰鬥中不幸死亡")

    st.write("三、天神的虔誠子民")
    st.checkbox("中庸之道：有英雄使用過護符中兩種不同的祝福類型")
    st.checkbox("天作之合：一位英雄在至少五個不同地點尋獲信奉神祇之祭壇")
    st.checkbox("赤子之心：所有英雄在所有接觸到的祭壇都進行供奉行為")
    st.checkbox("一念之間：一位英雄曾經和其信奉神祇進行（實際或意念）交流")

    st.write("四、額外的迷惑行為")
    st.checkbox("亡命之徒：？？？")
    st.checkbox("不智之舉：？？？")
    st.checkbox("眾矢之的：在一次神諭中與所有出現之 NPC 進行戰鬥")
    st.checkbox("九泉之下：？？？")


#def content_default(tab_title):
    #st.header(f"{tab_title}（內容範例）")
    #st.write("這裡是範例內容。請填入實際模組資料。")

# 通關驗證邏輯（支援單一密碼或多密碼）
def gated_content(tab, password_required, content_function, tab_title):
    with tab:
        session_key = f"access_{tab_title}"

        # 如果不需要密碼，直接顯示內容
        if password_required is None:
            content_function()
            return

        if session_key not in st.session_state:
            st.session_state[session_key] = False

        if not st.session_state[session_key]:
            code = st.text_input("請輸入通關碼以檢視內容：", type="password", key=f"code_{tab_title}")
            if isinstance(password_required, list):
                if code in password_required:
                    st.success("通關成功！")
                    st.session_state[session_key] = True
                elif code != "":
                    st.error("通關碼錯誤，請再試一次")
            else:
                if code == password_required:
                    st.success("通關成功！")
                    st.session_state[session_key] = True
                elif code != "":
                    st.error("通關碼錯誤，請再試一次")

        if st.session_state[session_key]:
            content_function()

# tabs 建立
tabs = st.tabs([title for title, _ in tabs_config])

# 指定哪些 tab 用哪個內容函數
custom_tab_functions = {
    "模組簡介": content_tab1,
    "雅典城": content_tab2,
    "涅墨亞獅子": content_tab3,
    "九頭蛇海德拉": content_tab4,
    "克列尼亞牝鹿": content_tab5,
    "厄律曼托斯山野豬": content_tab6,
    "奧格阿斯牛廄": content_tab7,
    "斯廷法利斯湖怪鳥": content_tab8,
    "克里特公牛": content_tab9,
    "狄俄墨得斯牝馬": content_tab10,
    "亞馬遜王國": content_tab11,
    "格律翁牛群": content_tab12,
    "聖園": content_tab13,
    "冥界": content_tab14,
    "成就表": content_tab15,  # 其他 tab 可擴充
}

#custom_tab_functions = {
    #"模組簡介": content_tab1,
    #"雅典城": content_tab2,
    #"1": content_tab3,
    #"2": content_tab4,
    #"3": content_tab5,
    #"4": content_tab6,
    #"5": content_tab7,
    #"6": content_tab8,
    #"7": content_tab9,
    #"8": content_tab10,
    #"9": content_tab11,
    #"10": content_tab12,
    #"11": content_tab13,
    #"12": content_tab14,
    #"成就表": content_tab15,
    # 其他 tab 可擴充
#}

# 配對並執行每個 tab 的內容與密碼驗證
for i, (tab_title, password) in enumerate(tabs_config):
    content_func = custom_tab_functions.get(tab_title, lambda: content_default(tab_title))
    gated_content(tabs[i], password, content_func, tab_title)
