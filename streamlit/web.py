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

left,right = st.columns(2)

# สร้าง sidebar
st.sidebar.header("Menu")

# สร้างปุ่มเพื่อเปลี่ยนหน้า
if st.sidebar.button("กติกา"):
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
    st.markdown("<h1 style='color: white;text-shadow: 2px 2px 4px #000000;'>NBA</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='color: white;'>เอ็นบีเอ (NBA) ย่อมาจาก National Basketball Association ซึ่งเป็นชื่อของลีกบาสเกตบอลอาชีพในอเมริกาเหนือ ซึ่งรวมประเทศสหรัฐอเมริกาและแคนาดา มีนักกีฬาบาสเก็ตบอลชั้นนำของโลกเล่นอยู่ในเอ็นบีเอนี้เป็นจำนวนมาก ซึ่งทำให้มาตรฐานระดับการแข่งขันนั้นถือว่าอยู่ในระดับสูง สัญลักษณ์ประจำเอ็นบีเอทางด้านขวานั้น เป็นภาพเงาของ เจอร์รี เวสต์ ซึ่งเคยเป็นผู้จัดการทั่วไปของทีมเลเกอร์ส และทีมเมมฟิส กริซลีส์</h3>", unsafe_allow_html=True)
    st.markdown("<h3 style='color: white;'>เอ็นบีเอ ก่อตั้งขึ้นที่นครนิวยอร์ก ในวันที่ 6 มิถุนายน ค.ศ. 1946 ในชื่อ Basketball Association of America (BAA) ซึ่งต่อมาเปลี่ยนชื่อเป็น National Basketball Association ในช่วงฤดูใบไม้ร่วงในปี ค.ศ. 1949 หลังจากการรวมตัวกับทีมจาก National Basketball League (NBL)</h3>", unsafe_allow_html=True)
    st.markdown("<h3 style='color: white;'>เอ็นบีเอนั้นเป็นลีกกีฬาอาชีพแรก ที่มีโค้ชหลักเป็นคนผิวดำ ในปี ค.ศ. 1966 และก็ยังเป็นลีกแรก ที่มีผู้จัดการทั่วไปเป็นคนผิวดำ ในปี ค.ศ. 1972 นอกจากนี้แล้ว ยังเป็นลีกแรก ที่มีเจ้าของทีมเป็นคนผิวดำ ในปี ค.ศ. 200</h3>", unsafe_allow_html=True)

    st.markdown("<h1 style='color: white;text-shadow: 2px 2px 4px #000000;'>อ้างอิง</h1>", unsafe_allow_html=True)
    st.markdown("https://th.wikipedia.org/wiki/%E0%B9%80%E0%B8%AD%E0%B9%87%E0%B8%99%E0%B8%9A%E0%B8%B5%E0%B9%80%E0%B8%AD")

if st.sidebar.button("Division"):
    division_option = st.sidebar.radio("Select Division", ["ATLANTIC", "CENTRAL", "SOUTHEAST","NORTHWEST", "PACIFIC","SOUTHWEST"])
    st.sidebar.write(f"You selected: {division_option}")
    
    if division_option == "ATLANTIC":
        st.markdown("<h1 style='color: red; text-shadow: 2px 2px white;'>ATLANTIC Division</h1>", unsafe_allow_html=True)
    tabs = st.columns(5)

    with st.container():
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
        
        st.markdown("[ประวัติเต็มๆ](https://www.blockdit.com/posts/5f99ac5e374f920ccb3c1122)")

        st.markdown("<h2 style='color: #006BB6;'>New York Knicks</h2>", unsafe_allow_html=True)
        st.markdown("<p style='color: white;'>นิวยอร์ก นิกส์</p>", unsafe_allow_html=True)

        st.markdown("<h2 style='color: #ED174C;'>Philadelphia 76ers</h2>", unsafe_allow_html=True)
        st.markdown("<p style='color: white;'>ฟิลาเดลเฟีย เซเวนตีซิกเซอร์ส</p>", unsafe_allow_html=True)

        st.markdown("<h2 style='color: #CE1141;'>Toronto Raptors</h2>", unsafe_allow_html=True)
        st.markdown("<p style='color: white;'>โทรอนโต แร็ปเตอร์ส์</p>", unsafe_allow_html=True)
