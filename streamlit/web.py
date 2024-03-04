import streamlit as st
import time

page_bg_img = '''<style>
.stApp {
    background-image: url("https://images.unsplash.com/photo-1587960184060-aa880aabdd04?q=80&w=1932&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D");
    background-size: cover;
}
</style>'''

#ส่วนรายละเอียดเว็บ main
st.markdown(page_bg_img, unsafe_allow_html=True)
st.markdown("<h1 style='color: white;text-shadow: 2px 2px 4px #000000;'>Basketball</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='color: white;'>ประวัติกีฬาบาสเกตบอลเกิดขึ้นในประเทศสหรัฐอเมริกา โดย ดร. เจมส์ ไนสมิท (Dr. James Naismith) คิดค้นกีฬาสำหรับเล่นในร่ม เพื่อให้นักกีฬาออกกำลังระหว่างช่วงฤดูหนาวปี ค.ศ.1891 ภายหลังกีฬาชนิดใหม่นี้ยกระดับจากกีฬามหาวิทยาลัย สู่ลีกอาชีพ บาสเกตบอลเป็นที่ยอมรับทั่วโลกเมื่อบรรจุในกีฬาโอลิมปิกฤดูร้อน ณ กรุงเบอร์ลิน ค.ศ.1936</h3>", unsafe_allow_html=True)
st.image("https://static.thairath.co.th/media/Dtbezn3nNUxytg04ajZ4trJVmOwXQtJMEuvTXOVgL14wBg.webp", 
         caption="James Naismith ผู้คิดค้นกีฬาบาสเกตบอล ภาพจาก springfield.edu", 
         use_column_width=True)

st.markdown("<style>div.stImage>div>div>div:nth-child(2){color: white;}</style>", unsafe_allow_html=True)

st.markdown("<h3 style='color: white;'>ผู้คิดค้นกีฬาบาสเกตบอลคือ ดร. เจมส์ ไนสมิท (Dr. James Naismith) ครูสอนพลศึกษาในสมาคมยุวชนคริสเตียนนานาชาติ International Y.M.C.A. Training School (ปัจจุบันคือส่วนหนึ่งในวิทยาลัยสปริงฟิลด์ รัฐแมสซาชูเซตส์ สหรัฐอเมริกา) เนื่องจากฤดูหนาวปี ค.ศ.1891 สภาพอากาศเป็นอุปสรรคต่อการออกกำลังกายกลางแจ้ง นักกีฬาไม่สามารถเล่นอเมริกันฟุตบอล และเบสบอลได้ ดร. เจมส์ ไนสมิท (Dr. James Naismith) พยายามคิดค้นเกมที่เข้าใจได้ง่าย แต่มีชั้นเชิงพอที่จะทำให้ทุกคนสนใจอยากเล่น สามารถเล่นเป็นทีมพร้อมกันได้หลายคน และไม่กระทบกระทั่งกันจนเสี่ยงต่อการบาดเจ็บ</h3>", unsafe_allow_html=True)
st.markdown("<h3 style='color: white;'>ดร. เจมส์ ไนสมิท จึงคิดเกมด้วยการดัดแปลงกีฬาต่างๆ เข้าด้วยกัน จนได้เกมที่ใช้ลูกบอลกับตะกร้าผลไม้เป็นอุปกรณ์ในการเล่น ด้วยการแขวนตะกร้าไว้บนผนังโรงยิม ในระดับเหนือศีรษะผู้เล่น 2 ฝั่ง และแบ่งผู้เล่นเป็น 2 ทีม ผู้เล่นต้องพยายามโยนลูกบนลงตะกร้าฝ่ายตรงข้ามให้ได้ สุดท้ายทีมที่โยนลูกบอลลงตะกร้าฝ่ายตรงข้ามได้มากที่สุดเป็นผู้ชนะ</h3>", unsafe_allow_html=True)

st.markdown("<h1 style='color: white;text-shadow: 2px 2px 4px #000000;'>เปิดเพลงเพื่ออรรถรส</h1>", unsafe_allow_html=True)
st.audio("streamlit/Lil Uzi Vert - The Way Life Goes [Official Visualizer].mp3", format="audio/mp3")


left,right = st.columns(2)

# สร้าง sidebar
st.sidebar.markdown("<h1 style='text-shadow: 2px 2px 8px rgba(0,0,0,0.5);'>Menu</h1>", unsafe_allow_html=True)


# สร้างปุ่มเพื่อเปลี่ยนหน้า
if st.sidebar.button("กติกา"):

    with st.spinner('Wait for it...'):
        time.sleep(1)

    st.markdown("<h1 style='color: white;text-shadow: 2px 2px 4px #000000;'>กติกาการแข่งขันบาสเกตบอล</h1>", unsafe_allow_html=True)

    st.markdown("<h2 style='color: white; text-shadow: 2px 2px 4px #000000;'>ผู้เล่น</h2>", unsafe_allow_html=True)
    st.markdown("<h3 style='color: white;'>ผู้เล่น มีสิทธิ์ลงแข่งขันจำนวน 12 คน รวมหัวหน้าทีม ในเวลาแข่งขัน ผู้เล่น 5 คนอยู่ในสนามแข่ง และสามารถเปลี่ยนตัวได้</h3>", unsafe_allow_html=True)


    st.markdown("<h2 style='color: white;text-shadow: 2px 2px 4px #000000;'>สนามแข่งขัน</h2>", unsafe_allow_html=True)
    st.markdown("<h3 style='color: white;'>สนามแข่งขันเป็นพื้นเรียบ กว้าง 15 เมตร ยาว 28 เมตร วัดจากขอบในของเส้นขอบสนาม</h3>", unsafe_allow_html=True)
    

    st.markdown("<h3 style='color: white;'>เส้น ตีเส้นขอบสนามด้วยสีเดียวกัน เพื่อให้เห็นได้ชัดเจน กว้าง 5 เซนติเมตร ได้แก่ เส้นเขตสนาม (Boundary Line), เส้นกลาง (Centre Line), เส้นวงกลมกลาง (Centre Circle) และเส้นครึ่งวงกลมโยนโทษ (Free-Throw Semi-Circles)</h3>", unsafe_allow_html=True)
    

    st.markdown("<h2 style='color: white;text-shadow: 2px 2px 4px #000000;'>อุปกรณ์การแข่งขัน</h2>", unsafe_allow_html=True)
    st.markdown("<h3 style='color: white;'>1. ชุดห่วงตาข่ายยึดกระดานหลัง</h3>", unsafe_allow_html=True)
    st.markdown("<h3 style='color: white;'>2. ลูกบาสเกตบอล</h3>", unsafe_allow_html=True)
    st.markdown("<h3 style='color: white;'>3. นาฬิกาแข่งขัน</h3>", unsafe_allow_html=True)
    st.markdown("<h3 style='color: white;'>4. ป้ายคะแนน</h3>", unsafe_allow_html=True)
    st.markdown("<h3 style='color: white;'>5. นาฬิกาจับเวลา 24 วินาที</h3>", unsafe_allow_html=True)
    st.markdown("<h3 style='color: white;'>6. นาฬิกาจับเวลาการแข่งขัน</h3>", unsafe_allow_html=True)
    st.markdown("<h3 style='color: white;'>7. อุปกรณ์ให้สัญญาณเสียง 2 ชุด</h3>", unsafe_allow_html=True)
    st.markdown("<h3 style='color: white;'>8. ใบบันทึกคะแนน</h3>", unsafe_allow_html=True)
    st.markdown("<h3 style='color: white;'>9. ป้ายแสดงจำนวนการฟาวล์ของผู้เล่น</h3>", unsafe_allow_html=True)
    st.markdown("<h3 style='color: white;'>10. ป้ายแสดงจำนวนการฟาวล์ของทีม</h3>", unsafe_allow_html=True)
    st.markdown("<h3 style='color: white;'>11. ลูกศรสลับการครองบอล</h3>", unsafe_allow_html=True)
    st.markdown("<h3 style='color: white;'>12. สนามแข่งขันที่มีพื้นสนาม และแสงสว่างพอเหมาะ</h3>", unsafe_allow_html=True)


    st.markdown("<h2 style='color: white;text-shadow: 2px 2px 4px #000000;'>ลูกบาสเกตบอล</h2>", unsafe_allow_html=True)
    st.markdown("<h3 style='color: white;'>ขนาดของลูกบาสเกตบอลที่สหพันธ์บาสเกตบอลนานาชาติ และสมาคมกีฬาบาสเกตบอลแห่งประเทศไทย ให้การรับรอง มีดังนี้</h3>", unsafe_allow_html=True)


    st.markdown("<h3 style='color: white;'>- ประเภททีมหญิง ใช้ลูกบาสเกตบอล ขนาดเบอร์ 6 เส้นรอบวง 724-737 มิลลิเมตร น้ำหนัก 510-567 กรัม</h3>", unsafe_allow_html=True)
    st.markdown("<h3 style='color: white;'>- ประเภททีมชาย ใช้ลูกบาสเกตบอล ขนาดเบอร์ 7 เส้นรอบวง 749-780 มิลลิเมตร น้ำหนัก 567-650 กรัม</h3>", unsafe_allow_html=True)


    st.markdown("<h2 style='color: white;text-shadow: 2px 2px 4px #000000;'>การแข่งขัน</h2>", unsafe_allow_html=True)
    st.markdown("<h3 style='color: white;'>การแข่งขันในสนามการแข่งขันผู้เล่นของทีมต้องพยายามโยนลูกเข้าห่วงภายใน 24 วินาทีขณะครองบอล และปฏิบัติตามข้อกำหนดอื่นๆ ที่ระบุในกติกา</h3>", unsafe_allow_html=True)
    

    st.markdown("<h2 style='color: white;text-shadow: 2px 2px 4px #000000;'>การนับคะแนน</h2>", unsafe_allow_html=True)
    st.markdown("<h3 style='color: white;'>- เส้นทำคะแนนระยะเส้น 3 คะแนน ได้ 3 คะแนน</h3>", unsafe_allow_html=True)
    st.markdown("<h3 style='color: white;'>- เส้นทำคะแนนระยะเส้น 2 คะแนน ได้ 2 คะแนน</h3>", unsafe_allow_html=True)
    st.markdown("<h3 style='color: white;'>- ปล่อยลูกบาสจากเขตโยนโทษ ได้ 1 คะแนน</h3>", unsafe_allow_html=True)


    st.markdown("<h2 style='color: white;text-shadow: 2px 2px 4px #000000;'>ระยะเวลาการแข่งขัน</h2>", unsafe_allow_html=True)
    st.markdown("<h3 style='color: white;'>การแข่งขันประกอบด้วย 4 ช่วงเวลา ช่วงละ 10 นาที มีช่วงพักการแข่งขัน พักครึ่ง ช่วงต่อเวลา และช่วงต่อเวลาพิเศษ โดยจะมีเสียงสัญญาณนาฬิกาจับเวลาแข่งขัน</h3>", unsafe_allow_html=True)
    st.markdown("<h3 style='color: white;'>เมื่อนับรวมช่วงเวลาต่างๆ จึงใช้เวลาแข่งขันไม่ต่ำกว่า 50 นาทีต่อหนึ่งเกม</h3>", unsafe_allow_html=True)


    st.markdown("<h2 style='color: white;text-shadow: 2px 2px 4px #000000;'>ผู้ชนะการแข่งขัน</h2>", unsafe_allow_html=True)
    st.markdown("<h3 style='color: white;'>ทีมที่ได้คะแนนมากกว่าเมื่อสิ้นสุดเวลาการแข่งขัน ถือเป็นผู้ชนะ</h3>", unsafe_allow_html=True)


    st.markdown("<h2 style='color: yellow; font-size: 16px;'>อ่านกติกาบาสเกตบอลล่าสุด 2022 ฉบับเต็ม</h2>", unsafe_allow_html=True)
    st.markdown("[อ่านที่นี่](http://www.bsatthai.org/wp-content/uploads/2022/10/%E0%B8%81%E0%B8%95%E0%B8%B4%E0%B8%81%E0%B8%B2%E0%B8%9A%E0%B8%B2%E0%B8%AA%E0%B9%80%E0%B8%81%E0%B8%95%E0%B8%9A%E0%B8%AD%E0%B8%A5-2022.pdf)")

if st.sidebar.button("NBA"):

    with st.spinner('Wait for it...'):
        time.sleep(1)

    st.markdown("<h1 style='color: white;text-shadow: 2px 2px 4px #000000;'>NBA</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='color: white;'>เอ็นบีเอ (NBA) ย่อมาจาก National Basketball Association ซึ่งเป็นชื่อของลีกบาสเกตบอลอาชีพในอเมริกาเหนือ ซึ่งรวมประเทศสหรัฐอเมริกาและแคนาดา มีนักกีฬาบาสเก็ตบอลชั้นนำของโลกเล่นอยู่ในเอ็นบีเอนี้เป็นจำนวนมาก ซึ่งทำให้มาตรฐานระดับการแข่งขันนั้นถือว่าอยู่ในระดับสูง สัญลักษณ์ประจำเอ็นบีเอทางด้านขวานั้น เป็นภาพเงาของ เจอร์รี เวสต์ ซึ่งเคยเป็นผู้จัดการทั่วไปของทีมเลเกอร์ส และทีมเมมฟิส กริซลีส์</h3>", unsafe_allow_html=True)
    st.markdown("<h3 style='color: white;'>เอ็นบีเอ ก่อตั้งขึ้นที่นครนิวยอร์ก ในวันที่ 6 มิถุนายน ค.ศ. 1946 ในชื่อ Basketball Association of America (BAA) ซึ่งต่อมาเปลี่ยนชื่อเป็น National Basketball Association ในช่วงฤดูใบไม้ร่วงในปี ค.ศ. 1949 หลังจากการรวมตัวกับทีมจาก National Basketball League (NBL)</h3>", unsafe_allow_html=True)
    st.markdown("<h3 style='color: white;'>เอ็นบีเอนั้นเป็นลีกกีฬาอาชีพแรก ที่มีโค้ชหลักเป็นคนผิวดำ ในปี ค.ศ. 1966 และก็ยังเป็นลีกแรก ที่มีผู้จัดการทั่วไปเป็นคนผิวดำ ในปี ค.ศ. 1972 นอกจากนี้แล้ว ยังเป็นลีกแรก ที่มีเจ้าของทีมเป็นคนผิวดำ ในปี ค.ศ. 200</h3>", unsafe_allow_html=True)

    st.markdown("<h1 style='color: white;text-shadow: 2px 2px 4px #000000;'>อ้างอิง</h1>", unsafe_allow_html=True)
    st.markdown("https://th.wikipedia.org/wiki/%E0%B9%80%E0%B8%AD%E0%B9%87%E0%B8%99%E0%B8%9A%E0%B8%B5%E0%B9%80%E0%B8%AD")

#Division header
st.sidebar.markdown("<h1 style='text-shadow: 2px 2px 8px rgba(0,0,0,0.5);'>Division</h1>", unsafe_allow_html=True)
st.sidebar.subheader("## ข้อมูลอัพเดตล่าสุด 2021")


if st.sidebar.button('ATLANTIC'):
            
        with st.spinner('Wait for it...'):
            time.sleep(1)

        #with st.container():
            st.markdown("<h1 style='color: red; text-shadow: 2px 2px white;'>Division ATLANTIC</h1>", unsafe_allow_html=True)
            st.markdown("<h2 style='color: #007A33;'>Boston Celtics</h2>", unsafe_allow_html=True)
            st.markdown("<p style='color: #007A33;'>บอสตัน เซลติกส์</p>", unsafe_allow_html=True)
        
        #celtics png
            celtics_png = "https://www.pngall.com/wp-content/uploads/13/Celtics-Logo-PNG-Images.png"
            st.image(celtics_png, caption='Boston Celtics Logo', width=100, use_column_width=True)

        #celtics main
            st.markdown("<p style='color: white;'>Boston Celtics เป็นทีมบาสเกตบอลมืออาชีพที่ตั้งอยู่ในเมืองบอสตัน รัฐแมสซาชูเซตส์ สหรัฐอเมริกา ทีมเริ่มต้นเข้าร่วม NBA เมื่อปี 1946 และเป็นหนึ่งในสมาชิกสมาคมบาสเกตบอลชาติสหรัฐอเมริกา (NBA) จากนั้นทีมได้รับความนิยมมากขึ้นในยุค 1960s โดยได้คว้าแชมป์ NBA ในยุคหนึ่ง และเป็นทีมที่ได้รับรางวัลแชมป์ NBA มากที่สุดในประวัติศาสตร์ โดยทั้งหมดเป็นจำนวน 17 ครั้ง</p>", unsafe_allow_html=True)
            st.markdown("""
            - **สังกัดในฝั่งตะวันออก** - <span style='color:white;'>Atlantic Division</span>
            - **ปีก่อตั้ง** - <span style='color:white;'>1946</span>
            - **ชื่อเดิม** - <span style='color:white;'>Boston Celtics (1946-ปัจจุบัน)</span>
            - **สถานที่ตั้ง** - <span style='color:white;'>เมือง Boston, รัฐ Massachusetts</span>
            - **ชื่อสนามเหย้า** - <span style='color:white;'>TD Arena</span>
            - **เจ้าของทีม** - <span style='color:white;'>Boston Basketball Partners L.L.C.</span>
            - **CEO** - <span style='color:white;'>Wyc Grousbeck</span>
            - **GM (ผู้จัดการทั่วไป)** - <span style='color:white;'>Danny Ainge</span>
            - **HC (โค้ชหลัก)** - <span style='color:white;'>Brad Stevens</span>
            - **ทีมสังกัดใน G-League** - <span style='color:white;'>Maine Red Claws</span>
            - **จำนวนครั้งที่ได้แชมป์ลีก** - <span style='color:white;'>17 (1957, 1959-1966, 1968, 1969, 1974, 1976, 1981, 1984, 1986, 2008)</span>
            - **จำนวนครั้งที่ได้แชมป์ฝั่งทวีป** - <span style='color:white;'>21 (1957-1966, 1968, 1969, 1974, 1976, 1981, 1984-1987, 2008, 2010)</span>
            - **จำนวนครั้งที่ได้แชมป์ Division** - <span style='color:white;'>22 (1972-1976, 1980-1982, 1984-1988, 1991, 1992, 2005, 2008-2012, 2017)</span>
            - **จำนวนเบอร์เสื้อที่ทำการเกษียณ** - <span style='color:white;'>23 (00, 1, 2, 3, 5, 6, 10, 14, 15, 16, 17, 18, 19, 21, 22, 23, 24, 25, 31, 32, 33, 34, 35)</span>
            """, unsafe_allow_html=True)
            st.markdown("[official website](https://www.nba.com/celtics/)")
            st.markdown("[ประวัติเต็มๆ](https://www.blockdit.com/posts/5f93175a5c8bc80cc8558642)")



            st.markdown("<h2 style='color: #000000;'>Brooklyn Nets</h2>", unsafe_allow_html=True)
            st.markdown("<p style='color: white;'>บรูคลิน เน็ตส์</p>", unsafe_allow_html=True)

        #brooklyn png
            brooklyn_png = "streamlit/pngegg.png"
            st.image(brooklyn_png, caption='Brooklyn Nets Logo', width=100, use_column_width=True)

        #brooklyn main
            st.markdown("<p style='color: white;'>Brooklyn Nets เป็นอเมริกันมืออาชีพบาสเกตบอลทีมที่อยู่ในนิวยอร์กซิตี้ ตาข่ายแข่งขันในสมาคมบาสเกตบอลแห่งชาติ (NBA) เป็นสโมสรสมาชิกของกองแอตแลนติกของการประชุมภาคตะวันออก ทีมที่เล่นเกมในบ้านของที่ Barclays ศูนย์ที่ตั้งอยู่ในเขตเลือกตั้งของบรูคลิ พวกเขาเป็นหนึ่งในสองทีมเอ็นบีเอที่ตั้งอยู่ในมหานครนิวยอร์ก; อื่น ๆ ที่เป็นนิวยอร์กนิกส์ ทีมที่ก่อตั้งขึ้นในปี 1967 ในฐานะที่เป็นแฟรนไชส์กฎบัตรของลีกเอ็นบีเอของคู่แข่งที่สมาคมบาสเกตบอลอเมริกัน (ABA) พวกเขาเป็นที่รู้จักในฐานะชาวอเมริกันในรัฐนิวเจอร์ซีย์ในช่วงฤดูกาลแรกของพวกเขาก่อนที่จะย้ายไปลองไอส์แลนด์ในปี 1968 และเปลี่ยนชื่อของพวกเขาไปนิวยอร์กตาข่าย ในช่วงเวลานี้ตาข่ายได้รับรางวัลสองประชัน ABA (ในปี 1974 และ 1976) ในปี 1976 สถาบันการเงินรวมกับเอ็นบีเอและตาข่ายถูกดูดซึมเข้าสู่เอ็นบีเอพร้อมกับสามทีม ABA อื่น ๆ (คนสเปอร์สในซานอันโตนิโอ, อินเดียนา Pacers และเดนเวอร์นักเกตทุกคนยังคงอยู่ในลีกวันนี้)</p>", unsafe_allow_html=True)
            st.markdown("""
            - **สังกัดในฝั่งตะวันออก** - <span style='color:white;'>Atlantic Division</span>
            - **ปีก่อตั้ง** - <span style='color:white;'>1967</span>
            - **ชื่อเดิม** - 
              - <span style='color:white;'>New Jersey Americans (1967-1968)</span>
              - <span style='color:white;'>New York Nets (1968-1977)</span>
              - <span style='color:white;'>New Jersey Nets (1977-2012)</span>
              - <span style='color:white;'>Brooklyn Nets (2012-ปัจจุบัน)</span>
            - **สถานที่ตั้ง** - <span style='color:white;'>เมือง Brooklyn, รัฐ New York</span>
            - **ชื่อสนามเหย้า** - <span style='color:white;'>Barclays Center</span>
            - **เจ้าของทีม** - <span style='color:white;'>Joseph Tsai</span>
            - **CEO** - <span style='color:white;'>John Abbamondi</span>
            - **GM (ผู้จัดการทั่วไป)** - <span style='color:white;'>Sean Marks</span>
            - **HC (โค้ชหลัก)** - <span style='color:white;'>Steve Nash</span>
            - **ทีมสังกัดใน G-League** - <span style='color:white;'>Long Island Nets</span>
            - **จำนวนครั้งที่ได้แชมป์ลีก** - <span style='color:white;'>2 (1974, 1976)</span>
            - **จำนวนครั้งที่ได้แชมป์ฝั่งทวีป** - <span style='color:white;'>5 (1972, 1974, 1976, 2002, 2003)</span>
            - **จำนวนครั้งที่ได้แชมป์ Division** - <span style='color:white;'>5 (1974, 2002-2004, 2006)</span>
            - **จำนวนเบอร์เสื้อที่ทำการเกษียณ** - <span style='color:white;'>6 (3, 5, 23, 25, 32, 52)</span>
            """, unsafe_allow_html=True)
        
        
            st.markdown("[official website](https://www.nba.com/nets)")
            st.markdown("[ประวัติเต็มๆ](https://www.blockdit.com/posts/5f99ac5e374f920ccb3c1122)")



            st.markdown("<h2 style='color: #006BB6;'>New York Knicks</h2>", unsafe_allow_html=True)
            st.markdown("<p style='color: white;'>นิวยอร์ก นิกส์</p>", unsafe_allow_html=True)

        #New York Knicks png
            NewYorkKnicks_png = "https://t1.blockdit.com/photos/2021/04/606efa177acd3b23d47e030a.png"
            st.image(NewYorkKnicks_png, caption='NewYorkKnicks Logo', width=100, use_column_width=True)

        #New York Knicks main
            st.markdown("<p style='color: white;'>นิวยอร์ก นิกส์ เป็นทีมบาสเกตบอลในลีกเอ็นบีเอ ในเมืองนิวยอร์ก รัฐนิวยอร์ก เล่นอยู่ในดิวิชั่นแอตแลนติกในคอนเฟอเรนส์ตะวันออก เดิมทีเล่นอยู่ในลีกบีเอเอ กระทั่งมีการรวมลีกจึงย้ายมาเล่นในเอ็นบีเอ นิวยอร์ก นิกส์ เป็นเพียงสองทีมในปัจจุบันที่ยังคงเล่นอยู่ในเมืองเดิมตั้งแต่ก่อตั้งทีม (อีกทีมคือ บอสตัน เซลติกส์)</p>", unsafe_allow_html=True)
            st.markdown("""
            - **สังกัดในฝั่งตะวันออก** - <span style='color:white;'>Atlantic Division</span>
            - **ปีที่ก่อตั้ง** - <span style='color:white;'>1946</span>
            - **ชื่อเดิม** - <span style='color:white;'>New York Knicks (1946-ปัจจุบัน)</span>
            - **สถานที่ตั้ง** - <span style='color:white;'>เมือง New York City, รัฐ New York</span>
            - **ชื่อสนามเหย้า** - <span style='color:white;'>Madison Square Garden</span>
            - **เจ้าของทีม** - <span style='color:white;'>Madison Square Garden Sports</span>
            - **CEO** - <span style='color:white;'>James L. Dolan</span>
            - **GM (ผู้จัดการทั่วไป)** - <span style='color:white;'>Scott Perry</span>
            - **HC (โค้ชหลัก)** - <span style='color:white;'>Tom Thibodeau</span>
            - **ทีมสังกัดใน G-League** - <span style='color:white;'>Westchester Knicks</span>
            - **จำนวนครั้งที่ได้แชมป์ลีก** - <span style='color:white;'>2 (1970, 1973)</span>
            - **จำนวนครั้งที่ได้แชมป์ฝั่งทวีป** - <span style='color:white;'>4 (1972-1974, 1999)</span>
            - **จำนวนครั้งที่ได้แชมป์ Division** - <span style='color:white;'>8 (1953, 1954, 1970, 1971, 1989, 1993, 1994, 2013)</span>
            - **จำนวนเบอร์เสื้อที่ทำการเกษียณ** - <span style='color:white;'>9 (10, 12, 15 (สองสิทธิ์), 19, 22, 24, 33, 613)</span>
            """, unsafe_allow_html=True)

            st.markdown("[official website](https://www.nba.com/knicks/)")
            st.markdown("[ประวัติเต็มๆ](https://www.blockdit.com/posts/606efb167acd3b23d47e518a)")



            st.markdown("<h2 style='color: #ED174C;'>Philadelphia 76ers</h2>", unsafe_allow_html=True)
            st.markdown("<p style='color: white;'>ฟิลาเดลเฟีย เซเวนตีซิกเซอร์ส</p>", unsafe_allow_html=True)

        #Philadelphia 76ers png
            Philadelphia76ers_png = "https://t1.blockdit.com/photos/2021/04/60858dbb44a4470c5620b91b.png"
            st.image(Philadelphia76ers_png, caption='Philadelphia76ers Logo', width=100, use_column_width=True)

        #Philadelphia 76ers main
            st.markdown("<p style='color: white;'>ฟิลาเดล 76ers (หรือที่เรียกกันทั่วไปว่าเป็นซิกส์) เป็นอเมริกันมืออาชีพบาสเกตบอลทีมที่อยู่ในฟิลาเดล, เพนซิล พวกเขาเล่นในมหาสมุทรแอตแลนติกของการประชุมภาคตะวันออกของสมาคมบาสเกตบอลแห่งชาติ (NBA) ก่อตั้งขึ้นในปี 1946 และเป็นที่รู้จักในฐานะเดิมซีราคิวส์ในพระบรมราชูปถัมภ์พวกเขาเป็นหนึ่งในแฟรนไชส์ที่เก่าแก่ที่สุดในเอ็นบีเอและหนึ่งในแปด (จาก 23) เพื่อความอยู่รอดทศวรรษแรกของลีก</p>", unsafe_allow_html=True)
            st.markdown("""
            - **สังกัดในฝั่งตะวันออก** - <span style='color:white;'>Atlantic Division</span>
            - **ปีที่ก่อตั้ง** - <span style='color:white;'>1946</span>
            - **ชื่อเดิม** - 
              - Syracuse Nationals (1946-1963)
              - Philadelphia 76ers (1963-ปัจจุบัน)
            - **สถานที่ตั้ง** - <span style='color:white;'>เมือง Philadelphia, รัฐ Pennsylvania</span>
            - **ชื่อสนามเหย้า** - <span style='color:white;'>Wells Fargo Center</span>
            - **เจ้าของทีม** - <span style='color:white;'>Josh Harris</span>
            - **CEO** - <span style='color:white;'>Thaddeus Brown</span>
            - **GM (ผู้จัดการทั่วไป)** - <span style='color:white;'>Elton Brand</span>
            - **HC (โค้ชหลัก)** - <span style='color:white;'>Doc Rivers</span>
            - **ทีมสังกัดใน G-League** - <span style='color:white;'>Delaware Blue Coats</span>
            - **จำนวนครั้งที่ได้แชมป์ลีก** - <span style='color:white;'>3 (1955, 1967, 1983)</span>
            - **จำนวนครั้งที่ได้แชมป์ฝั่งทวีป** - <span style='color:white;'>5 (1977, 1980, 1982, 1983, 2001)</span>
            - **จำนวนครั้งที่ได้แชมป์ Division** - <span style='color:white;'>12 (1950, 1952, 1955, 1966-1968, 1977, 1978, 1983, 1990, 2001, 2021)</span>
            - **จำนวนเบอร์เสื้อที่ทำการเกษียณ** - <span style='color:white;'>10 (2, 3, 4, 6, 10, 13, 15, 24, 32, 34)</span>
            """, unsafe_allow_html=True)

            st.markdown("[official website](https://www.nba.com/sixers/)")
            st.markdown("[ประวัติเต็มๆ](https://www.blockdit.com/posts/60858d8de187fa0c61e08d46)")



            st.markdown("<h2 style='color: #CE1141;'>Toronto Raptors</h2>", unsafe_allow_html=True)
            st.markdown("<p style='color: white;'>โทรอนโต แร็ปเตอร์ส์</p>", unsafe_allow_html=True)


        #Toronto Raptors png
            Toronto_Raptors_png = "streamlit/toronto_png.png"
            st.image(Toronto_Raptors_png, caption='Toronto Raptors Logo', width=100, use_column_width=True)

        #Toronto Raptors main
            st.markdown("<p style='color: white;'>โทรอนโต แร็ปเตอรส์ เป็นทีมบาสเกตบอลในลีกเอ็นบีเอ ในเมืองโทรอนโต รัฐออนแทรีโอ ในประเทศแคนาดา เล่นอยู่ในดิวิชั่นแอตแลนติกในคอนเฟอเรนส์ตะวันออก เป็นทีมที่ถูกเพิ่มขึ้นมาจากการขยายเอ็นบีเอเข้าไปในแคนาดาในปี ค.ศ. 1995 พร้อมกับทีมแวนคูเวอร์ กริซลีส์</p>", unsafe_allow_html=True)
            st.markdown("""
            - **Conference - สมาพันธ์** - <span style='color:white;'>Eastern</span>
            - **Division - ดิวิชั่น** - <span style='color:white;'>Atlantic</span>
            - **Founded - ก่อตั้ง** - <span style='color:white;'>1995[1]</span>
            - **History - ประวัติศาสตร์** - <span style='color:white;'>Toronto Raptors 1995–present[2][3]</span>
            - **Arena - สนามกีฬา** - <span style='color:white;'>Scotiabank Arena</span>
            - **Location - สถานที่ตั้ง** - <span style='color:white;'>Toronto, Ontario</span>
            - **Team colours - สีของทีม** - <span style='color:white;'>Red, black, purple, gold, white[4][5][6]</span>
            - **Main sponsor - ผู้สนับสนุนหลัก** - <span style='color:white;'>Sun Life Financial[7]</span>
            - **President - ประธาน** - <span style='color:white;'>Masai Ujiri</span>
            - **General manager - ผู้จัดการทั่วไป** - <span style='color:white;'>Bobby Webster</span>
            - **Head coach - หัวหน้าโค้ช** - <span style='color:white;'>Darko Rajaković</span>
            - **Ownership - การเป็นเจ้าของ** - <span style='color:white;'>Maple Leaf Sports & Entertainment[8]</span>
            - **Affiliation(s) - สังกัด** - <span style='color:white;'>Raptors 905</span>
            - **Championships - จำนวนครั้งที่ได้แชมป์** - <span style='color:white;'>1 (2019)</span>
            - **Conference titles - จำนวนครั้งที่ได้แชมป์ในสมาพันธ์** - <span style='color:white;'>1 (2019)</span>
            - **Division titles - จำนวนครั้งที่ได้แชมป์ในดิวิชั่น** - <span style='color:white;'>7 (2007, 2014, 2015, 2016, 2018, 2019, 2020)</span>
            """, unsafe_allow_html=True)

            st.markdown("[official website](https://www.nba.com/raptors/)")
            st.markdown("[ประวัติเต็มๆ](https://hmong.in.th/wiki/Toronto_Raptors)")

if st.sidebar.button('CENTRAL'):
    
    with st.spinner('Wait for it...'):
        time.sleep(1)

    # Division Central
    st.markdown("<h1 style='color: red; text-shadow: 2px 2px white;'>Division CENTRAL</h1>", unsafe_allow_html=True)

    #Chicago Bulls
    st.markdown("<font color='#CE1141'><h2>Chicago Bulls</h2></font>", unsafe_allow_html=True)
    st.markdown("<font color='white '><p>ชิคาโก บูลส์</p></font>", unsafe_allow_html=True)

    #Chicago Bull png
    chicago_Bulls_png = "streamlit/Chicago_Bulls.png"
    st.image(chicago_Bulls_png, caption='Chicago Bull Logo', width=100, use_column_width=True)

    #Chicago Bull main
    st.markdown("<p style='color: white;'>ทีมชิคาโก บูลส์ เป็นทีมบาสเกตบอลเอ็นบีเอที่ก่อตั้งขึ้นเป็นทีมที่สาม ถัดจากชิคาโก สแต็กส์ (Stags) ซึ่งเล่นระหว่างปี ค.ศ. 1946 ถึง 1950 และ ชิคาโก แพ็กเกอร์ (Packer) ซึ่งต่อมาเปลี่ยนชื่อเป็น เซไฟร์ (Zephyrs) และย้ายไปอยู่เมืองบัลติมอร์ (ปัจจุบันคือ วอชิงตัน วิซาร์ดส์) ชิคาโก บูลส์ เริ่มลงสนามในการแข่งขันบาสเกตบอลเอ็นบีเอครั้งแรก ในฤดูกาล ค.ศ. 1966-67 ซึ่งตลอดระยะเวลาในการทำการแข่งขันชิคาโก บูลส์ ก็ไม่ประสบความสำเร็จเท่าที่ควร ในช่วงกลางคริสต์ทศวรรษที่ 1970 ชิคาโก บูลส์ เป็นที่รู้จักเรื่องเกมรับที่แข็ง มีผู้เล่นมีชื่อเสียงหลายคนหลายคน เช่น บ็อบ เลิฟ (Bob Love), นอร์ม แวนเลียร์ (Norm Van Lier), เจอร์รี่ สโลน (Jerry Sloan) แต่ทีมสามารถคว้าอันดับหนึ่งในดิวิชันเพียงครั้งเดียวและไม่เคยเข้าถึงรอบไฟนอลในเพลย์ออฟได้เลย</p>", unsafe_allow_html=True)
    st.markdown("""
        - **สังกัดในฝั่งตะวันออก** - <span style='color:white;'>Central Division</span>
        - **ปีก่อตั้ง** - <span style='color:white;'>1966</span>
        - **ชื่อเดิม** - <span style='color:white;'>Chicago Bulls (1966-ปัจจุบัน)</span>
        - **สถานที่ตั้ง** - <span style='color:white;'>เมือง Chicago รัฐ Illinois</span>
        - **ชื่อสนามเหย้า** - <span style='color:white;'>United Center</span>
        - **เจ้าของทีม** - <span style='color:white;'>Jerry Reinsdorf</span>
        - **CEO** - <span style='color:white;'>Jerry Reinsdorf</span>
        - **GM (ผู้จัดการทั่วไป)** - <span style='color:white;'>Marc Eversley</span>
        - **HC (โค้ชหลัก)** - <span style='color:white;'>Billy Donovan</span>
        - **ทีมสังกัดใน G-League** - <span style='color:white;'>Windy City Bulls</span>
        - **จำนวนครั้งที่ได้แชมป์ลีก** - <span style='color:white;'>6 (1991-1993, 1996-1998)</span>
        - **จำนวนครั้งที่ได้แชมป์ฝั่งทวีป** - <span style='color:white;'>6 (1991-1993, 1996-1998)</span>
        - **จำนวนครั้งที่ได้แชมป์ Division** - <span style='color:white;'>9 (1975, 1991-1993, 1996-1998, 2011, 2012)</span>
        - **จำนวนเบอร์เสื้อที่ทำการ Retired** - <span style='color:white;'>4 (4, 10, 23, 33)</span>
        """, unsafe_allow_html=True)

    
    #chicago bulls link
    st.markdown("[official website](https://www.nba.com/bulls/)")
    st.markdown("[ประวัติเต็มๆ](https://www.blockdit.com/posts/5fb3d4291280b804e80cec8d?id=5fb3d4291280b804e80cec8d&series=5f97ea813ea0500c89ca96cd)")


    #Cleveland Cavaliers 
    st.markdown("<font color='#CE1141'><h2>Cleveland Cavaliers</h2></font>", unsafe_allow_html=True)
    st.markdown("<font color='white'><p>คลีฟแลนด์ คาวาเลียส์</p></font>", unsafe_allow_html=True)

    #Cleveland Cavaliers png
    Cleveland_Cavaliers_png = "streamlit/Cleveland Cavaliers.png"
    st.image(Cleveland_Cavaliers_png, caption='Cleveland Cavaliers Logo', width=100, use_column_width=True)

    #Cleveland Cavaliers main
    st.markdown("<p style='color: white;'>คลีฟแลนด์แควาเลียส์เป็นทีมบาสเกตบอลในลีกเอ็นบีเอ ในเมืองคลีฟแลนด์ รัฐโอไฮโอ เล่นอยู่ในดิวิชั่นภาคกลางในคอนเฟอเรนส์ตะวันออกคลีฟแลนด์แควาเลียส์ เป็นทีมที่ถูกเพิ่มขึ้นมาในปี ค.ศ. 1970 จากการขยายเอ็นบีเอ นอกจากนี้ คลีฟแลนด์แควาเลียส์ ยังเคยเป็นทีมของ เลอบรอน เจมส์ นักบาสเกตบอลเอ็นบีเอ ที่มีชื่อเสียง</p>", unsafe_allow_html=True)
    st.markdown("""
        - **สังกัดในฝั่งตะวันออก** - <span style='color:white;'>Central Division</span>
        - **ปีก่อตั้ง** - <span style='color:white;'>1970</span>
        - **ชื่อเดิม** - <span style='color:white;'>Cleveland Cavaliers (1970-ปัจจุบัน)</span>
        - **สถานที่ตั้ง** - <span style='color:white;'>เมือง Cleveland รัฐ Ohio</span>
        - **ชื่อสนามเหย้า** - <span style='color:white;'>Rocket Mortgage FieldHouse</span>
        - **เจ้าของทีม** - <span style='color:white;'>Dan Gilbert</span>
        - **CEO** - <span style='color:white;'>Len Komorovski</span>
        - **GM (ผู้จัดการทั่วไป)** - <span style='color:white;'>Koby Altman</span>
        - **HC (โค้ชหลัก)** - <span style='color:white;'>J. B. Bickerstaff</span>
        - **ทีมสังกัดใน G-League** - <span style='color:white;'>Canton Charge</span>
        - **จำนวนครั้งที่ได้แชมป์ลีก** - <span style='color:white;'>1 (2016)</span>
        - **จำนวนครั้งที่ได้แชมป์ฝั่งทวีป** - <span style='color:white;'>5 (2007, 2015-2018)</span>
        - **จำนวนครั้งที่ได้แชมป์ Division** - <span style='color:white;'>7 (1976, 2009, 2010, 2015-2018)</span>
        - **จำนวนเบอร์เสื้อที่ทำการ Retired** - <span style='color:white;'>7 (7, 11, 22, 25, 34, 42, 43)</span>
        """, unsafe_allow_html=True)
    
    #Cleveland Cavaliers link
    st.markdown("[official website](https://www.nba.com/cavaliers/)")
    st.markdown("[ประวัติเต็มๆ](https://www.blockdit.com/posts/5fc39b14e56cdd0cc63e3a3d?id=5fc39b14e56cdd0cc63e3a3d&series=5f97ea813ea0500c89ca96cd)")


    #Detroit Pistons ดีทรอยต์ พิสตันส์
    st.markdown("<font color='blue'><h2>Detroit Pistons</h2></font>", unsafe_allow_html=True)
    st.markdown("<font color='white'><p>Pistons</p></font>", unsafe_allow_html=True)

    #Detroit Pistons png
    Detroit_Pistons_png = "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c9/Logo_of_the_Detroit_Pistons.svg/1024px-Logo_of_the_Detroit_Pistons.svg.png"
    st.image(Detroit_Pistons_png, caption='Detroit Pistons Logo', width=100, use_column_width=True)

    #Detroit Pistons main
    st.markdown("<p style='color: white;'>ดีทรอยต์ พิสตันส์ , มืออาชีพชาวอเมริกัน บาสเกตบอล ทีมที่อยู่ในออเบิร์นฮิลส์, มิชิแกน , นอกเมืองดีทรอยต์ Pistons ได้รับรางวัลสมาคมบาสเกตบอลแห่งชาติ (NBA) สามครั้ง (1989, 1990, 2004) ก่อตั้งขึ้นในปี 1941 ในชื่อ Zollner Pistons (ตั้งชื่อตามเจ้าของทีมและผู้ผลิตชิ้นส่วนรถยนต์ Fred Zollner) และตั้งอยู่ในเมืองฟอร์ตเวย์น รัฐอินเดียน่า เดิมทีม Pistons เล่นใน National Basketball League (NBL) ซึ่งพวกเขาได้แชมป์ลีกสองสมัย (1944– 45). Pistons เข้าร่วมสมาคมบาสเกตบอลแห่งอเมริกา (BAA) สำหรับฤดูกาล 1948–49 ซึ่งทำให้ Zollner หลุดพ้นจากชื่อของพวกเขา และพวกเขาก็กลายเป็นส่วนหนึ่งของ NBA ในปี 1949 เมื่อลีกถูกสร้างขึ้นจากการควบรวมกิจการของ BAA และ NBL Pistons เข้าสู่รอบชิงชนะเลิศ NBA ในปี 1955 และ 1956 แต่แพ้ในแต่ละโอกาส</p>", unsafe_allow_html=True)
    st.markdown("""
        - **สังกัดในฝั่งตะวันออก** - <span style='color:white;'>Central Division</span>
        - **ปีก่อตั้ง** - <span style='color:white;'>1941</span>
        - **ชื่อเดิม** - <span style='color:white;'>Fort Wayne Zoliner Pistons (1941-1948)<br>Fort Wayne Pistons (1948-1957)<br>Detroit Pistons (1957-ปัจจุบัน)</span>
        - **สถานที่ตั้ง** - <span style='color:white;'>เมือง Detroit รัฐ Michigan</span>
        - **ชื่อสนามเหย้า** - <span style='color:white;'>Little Caesars Arena</span>
        - **เจ้าของทีม** - <span style='color:white;'>Tom Gores</span>
        - **CEO** - <span style='color:white;'>Tom Gores</span>
        - **GM (ผู้จัดการทั่วไป)** - <span style='color:white;'>Troy Weaver</span>
        - **HC (โค้ชหลัก)** - <span style='color:white;'>Dwane Casey</span>
        - **ทีมสังกัดใน G-League** - <span style='color:white;'>Grand Rapids Drive</span>
        - **จำนวนครั้งที่ได้แชมป์ลีก** - <span style='color:white;'>3 (1989, 1990, 2004)</span>
        - **จำนวนครั้งที่ได้แชมป์ฝั่งทวีป** - <span style='color:white;'>5 (1988-1990, 2004, 2005)</span>
        - **จำนวนครั้งที่ได้แชมป์ Division** - <span style='color:white;'>11 (1955, 1956, 1988-1990, 2002, 2003, 2005-2008)</span>
        - **จำนวนเบอร์เสื้อที่ทำการ Retired** - <span style='color:white;'>11 (1, 2, 3, 4, 10, 11, 15, 16, 21, 32, 40)</span>
        """, unsafe_allow_html=True)

    #Detroit Pistons link
    st.markdown("[official website](https://www.nba.com/pistons/)")
    st.markdown("[ประวัติเต็มๆ](https://www.blockdit.com/posts/5fee0d679ef9150cd43b0a3f)")


    #Indiana Pacers อินเดียนา เพเซอร์ส
    st.markdown("<font color='yellow'><h2>Indiana Pacers</h2></font>", unsafe_allow_html=True)
    st.markdown("<font color='white'><p>อินเดียนา เพเซอร์ส</p></font>", unsafe_allow_html=True)

    #Indiana Pacers png
    Indiana_Pacers_png = "https://upload.wikimedia.org/wikipedia/en/thumb/1/1b/Indiana_Pacers.svg/1024px-Indiana_Pacers.svg.png"
    st.image(Indiana_Pacers_png, caption='Indiana Pacers Logo', width=100, use_column_width=True)

    #Indiana Pacers main
    st.markdown("<p style='color: white;'>Indiana Pacers เป็นมืออาชีพบาสเกตบอลทีมที่อยู่ในอินเดียแนโพลิ พวกเขาเป็นสมาชิกของภาคกลางในการประชุมภาคตะวันออกของสมาคมบาสเกตบอลแห่งชาติ (NBA) Pacers ถูกก่อตั้งขึ้นครั้งแรกในปี 1967 ในฐานะสมาชิกของสมาคมบาสเกตบอลอเมริกัน (ABA) และกลายเป็นสมาชิกของเอ็นบีเอในปี 1976 เป็นผลมาจากการควบรวมกิจการสดเอ็นบีเอ พวกเขาเล่นเกมในบ้านของพวกเขาที่ธนาคารชีวิตเฮาส์ ทีมที่เป็นที่ตั้งชื่อตามชื่ออินดีแอนา’ประวัติศาสตร์กับอินเดียนาโปลิส 500 ของก้าวรถยนต์และมีแข่งอุตสาหกรรม. Pacers ได้รับรางวัลสามประชันทั้งหมดในสถาบันการเงิน Pacers เป็นตัวแทนประชุมทางทิศตะวันออกใน2000 ทีมที่ได้รับรางวัลแปดชื่อส่วน ห้าฮอลล์ออฟเฟมผู้เล่น- เรกกีมิลเลอร์, คริสมัลลิน, อเล็กซ์ภาษาอังกฤษ, เมลแดเนียลส์และโรเจอร์บราวน์ -. เล่นกับ Pacers สำหรับหลายฤดูกาล</p>", unsafe_allow_html=True)
    st.markdown("""
        - **สังกัดในฝั่งตะวันออก** - <span style='color:white;'>Central Division</span>
        - **ปีก่อตั้ง** - <span style='color:white;'>1967</span>
        - **ชื่อเดิม** - <span style='color:white;'>Indiana Pacers (1967-ปัจจุบัน)</span>
        - **สถานที่ตั้ง** - <span style='color:white;'>เมือง Indianapolis รัฐ Indiana</span>
        - **ชื่อสนามเหย้า** - <span style='color:white;'>Bankers Life Fieldhouse</span>
        - **เจ้าของทีม** - <span style='color:white;'>Herbert Simon</span>
        - **CEO** - <span style='color:white;'>Kevin Lee Pritchard</span>
        - **GM (ผู้จัดการทั่วไป)** - <span style='color:white;'>Chad Buchanan</span>
        - **HC (โค้ชหลัก)** - <span style='color:white;'>Nate Bjorkgren</span>
        - **ทีมสังกัดใน G-League** - <span style='color:white;'>Fort Wayne Mad Ants</span>
        - **จำนวนครั้งที่ได้แชมป์ลีก** - <span style='color:white;'>3 (1970, 1972, 1973)</span>
        - **จำนวนครั้งที่ได้แชมป์ฝั่งทวีป** - <span style='color:white;'>1 (2000)</span>
        - **จำนวนครั้งที่ได้แชมป์ Division** - <span style='color:white;'>9 (1969-1971, 1995, 1999, 2000, 2004, 2013, 2014)</span>
        - **จำนวนเบอร์เสื้อที่ทำการ Retired** - <span style='color:white;'>5 (30, 31, 34, 35, 529)</span>
        """, unsafe_allow_html=True)

    #Indiana Pacers link
    st.markdown("[official website](https://www.nba.com/pacers/)")
    st.markdown("[ประวัติเต็มๆ](https://www.blockdit.com/posts/6005b3c5f293341b7adc5cff?id=6005b3c5f293341b7adc5cff&series=5f97ea813ea0500c89ca96cd)")


    #Milwaukee Bucks มิลวอกี บักส์
    st.markdown("<font color='green'><h2>Milwaukee Bucks</h2></font>", unsafe_allow_html=True)
    st.markdown("<font color='white'><p>มิลวอกี บักส์</p></font>", unsafe_allow_html=True)

    #Milwaukee Bucks png
    Milwaukee_Bucks_png = "https://upload.wikimedia.org/wikipedia/en/thumb/4/4a/Milwaukee_Bucks_logo.svg/800px-Milwaukee_Bucks_logo.svg.png"
    st.image(Milwaukee_Bucks_png, caption='Milwaukee Bucks Logo', width=100, use_column_width=True)

    #Milwaukee Bucks main
    st.markdown("<p style='color: white;'>มิลวอกี บักส์ เป็นทีมบาสเกตบอลในลีกเอ็นบีเอ ในเมืองมิลวอกี รัฐวิสคอนซิน เล่นอยู่ในดิวิชั่นภาคกลางในคอนเฟอเรนส์ตะวันออกBucks มิลวอกีเป็นชาวอเมริกันมืออาชีพบาสเกตบอลแฟรนไชส์ที่อยู่ในมิลวอกีรัฐวิสคอนซิน เหรียญในการแข่งขันในสมาคมบาสเกตบอลแห่งชาติ (NBA) เป็นทีมสมาชิกของการประชุมภาคตะวันออกภาคกลาง ทีมที่ก่อตั้งขึ้นในปี 1968 เป็นขยายตัวของทีมและเล่นที่  BMO แฮร์ริสแบรดลีย์ศูนย์ อดีตวุฒิสมาชิกสหรัฐสมุนไพรตาเป็นเจ้าของเป็นเวลานานของทีมงานที่มีจอห์นแฮมมอนด์เป็นผู้จัดการทั่วไปในปัจจุบัน ณ วันที่ 16 เมษายน 2014 กลุ่มที่นำโดยมหาเศรษฐีกองทุนป้องกันความเสี่ยงผู้จัดการเวสลีย์Edens และมาร์ค Lasry ตกลงที่จะซื้อส่วนใหญ่สนใจในทีมจากตา, การขายที่ได้รับการอนุมัติโดยเจ้าของของเอ็นบีเอและคณะของผู้ปกครองเดือนต่อมาเป็น เมื่อวันที่ 16 พฤษภาคม   ทีมปัจจุบันมีมูลค่า$ 600,000,000 ตามฟอร์บ, การจัดอันดับล่าสุดในลีก</p>", unsafe_allow_html=True)
    st.markdown("""
        - **สังกัดในฝั่งตะวันออก** - <span style='color:white;'>Central Division</span>
        - **ปีก่อตั้ง** - <span style='color:white;'>1968</span>
        - **ชื่อเดิม** - <span style='color:white;'>Milwaukee Bucks (1968-ปัจจุบัน)</span>
        - **สถานที่ตั้ง** - <span style='color:white;'>เมือง Milwaukee รัฐ Wisconsin</span>
        - **ชื่อสนามเหย้า** - <span style='color:white;'>Fiserv Forum</span>
        - **เจ้าของทีม** - <span style='color:white;'>Wes Edens, Marc Lasry, Jamie Dinan, Mike Fascitelli</span>
        - **CEO** - <span style='color:white;'>Marc Lasry</span>
        - **GM (ผู้จัดการทั่วไป)** - <span style='color:white;'>Jon Horst</span>
        - **HC (โค้ชหลัก)** - <span style='color:white;'>Mike Budenholzer</span>
        - **ทีมสังกัดใน G-League** - <span style='color:white;'>Wisconsin Herd</span>
        - **จำนวนครั้งที่ได้แชมป์ลีก** - <span style='color:white;'>1 (1971)</span>
        - **จำนวนครั้งที่ได้แชมป์ฝั่งทวีป** - <span style='color:white;'>2 (1971, 1974)</span>
        - **จำนวนครั้งที่ได้แชมป์ Division** - <span style='color:white;'>15 (1971-1974, 1976, 1980-1986, 2001, 2019, 2020)</span>
        - **จำนวนเบอร์เสื้อที่ทำการ Retired** - <span style='color:white;'>9 (1, 2, 4, 8, 10, 14, 16, 32, 33)</span>
        """, unsafe_allow_html=True)
    
    #Milwaukee Bucks link
    st.markdown("[official website](https://www.nba.com/bucks/)")
    st.markdown("[ประวัติเต็มๆ](https://www.blockdit.com/posts/604db63441e0820c0d346544?id=604db63441e0820c0d346544&series=5f97ea813ea0500c89ca96cd)")

if st.sidebar.button('SOUTHEAST'):
      
    with st.spinner('Wait for it...'):
        time.sleep(1)

    # Division SOUTHEAST
    st.markdown("<h1 style='color: red; text-shadow: 2px 2px white;'>Division SOUTHEAST</h1>", unsafe_allow_html=True)

    #Atlanta Hawks แอตแลนตา ฮอกส์
    st.markdown("<font color='red'><h2>Atlanta Hawks</h2></font>", unsafe_allow_html=True)
    st.markdown("<font color='white '><p>แอตแลนตา ฮอกส์</p></font>", unsafe_allow_html=True)

    #Atlanta Hawks png
    Atlanta_Hawks_png = "https://upload.wikimedia.org/wikipedia/en/thumb/2/24/Atlanta_Hawks_logo.svg/1024px-Atlanta_Hawks_logo.svg.png"
    st.image(Atlanta_Hawks_png, caption='Atlanta Hawks Logo', width=100, use_column_width=True)

    #Atlanta Hawks main
    st.markdown("<p style='color: white;'>เดิมทีทีมแอตแลนตา ฮอกส์ ไม่ได้ตั้งอยู่ที่ แอตแลนต้า ทีมนี้ถูกก่อตั้งในปี ค.ศ. 1946 ภายในเขตเมือง 3 เมืองติดกัน(ไทร-ซิตี้)ของเมือง ดาเวนพอร์ท (รัฐไอโอวา) และเมืองโมลีนกับเมืองร็อคไอส์แลนด์ (รัฐอิลลินอยส์) โดยใช้ชื่อว่า ไทร-ซิตี้ แบลคฮอกส์ ก่อนที่จะย้ายไปเมืองมิลวอกี ใน ค.ศ. 1951 โดยเปลี่ยนชื่อจาก แบล็คฮอกส์ ไปเป็น ฮอกส์ และก็ย้ายไปอยู่ที่ เซนต์หลุยส์ ในปี ค.ศ. 1955 ก่อนจะย้ายไปอยู่ที่เมือง แอตแลนต้า ในปัจจุบันตั้งแต่ปี ค.ศ. 1968-ปัจจุบัน</p>", unsafe_allow_html=True)
    st.markdown("""
        - **สังกัดในฝั่งตะวันออก** - <span style='color:white;'>Southeast Division</span>
        - **ปีก่อตั้ง** - <span style='color:white;'>1946</span>
        - **ชื่อเดิม** - <span style='color:white;'>Buffalo Bisons (1946)<br>Tri-Cities Blackhawks (1946-1951)<br>Milwaukee Hawks (1951-1955)<br>St.Louis Hawks (1955-1968)</span>
        - **สถานที่ตั้ง** - <span style='color:white;'>เมือง Atlanta รัฐ Georgia</span>
        - **ชื่อสนามเหย้า** - <span style='color:white;'>State Farm Arena</span>
        - **เจ้าของทีม** - <span style='color:white;'>Tony Ressler</span>
        - **CEO** - <span style='color:white;'>Steve Koonin</span>
        - **GM (ผู้จัดการทั่วไป)** - <span style='color:white;'>Travis Schlenk</span>
        - **HC (โค้ชหลัก)** - <span style='color:white;'>Lloyd Pierce</span>
        - **ทีมสังกัดใน G-League** - <span style='color:white;'>College Park Skyhawks</span>
        - **จำนวนครั้งที่ได้แชมป์ลีก** - <span style='color:white;'>1 (1958)</span>
        - **จำนวนครั้งที่ได้แชมป์ฝั่งทวีป** - <span style='color:white;'>4 (1957, 1958, 1960, 1961)</span>
        - **จำนวนครั้งที่ได้แชมป์ Division** - <span style='color:white;'>5 (1970, 1980, 1987, 1994, 2015)</span>
        - **จำนวนเบอร์เสื้อที่ทำการ Retired** - <span style='color:white;'>6 (9, 21, 23, 44, 55, 59)</span>
        """, unsafe_allow_html=True)
    
    #Atlanta Hawks link
    st.markdown("[official website](https://www.nba.com/hawks/)")
    st.markdown("[ประวัติเต็มๆ](https://www.blockdit.com/posts/5f910d229b6ebe27e2b5d8b7?id=5f910d229b6ebe27e2b5d8b7&series=5f97ea813ea0500c89ca96cd)")

    #Charlotte Hornets ชาล็อต ฮอร์เน็ตส์
    st.markdown("<font color='light blue'><h2>Charlotte Hornets</h2></font>", unsafe_allow_html=True)
    st.markdown("<font color='white '><p>ชาล็อต ฮอร์เน็ตส์</p></font>", unsafe_allow_html=True)

    #Charlotte Hornets png
    Charlotte_Hornets_png = "https://upload.wikimedia.org/wikipedia/en/thumb/c/c4/Charlotte_Hornets_%282014%29.svg/1024px-Charlotte_Hornets_%282014%29.svg.png"
    st.image(Charlotte_Hornets_png, caption='Charlotte Hornets Logo', width=100, use_column_width=True)

    #Charlotte Hornets main
    st.markdown("<p style='color: white;'>เมื่อทีมชาล็อตฮอร์เนตส์ย้ายไปที่เมืองนิวออลีนส์ เมืองชาล็อตและลีกเอ็นบีเอตกลงที่จะสร้างทีมใหม่ในชาล็อตในฤดูกาล 2004-05 มีหลายกลุ่มรวมทั้งอดีตนักกีฬาชื่อดังจากทีมบอสตัน เซลติกส์ ลาร์รี เบิร์ด ก็เข้าเสนอตัว สุดท้ายกลุ่มที่นำโดยเศรษฐีพันล้าน โรเบิร์ต แอล จอห์นสัน จากธุรกิจเคเบิลทีวีสถานี BET (Black Entertainment TV) ก็ได้ชัยชนะ ชื่อบ็อบแคทส์ก็มาจาก จอห์นสัน เพราะ บ็อบ เป็นชื่อเล่นของโรเบิร์ตเอ็นบีเอจัดให้บ็อบแคทส์คัดตัวผู้เล่นจากทีมอื่น ๆ หรือที่เรียกกันว่า expansion draft เมื่อ 22 มิถุนายน ค.ศ. 2004 (พ.ศ. 2547) ได้ผู้เล่นอายุน้อยที่มีพรสวรรค์เช่น เจอรัล วอลเลส (Gerald Wallace) และยังได้ดราฟผู้เล่น เอเมกา โอกาฟอร์ (Emeka Okafor) ซึ่งได้รางวัลผู้เล่นหน้าใหม่ยอดเยี่ยมแห่งปีเมื่อหมดฤดูกาลแรกเกมแรกที่แข่งของทีม ผลปรากฏว่าแพ้วอชิงตัน วิซารดส์ ด้วยคะแนน 96 ต่อ 103 ในวันที่ 4 พฤศจิกายน ค.ศ. 2004 บ็อบแคทส์ชนะครั้งแรกในประวัติศาสตร์ของแฟรนไชส์ด้วยคะแนน 111 ต่อ 100 กับทีมออร์แลนโดแมจิกส่วนปี ค.ศ. 2005 ได้ดราฟ เรย์มอน เฟลตัน (Raymond Felton) ฌอน เมย์ (Sean May) บ็อบแคทส์ตั้งความหวังกับผู้เล่นเหล่านี้ รวมไปถึงโอกาฟอร์ ว่าจะเป็นรากฐานของความสำเร็จในอนาคต</p>", unsafe_allow_html=True)
    st.markdown("""
        - **สังกัดในฝั่งตะวันออก** - <span style='color:white;'>Southeast Division</span>
        - **ปีก่อตั้ง** - <span style='color:white;'>1988</span>
        - **ชื่อเดิม** - <span style='color:white;'>Charlotte Hornets (1988-2002 และ 2014-ปัจจุบัน)<br>Charlotte Bobcats (2004-2014)</span>
        - **สถานที่ตั้ง** - <span style='color:white;'>เมือง Charlotte รัฐ North Carolina</span>
        - **ชื่อสนามเหย้า** - <span style='color:white;'>Spectrum Center</span>
        - **เจ้าของทีม** - <span style='color:white;'>Michael Jordan</span>
        - **CEO** - <span style='color:white;'>Mitch Kupchak</span>
        - **GM (ผู้จัดการทั่วไป)** - <span style='color:white;'>Mitch Kupchak</span>
        - **HC (โค้ชหลัก)** - <span style='color:white;'>James Borrego</span>
        - **ทีมสังกัดใน G-League** - <span style='color:white;'>Greensboro Swarm</span>
        - **จำนวนครั้งที่ได้แชมป์ลีก** - <span style='color:white;'>0</span>
        - **จำนวนครั้งที่ได้แชมป์ฝั่งทวีป** - <span style='color:white;'>0</span>
        - **จำนวนครั้งที่ได้แชมป์ Division** - <span style='color:white;'>0</span>
        - **จำนวนเบอร์เสื้อที่ทำการ Retired** - <span style='color:white;'>1 (13)</span>
        """, unsafe_allow_html=True)
    
    #Charlotte Hornets link
    st.markdown("[official website](https://www.nba.com/hornets/)")
    st.markdown("[ประวัติเต็มๆ](https://www.blockdit.com/posts/5fa5650cb4bdac09901ee8b0?id=5fa5650cb4bdac09901ee8b0&series=5f97ea813ea0500c89ca96cd)")


    #Miami Heat ไมอามี ฮีท
    st.markdown("<font color='red'><h2>Miami Heat</h2></font>", unsafe_allow_html=True)
    st.markdown("<font color='white '><p>ไมอามี ฮีท</p></font>", unsafe_allow_html=True)

    #Miami Heat png
    Miami_Heat_png = "https://upload.wikimedia.org/wikipedia/en/thumb/f/fb/Miami_Heat_logo.svg/800px-Miami_Heat_logo.svg.png"
    st.image(Miami_Heat_png, caption='Miami Heat Logo', width=100, use_column_width=True)

    #Miami Heat main
    st.markdown("<p style='color: white;'>ไมอามี่เป็นอเมริกันทีมบาสเกตบอลมืออาชีพที่อยู่ในไมอามี่ ฟลอริด้า ทีมนี้เป็นสมาชิกของกองตะวันออกเฉียงใต้ในการประชุมภาคตะวันออกของสมาคมบาสเกตบอลแห่งชาติ (NBA) พวกเขาเล่นเกมในบ้านของพวกเขาที่อเมริกันแอร์ไลน์อารีน่าในเมืองไมอามี เจ้าของทีมคือมิกกี้ Arison ที่ยังเป็นเจ้าของยักษ์ล่องเรือเรือCarnival คอร์ปอเรชั่น ประธานทีมและพฤตินัยผู้จัดการทั่วไปเป็นแพทไรลีย์และหัวหน้าโค้ชเป็นErik Spoelstra มิ่งขวัญของทีมเป็นเบอร์นีเป็นลูกไฟมนุษย์ที่เกิดขึ้นในปี 1988 เป็นหนึ่งในสี่ของเอ็นบีเอแฟรนไชส์การขยายตัวของความร้อนที่ได้รับรางวัลสามประชันลีก (ใน2006, 2012และ2013) ห้าชื่อการประชุมและ 11 ชื่อส่วน จาก 3 กุมภาพันธ์ – 27 มีนาคม 2013, ความร้อนได้รับรางวัล 27 เกมในแถวแนวที่สองที่ยาวที่สุดในประวัติศาสตร์เอ็นบีเอ (หลัง1971-1972 Los Angeles Lakers ‘ชนะ 33) ในปี 2013 ฟอร์บมูลค่าความร้อนที่ $ 625,000,000, หกมากที่สุดที่มีคุณค่าของแฟรนไชส์เอ็นบีเอความร้อนจะไม่เกี่ยวข้องกับไมอามี่ Floridians เป็น ABA ทีมในต้นปี 1970 แม้ว่าความร้อนได้จ่ายเงินเป็นครั้งคราวส่วยให้แฟรนไชส์ที่มีอายุมากกว่าโดยการสวมใส่รุ่นแบบจำลองของเครื่องแบบ Floridians ‘สำหรับเอ็นบีเอ “คลาสสิกจากไม้เนื้อแข็งคืน” ในช่วงปี 2005 -06 และฤดูกาล 2011-12</p>", unsafe_allow_html=True)
    st.markdown("""
        - **สังกัดในฝั่งตะวันออก** - <span style='color:white;'>Southeast Division</span>
        - **ปีก่อตั้ง** - <span style='color:white;'>1988</span>
        - **ชื่อเดิม** - <span style='color:white;'>Miami Heat (1988-ปัจจุบัน)</span>
        - **สถานที่ตั้ง** - <span style='color:white;'>เมือง Miami รัฐ Florida</span>
        - **ชื่อสนามเหย้า** - <span style='color:white;'>American Airlines Arena</span>
        - **เจ้าของทีม** - <span style='color:white;'>Micky Arison</span>
        - **CEO** - <span style='color:white;'>Nick Arison</span>
        - **GM (ผู้จัดการทั่วไป)** - <span style='color:white;'>Andy Elisburg</span>
        - **HC (โค้ชหลัก)** - <span style='color:white;'>Erik Spoelstra</span>
        - **ทีมสังกัดใน G-League** - <span style='color:white;'>Sioux Falls Skyforce</span>
        - **จำนวนครั้งที่ได้แชมป์ลีก** - <span style='color:white;'>3 (2006, 2012, 2013)</span>
        - **จำนวนครั้งที่ได้แชมป์ฝั่งทวีป** - <span style='color:white;'>6 (2006, 2011-2014, 2020)</span>
        - **จำนวนครั้งที่ได้แชมป์ Division** - <span style='color:white;'>14 (1997-2000, 2005-2007, 2011-2014, 2016, 2018, 2020)</span>
        - **จำนวนเบอร์เสื้อที่ทำการ Retired** - <span style='color:white;'>6 (1, 3, 10, 23, 32, 33)</span>
        """, unsafe_allow_html=True)
    
    #Miami Heat link
    st.markdown("[official website](https://www.nba.com/heat)")
    st.markdown("[ประวัติเต็มๆ](https://www.blockdit.com/posts/6029293d7acb770bc14a81d6?id=6029293d7acb770bc14a81d6&series=5f97ea813ea0500c89ca96cd)")


    #Orlando Magic ออร์แลนโด แมจิก
    st.markdown("<font color='blue'><h2>Orlando Magic</h2></font>", unsafe_allow_html=True)
    st.markdown("<font color='white '><p>ออร์แลนโด แมจิก</p></font>", unsafe_allow_html=True)
    
    #Orlando Magic png
    Orlando_Magic_png = "https://upload.wikimedia.org/wikipedia/en/thumb/1/10/Orlando_Magic_logo.svg/1280px-Orlando_Magic_logo.svg.png"
    st.image(Orlando_Magic_png, caption='Orlando Magic Logo', width=100, use_column_width=True)

    #Orlando Magic main
    st.markdown("<p style='color: white;'>ออร์แลนโดเมจิกเป็นอเมริกันมืออาชีพบาสเกตบอลทีมอยู่ในออร์แลนโด, ฟลอริด้า ในการแข่งขันเมจิกในสมาคมบาสเกตบอลแห่งชาติ (NBA) เป็นสมาชิกของลีกประชุมทางทิศตะวันออก ส่วนตะวันออกเฉียงใต้ แฟรนไชส์ก่อตั้งขึ้นในปี 1989 เป็นขยายตัวของแฟรนไชส์และเช่นดาวเอ็นบีเอที่โดดเด่นเป็นShaquille O'Neal , Penny Hardaway , แกรนท์ฮิลล์ , เทรซี่สำเร็จสูงสุดและไวต์โฮเวิร์ดได้เล่นให้กับสโมสรตลอดประวัติศาสตร์หนุ่ม ในปี 2020 แฟรนไชส์ได้เล่นในรอบตัดเชือกของ NBA16 ครั้งใน 31 ฤดูกาลและครั้งที่สองไปที่เอ็นบีเอรอบชิงชนะเลิศใน1995และ2009 ออร์แลนโดเป็นทีมที่ประสบความสำเร็จมากที่สุดเป็นอันดับสองจากสี่ทีมเสริมที่นำเข้ามาในลีกในปี 1988 และ 1989 ในแง่ของเปอร์เซ็นต์การชนะ ต่อจากไมอามี่ ฮีตเท่านั้น</p>", unsafe_allow_html=True)
    st.markdown("""
        - **สังกัดในฝั่งตะวันออก** - <span style='color:white;'>Southeast Division</span>
        - **ปีก่อตั้ง** - <span style='color:white;'>1989</span>
        - **ชื่อเดิม** - <span style='color:white;'>Orlando Magic (1989-ปัจจุบัน)</span>
        - **สถานที่ตั้ง** - <span style='color:white;'>เมือง Orlando รัฐ Florida</span>
        - **ชื่อสนามเหย้า** - <span style='color:white;'>Amway Center</span>
        - **เจ้าของทีม** - <span style='color:white;'>RDV Sports, Inc.</span>
        - **CEO** - <span style='color:white;'>Alex Martins</span>
        - **GM (ผู้จัดการทั่วไป)** - <span style='color:white;'>John Hammond</span>
        - **HC (โค้ชหลัก)** - <span style='color:white;'>Jamahl Mosley</span>
        - **ทีมสังกัดใน G-League** - <span style='color:white;'>Lakeland Magic</span>
        - **จำนวนครั้งที่ได้แชมป์ลีก** - <span style='color:white;'>0</span>
        - **จำนวนครั้งที่ได้แชมป์ฝั่งทวีป** - <span style='color:white;'>2 (1995, 2009)</span>
        - **จำนวนครั้งที่ได้แชมป์ Division** - <span style='color:white;'>6 (1995, 1996, 2008-2010, 2019)</span>
        - **จำนวนเบอร์เสื้อที่ทำการ Retired** - <span style='color:white;'>1 (6)</span>
        """, unsafe_allow_html=True)

    #Orlando Magic link
    st.markdown("[official website](https://www.nba.com/team/1610612753/magic)")
    st.markdown("[ประวัติเต็มๆ](https://www.blockdit.com/posts/60804c7ab844e139af49879b?id=60804c7ab844e139af49879b&series=5f97ea813ea0500c89ca96cd)")


    #Washington Wizards วอชิงตัน วิซาร์ดส์
    st.markdown("<font color='blue'><h2>Washington Wizards</h2></font>", unsafe_allow_html=True)
    st.markdown("<font color='white '><p>วอชิงตัน วิซาร์ดส์</p></font>", unsafe_allow_html=True)

    #Washington Wizards png
    Washington_Wizards_png = "https://upload.wikimedia.org/wikipedia/en/thumb/0/02/Washington_Wizards_logo.svg/1024px-Washington_Wizards_logo.svg.png"
    st.image(Washington_Wizards_png, caption='Washington Wizards Logo', width=100, use_column_width=True)

    #Washington Wizards main
    st.markdown("<p style='color: white;'>วอชิงตัน วิซาร์ดส์ (Washington Wizards) สโมสรกีฬาบาสเกตบอลมืออาชีพซึ่งตั้งอยู่ในกรุงวอชิงตันดีซี แข่งขันในระดับ National Basketball Association (NBA) เป็นกลุ่มสมาชิกในตะวันออก ส่วนตะวันออกเฉียงเหนือ สนามแข่งคือ Capital One Arena ( แคปปิตตอล วัน อารีน่า ) ซึ่งอยู่ในย่านไชน่าทาวน์ของวอชิงตันดีซี ของสหรัฐอเมริกา</p>", unsafe_allow_html=True)
    st.markdown("""
        - **สังกัดในฝั่งตะวันออก** - <span style='color:white;'>Southeast Division</span>
        - **ปีก่อตั้ง** - <span style='color:white;'>1961</span>
        - **ชื่อเดิม** - <span style='color:white;'>Washington Wizards (1961-ปัจจุบัน)</span>
        - **สถานที่ตั้ง** - <span style='color:white;'>เมือง Washington รัฐ Washington, D.C.</span>
        - **ชื่อสนามเหย้า** - <span style='color:white;'>Capital One Arena</span>
        - **เจ้าของทีม** - <span style='color:white;'>Monumental Sports & Entertainment (Ted Leonsis, Chairman/CEO)</span>
        - **CEO** - <span style='color:white;'>Ted Leonsis</span>
        - **GM (ผู้จัดการทั่วไป)** - <span style='color:white;'>Will Dawkins</span>
        - **HC (โค้ชหลัก)** - <span style='color:white;'>Tristan Vukcevic</span>
        - **ทีมสังกัดใน G-League** - <span style='color:white;'>The Capital City Go-Go</span>
        - **จำนวนครั้งที่ได้แชมป์ลีก** - <span style='color:white;'>1</span>
        - **จำนวนครั้งที่ได้แชมป์ฝั่งทวีป** - <span style='color:white;'>1 (1978)</span>
        - **จำนวนครั้งที่ได้แชมป์ Division** - <span style='color:white;'>	8 (1969,1971,1972,1973,1974,1975,1979,2017)</span>
        - **จำนวนเบอร์เสื้อที่ทำการ Retired** - <span style='color:white;'>5 (10,11,25,41,45)</span>
        """, unsafe_allow_html=True)

    #Washington Wizards link
    st.markdown("[official website](https://www.nba.com/wizards/)")
    st.markdown("[ประวัติเต็มๆ](https://www.databet.wiki/%E0%B8%A7%E0%B8%AD%E0%B8%8A%E0%B8%B4%E0%B8%87%E0%B8%95%E0%B8%B1%E0%B8%99-%E0%B8%A7%E0%B8%B4%E0%B8%8B%E0%B8%B2%E0%B8%A3%E0%B9%8C%E0%B8%94%E0%B8%AA%E0%B9%8C/)")

if st.sidebar.button('NORTHWEST'):

    with st.spinner('Wait for it...'):
        time.sleep(1)

    # Division NORTHWEST
    st.markdown("<h1 style='color: red; text-shadow: 2px 2px white;'>Division NORTHWEST</h1>", unsafe_allow_html=True)

    #Denver Nuggets เดนเวอร์ นักเก็ตส์
    st.markdown("<font color='yellow'><h2>Denver Nuggets</h2></font>", unsafe_allow_html=True)
    st.markdown("<font color='blue '><p>เดนเวอร์ นักเก็ตส์</p></font>", unsafe_allow_html=True)

    #Denver Nuggets png
    Denver_Nuggets_png = "https://upload.wikimedia.org/wikipedia/en/thumb/7/76/Denver_Nuggets.svg/1024px-Denver_Nuggets.svg.png"
    st.image(Denver_Nuggets_png, caption='Denver Nuggets Logo', width=100, use_column_width=True)

    #Denver Nuggets main
    st.markdown("<p style='color: white;'>เดนเวอร์ นักเก็ตส์ เป็นทีมบาสเกตบอลในลีกเอ็นบีเอ ในเมืองเดนเวอร์ รัฐโคโลราโด เล่นอยู่ในดิวิชั่นภาคตะวันตกเฉียงเหนือในคอนเฟอเรนส์ตะวันออก เริ่มแรกคือทีม เดนเวอร์ รอกเก็ตส์ ซึ่งเล่นอยู่ในลีกเอบีเอ ต่อมาในปี ค.ศ. 1976 จึงเข้าร่วมลีกเอ็นบีเอเดนเวอร์นักเกตเป็นทีมบาสเกตบอลมืออาชีพชาวอเมริกันที่อยู่ในเดนเวอร์โคโลราโด นักเก็ตเป็นสมาชิกคนหนึ่งของภาคตะวันตกเฉียงเหนือกองของสายตะวันตกในสมาคมบาสเกตบอลแห่งชาติ (NBA) ทีมที่ได้รับการก่อตั้งขึ้นเป็นเดนเวอร์ Larks ในปี 1967 ในฐานะที่เป็นแฟรนไชส์กฎบัตรของสมาคมบาสเกตบอลอเมริกัน (ABA) แต่เปลี่ยนชื่อเป็นจรวดก่อนที่ฤดูกาลแรก. มันเปลี่ยนชื่ออีกครั้งเพื่อให้นักเก็ตในปี 1974 และเล่นให้กับ สุดท้าย ABA แชมป์ชื่อในปี  1976 แพ้ไปนิวยอร์กตาข่ายทีมที่เข้าร่วมในเอ็นบีเอในปี 1976 หลังจากการควบรวมกิจการสดเอ็นบีเอและได้มีบางช่วงของความสำเร็จมีคุณสมบัติสำหรับรอบตัดเชือกในเก้าฤดูกาลติดต่อกันในปี 1980 และการทำเช่นเดียวกันสำหรับก่อนหน้านี้สิบฤดูกาล แต่ก็ยังไม่ได้ปรากฏตัวในหนึ่งรอบชิงแชมป์ตั้งแต่ปีที่แล้วในสถาบันการเงิน นักเก็ตเล่นเกมในบ้านของพวกเขาที่เป๊ปซี่เซ็นเตอร์ซึ่งพวกเขาร่วมกับโคโลราโดถล่มของสมาคมฮอกกี้แห่งชาติ (NHL)</p>", unsafe_allow_html=True)
    st.markdown("""
        - **สังกัดในฝั่งตะวันตก** - <span style='color:white;'>Northwest Division</span>
        - **ปีที่ก่อตั้ง** - <span style='color:white;'>1967</span>
        - **ชื่อเดิม** - 
          <span style='color:white;'>Denver Rockets (1967-1974)</span>
          <span style='color:white;'>Denver Nuggets (1974-ปัจจุบัน)</span>
        - **สถานที่ตั้ง** - <span style='color:white;'>เมือง Denver รัฐ Colorado</span>
        - **ชื่อสนามเหย้า** - <span style='color:white;'>Ball Arena</span>
        - **เจ้าของทีม** - <span style='color:white;'>Ann Walton Kroenke</span>
        - **CEO** - <span style='color:white;'>Jim Martin</span>
        - **GM (General Manager)** - <span style='color:white;'>Calvin Booth</span>
        - **HC (Head Coach)** - <span style='color:white;'>Michael Malone</span>
        - **ทีมสังกัดใน G-League** - <span style='color:white;'>ไม่มี</span>
        - **จำนวนครั้งที่ได้แชมป์ลีก** - <span style='color:white;'>0</span>
        - **จำนวนครั้งที่ได้แชมป์ฝั่งทวีป** - <span style='color:white;'>0</span>
        - **จำนวนครั้งที่ได้แชมป์ Division** - <span style='color:white;'>11 (1970, 1975, 1977, 1978, 1985, 1988, 2006, 2009, 2010, 2019, 2020)</span>
        - **จำนวนเบอร์เสื้อที่ทำการ Retired** - <span style='color:white;'>7 (2, 12, 33, 40, 44, 55, 432)</span>
        """, unsafe_allow_html=True)

    #Denver Nuggets link
    st.markdown("[official website](https://www.nba.com/nuggets/)")
    st.markdown("[ประวัติเต็มๆ](https://www.blockdit.com/posts/5fe744d35e4d4d0cdbd82093?id=5fe744d35e4d4d0cdbd82093&series=5f97ea813ea0500c89ca96cd)")


    #Minnesota Timberwolves มินเนโซตา ทิมเบอร์วูลฟ์ส
    st.markdown("<font color='blue'><h2>Minnesota Timberwolves</h2></font>", unsafe_allow_html=True)
    st.markdown("<font color='white '><p>มินเนโซตา ทิมเบอร์วูลฟ์ส</p></font>", unsafe_allow_html=True)

    #Minnesota Timberwolves png
    Minnesota_Timberwolves_png = "https://upload.wikimedia.org/wikipedia/en/thumb/c/c2/Minnesota_Timberwolves_logo.svg/1024px-Minnesota_Timberwolves_logo.svg.png"
    st.image(Minnesota_Timberwolves_png, caption='Minnesota Timberwolves Logo', width=100, use_column_width=True)

    #Minnesota Timberwolves main
    st.markdown("<p style='color: white;'>Minnesota Timberwolves (ยังเรียกว่าT-หมาป่าหรือหมาป่า) เป็นทีมบาสเกตบอลมืออาชีพชาวอเมริกันที่อยู่ใน Minneapolis, Minnesota พวกเขาเล่นในภาคตะวันตกเฉียงเหนือกองของสายตะวันตกในสมาคมบาสเกตบอลแห่งชาติ (NBA). ก่อตั้งขึ้นในปี 1989 ทีมที่เป็นเจ้าของโดยเกลนเทย์เลอร์.  ทิมเบอร์วูเล่นเกมในบ้านของพวกเขาระหว่างเมโทรโดมและศูนย์Met ในช่วงต้นฤดูกาลของพวกเขาก่อนที่จะย้ายไปยังศูนย์เป้าหมายในปี 1990 ชอบมากที่สุดขยายทีมงานที่ Timberwolves ต่อสู้ในช่วงปีแรกของพวกเขา แต่หลังจากที่เข้าซื้อกิจการของเควินการ์เน็ตใน 1995 เอ็นบีเอร่างทีมทำรอบตัดเชือกแปดครั้งติดต่อกันจากปี 1997 ปี 2004 แม้จะมีการสูญเสียในรอบแรกในความพยายามครั้งแรกของพวกเจ็ด ที่ได้รับรางวัลชื่อ Timberwolves ส่วนแรกของพวกเขาใน2004และก้าวเข้าสู่รอบรองชนะเลิศสายตะวันตก การ์เน็ตก็ยังตั้งชื่อเอ็นบีเอที่ให้คุณค่าสูงสุดกับรางวัลผู้เล่นสำหรับฤดูกาลนี้. ทีมงานได้รับในการสร้างโหมดสำหรับทศวรรษที่ผ่านมาหายไปตั้งแต่รอบตัดเชือกในปี 2005 และการค้าการ์เน็ตกับบอสตันเซลติกส์ในปี 2007  Garnett กลับ ไป Timberwolves ในกุมภาพันธ์ 2015</p>", unsafe_allow_html=True)
    st.markdown("""
        - **สังกัดในฝั่งตะวันตก** - <span style='color:white;'>Northwest Division</span>
        - **ปีที่ก่อตั้ง** - <span style='color:white;'>1989</span>
        - **ชื่อเดิม** - <span style='color:white;'>Minnesota Timberwolves (1989-ปัจจุบัน)</span>
        - **สถานที่ตั้ง** - <span style='color:white;'>เมือง Minneapolis รัฐ Minnesota</span>
        - **ชื่อสนามเหย้า** - <span style='color:white;'>Target Center</span>
        - **เจ้าของทีม** - <span style='color:white;'>Glen Taylor</span>
        - **CEO** - <span style='color:white;'>Ethan Casson</span>
        - **GM (General Manager)** - <span style='color:white;'>ไม่มี</span>
        - **HC (Head Coach)** - <span style='color:white;'>Chris Finch</span>
        - **ทีมสังกัดใน G-League** - <span style='color:white;'>Iowa Wolves</span>
        - **จำนวนครั้งที่ได้แชมป์ลีก** - <span style='color:white;'>0</span>
        - **จำนวนครั้งที่ได้แชมป์ฝั่งทวีป** - <span style='color:white;'>0</span>
        - **จำนวนครั้งที่ได้แชมป์ Division** - <span style='color:white;'>1 (2004)</span>
        - **จำนวนเบอร์เสื้อที่ทำการ Retired** - <span style='color:white;'>1 (2)</span>
        """, unsafe_allow_html=True)
    
    #Minnesota Timberwolves link
    st.markdown("[official website](https://www.nba.com/timberwolves/)")
    st.markdown("[ประวัติเต็มๆ](https://www.blockdit.com/posts/605753d66494ea0c447d3306?id=605753d66494ea0c447d3306&series=5f97ea813ea0500c89ca96cd)")


    #Oklahoma City Thunder โอคลาโฮมา ซิตี้ ธันเดอร์ 
    st.markdown("<font color='blue'><h2>Oklahoma City Thunder</h2></font>", unsafe_allow_html=True)
    st.markdown("<font color='white '><p>โอคลาโฮมา ซิตี้ ธันเดอร์ </p></font>", unsafe_allow_html=True)

    #Oklahoma City Thunder png
    Oklahoma_City_Thunder_png = "https://upload.wikimedia.org/wikipedia/en/thumb/5/5d/Oklahoma_City_Thunder.svg/1024px-Oklahoma_City_Thunder.svg.png"
    st.image(Oklahoma_City_Thunder_png, caption='Oklahoma City Thunder Logo', width=100, use_column_width=True) 

    #Oklahoma City Thunder main
    st.markdown("<p style='color: white;'>โอคลาโฮมาซิตีธันเดอร์เป็น ทีมบาสเกตบอลมืออาชีพชาวอเมริกันที่อยู่ในโอคลาโฮมาซิตี, โอคลาโฮมา ทันเดอร์ในการแข่งขันในสมาคมบาสเกตบอลแห่งชาติ (NBA) ในฐานะสมาชิกคนหนึ่งของสายตะวันตกตะวันตกเฉียงเหนือกอง. ทีมที่เล่นเกมที่บ้านของChesapeake Energy Arena. ทันเดอร์ของเอ็นบีเอพัฒนาลีกพันธมิตรคือโอคลาโฮมาเมืองสีฟ้าซึ่งเป็นเจ้าของโดยทันเดอร์. ทันเดอร์เป็นทีมเดียวในกีฬาอเมริกันมืออาชีพที่สำคัญเหนือลีกที่อยู่ในรัฐโอคลาโฮมา.ทีมแรกที่จัดตั้งขึ้นในขณะที่ซีแอตเติล SuperSonics การขยายตัวของทีมที่เข้าร่วมในเอ็นบีเอฤดูกาล 1967-68  SuperSonics ย้ายในปี 2008 หลังจากที่นิคมถึงระหว่างกลุ่มเจ้าของนำโดยดินเบนเน็ตต์และฝ่ายนิติบัญญัติในซีแอตเติลวอชิงตันต่อไปนี้คดี ในซีแอตเติที่ SuperSonics คุณสมบัติสำหรับเอ็นบีเอเพลย์ออฟ 22 ครั้งได้รับรางวัลส่วนของหกครั้งและได้รับรางวัล 1979 แชมป์เอ็นบีเอ ในโอคลาโฮมาซิตี้ทันเดอร์ที่มีคุณภาพสำหรับเรือท่องเที่ยวแรกของพวกเขาในช่วงฤดูกาล 2009-10 พวกเขาประสบความสำเร็จตามมาด้วยการชนะการแบ่งหัวข้อแรกของพวกเขาในขณะที่ทันเดอร์ในฤดูกาล 2010-11 และแชมป์สายตะวันตกของพวกเขาเป็นครั้งแรกที่ทันเดอร์ในฤดูกาล 2011-12 ที่ปรากฏในรอบชิงชนะเลิศเอ็นบีเอเป็นครั้งที่สี่ในประวัติศาสตร์แฟรนไชส์และเป็นครั้งแรกนับตั้งแต่ 1996 เมื่อสโมสรที่อยู่ในซีแอตติ</p>", unsafe_allow_html=True)
    st.markdown("""
        - **สังกัดในฝั่งตะวันตก** - <font color="white">Northwest Division</font>
        - **ปีที่ก่อตั้ง** - <font color="white">1967</font>
        - **ชื่อเดิม** - <font color="white">Seattle Supersonics (1967-2008), Oklahoma City Thunder (2008-ปัจจุบัน)</font>
        - **สถานที่ตั้ง** - <font color="white">เมือง Oklahoma City รัฐ Oklahoma</font>
        - **ชื่อสนามเหย้า** - <font color="white">Chesapeake Energy Arena</font>
        - **เจ้าของทีม** - <font color="white">Professional Basketball Club LLC</font>
        - **CEO** - <font color="white">Clay Bennett</font>
        - **GM (General Manager)** - <font color="white">Sam Presti</font>
        - **HC (Head Coach)** - <font color="white">Mark Daigneault</font>
        - **ทีมสังกัดใน G-League** - <font color="white">Oklahoma City Blue</font>
        - **จำนวนครั้งที่ได้แชมป์ลีก** - <font color="white">1 (1979)</font>
        - **จำนวนครั้งที่ได้แชมป์ฝั่งทวีป** - <font color="white">4 (1978, 1979, 1996, 2012)</font>
        - **จำนวนครั้งที่ได้แชมป์ Division** - <font color="white">11 (1979, 1994, 1996-1998, 2005, 2011-2014, 2016)</font>
        - **จำนวนเบอร์เสื้อที่ทำการ Retired** - <font color="white">7 (1, 4, 10, 19, 24, 32, 43)</font>
        """, unsafe_allow_html=True)
    
    #Oklahoma City Thunder link
    st.markdown("[official website](https://www.nba.com/thunder/)")
    st.markdown("[ประวัติเต็มๆ](https://www.blockdit.com/posts/60780ae74bbb3e0c2ee60b91?id=60780ae74bbb3e0c2ee60b91&series=5f97ea813ea0500c89ca96cd)")


    #Portland Trail Blazers พอร์ตแลนด์ เทรลเบลเซอร์ส
    st.markdown("<font color='blue'><h2>Portland Trail Blazers</h2></font>", unsafe_allow_html=True)
    st.markdown("<font color='white '><p>พอร์ตแลนด์ เทรลเบลเซอร์ส </p></font>", unsafe_allow_html=True) 

    #Portland Trail Blazers png
    Portland_Trail_Blazers_png = "https://upload.wikimedia.org/wikipedia/en/thumb/2/21/Portland_Trail_Blazers_logo.svg/1024px-Portland_Trail_Blazers_logo.svg.png"
    st.image(Portland_Trail_Blazers_png, caption='Portland Trail Blazers Logo', width=100, use_column_width=True) 

    #Portland Trail Blazers main
    st.markdown("<p style='color: white;'>พอร์ตแลนด์เทรลเบลเซอร์ที่รู้จักกันทั่วไปว่าเป็นพอร์ตแลนด์มีทีมบาสเกตบอลมืออาชีพชาวอเมริกันที่อยู่ในพอร์ตแลนด์โอเรกอน พวกเขาเล่นในภาคตะวันตกเฉียงเหนือกองของสายตะวันตกในสมาคมบาสเกตบอลแห่งชาติ (NBA) พอร์ตแลนด์เทรลเบลเซอร์ที่เล่นเกมในบ้านของพวกเขาในสนามกีฬาอนุสรณ์ก่อนที่จะย้ายไปModa ศูนย์ในปี1995 (เรียกว่าโรสการ์เด้จนกระทั่ง 2013) แฟรนไชส์เข้าลีกในปี 1970 และได้รับการพอร์ตแลนด์เมืองที่บ้านของตนเท่านั้น แฟรนไชส์มีความสุขต่อไปนี้ที่แข็งแกร่ง; จาก 1977 ผ่าน 1995 ทีมขายออก 814 เกมในบ้านติดต่อกันแนวดังกล่าวที่ยาวที่สุดในกีฬาอเมริกันมืออาชีพที่สำคัญในเวลาเพียงค้นพบโดยคลีฟแลนด์อินเดียและบอสตันเรดซอกซ์. เอ็นบีเอทีมที่อยู่ใน binational แปซิฟิกตะวันตกเฉียงเหนือหลังจากที่ริซลี่แวนคูเวอร์ย้ายไปอยู่ที่เมมฟิสและกลายเป็นเมมฟิสกริซลีในปี2001 และซีแอตเติล SuperSonics ย้ายไปอยู่ที่เมืองโอคลาโฮมาและกลายเป็นโอคลาโฮมาซิตีธันเดอร์ในปี2008ทีมที่ได้ก้าวเข้าสู่รอบชิงชนะเลิศเอ็นบีเอสามครั้งชนะการแข่งขันชิงแชมป์เอ็นบีเอครั้งใน 1977 ปรากฏรอบชิงชนะเลิศเอ็นบีเออื่น ๆ ของพวกเขาอยู่ใน 1990 และ 1992. ทีมมีคุณสมบัติในรอบตัดเชือกในวันที่ 31 ฤดูกาลของการดำรงอยู่ 45 ฤดูกาลของพวกเขารวมถึงแนวของ 21 ปรากฏตรงจาก 1983 ผ่าน 2003 แนวยาวที่สุดเป็นอันดับสองในประวัติศาสตร์เอ็นบีเอ . พอร์ตแลนด์เทรลเบลเซอร์ ’31 เลื่อนอันดับที่สามในเอ็นบีเอเท่านั้นที่อยู่เบื้องหลัง Los Angeles Lakers และสเปอร์สในซานอันโตนิโอตั้งแต่เริ่มก่อตั้งทีมในปี1970  หกฮอลล์ออฟเฟมเล่นได้เล่นให้กับเสื้อคลุมแกะรอย  (Lenny Wilkens, Bill Walton, Clyde Drexler, Dražen Petrović, Arvydas Sabonis, and Scottie Pippen)  บิลวอลตันเป็นผู้เล่นที่อลังการที่สุดของแฟรนไชส์; เขาเป็นรอบชิงชนะเลิศเอ็นบีเอมากนักใน1977และฤดูกาลปกติMVP ต่อไปนี้ปี. ล่วงหน้าสี่ Blazer (เจฟฟ์เพท, ซิดนีย์สาดแสง, แบรนดอนรอยและเดเมียน Lillard) ได้รับรางวัล Rookie เอ็นบีเอของปีรางวัล. สองฮอลล์ออฟเฟมของโค้ช, เลนนี่ Wilkens และแจ็ค Ramsay ได้ลาดตระเวนสนามสำหรับเสื้อคลุมและสองคนอื่น ๆไมค์ชูเลอร์และไมค์ Dunleavy, ได้รับรางวัลโค้ชเอ็นบีเอในปีนี้ได้รับรางวัลกับทีม.</p>", unsafe_allow_html=True)
    st.markdown("""
        - **สังกัดในฝั่งตะวันตก** - <font color="white">Northwest Division</font>
        - **ปีที่ก่อตั้ง** - <font color="white">1970</font>
        - **ชื่อเดิม** - <font color="white">Portland Trail Blazers (1970-ปัจจุบัน)</font>
        - **สถานที่ตั้ง** - <font color="white">เมือง Portland รัฐ Oregon</font>
        - **ชื่อสนามเหย้า** - <font color="white">Moda Center</font>
        - **เจ้าของทีม** - <font color="white">Paul G. Allen Trust</font>
        - **CEO** - <font color="white">Chris McGowan</font>
        - **GM (General Manager)** - <font color="white">Neil Olshey</font>
        - **HC (Head Coach)** - <font color="white">Terry Stotts</font>
        - **ทีมสังกัดใน G-League** - <font color="white">ไม่มี</font>
        - **จำนวนครั้งที่ได้แชมป์ลีก** - <font color="white">1 (1977)</font>
        - **จำนวนครั้งที่ได้แชมป์ฝั่งทวีป** - <font color="white">3 (1977, 1990, 1992)</font>
        - **จำนวนครั้งที่ได้แชมป์ Division** - <font color="white">6 (1978, 1991, 1992, 1999, 2015, 2018)</font>
        - **จำนวนเบอร์เสื้อที่ทำการ Retired** - <font color="white">12 (1, 13, 14, 15, 20, 22, 30 (สองคน), 32, 36, 45, 77)</font>
        """, unsafe_allow_html=True)
    
    #Portland Trail Blazers link
    st.markdown("[official website](https://www.nba.com/blazers/)")
    st.markdown("[ประวัติเต็มๆ](https://www.blockdit.com/posts/60a12545bbaba50c4bb84c7b?id=60a12545bbaba50c4bb84c7b&series=5f97ea813ea0500c89ca96cd)")


    #Utah Jazz ยูทาห์ แจ๊ซ
    st.markdown("<font color='blue'><h2>Utah Jazz</h2></font>", unsafe_allow_html=True)
    st.markdown("<font color='white '><p>ยูทาห์ แจ๊ซ </p></font>", unsafe_allow_html=True) 

    #Utah Jazz png
    Utah_Jazz_png = "https://upload.wikimedia.org/wikipedia/en/thumb/5/52/Utah_Jazz_logo_2022.svg/1280px-Utah_Jazz_logo_2022.svg.png"
    st.image( Utah_Jazz_png, caption='Utah Jazz Logo', width=100, use_column_width=True) 

    #Utah Jazz main
    st.markdown("<p style='color: white;'>ยูทาห์แจ๊เป็นทีมบาสเกตบอลอาชีพชาวอเมริกันที่อยู่ในSalt Lake City, ยูทาห์ แจ๊สในการแข่งขันในสมาคมบาสเกตบอลแห่งชาติ (NBA) เป็นทีมสมาชิกของสายตะวันตกส่วนที่ภาคตะวันตกเฉียงเหนือ ทีมที่เล่นเกมที่บ้านของVivint สนามกีฬาบ้านสมาร์ทในSalt Lake City ทีมที่เริ่มเล่นในปี 1974 ในขณะที่แจ๊สนิวออร์ซึ่งตั้งอยู่ในนิวออร์, หลุยเซีย ย้ายไปร่วมทีมซอลต์เลกซิตีในปี 1979แจ๊สเป็นหนึ่งที่ประสบความสำเร็จในทีมอย่างน้อยในลีกในปีแรกของพวกเขา แม้ว่าที่ผ่านไป 10 ฤดูกาลก่อนที่แจ๊สที่มีคุณภาพสำหรับแรกของพวกเขาปรากฏตัวรอบรองชนะเลิศ (ใน1984) พวกเขาจะไม่พลาดในรอบตัดเชือกอีกเลยจนกระทั่งปี 2004 ในช่วงปลายปี 1980 จอห์นสต็อกตันและคาร์ลมาโลนที่เกิดขึ้นเป็นผู้เล่นแฟรนไชส์ให้กับทีมและเกิดขึ้นอย่างใดอย่างหนึ่งของที่มีชื่อเสียงมากที่สุดยามจุด – อำนาจไปข้างหน้า Duos ในประวัติศาสตร์เอ็นบีเอ นำโดยโค้ชเจอร์รีสโลนที่เอาไปสำหรับแฟรงค์ Layden ในปี 1988 พวกเขากลายเป็นหนึ่งในทีมที่โรงไฟฟ้าของปี 1990 สูงสุดในสองรอบชิงชนะเลิศเอ็นบีเอที่ปรากฏใน 1997 และ 1998 ที่พวกเขาหายไปทั้งสองครั้งกับชิคาโกบูลส์นำโดยไมเคิลจอร์แดนทั้งสต็อกตันและย้ายมาโลนในปี 2003 หลังจากที่หายไปรอบตัดเชือกสามฤดูกาลติดต่อกันแจ๊สกลับมาให้ความสำคัญภายใต้การนำในศาลของจุดเฝ้าเดรอนวิลเลียมส์แต่ครึ่งผ่าน 2010-11 เอ็นบีเอฤดูกาล, แจ๊สเริ่มปรับโครงสร้างหนี้หลังจากการเกษียณอายุของสโลนและการค้าวิลเลียมส์กับมลรัฐนิวเจอร์ซีย์แห ทีมที่ได้ทำให้รอบตัดเชือกตั้งแต่นั้นใน2012 ภายใต้โค้ชไทโรนคอร์และเป็นจุดเริ่มต้นยุคใหม่ภายใต้โค้ชวินไนเดอร์แจ๊สเป็นหนึ่งในสองทีมในเมเจอร์ลีกกีฬาอาชีพที่ตั้งอยู่ในรัฐยูทาห์; ทีมอื่น ๆ ที่เป็นจริงSalt Lake เป็นมืออาชีพฟุตบอลทีมในเมเจอร์ลีกซอกเกอร์ (MLS)มูลค่า $ 850,000,000 โดย Forbes, ยศแจ๊สเป็นแฟรนไชส์ที่มีค่าที่สุดที่ 20 ในเอ็นบีเอไปข้างหน้าของอินเดียนา Pacers และแอตแลนตาฮอกส์</p>", unsafe_allow_html=True)
    st.markdown("""
    - **สังกัดในฝั่งตะวันตก** - <font color="white">Northwest Division</font>
    - **ปีที่ก่อตั้ง** - <font color="white">1970</font>
    - **ชื่อเดิม** - <font color="white">Utah Jazz (1970-ปัจจุบัน)</font>
    - **สถานที่ตั้ง** - <font color="white">เมือง Salt Lake City รัฐ Utah</font>
    - **ชื่อสนามเหย้า** - <font color="white">Vivint Smart Home Arena</font>
    - **เจ้าของทีม** - <font color="white">Gail Miller and the Miller Family</font>
    - **CEO** - <font color="white">Jim Olson</font>
    - **GM (General Manager)** - <font color="white">Justin Zanik</font>
    - **HC (Head Coach)** - <font color="white"> Quin Snyder</font>
    - **ทีมสังกัดใน G-League** - <font color="white">Salt Lake City Stars</font>
    - **จำนวนครั้งที่ได้แชมป์ลีก** - <font color="white">0</font>
    - **จำนวนครั้งที่ได้แชมป์ฝั่งทวีป** - <font color="white">0</font>
    - **จำนวนครั้งที่ได้แชมป์ Division** - <font color="white">9 (1984, 1989, 1992-1994, 1996-1998, 2000)</font>
    - **จำนวนเบอร์เสื้อที่ทำการ Retired** - <font color="white"> 6 (1, 4, 7, 9, 12, 14)</font>
    """, unsafe_allow_html=True)

    #Utah Jazz link
    st.markdown("[official website](https://www.nba.com/jazz/)")
    st.markdown("[ประวัติเต็มๆ](https://hmong.in.th/wiki/Utah_Jazz)")

if st.sidebar.button('PACIFIC'):
    
    with st.spinner('Wait for it...'):
        time.sleep(1)

    # Division PACIFIC
    st.markdown("<h1 style='color: red; text-shadow: 2px 2px white;'>Division PACIFIC</h1>", unsafe_allow_html=True)

    #Golden State Warriors โกลเด้น สเตท วอริเออร์ส
    st.markdown("<font color='blue'><h2>Golden State Warriors</h2></font>", unsafe_allow_html=True)
    st.markdown("<font color='yellow '><p>โกลเด้น สเตท วอริเออร์ส</p></font>", unsafe_allow_html=True)

    #Golden State Warriors png
    Golden_State_Warriors_png = "https://upload.wikimedia.org/wikipedia/en/thumb/0/01/Golden_State_Warriors_logo.svg/800px-Golden_State_Warriors_logo.svg.png"
    st.image(Golden_State_Warriors_png, caption='Golden State Warriors Logo', width=100, use_column_width=True)

    #Golden State Warriors main
    st.markdown("<p style='color: white;'>รัฐแคริฟอร์เนียนักรบเป็นทีมบาสเกตบอลมืออาชีพชาวอเมริกันที่อยู่ในโอ๊คแลนด์แคลิฟอร์เนีย พวกเขาเป็นสมาชิกของกองแปซิฟิกในการประชุมตะวันตกของสมาคมบาสเกตบอลแห่งชาติ (NBA) ทีมที่ก่อตั้งขึ้นในปี 1946 ในขณะที่ฟิลาเดลนักรบอยู่ในฟิลาเดล, เพนซิลเป็นสมาชิกผู้ก่อตั้งของสมาคมบาสเกตบอลแห่งอเมริกา (BAA) และมันจะเปิด1947 รอบชิงชนะเลิศสนามบินที่ตอนนี้ถือว่าเป็นครั้งแรกที่แชมป์เอ็นบีเอ. ในปี 1962 แฟรนไชส์ย้ายไปอยู่ที่บริเวณอ่าวและถูกเปลี่ยนชื่อเป็นนักรบซานฟรานซิสจนกระทั่งปี1971 เมื่อมันเปลี่ยนชื่อเล่นทางภูมิศาสตร์ในการโกลเด้นรัฐชื่อเล่นของรัฐแคลิฟอร์เนียรัฐ. ตั้งแต่ปี 1972 ศาลที่บ้านของทีมที่ได้รับสนามกีฬา Oracle Arena ในโอกแลนด์นักรบที่ได้รับรางวัลสี่ประชันเอ็นบีเอ พวกเขาส่วนใหญ่เมื่อเร็ว ๆ นี้ได้รับรางวัลการแข่งขันชิงแชมป์เอ็นบีเอโดยการเอาชนะคลีฟแลนด์คาวาเลียใน2015 รอบรองชนะเลิศ</p>", unsafe_allow_html=True)
    st.markdown("""
        - **สังกัดในฝั่งตะวันตก** - <font color="white">Pacific Division</font>
        - **ปีที่ก่อตั้ง** - <font color="white">1946</font>
        - **ชื่อเดิม** - <font color="white">Philadelphia Warriors (1946-1962), San Francisco Warriors (1962-1971), Golden State Warriors (1971-ปัจจุบัน)</font>
        - **สถานที่ตั้ง** - <font color="white">เมือง San Francisco รัฐ California</font>
        - **ชื่อสนามเหย้า** - <font color="white">Chase Center</font>
        - **เจ้าของทีม** - <font color="white">Joe Lacob</font>
        - **CEO** - <font color="white">Joe Lacob</font>
        - **GM (General Manager)** - <font color="white">Bob Myers</font>
        - **HC (Head Coach)** - <font color="white">Steve Kerr</font>
        - **ทีมสังกัดใน G-League** - <font color="white">Santa Cruz Warriors</font>
        - **จำนวนครั้งที่ได้แชมป์ลีก** - <font color="white">6 (1947, 1956, 1975, 2015, 2017, 2018)</font>
        - **จำนวนครั้งที่ได้แชมป์ฝั่งทวีป** - <font color="white">6 (1975, 2015-2019)</font>
        - **จำนวนครั้งที่ได้แชมป์ Division** - <font color="white">12 (1948, 1951, 1956, 1964, 1967, 1975, 1976, 2015-2019)</font>
        - **จำนวนเบอร์เสื้อที่ทำการ Retired** - <font color="white">6 (13, 14, 16, 17, 24, 42)</font>
        """, unsafe_allow_html=True)
    
    #Golden State Warriors link
    st.markdown("[official website](https://www.nba.com/warriors)")
    st.markdown("[ประวัติเต็มๆ](https://www.blockdit.com/posts/5ff1a9f91b2c040ce5797f9f?id=5ff1a9f91b2c040ce5797f9f&series=5f97ea813ea0500c89ca96cd)")


    #LA Clippers ลอสแอนเจลิส คลิปเปอร์ส
    st.markdown("<font color='blue'><h2>LA Clippers</h2></font>", unsafe_allow_html=True)
    st.markdown("<font color='white '><p>ลอสแอนเจลิส คลิปเปอร์ส</p></font>", unsafe_allow_html=True)

    #LA Clippers png
    LA_Clippers_png = "https://upload.wikimedia.org/wikipedia/en/thumb/b/bb/Los_Angeles_Clippers_%282015%29.svg/1280px-Los_Angeles_Clippers_%282015%29.svg.png"
    st.image(LA_Clippers_png, caption='LA Clippers Logo', width=100, use_column_width=True)

    #LA Clippers main
    st.markdown("<p style='color: white;'>Los Angeles Clippers เป็นอเมริกันมืออาชีพบาสเกตบอลทีมอยู่ในLos Angeles, California กรรไกรตัดเล็บแข่งขันในสมาคมบาสเกตบอลแห่งชาติ (NBA) เป็นสมาชิกของลีกกองแปซิฟิกของการประชุมตะวันตก กรรไกรตัดเล็บเล่นเกมในบ้านของพวกเขาที่เตเปิลเซ็นเตอร์, เวทีร่วมกับLos Angeles Lakers ของเอ็นบีเอที่ลอสแอนเจลิสปาร์กของสตรีสมาคมบาสเกตบอลแห่งชาติ (ดับเบิลยูเอ็น) และLos Angeles Kings ของสมาคมฮอกกี้แห่งชาติ (NHL) .แฟรนไชส์ก่อตั้งขึ้นในปี 1970 ในขณะที่บัฟฟาโลเบรฟส์หนึ่งในสามของการขยายทีมงานที่จะเข้าร่วมในเอ็นบีเอในปีนั้น เบรฟส์ย้ายจากบัฟฟาโล, นิวยอร์กไปซานดิเอโก, แคลิฟอร์เนียในปี 1978 และกลายเป็นที่รู้จักในฐานะที่ซานดิเอโกกรรไกร ในปี 1984 ย้ายไป Los Angeles Clippers ผ่านของประวัติศาสตร์แฟรนไชส์ไม่เห็นฤดูกาลปกติอย่างมีนัยสำคัญหรือประสบความสำเร็จในรอบรองชนะเลิศ กรรไกรตัดเล็บได้เห็นบ่อยเป็นตัวอย่างของการเป็นผู้แพ้ตลอดกาลในกีฬาอาชีพชาวอเมริกัน, การวาดภาพการเปรียบเทียบที่ไม่เอื้ออำนวยกับ Lakers ที่ประสบความสำเร็จในอดีตที่พวกเขาได้ร่วมกันเป็นตลาดตั้งแต่ปี 1984 และตั้งแต่ปี 1999 ที่เกิดเหตุความมั่งคั่งกรรไกร ‘เปิดในช่วงต้นยุค 2010 ด้วยการซื้อกิจการของผู้เล่นหลักของเบลคกริฟฟิ, DeAndre จอร์แดนและคริสพอ ใน2013, แฟรนไชส์ได้รับรางวัลส่วนแรกเป็นทีมที่ทำให้รอบตัดเชือกเป็นครั้งที่เก้าในประวัติศาสตร์แฟรนไชส์และเป็นครั้งที่สามในก่อนหน้านี้แปดฤดูกาล พวกเขายังเพิ่มให้กับรุ่นของพวกเขาแข่งขันกับLakers ขณะที่พวกเขาจบด้วยดีกว่าสถิติ Lakers เป็นครั้งที่ห้าและได้รับรางวัลซีรีส์ฤดูกาลเป็นครั้งที่สองนับตั้งแต่ย้ายไป Los Angeles ในปี 1984 ในครั้งนี้กวาดพวกเขาซ้ำแล้วซ้ำอีกเป็นฝ่ายชนะใน2014</p>", unsafe_allow_html=True)
    st.markdown("""
        - **สังกัดในฝั่งตะวันตก** - <font color="white">Pacific Division</font>
        - **ปีที่ก่อตั้ง** - <font color="white">1970</font>
        - **ชื่อเดิม** - <font color="white">Buffalo Braves (1970-1978), San Diego Clippers (1978-1984), Los Angeles Clippers (1984-ปัจจุบัน)</font>
        - **สถานที่ตั้ง** - <font color="white">เมือง Los Angeles รัฐ California</font>
        - **ชื่อสนามเหย้า** - <font color="white">Staples Center</font>
        - **เจ้าของทีม** - <font color="white">Steve Ballmer</font>
        - **CEO** - <font color="white">Steve Ballmer</font>
        - **GM (General Manager)** - <font color="white">Michael Winger</font>
        - **HC (Head Coach)** - <font color="white">Tyronn Lue</font>
        - **ทีมสังกัดใน G-League** - <font color="white">Agua Caliente Clippers</font>
        - **จำนวนครั้งที่ได้แชมป์ลีก** - <font color="white">0</font>
        - **จำนวนครั้งที่ได้แชมป์ฝั่งทวีป** - <font color="white">0</font>
        - **จำนวนครั้งที่ได้แชมป์ Division** - <font color="white">2 (2013, 2014)</font>
        - **จำนวนเบอร์เสื้อที่ทำการ Retired** - <font color="white">0</font>
        """, unsafe_allow_html=True)

    #LA Clippers link
    st.markdown("[official website](https://www.nba.com/clippers/)")
    st.markdown("[ประวัติเต็มๆ](https://www.blockdit.com/posts/601417a42a4e911325ca5262?id=601417a42a4e911325ca5262&series=5f97ea813ea0500c89ca96cd)")


    #Los Angeles Lakers ลอสแอนเจลิส เลเกอรส์
    st.markdown("<font color='purple'><h2>Los Angeles Lakers</h2></font>", unsafe_allow_html=True)
    st.markdown("<font color='yellow'><p>ลอสแอนเจลิส เลเกอรส์</p></font>", unsafe_allow_html=True)

    #Los Angeles Lakers png
    Los_Angeles_Lakers_png = "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3c/Los_Angeles_Lakers_logo.svg/1920px-Los_Angeles_Lakers_logo.svg.png"
    st.image(Los_Angeles_Lakers_png, caption='Los Angeles Lakers Logo', width=100, use_column_width=True)

    #Los Angeles Lakers main
    st.markdown("<p style='color: white;'>ลอสแอนเจลิส เลเกอร์ส เป็นทีมบาสเกตบอลในลีกเอ็นบีเอ ในเมืองลอสแอนเจลิส รัฐแคลิฟอร์เนีย ตามสถิติเมื่อสิ้นสุดฤดูกาล 2004-05 เป็นทีมที่ชนะมากที่สุด (คือ 2,621 เกม) มีเปอร์เซนต์ชนะสูงสุด (61.9%) เล่นในรอบชิงชนะเลิศมากที่สุด (30 ครั้ง) และชนะเลิศในลึกมากเป็นอันดับสอง คือ 16 ครั้ง เป็นรองเพียงทีมบอสตัน เซลติกส์ ซึ่งชนะ 17 ครั้ง นอกจากนี้ยังมีสถิติชนะติดต่อกันมากที่สุดในฤดูกาลคือ 33 เกม</p>", unsafe_allow_html=True)
    st.markdown("""
        - **สังกัดในฝั่งตะวันตก** - <font color="white">Pacific Division</font>
        - **ปีที่ก่อตั้ง** - <font color="white">1947</font>
        - **ชื่อเดิม** - <font color="white">Minneapolis Lakers (1947-1960), Los Angeles Lakers (1960-ปัจจุบัน)</font>
        - **สถานที่ตั้ง** - <font color="white">เมือง Los Angeles รัฐ California</font>
        - **ชื่อสนามเหย้า** - <font color="white">Staples Center</font>
        - **เจ้าของทีม** - <font color="white">Buss Family Trusts</font>
        - **CEO** - <font color="white">Jeanie Buss</font>
        - **GM (General Manager)** - <font color="white">Rob Pelinka</font>
        - **HC (Head Coach)** - <font color="white">Frank Vogel</font>
        - **ทีมสังกัดใน G-League** - <font color="white">South Bay Lakers</font>
        - **จำนวนครั้งที่ได้แชมป์ลีก** - <font color="white">17 (1949, 1950, 1952-1954, 1972, 1980, 1982, 1985, 1987, 1988, 2000-2002, 2009, 2010, 2020)</font>
        - **จำนวนครั้งที่ได้แชมป์ฝั่งทวีป** - <font color="white">19 (1972, 1973, 1980, 1982-1985, 1987-1989, 1991, 2000-2002, 2004, 2008-2010, 2020)</font>
        - **จำนวนครั้งที่ได้แชมป์ Division** - <font color="white">33 (1950, 1951, 1953, 1954, 1962, 1963, 1965, 1966, 1969, 1971-1974, 1977, 1980, 1982-1990, 2000, 2001, 2004, 2008-2012, 2020)</font>
        - **จำนวนเบอร์เสื้อที่ทำการ Retired** - <font color="white">11 (8, 13, 22, 24, 25, 32, 33, 34, 42, 44, 52)</font>
        """, unsafe_allow_html=True)
    
    #Los Angeles Lakers link
    st.markdown("[official website](https://www.nba.com/lakers/)")
    st.markdown("[ประวัติเต็มๆ](https://www.blockdit.com/posts/60198127dea5120b93ca418e?id=60198127dea5120b93ca418e&series=5f97ea813ea0500c89ca96cd)")


    #Phoenix Suns ฟีนิกซ์ ซันส์
    st.markdown("<font color='orange'><h2>Phoenix Suns</h2></font>", unsafe_allow_html=True)
    st.markdown("<font color='purple '><p>ฟีนิกซ์ ซันส์</p></font>", unsafe_allow_html=True)

    #Phoenix Suns png
    Phoenix_Suns_png = "https://upload.wikimedia.org/wikipedia/en/thumb/d/dc/Phoenix_Suns_logo.svg/1024px-Phoenix_Suns_logo.svg.png"
    st.image(Phoenix_Suns_png, caption='Phoenix Suns Logo', width=100, use_column_width=True)

    #Phoenix Suns main
    st.markdown("<p style='color: white;'>ฟีนิกซ์ดาวทองเป็นทีมบาสเกตบอลมืออาชีพชาวอเมริกันที่อยู่ในฟินิกซ์ พวกเขาเป็นสมาชิกของกองแปซิฟิกของการประชุมตะวันตกในสมาคมบาสเกตบอลแห่งชาติ(NBA) และเป็นทีมเดียวในส่วนของพวกเขาไม่ได้ที่จะอยู่ในรัฐแคลิฟอร์เนีย ตั้งแต่ปี 1992 ดาวทองมีการเล่นเกมในบ้านของพวกเขาที่Talking Stick รีสอร์ทสนามกีฬาในเมืองฟีนิกซ์ดาวทองเริ่มเล่นเป็นทีมการขยายตัวใน1968 เจ้าของแฟรนไชส์ของเอ็นบีเอสี่ที่ดีที่สุดทุกครั้งชนะร้อยชนะ 55% ของเกมเป็นของปลาย2014-15 ฤดูกาล. ใน 47 ปีของการเล่นที่พวกเขาได้ทำในรอบตัดเชือก 29 ครั้งโพสต์ 19 ของฤดูกาล 50 หรือมากกว่าชนะเก้าเดินทางไปรอบรองชนะเลิศสายตะวันตกและก้าวเข้าสู่รอบชิงชนะเลิศเอ็นบีเอเป็นครั้งที่สองใน1976และ1993 เป็นผลให้ในอัตราร้อยละชนะการสูญเสียทุกครั้งที่พวกเขาเป็นทีมดาวทองที่มีเปอร์เซ็นต์ชนะสูงสุดจะไม่เคยได้รับรางวัลการแข่งขันชิงแชมป์เอ็นบีเอ. ด้วยสมาคมฮอกกี้แห่งชาติ (NHL) ‘s ฟีนิกซ์หมาป่าเปลี่ยนชื่อที่ตั้งทางภูมิศาสตร์ของพวกเขาไปแอริโซนาหมาป่าใน 27 มิถุนายน 2014 (ซึ่งเป็นที่ต้องการเป็นส่วนหนึ่งของใหม่ของพวกเขาArena แม่น้ำก่าสัญญาเช่า), ดาวทองเป็นเพียงคนเดียวที่สำคัญระดับมืออาชีพแฟรนไชส์กีฬาที่อยู่ในรัฐแอริโซนาที่แบรนด์ของตัวเองโดยเฉพาะที่เมืองฟีนิกซ์มากกว่ารัฐที่เป็นทั้ง</p>", unsafe_allow_html=True)
    st.markdown("""
        - **สังกัดในฝั่งตะวันตก** - <font color="white">Pacific Division</font>
        - **ปีที่ก่อตั้ง** - <font color="white">1968</font>
        - **ชื่อเดิม** - <font color="white">Phoenix Suns (1968-ปัจจุบัน)</font>
        - **สถานที่ตั้ง** - <font color="white">เมือง Phoenix รัฐ Arizona</font>
        - **ชื่อสนามเหย้า** - <font color="white">Phoenix Suns Arena</font>
        - **เจ้าของทีม** - <font color="white">Robert Sarver</font>
        - **CEO** - <font color="white">Jason Rowley</font>
        - **GM (General Manager)** - <font color="white">James Jones</font>
        - **HC (Head Coach)** - <font color="white">Monty Williams</font>
        - **ทีมสังกัดใน G-League** - <font color="white">ไม่มี</font>
        - **จำนวนครั้งที่ได้แชมป์ลีก** - <font color="white">0</font>
        - **จำนวนครั้งที่ได้แชมป์ฝั่งทวีป** - <font color="white">3 (1976, 1993, 2021)</font>
        - **จำนวนครั้งที่ได้แชมป์ Division** - <font color="white">7 (1981, 1993, 1995, 2005-2007, 2021)</font>
        - **จำนวนเบอร์เสื้อที่ทำการ Retired** - <font color="white">6 (5, 6, 7, 33, 42, 44)</font>
        """, unsafe_allow_html=True)
    
    #Phoenix Suns link
    st.markdown("[official website](https://www.nba.com/suns)")
    st.markdown("[ประวัติเต็มๆ](https://www.blockdit.com/posts/60916d69c509b10c603e1a2e?id=60916d69c509b10c603e1a2e&series=5f97ea813ea0500c89ca96cd)")


    #Sacramento Kings ซาคราเมนโต คิงส์
    st.markdown("<font color='purple'><h2>Sacramento Kings</h2></font>", unsafe_allow_html=True)
    st.markdown("<font color='white '><p>ซาคราเมนโต คิงส์</p></font>", unsafe_allow_html=True)

    #Sacramento Kings png
    Sacramento_Kings_png = "https://upload.wikimedia.org/wikipedia/en/thumb/c/c7/SacramentoKings.svg/800px-SacramentoKings.svg.png"
    st.image(Sacramento_Kings_png, caption='Sacramento Kings Logo', width=100, use_column_width=True)

    #Sacramento Kings main
    st.markdown("<p style='color: white;'>ซาคราเมนโตคิงส์เป็นทีมบาสเกตบอลมือชีพอีกทีมหนึ่งที่อยู่ในซาคราเมนโตแคลิฟอร์เนีย The kings แข่งขันในสมาคมบาสเกตบอลแห่งชาติ (NBA) ในฐานะสมาชิกของสายตะวันตกของแปซิฟิก คิงส์เป็นทีมเดียวในกีฬาที่สำคัญเป็นมืออาชีพในทวีปอเมริกาเหนือลีกอยู่ในซาคราเมนโต เล่นกันในอารีน่าคิงส์เป็นแฟรนไซส์ที่เก่าแก่ที่สุดในเอ็นบีเอและเป็นหนึ่งในมืออาชีพที่เก่าแก่ที่สุดพวกเขามาในโรเชสเตอร์, นิวยอร์กเป็นโรเชสเตอร์พระราชวงศ์ในปี1945 และเข้าร่วมในลีกบาสเกตบอลแห่งชาติ พวกเขากระโดดสมาคมบาสเกตบอลแห่งอเมริกาบรรพบุรุษของเอ็นบีเอในปี1948 ในฐานะที่เป็นพระราชวงศ์ทีมที่ประสบความสำเร็จมักจะเป็นในศาลชนะการแข่งขันชิงแชมป์เอ็นบีเอในปี 1951 แต่พวกเขาพบว่ามันยากมากขึ้นที่จะทำกำไรในที่ ตลาดขนาดเล็กเมื่อเทียบกับโรเชสเตอร์และย้ายไปที่ซินซิน, โอไฮโอในปี 1957 กลายเป็นซินซินพระราชวงศ์ ในปี 1972 ทีมที่ย้ายไปอยู่กับแคนซัสซิตีต้นเกมของพวกเขาแยกระหว่างแคนซัสซิตี้และโอมาฮา, เนบราสก้าและการขึ้นชื่อแคนซัสซิตี้กษัตริย์ ทีมอีกครั้งล้มเหลวที่จะพบความสำเร็จในตลาดนั้นและย้ายไปอยู่ที่ซาคราเมนโตในปี 1985</p>", unsafe_allow_html=True)
    st.markdown("""
        - **สังกัดในฝั่งตะวันตก** - <font color="white">Pacific Division</font>
        - **ปีที่ก่อตั้ง** - <font color="white">1923</font>
        - **ชื่อเดิม** - <font color="white">Rochester Seagrams (1923-1942), Rochester Eber Seagrams (1942-1943), Rochester Pros (1943-1945), Rochester Royals (1945-1957), Cincinnati Royals (1957-1972), Kansas City-Omaha Kings (1972-1975), Kansas City Kings (1975-1985), Sacramento Kings (1985-ปัจจุบัน)</font>
        - **สถานที่ตั้ง** - <font color="white">เมือง Sacramento รัฐ California</font>
        - **ชื่อสนามเหย้า** - <font color="white">Golden 1 Center</font>
        - **เจ้าของทีม** - <font color="white">Vivek Ranadivé</font>
        - **CEO** - <font color="white">Vivek Ranadivé</font>
        - **GM (General Manager)** - <font color="white">Monte McNair</font>
        - **HC (Head Coach)** - <font color="white">Luke Walton</font>
        - **ทีมสังกัดใน G-League** - <font color="white">Stockton Kings</font>
        - **จำนวนครั้งที่ได้แชมป์ลีก** - <font color="white">1 (1951)</font>
        - **จำนวนครั้งที่ได้แชมป์ฝั่งทวีป** - <font color="white">0</font>
        - **จำนวนครั้งที่ได้แชมป์ Division** - <font color="white">5 (1949, 1952, 1979, 2002, 2003)</font>
        - **จำนวนเบอร์เสื้อที่ทำการ Retired** - <font color="white">11 (1, 2, 4, 6, 11, 12, 14, 16, 21, 27, 44)</font>
        """, unsafe_allow_html=True)
    
    #Sacramento Kings link
    st.markdown("[official website](https://www.nba.com/kings/)")
    st.markdown("[ประวัติเต็มๆ](https://www.blockdit.com/posts/60afb44bf3eb711499db3a26?id=60afb44bf3eb711499db3a26&series=5f97ea813ea0500c89ca96cd)")

if st.sidebar.button('SOUTHWEST'):
     
    with st.spinner('Wait for it...'):
        time.sleep(1)

    #Division SOUTHWEST
    st.markdown("<h1 style='color: red; text-shadow: 2px 2px white;'>Division SOUTHWEST</h1>", unsafe_allow_html=True)

    #Dallas Mavericks ดัลลัส แมฟเวอริกส์
    st.markdown("<font color='blue'><h2>Dallas Mavericks</h2></font>", unsafe_allow_html=True)
    st.markdown("<font color='white '><p>ดัลลัส แมฟเวอริกส์</p></font>", unsafe_allow_html=True)

    #Dallas Mavericks png
    Dallas_Mavericks_png = "https://upload.wikimedia.org/wikipedia/en/thumb/9/97/Dallas_Mavericks_logo.svg/1024px-Dallas_Mavericks_logo.svg.png"
    st.image(Dallas_Mavericks_png, caption='Dallas Mavericks Logo', width=100, use_column_width=True)

    #Dallas Mavericks main
    st.markdown("<p style='color: white;'>ดัลลัส แมฟเวอริกส์เป็นทีมบาสเกตบอลในลีกเอ็นบีเอ ในเมืองดัลลัส รัฐเทกซัส เล่นอยู่ในดิวิชั่นภาคตะวันตกเฉียงใต้ในคอนเฟอเรนส์ตะวันตก เป็นแชมป์ทีมล่าสุดจากฤดูกาล 2010-2011 Dallas Mavericks หลังจากดัลลัสได้ก่อตั้งทีมบาสเก็ตบอลขึ้นในปี 1980 โดยนาย Don Carter เศรษฐีนักธุรกิจชาวฟลอริด้า (เจ้าของคนแรก) ดัลลัส เรดิโอ สื่อวิทยุท้องถิ่นก็ได้จัดประกวดการตั้งฉายาทีม โดยให้ชาวดัลลัสส่งชื่อเข้ามา ซึ่งงานนี้มีชาวดัลลัสส่งชื่อเข้ามากันถึง 4,600 คน และชื่อที่ได้รับคัดเลือกให้เข้ารอบสุดท้ายก็ได้แก่ Wranglers, Express, และ Mavericks โดยชื่อสุดท้ายนั่นมีที่มาจากภาพยนตร์โทรทัศน์ชื่อดังที่พูดถึงตัวละครเอกซึ่งเป็นพี่น้องคาวบอยพเนจรชาวเท็กซัส ที่พกพาการเล่นไพ่ชั้นเซียนออกตะลอนไปทั่วอเมริกานามว่า Bret กับ Bart Maverick ซึ่งหนึ่งในนักแสดงของซีรี่ส์ชุดนี้นั่นคือ เจมส์ การ์เนอร์ อดีตหุ้นส่วนของทีม ดอน คาร์เตอร์เลยถือเป็นเกียรติที่จะได้ใช้ชื่อนี้เป็นฉายาทีม ซึ่งก็เป็นชื่อที่แฟนๆชื่นชอบ เพราะโดยความหมายแล้ว แมฟเวอริคส์ ก็หมายถึงคนที่เป็นอิสระหรือสัตว์ที่มิได้ถูกตีตราซึ่งเป็นความหมายที่ดี</p>", unsafe_allow_html=True)
    st.markdown("""
        - **สังกัดในฝั่งตะวันตก** - <font color="white">Southwest Division</font>
        - **ปีที่ก่อตั้ง** - <font color="white">1980</font>
        - **ชื่อเดิม** - <font color="white">Dallas Mavericks (1980-ปัจจุบัน)</font>
        - **สถานที่ตั้ง** - <font color="white">เมือง Dallas รัฐ Texas</font>
        - **ชื่อสนามเหย้า** - <font color="white">Americans Airlines Center</font>
        - **เจ้าของทีม** - <font color="white">Mark Cuban</font>
        - **CEO** - <font color="white">Cynt Marshall</font>
        - **GM (General Manager)** - <font color="white">Donnie Nelson</font>
        - **HC (Head Coach)** - <font color="white">Rick Carlisle</font>
        - **ทีมสังกัดใน G-League** - <font color="white">Texas Legends</font>
        - **จำนวนครั้งที่ได้แชมป์ลีก** - <font color="white">1 (2011)</font>
        - **จำนวนครั้งที่ได้แชมป์ฝั่งทวีป** - <font color="white">2 (2006, 2011)</font>
        - **จำนวนครั้งที่ได้แชมป์ Division** - <font color="white">3 (1987, 2007, 2010)</font>
        - **จำนวนเบอร์เสื้อที่ทำการ Retired** - <font color="white">3 (12, 15, 22)</font>
        """, unsafe_allow_html=True)
    
    #Dallas Mavericks link
    st.markdown("[official website](https://www.nba.com/team/1610612742/mavericks)")
    st.markdown("[ประวัติเต็มๆ](https://www.blockdit.com/posts/5fcb7040d2ff850cb6c03e58?id=5fcb7040d2ff850cb6c03e58&series=5f97ea813ea0500c89ca96cd)")


    #Houston Rockets ฮิวสตัน รอกเก็ตส์
    st.markdown("<font color='red'><h2>Houston Rockets</h2></font>", unsafe_allow_html=True)
    st.markdown("<font color='white '><p>ฮิวสตัน รอกเก็ตส์</p></font>", unsafe_allow_html=True)

    #Houston Rockets png
    Houston_Rockets_png = "https://upload.wikimedia.org/wikipedia/en/thumb/2/28/Houston_Rockets.svg/800px-Houston_Rockets.svg.png"
    st.image(Houston_Rockets_png, caption='Houston Rockets Logo', width=100, use_column_width=True)

    #Houston Rockets main
    st.markdown("<p style='color: white;'>ฮิวสตัน รอกเก็ตส์ เป็นทีมบาสเกตบอลในลีกเอ็นบีเอ ในเมืองฮิวสตัน รัฐเท็กซัส เล่นอยู่ในดิวิชั่นภาคตะวันตกเฉียงใต้ในคอนเฟอเรนส์ตะวันตก เดิมทีเล่นอยู่ในเมืองแซนดิเอโก 4 ปี ก่อนย้ายมาที่เมืองฮิวสตัน นอกจากนี้ ฮิวสตัน รอกเก็ตส์ ยังเคยเป็นทีมของ เหยา หมิง นักบาสเกตบอลเอ็นบีเอชาวจีนที่มีชื่อเสียง</p>", unsafe_allow_html=True)
    st.markdown("""
        - **สังกัดในฝั่งตะวันตก** - <font color="white">Southwest Division</font>
        - **ปีที่ก่อตั้ง** - <font color="white">1967</font>
        - **ชื่อเดิม** - <font color="white">San Diego Rockets (1967-1971), Houston Rockets (1971-ปัจจุบัน)</font>
        - **สถานที่ตั้ง** - <font color="white">เมือง Houston รัฐ Texas</font>
        - **ชื่อสนามเหย้า** - <font color="white">Toyota Center</font>
        - **เจ้าของทีม** - <font color="white">Tilman Fertitta</font>
        - **CEO** - <font color="white">Tad Brown</font>
        - **GM (General Manager)** - <font color="white">Rafael Stone</font>
        - **HC (Head Coach)** - <font color="white">Stephen Silas</font>
        - **ทีมสังกัดใน G-League** - <font color="white">Rio Grande Valley Vipers</font>
        - **จำนวนครั้งที่ได้แชมป์ลีก** - <font color="white">2 (1994, 1995)</font>
        - **จำนวนครั้งที่ได้แชมป์ฝั่งทวีป** - <font color="white">4 (1981, 1986, 1994, 1995)</font>
        - **จำนวนครั้งที่ได้แชมป์ Division** - <font color="white">8 (1977, 1986, 1993, 1994, 2015, 2018-2020)</font>
        - **จำนวนเบอร์เสื้อที่ทำการ Retired** - <font color="white">6 (11, 22, 23, 24, 34, 45)</font>
        """, unsafe_allow_html=True)
    
    #Houston Rockets link
    st.markdown("[official website](https://www.nba.com/rockets)")
    st.markdown("[ประวัติเต็มๆ](https://www.blockdit.com/posts/5ff87a9935c89e0ee6754b84?id=5ff87a9935c89e0ee6754b84&series=5f97ea813ea0500c89ca96cd)")


    #Memphis Grizzlies เมมฟิส กริซลีส์
    st.markdown("<font color='blue'><h2>Memphis Grizzlies</h2></font>", unsafe_allow_html=True)
    st.markdown("<font color='white '><p>เมมฟิส กริซลีส์</p></font>", unsafe_allow_html=True)

    #Memphis Grizzlies png
    Memphis_Grizzlies_png = "https://upload.wikimedia.org/wikipedia/en/thumb/f/f1/Memphis_Grizzlies.svg/800px-Memphis_Grizzlies.svg.png"
    st.image(Memphis_Grizzlies_png, caption='Memphis Grizzlies Logo', width=100, use_column_width=True)

    #Memphis Grizzlies main
    st.markdown("<p style='color: white;'>เมมฟิสกริซลีเป็นชาวอเมริกันมืออาชีพบาสเกตบอลทีมที่อยู่ในเมมฟิสรัฐเทนเนสซี ริซลี่แข่งขันในสมาคมบาสเกตบอลแห่งชาติ (NBA) เป็นสมาชิกของลีกประชุมตะวันตก ภาคตะวันตกเฉียงใต้กอง ริซลี่เล่นเกมในบ้านของพวกเขาที่FedExForum ทีมที่เป็นเจ้าของโดยโรเบิร์ต Pera ริซลี่ขณะนี้ทีมเดียวในอาชีพหลักอเมริกาเหนือลีกกีฬาในเมืองเมมฟิสและเป็นทีมบาสเกตบอลเพียงมืออาชีพในรัฐเทนเนสซี ทีมแรกที่จัดตั้งขึ้นเป็นแวนคูเวอร์ริซลี่การขยายตัวของทีมที่เข้าร่วมในเอ็นบีเอฤดูกาล 1995-96 หลังจากสิ้นสุดฤดูกาล 2000-01กริซลี่ส์ย้ายไปเมมฟิส</p>", unsafe_allow_html=True)
    st.markdown("""
        - **สังกัดในฝั่งตะวันตก** - <font color="white">Southwest Division</font>
        - **ปีที่ก่อตั้ง** - <font color="white">1995</font>
        - **ชื่อเดิม** - <font color="white">Vancouver Grizzlies (1995-2001), Memphis Grizzlies (2001-ปัจจุบัน)</font>
        - **สถานที่ตั้ง** - <font color="white">เมือง Memphis รัฐ Tennessee</font>
        - **ชื่อสนามเหย้า** - <font color="white">FedExForum</font>
        - **เจ้าของทีม** - <font color="white">Memphis Basketball, LLC</font>
        - **CEO** - <font color="white">Jeanie Buss</font>
        - **GM (General Manager)** - <font color="white">Robert Pera</font>
        - **HC (Head Coach)** - <font color="white">Taylor Jenkins</font>
        - **ทีมสังกัดใน G-League** - <font color="white">Memphis Hustle</font>
        - **จำนวนครั้งที่ได้แชมป์ลีก** - <font color="white">0</font>
        - **จำนวนครั้งที่ได้แชมป์ฝั่งทวีป** - <font color="white">0</font>
        - **จำนวนครั้งที่ได้แชมป์ Division** - <font color="white">0</font>
        - **จำนวนเบอร์เสื้อที่ทำการ Retired** - <font color="white">ไม่มี</font>
        """, unsafe_allow_html=True)

    #Memphis Grizzlies link
    st.markdown("[official website](https://www.nba.com/grizzlies/)")
    st.markdown("[ประวัติเต็มๆ](https://www.blockdit.com/posts/60262b0940b9e70b9d1f6e81?id=60262b0940b9e70b9d1f6e81&series=5f97ea813ea0500c89ca96cd)")


    #New Orleans Pelicans นิว ออร์ลีนส์ พิลีแกนส์
    st.markdown("<font color='yellow'><h2>New Orleans Pelicans</h2></font>", unsafe_allow_html=True)
    st.markdown("<font color='blue '><p>นิว ออร์ลีนส์ พิลีแกนส์</p></font>", unsafe_allow_html=True)

    #New Orleans Pelicans png
    New_Orleans_Pelicans_png = "https://upload.wikimedia.org/wikipedia/en/thumb/0/0d/New_Orleans_Pelicans_logo.svg/1920px-New_Orleans_Pelicans_logo.svg.png"
    st.image(New_Orleans_Pelicans_png, caption='New Orleans Pelicans Logo', width=100, use_column_width=True)

    #New Orleans Pelicans main
    st.markdown("<p style='color: white;'>New Orleans Pelicans เป็นอเมริกันมืออาชีพบาสเกตบอลทีมที่อยู่ในนิวออร์, หลุยเซีย Orleans เป็นสโมสรสมาชิกของกองตะวันตกเฉียงใต้ของสายตะวันตกในสมาคมบาสเกตบอลแห่งชาติ (NBA) ทีมที่เล่นเกมในบ้านของพวกเขาในสมูทตี้คิงศูนย์ (เดิมชื่อนิวออร์อารีน่า)นกกระยางถูกจัดตั้งขึ้นเป็นนิวออร์ฮอร์เน็ตในฤดูกาล2002-03 เมื่อนั้นเจ้าของลอตต์ฮอร์เน็ต, จอร์จ Shinnย้ายแฟรนไชส์ให้กับนิวออร์ เนื่องจากความเสียหายที่เกิดจากพายุเฮอริเคนแคทรีนาในปี2005 แฟรนไชส์ย้ายชั่วคราวไปโอคลาโฮมาซิตีที่พวกเขาใช้เวลาสองฤดูกาลที่รู้จักกันอย่างเป็นทางการเป็นนิวออร์ / โอคลาโฮมาซิตีฮอร์เน็ต ทีมงานกลับไปนิวออร์เต็มเวลาสำหรับฤดูกาล 2007-08 เมื่อวันที่ 24 มกราคม 2013, แฟรนไชส์ประกาศว่าจะเปลี่ยนชื่อตัวเองนกกระยางได้. การเปลี่ยนแปลงชื่อนกกระยางมีผลหลังจากที่ข้อสรุปของฤดูกาล 2012-13 ชาร์ลอฮอร์เน็ตชื่อประวัติศาสตร์และระเบียนจาก 1988-2002 ถูกส่งกลับไปยังเมืองเดิมที่จะใช้จากนั้นลอตต์บ็อบแคทแฟรนไชส์ซึ่งต่อมากลายเป็นลอตต์ฮอร์เน็ตเริ่มต้นที่ 20 พฤษภาคม 2014 ในฤดูกาลที่ 13 ของการเล่นตั้งแต่แฟรนไชส์เดิมย้ายมาจากแคโรไลนา, แฟรนไชส์หลุยเซียได้ประสบความสำเร็จฤดูกาลปกติโดยรวมของ 498-552 และมีคุณสมบัติในการแข่งขันรอบตัดเชือกหกครั้ง ความสำเร็จของพวกเขารวมถึงชัยชนะท่องเที่ยวแบบหนึ่งและแบ่งหัวข้อหนึ่ง</p>", unsafe_allow_html=True)
    st.markdown("""
        - **สังกัดในฝั่งตะวันตก** - <font color="white">Southwest Division</font>
        - **ปีที่ก่อตั้ง** - <font color="white">2002</font>
        - **ชื่อเดิม** - <font color="white">New Orleans Hornets (2002-2005, 2007-2013), New Orleans/Oklahoma City Hornets (2005-2007), New Orleans Pelicans (2013-ปัจจุบัน)</font>
        - **สถานที่ตั้ง** - <font color="white">เมือง New Orleans รัฐ Louisiana</font>
        - **ชื่อสนามเหย้า** - <font color="white">Smoothie King Center</font>
        - **เจ้าของทีม** - <font color="white">Gayle Benson</font>
        - **CEO** - <font color="white">Gayle Benson</font>
        - **GM (General Manager)** - <font color="white">Trajan Langdon</font>
        - **HC (Head Coach)** - <font color="white">Stan Van Gundy</font>
        - **ทีมสังกัดใน G-League** - <font color="white">Erie BayHawks</font>
        - **จำนวนครั้งที่ได้แชมป์ลีก** - <font color="white">0</font>
        - **จำนวนครั้งที่ได้แชมป์ฝั่งทวีป** - <font color="white">0</font>
        - **จำนวนครั้งที่ได้แชมป์ Division** - <font color="white">1 (2008)</font>
        - **จำนวนเบอร์เสื้อที่ทำการ Retired** - <font color="white">1 (7)</font>
        """, unsafe_allow_html=True)
    
    #New Orleans Pelicans link
    st.markdown("[official website](https://www.nba.com/pelicans/)")
    st.markdown("[ประวัติเต็มๆ](https://www.blockdit.com/posts/6060888b02d45e0c44e8914f?id=6060888b02d45e0c44e8914f&series=5f97ea813ea0500c89ca96cd)")


    #San Antonio Spurs ซานแอนโตนิโอ สเปอรส์
    st.markdown("<font color='black'><h2>San Antonio Spurs</h2></font>", unsafe_allow_html=True)
    st.markdown("<font color='white '><p>ซานแอนโตนิโอ สเปอรส์</p></font>", unsafe_allow_html=True)

    #San Antonio Spurs png
    San_Antonio_Spurs_png = "https://upload.wikimedia.org/wikipedia/en/thumb/a/a2/San_Antonio_Spurs.svg/1920px-San_Antonio_Spurs.svg.png"
    st.image(San_Antonio_Spurs_png, caption='San Antonio Spurs Logo', width=100, use_column_width=True)

    #San Antonio Spurs main
    st.markdown("<p style='color: white;'>แซน แอนโตนิโอ สเปอร์ส (อังกฤษ: San Antonio Spurs) เป็นทีมบาสเกตบอลอาชีพในลีกเอ็นบีเอของสหรัฐอเมริกา อยู่เมืองแซน แอนโตนิโอ รัฐเท็กซัสก่อตั้งขึ้นเมื่อปี พ.ศ. 2510 (ค.ศ. 1967) เดิมอยู่ลีกเอบีเอ สเปอร์สเป็นทีมเดียวที่มาจากเอบีเอที่เคยได้แชมป์เอ็นบีเอ โดยได้แชมป์ทั้งหมด 4 สมัย และเมื่อนับสถิติการเล่นจากอดีตจนถึงพฤศจิกายน พ.ศ. 2549 สเปอร์สมีสถิติเปอร์เซนต์ชนะสูงเป็นอันดับที่สองรองจากทีม ลอส แอนเจลิส เลเกอร์ส และพลาดการเล่นเพลย์ออฟเพียงสี่ฤดูกาลเท่านั้น</p>", unsafe_allow_html=True)
    st.markdown(""" 
        - **การประชุม** - <font color="white">ตะวันตก</font>
        - **แผนก** - <font color="white">ตะวันตกเฉียงใต้</font>
        - **ก่อตั้งขึ้น** - <font color="white">พ.ศ. 2510</font>
        - **ประวัติศาสตร์** - <font color="white">Dallas Chaparrals 1967–1970, 1971–1973 (ABA) Texas Chaparrals 1970–1971 (ABA) San Antonio Spurs 1973–1976 (ABA) 1976 - ปัจจุบัน (NBA)</font>
        - **อารีน่า** - <font color="white">ศูนย์ AT&T</font>
        - **สถานที่** - <font color="white">ซานอันโตนิโอเท็กซัส</font>
        - **สีของทีม** - <font color="white">ดำเงิน</font>
        - **ผู้สนับสนุนหลัก** - <font color="white">ฟรอสต์แบงก์</font>
        - **ประธาน** - <font color="white">Gregg Popovich</font>
        - **ผู้จัดการทั่วไป** - <font color="white">ไบรอันไรท์</font>
        - **หัวหน้าโค้ช** - <font color="white">Gregg Popovich</font>
        - **กรรมสิทธิ์** - <font color="white">Spurs Sports & Entertainment (ปีเตอร์จอห์นโฮลท์ประธานและซีอีโอ)</font>
        - **สังกัด** - <font color="white">ออสตินสเปอร์ส</font>
        - **ประชัน** - <font color="white">5 ( 2542 , 2546 , 2548 , 2550 , 2557 )</font>
        - **ชื่อการประชุม** - <font color="white">6 ( 2542 , 2546 , 2548 , 2550 , 2556 , 2557 )</font>
        - **ชื่อกอง** - <font color="white">22 ( 2521 , 2522 , 2524 , 2525 , 2526 , 2533 , 2534 , 2538 , 2539 , 2542 , 2544 , 2545 , 2546 , 2548 , 2549 , 2552 , 2554 , 2555 , 2556 , 2557 , 2559 , 2560 )</font>
        - **หมายเลขเกษียณ** - <font color="white">10 ( 00 , 6 , 9 , 12 , 13 , 20 , 21 , 32 , 44 , 50 )</font>
        """, unsafe_allow_html=True)
    
    #San Antonio Spurs link
    st.markdown("[official website](https://www.nba.com/spurs/)")
    st.markdown("[ประวัติเต็มๆ](https://hmong.in.th/wiki/San_Antonio_Spurs)")

