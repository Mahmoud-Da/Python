#play with pandas

from pandas import DataFrame
shops =['A店', 'B店', 'C店', 'D店', 'E店', 'F店', 
        'A店', 'B店', 'C店', 'D店', 'E店', 'F店']

vals = [98700, 87600, 76500, 65400, 54300, 43200,
        123400, 67890, 34560,9100, 8760, 7650]

season =['上期', '上期', '上期', '上期', '上期', '上期', 
        '下期', '下期', '下期', '下期', '下期', '下期']
data = list(zip(shops,vals,season))
df = DataFrame(data=data,columns=('店名', '売上', '期間'))
df

#
import altair as alt
season_name = "上期" #@param ["上期", "下期"]
df2 = df.query('期間 == "' + season_name + '"')

alt.Chart(df2).mark_bar().encode(
    x = '売上',
    y = '店名'
)
#
crt = alt.Chart(df)

crt.mark_bar().encode(
    x = '売上',
    y = '店名',
    row = '期間'
)
#
crt = alt.Chart(df)

crt.mark_bar().encode(
    x = '売上',
    y = '店名',
    column = '期間'
)
#
crt = alt.Chart(df)

crt.mark_bar(color='red').encode(
    x = '売上',
    y = '店名'
)
#
crt = alt.Chart(df)

crt.mark_bar().encode(
    x = '売上',
    y = '店名',
    color = '期間'
)
#
crt = alt.Chart(df)

crt.mark_bar().encode(
    x = '売上',
    y = '店名',
    row = '期間',
    color = '店名'
)

#
crt = alt.Chart(df)

crt.mark_bar().encode(
    x = '売上',
    y = '店名',
    row = '期間',
    color = '売上'
)
