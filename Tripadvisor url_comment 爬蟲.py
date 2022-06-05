def url_comment(brand_URL,brand,dish_type):
    final_list   = []  #最終
    comment_list = []
    for URL in brand_URL:
        driver.get(f"https://www.tripadvisor.com.tw{URL}")
        time.sleep(1)
        soup = BeautifulSoup(driver.page_source)
        try:
            title = soup.find_all('li',{'class':'breadcrumb'}) #店名
            score_text = soup.find_all('label',{'class':'row_label label no_display'}) #文字 EX :超棒很棒超級棒
            Store_address = soup.find('span',{'class':'brMTW'}).text #店家地址
            score_text_quantity = soup.find_all('span',{'class':'row_num'}) #跟上一行文字對應的數量 
            score = soup.find('div',{'class':'eEwDq'}).text.split()[0] #總評分數 EX: 4.5 分
            number_of_comments = soup.find('div',{'class':'eEwDq'}).text.split()[1] #總評論數 很棒 (365)<--這邊指這個數字
            comment_title = soup.find_all('span',{'class':'noQuotes'}) #評論標題
            comment = soup.find_all('p',{'class':'partial_entry'}) #評論
            comment_time = soup.find_all('span',{'class':'ratingDate'}) #留言時間
            comment_score = soup.find_all('div',{'class':'ui_column is-9'}) #留言分數
            print('收錄：',title[-1].text)
        
        except: 
            title = soup.find_all('li',{'class':'breadcrumb'}) #店名
            print('未收錄：',title[-1].text)
            continue
        if brand in title[-1].text:
            for x,y,z,w in zip(comment_title,comment,comment_time,comment_score):
                comment_list.append({
                '來源網站':'Tripadvisor',
                '集團':'王品',
                '品牌':brand,
                '店名':title[-1].text,
                '店家地址':Store_address,
                '評論標題':x.text,
                '發表時間':z.text.replace('的評論',''),
                '評論內容':y.text,
                '個別評分':int(w.find('span').get('class')[1].split('_')[1])/10
                })
            time.sleep(1)
        # 資料爬取：ID 來源網站 集團 品牌 標題 文章內容 發表時間(年月日) 評分 瀏覽數 按讚數 收藏數 推薦/轉發數 留言數 正/負評 菜系
            final_list.append({
                '來源網站':'Tripadvisor',
                '集團':'王品',
                '品牌':brand,
                '店名':title[-1].text,
                '店家地址':Store_address,
                '總評分':score,
                '總評論數':number_of_comments,
                '很棒':score_text_quantity[0].text,
                '非常好':score_text_quantity[1].text,
                '一般':score_text_quantity[2].text,
                '差':score_text_quantity[3].text,
                '糟透了':score_text_quantity[4].text,
                '菜系':dish_type
                })

    print(len(final_list))
    df_final = pd.DataFrame(final_list)
    df_comment = pd.DataFrame(comment_list)
    return df_final,df_comment

if __name__=='__main__':
    ni_df1,ni_df2 = url_comment(ni,'夏慕尼','法式鐵板燒')
    mini_df1,mini_df2 = url_comment(mini,'12MINI','經典獨享鍋')
    duck_df1,duck_df2 = url_comment(enjoy_duck,'享鴨','烤鴨與中華料理')
    blue_flower_df1,blue_flower_df2 = url_comment(blue_flower,'青花驕','麻辣鍋')
    hokaido_df1,hokaido_df2 = url_comment(hokaido,'聚','北海道昆布鍋')
    putien_df1,putien_df2 = url_comment(putien,'莆田','新加坡料理')
    yiqi_df1,yiqi_df2 = url_comment(yiqi,'藝奇','新日本料理')
    pinpig_df1,pinpig_df2 = url_comment(pinpig,'品田牧場','日式豬排、咖哩')
    wang_df1,wang_df2 = url_comment(wang,'王品牛排','西式套餐')
    oburn_df1,oburn_df2 = url_comment(oburn,'原燒 O-NIKU','原味燒肉')
    city_df1,city_df2 = url_comment(city,'西堤牛排','西式套餐')
    house_df1,house_df2 = url_comment(house,'陶板屋','西式套餐')
    twelve_df1,twelve_df2 = url_comment(twelve,'石二鍋','涮涮鍋')
    hot7_df1,hot7_df2 = url_comment(hot7,'hot 7','新鉄板料理')
