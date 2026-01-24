
import json
import uuid

def create_markdown_cell(content):
    return {
        'cell_type': 'markdown',
        'id': str(uuid.uuid4())[:8],
        'metadata': {},
        'source': [line + '\n' for line in content.strip().split('\n')]
    }

def create_code_cell(content):
    return {
        'cell_type': 'code',
        'execution_count': None,
        'id': str(uuid.uuid4())[:8],
        'metadata': {},
        'outputs': [],
        'source': [line + '\n' for line in content.strip().split('\n')]
    }

file_path = r'e:\AI_Chilla\AI_CHILLA_2026\Repositories\ai_chilla\Data_Visualization\data_visualization.ipynb'

cells = []

# 1. PREMIUM HEADER (DESI VERSION)
header = """
<div style='background-color: #004d40; color: white; padding: 30px; border-radius: 15px; text-align: center; border: 5px solid #00251a; box-shadow: 0 4px 8px rgba(0,0,0,0.2);'>
    <h1 style='font-family: "Outfit", sans-serif; font-weight: 800; font-size: 45px; margin: 0;'>🎨 Data Visualization Ka Masterclass</h1>
    <h3 style='font-family: "Inter", sans-serif; font-weight: 400; opacity: 0.9;'>Full Professional Scene with 18 High-Impact Plots</h3>
    <hr style='border: 1px solid rgba(255,255,255,0.2); width: 50%; margin: 20px auto;'>
    <p style='font-size: 18px;'><b>Author:</b> <span style='color: #80cbc4;'>Muhammad Usman</span> | <i>Scientific Officer</i></p>
    <div style='display: flex; justify-content: center; gap: 15px; margin-top: 15px;'>
        <span style='background: #80cbc4; color: #004d40; padding: 5px 15px; border-radius: 20px; font-weight: bold;'>Kaggle Top Rank Scene</span>
        <span style='background: #80cbc4; color: #004d40; padding: 5px 15px; border-radius: 20px; font-weight: bold;'>DS Engineer</span>
    </div>
</div>
""".strip()
cells.append(create_markdown_cell(header))

# 2. FOUNDATIONS (DESI STYLE)
gog_section = """
## 🚀 Scene Kya Hai: Data Visualization Aur Iska Tariqa-e-Kaar

Assalam-o-Alaikum! Data Visualization ka matlab hai ke numbers aur bore data ko graphics mein badal dena taake fauto-fat sab samajh aa jaye. Yeh sirf 'khoobsurat graphs' ka naam nahi, balkay dimaag ko asani dene ka scene hai.

### Grammar of Graphics (GoG) - Asal Recipe
Jese Biryani ke liye chawal, gosht aur masalay chahiye hotay hain, wese hi har graph ke 7 main ingredients hotay hain:
- **Data**: Jo bhi hamara raw maal (CSV wagera) hai.
- **Aesthetics (AES)**: Kon sa pillar kidher jaye ga (X, Y) aur rang (Color) konsa hoga.
- **Geoms**: Graph ki shakal kesi hogi (Dots, Lines, bars).
- **Facets**: Aik hi screen pe chotay chotay partition bana dena.
- **Statistics**: Mean, Median wagera nikalna.
- **Coordinates**: Graph ka map (Linear ya Polar).
- **Themes**: Graph ka look aur feel (Piche ka background, fonts).
""".strip()
cells.append(create_markdown_cell(gog_section))

# 3. SETUP
setup_code = """
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import altair as alt
from plotnine import *
import folium
from folium.plugins import MarkerCluster, HeatMap

# Sample Datasets load ho rahe hain
tips = sns.load_dataset('tips')
iris = sns.load_dataset('iris')
gapminder = px.data.gapminder().query("year == 2007")

# Aesthetics set karein
sns.set_theme(style="whitegrid", palette="viridis")
plt.rcParams['figure.figsize'] = (10, 6)
print("Chalo bhai, system set hai! Data aur libraries load ho gayi hain.")
""".strip()
cells.append(create_code_cell(setup_code))

# --- MATPLOTLIB ---
cells.append(create_markdown_cell("# 🛠️ Section 1: Matplotlib (Original Foundation)"))

# 1.1 Line
cells.append(create_markdown_cell("""
### 1.1 Line Plot with Variance (Utaar Charhao Scene)
**Maqsad**: Jab dekhna ho ke time ke sath data kahan ja raha hai aur uncertainty kitni hai.
**Sabak**: Beech wali line trend batati hai aur shaded area batata hai ke scene kitna risk pe hai.
**Kaggle Tip**: Scientific plots mein yeh shaded area lazmi dikhayen, impression fit ho jata hai.
""".strip()))
cells.append(create_code_cell("""
x = np.linspace(0, 10, 100)
y = np.cumsum(np.random.randn(100))
plt.plot(x, y, color='#00796b', lw=3, label='Beech Wali Line')
plt.fill_between(x, y-5, y+5, color='#b2dfdb', alpha=0.3, label='Risk Area')
plt.title('Time ke sath Data ka Safar', fontsize=14)
plt.xlabel('Time Index')
plt.ylabel('Value')
plt.legend()
plt.show()
""".strip()))

# 1.2 Scatter
cells.append(create_markdown_cell("""
### 1.2 Multi-Dimensional Scatter Plot (Doston ka Group)
**Maqsad**: Do variables ka aapas mein talluq dekhna, aur rang aur size se mazeed info nikalna.
**Sabak**: Jo dots qareeb hain woh aik hi party ke hain. Size batata hai ke kiska wazan zyada hai.
**Kaggle Tip**: Feature engineering ke waqt clusters dekhne ke liye best cheez hai.
""".strip()))
cells.append(create_code_cell("""
plt.scatter(iris['sepal_length'], iris['sepal_width'], 
            c=iris['petal_length'], cmap='viridis', 
            s=iris['petal_width']*70, alpha=0.7)
plt.colorbar(label='Petal ki Length (Wazan)')
plt.title('Iris ka Full Depth Comparison', fontsize=14)
plt.xlabel('Sepal Length')
plt.ylabel('Sepal Width')
plt.show()
""".strip()))

# 1.3 Bar
cells.append(create_markdown_cell("""
### 1.3 Bar Chart with Error Caps (Muqabla Scene)
**Maqsad**: Mukhtalif groups ka aapas mein model test karna.
**Sabak**: Bar ki unchai average batati hai, aur upar wali dandi (error bar) batati hai ke data kitna hil raha hai.
**Kaggle Tip**: Categorical analysis mein bar chart se behtar koi scene nahi.
""".strip()))
cells.append(create_code_cell("""
means = tips.groupby('day')['total_bill'].mean()
errors = tips.groupby('day')['total_bill'].std()
plt.bar(means.index, means.values, yerr=errors, capsize=12, color='#004d40', alpha=0.8)
plt.title('Din ke hisab se Bill ka Average', fontsize=14)
plt.ylabel('Mean Bill Amount ($)')
plt.show()
""".strip()))

# --- SEABORN ---
cells.append(create_markdown_cell("# 🌊 Section 2: Seaborn (Stylista Graphics)"))

# 2.1 Violin
cells.append(create_markdown_cell("""
### 2.1 Split Violin Plot (Distribution ka Shashka)
**Maqsad**: Data ki bheer (density) dekhna. Beech se split karne se Males aur Females ka muqabla foran ho jata hai.
**Sabak**: Jahan se violin mota hai, wahan data zyada hai.
**Kaggle Tip**: Simple box plot se behtar hai violin plot use karein, professional lagta hai.
""".strip()))
cells.append(create_code_cell("""
sns.violinplot(data=tips, x='day', y='total_bill', hue='sex', split=True, palette='coolwarm')
plt.title('Bill ki Distribution: Gender vs. Day Muqabla', fontsize=14)
plt.show()
""".strip()))

# 2.2 Heatmap
cells.append(create_markdown_cell("""
### 2.2 Correlation Heatmap (Aapsi Rishta)
**Maqsad**: Puray dataset mein kon kon se variables aapas mein mile hue hain.
**Sabak**: Jitna gehra rang (1.0 ke qareeb), utna pakka rishta.
**Kaggle Tip**: Faltu variables drop karne ke liye yeh graph life-saver hai.
""".strip()))
cells.append(create_code_cell("""
corr = iris.drop('species', axis=1).corr()
sns.heatmap(corr, annot=True, cmap='YlGnBu', fmt=".2f")
plt.title('Variables ka Aapsi Mel Jole', fontsize=14)
plt.show()
""".strip()))

# 2.3 Joint
cells.append(create_markdown_cell("""
### 2.3 Joint Regression Plot (Do-Tok Baat)
**Maqsad**: Scatter aur Histogram ka combo. Trend line bhi mil jati hai.
**Sabak**: Line batati hai ke trend positive ja raha hai ya negative.
**Kaggle Tip**: Regression model se pehle outliers check karne ke liye is se fit kuch nahi.
""".strip()))
cells.append(create_code_cell("""
sns.jointplot(data=tips, x='total_bill', y='tip', kind='reg', color='#00796b')
plt.show()
""".strip()))

# --- PLOTLY ---
cells.append(create_markdown_cell("# 🎇 Section 3: Plotly (Interactive Magic)"))

# 3.1 Bubble
cells.append(create_markdown_cell("""
### 3.1 Animated Bubble Chart (Duniya Ghoom Lo)
**Maqsad**: Waqt ke sath trends kese badaltay hain. Bubble ka size population dikhata hai.
**Sabak**: Play ka button dabayen aur dekhen 2007 tak duniya kahan gayi.
**Kaggle Tip**: Presentation notebooks mein yeh graph add karein, rankings upar jayein gi.
""".strip()))
cells.append(create_code_cell("""
fig = px.scatter(px.data.gapminder(), x="gdpPercap", y="lifeExp", animation_frame="year", 
                 size="pop", color="continent", hover_name="country", log_x=True, size_max=50,
                 title="GDP vs Life Expectancy ka Safar")
fig.show()
""".strip()))

# 3.2 Sunburst
cells.append(create_markdown_cell("""
### 3.2 Sunburst Chart (Andar ki Baat)
**Maqsad**: Nested categories dekhna (Day -> Time -> Sex).
**Sabak**: Aik circle ke andar dusra circle, hierarchy foran samajh aa jati hai.
**Kaggle Tip**: E-commerce sales ko breakdown karne ke liye zabardast cheez hai.
""".strip()))
cells.append(create_code_cell("""
fig = px.sunburst(tips, path=['day', 'time', 'sex'], values='total_bill', 
                  color='total_bill', color_continuous_scale='Viridis',
                  title="Bill Breakdown ka Full Scene")
fig.show()
""".strip()))

# 3.3 3D
cells.append(create_markdown_cell("""
### 3.3 Interactive 3D Scatter (Har Angle se Check Karein)
**Maqsad**: 3 variables ko aik sath 3D space mein dekhna.
**Sabak**: Mouse se rotate karein aur clusters ko har side se check karein.
**Kaggle Tip**: Complex features ko visualize karne ke liye best graph hai.
""".strip()))
cells.append(create_code_cell("""
fig = px.scatter_3d(iris, x='sepal_length', y='sepal_width', z='petal_width', color='species',
                    symbol='species', title="3D Space mein Species ka Muqabla")
fig.show()
""".strip()))

# --- ALTAIR ---
cells.append(create_markdown_cell("# 📊 Section 4: Altair (Logic Based)"))

# 4.1 Linked
cells.append(create_markdown_cell("""
### 4.1 Linked Selection (Mouse ka Kamaal)
**Maqsad**: Graph pe kahin bhi select karein aur baki dots gray ho jayen gay.
**Sabak**: Is se specific areas ko zoom-in kiya ja sakta hai.
**Kaggle Tip**: User interactivity ke liye Altair ka koi muqabla nahi.
""".strip()))
cells.append(create_code_cell("""
brush = alt.selection_interval()
alt.Chart(iris).mark_point().encode(
    x='sepal_length',
    y='sepal_width',
    color=alt.condition(brush, 'species', alt.value('lightgray'))
).add_params(brush).properties(title="Select karein aur Focus Jamayen")
""".strip()))

# 4.2 Sorted
cells.append(create_markdown_cell("""
### 4.2 Sorted Bar Chart (Number One Kon?)
**Maqsad**: Categories ko unke wazan ke hisab se sort karna.
**Sabak**: Bars automically top-performer ko upar le aati hain.
**Kaggle Tip**: Ranking reports banane ke liye best logic hai.
""".strip()))
cells.append(create_code_cell("""
alt.Chart(tips).mark_bar().encode(
    x='mean(total_bill):Q',
    y=alt.Y('day:N', sort='-x'),
    color='day:N'
).properties(title="Ranking Scene (Top Business Days)")
""".strip()))

# 4.3 Area
cells.append(create_markdown_cell("""
### 4.3 Faceted Area Chart (Aapne Aapne Hisab se)
**Maqsad**: Component growth dekhna mukhtalif sections mein.
**Sabak**: Side-by-side muqabla Males aur Females ka.
**Kaggle Tip**: Time-series trends split karke dikhane ke liye use karein.
""".strip()))
cells.append(create_code_cell("""
alt.Chart(tips).mark_area(opacity=0.6).encode(
    x="total_bill:Q", y="tip:Q", color="day:N"
).facet(column='sex:N').properties(title="Group-wise Growth ka Scene")
""".strip()))

# --- PLOTNINE ---
cells.append(create_markdown_cell("# 🏗️ Section 5: Plotnine (Asal Purist)"))

# 5.1 Smooth
cells.append(create_markdown_cell("""
### 5.1 Faceted Regression (Alag Alag Trend)
**Maqsad**: ggplot2 ka logic Python mein. Har din ka alag trend dekhen.
**Sabak**: Facets banane se data clear ho jata hai ke kahan masla hai.
**Kaggle Tip**: Advanced correlation studies ke liye plotnine lazmi seekhen.
""".strip()))
cells.append(create_code_cell("""
(ggplot(tips, aes(x='total_bill', y='tip', color='time'))
 + geom_point(alpha=0.6)
 + geom_smooth(method='lm')
 + facet_wrap('~day')
 + theme_minimal()
 + labs(title='Rozana ke hisab se Bill vs Tip ka Scene'))
""".strip()))

# 5.2 Ridges
cells.append(create_markdown_cell("""
### 5.2 Density Ridges (Mahaul Level)
**Maqsad**: Overlapping distributions dekhna.
**Sabak**: Paharoon ki trah data density show hoti hai.
**Kaggle Tip**: Comparison reports mein visual impact fit karne ke liye perfect hai.
""".strip()))
cells.append(create_code_cell("""
(ggplot(tips, aes(x='total_bill', fill='day'))
 + geom_density(alpha=0.6)
 + scale_fill_brewer(type='qual', palette='Set1')
 + theme_minimal()
 + labs(title='Bill Density ka Pahar (Overlapping Scene)'))
""".strip()))

# 5.3 Box
cells.append(create_markdown_cell("""
### 5.3 Outlier Mapping Grid (Scrutiny Scene)
**Maqsad**: Faltu data (Outliers) pakarna har level pe.
**Sabak**: Jo dots box se bahar hain, woh outliers hain.
**Kaggle Tip**: Data cleaning ki logic justify karne ke liye best tool hai.
""".strip()))
cells.append(create_code_cell("""
(ggplot(tips, aes(x='time', y='total_bill', fill='time'))
 + geom_boxplot(show_legend=False)
 + facet_wrap('~day')
 + theme_classic()
 + labs(title='Outliers pakro har Partition mein'))
""".strip()))

# --- FOLIUM ---
cells.append(create_markdown_cell("# 🌍 Section 6: Folium (Apna Pakistan Context)"))

# NEW FOLIUM DATA
folium_data_setup = """
# Pakistan ke Sheharon ka Data
pak_cities = {
    'City': ['Karachi', 'Lahore', 'Faisalabad', 'Rawalpindi', 'Gujranwala', 
             'Peshawar', 'Multan', 'Islamabad', 'Quetta', 'Hyderabad'],
    'Lat': [24.86, 31.52, 31.41, 33.56, 32.18, 34.01, 30.15, 33.68, 30.17, 25.39],
    'Lon': [67.01, 74.35, 73.07, 73.01, 74.19, 71.52, 71.52, 73.04, 66.97, 68.37],
    'Population_M': [14.9, 11.1, 3.2, 2.1, 2.0, 1.9, 1.8, 1.0, 1.0, 1.7],
    'Province': ['Sindh', 'Punjab', 'Punjab', 'Punjab', 'Punjab', 
                'KPK', 'Punjab', 'ICT', 'Balochistan', 'Sindh']
}
df_pak = pd.DataFrame(pak_cities)
""".strip()
cells.append(create_code_cell(folium_data_setup))

# 6.1 Cluster
cells.append(create_markdown_cell("""
### 6.1 Urban Hub Cluster (Points Jamayen)
**Maqsad**: Map pe bohat sare locations ko group karna taake map kachra na lagay.
**Sabak**: Click karein gay to clusters khulen gay aur details milen gi.
**Kaggle Tip**: Logistics aur distribution networks dikhane ke liye top choice hai.
""".strip()))
cells.append(create_code_cell("""
m1 = folium.Map(location=[30.3753, 69.3451], zoom_start=5, tiles='cartodbpositron')
cluster = MarkerCluster().add_to(m1)
for i, row in df_pak.iterrows():
    folium.Marker(
        [row['Lat'], row['Lon']],
        popup=f"<b>{row['City']}</b><br>Aabadi: {row['Population_M']}M<br>Suba: {row['Province']}"
    ).add_to(cluster)
m1
""".strip()))

# 6.2 Heatmap
cells.append(create_markdown_cell("""
### 6.2 Population Heatmap (Kahan kitni Bheer?)
**Maqsad**: Dekhna ke Pakistan mein sab se zyada aabadi kahan concentrated hai.
**Sabak**: Red spots matlab buhat zyada density. Karachi aur Central Punjab 'hot' hain.
**Kaggle Tip**: Regional demand ya health data analyze karne ke liye fit graph hai.
""".strip()))
cells.append(create_code_cell("""
m2 = folium.Map(location=[30, 70], zoom_start=5, tiles='cartodbpositron')
heat_data = df_pak[['Lat', 'Lon', 'Population_M']].values.tolist()
HeatMap(heat_data, radius=25, blur=15).add_to(m2)
m2
""".strip()))

# 6.3 Circle
cells.append(create_markdown_cell("""
### 6.3 Size Comparison (Kis Shehar ka kitna Wazan?)
**Maqsad**: Sheharon ka muqabla aabadi ke size se map pe karna.
**Sabak**: Circle jitna bada, shehar ka magnitude utna fit.
**Kaggle Tip**: GDP ya Business size dikhane ke liye map pe proportional circles best hain.
""".strip()))
cells.append(create_code_cell("""
m3 = folium.Map(location=[30, 70], zoom_start=5, tiles='openstreetmap')
for i, row in df_pak.iterrows():
    folium.Circle(
        location=[row['Lat'], row['Lon']],
        radius=row['Population_M'] * 10000, 
        color='#004d40',
        fill=True,
        fill_opacity=0.6,
        popup=f"{row['City']}: {row['Population_M']}M Logo Ki Bheer"
    ).add_to(m3)
m3
""".strip()))

# FINAL FOOTER (DESI)
cells.append(create_markdown_cell("""
<div style='background-color: #004d40; color: white; padding: 25px; border-radius: 15px; text-align: center;'>
    <h3>🌟 Masterclass Khatam: Data ke Don Ban Jao</h3>
    Ab aapke paas 18 fit tareen graphs ki recipe hai. Kaggle pe upload karein aur dunya ko apna talent dikhayen.
    <br><br>
    <i>"Data bolta hai, bas usay dikhana aana chahiye." — Muhammad Usman</i>
</div>
""".strip()))

nb = {
    'cells': cells,
    'metadata': {
        'kernelspec': {'display_name': 'python3', 'name': 'python3'},
        'language_info': {'name': 'python', 'version': '3.14.2'}
    },
    'nbformat': 4, 'nbformat_minor': 5
}

with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=1)

print("Fit hai boss! Notebook Desi Style mein update ho gayi hai.")
