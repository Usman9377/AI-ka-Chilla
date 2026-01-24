
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

# 1. PREMIUM HEADER
header = """
<div style='background-color: #004d40; color: white; padding: 30px; border-radius: 15px; text-align: center; border: 5px solid #00251a; box-shadow: 0 4px 8px rgba(0,0,0,0.2);'>
    <h1 style='font-family: "Outfit", sans-serif; font-weight: 800; font-size: 45px; margin: 0;'>🎨 Data Visualization Masterclass</h1>
    <h3 style='font-family: "Inter", sans-serif; font-weight: 400; opacity: 0.9;'>Comprehensive Guide with 18 High-Impact Plots</h3>
    <hr style='border: 1px solid rgba(255,255,255,0.2); width: 50%; margin: 20px auto;'>
    <p style='font-size: 18px;'><b>Author:</b> <span style='color: #80cbc4;'>Muhammad Usman</span> | <i>Scientific Officer</i></p>
    <div style='display: flex; justify-content: center; gap: 15px; margin-top: 15px;'>
        <span style='background: #80cbc4; color: #004d40; padding: 5px 15px; border-radius: 20px; font-weight: bold;'>Kaggle Masterpiece</span>
        <span style='background: #80cbc4; color: #004d40; padding: 5px 15px; border-radius: 20px; font-weight: bold;'>DS Expert</span>
    </div>
</div>
""".strip()
cells.append(create_markdown_cell(header))

# 2. FOUNDATIONS
gog_section = """
## 🚀 Foundations: The Core & The Grammar

Data Visualization is the bridge between raw data and human intuition. It allows us to leverage the brain's massive visual processing power to identify complex patterns instantly.

### The Grammar of Graphics (GoG)
Think of GoG as the syntax of visualization. Every plot consists of:
- **Data**: The numbers we want to see.
- **Aesthetics**: How data maps to space (X/Y) or color.
- **Geoms**: The physical shape (points, lines, bars).
- **Facets**: Sub-dividing data into smaller grids.
- **Statistics**: Calculating moving averages, densities, or correlations.
- **Coordinates**: The map (linear, log, or polar).
- **Themes**: Everything else (fonts, margins, colors).
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

# Load Standard Datasets
tips = sns.load_dataset('tips')
iris = sns.load_dataset('iris')
gapminder = px.data.gapminder().query("year == 2007")

# Global Aesthetic Styling
sns.set_theme(style="whitegrid", palette="viridis")
plt.rcParams['figure.figsize'] = (10, 6)
print("Environment Ready: All 6 libraries and datasets are loaded.")
""".strip()
cells.append(create_code_cell(setup_code))

# Section 1-5 (Skipping full write for brevity in this step, focusing on the request)
# I will actually include them to ensure the notebook is complete as per previous versions.

# --- MATPLOTLIB ---
cells.append(create_markdown_cell("# 🛠️ Section 1: Matplotlib (The Foundation)"))
cells.append(create_markdown_cell("### 1.1 Line Plot with Variance Masking"))
cells.append(create_code_cell("""
x = np.linspace(0, 10, 100)
y = np.cumsum(np.random.randn(100))
plt.plot(x, y, color='#00796b', lw=3, label='Central Trend')
plt.fill_between(x, y-5, y+5, color='#b2dfdb', alpha=0.3, label='Standard Deviation Area')
plt.title('Time-Series Signal Analysis', fontsize=14)
plt.xlabel('Time Index')
plt.ylabel('Measured Value')
plt.legend()
plt.show()
""".strip()))

cells.append(create_markdown_cell("### 1.2 Multi-Dimensional Scatter Plot"))
cells.append(create_code_cell("""
plt.scatter(iris['sepal_length'], iris['sepal_width'], 
            c=iris['petal_length'], cmap='viridis', 
            s=iris['petal_width']*70, alpha=0.7)
plt.colorbar(label='Petal Length (Magnitude)')
plt.title('Iris Feature Space Interaction', fontsize=14)
plt.xlabel('Sepal Length')
plt.ylabel('Sepal Width')
plt.show()
""".strip()))

cells.append(create_markdown_cell("### 1.3 Bar Chart with Error Caps"))
cells.append(create_code_cell("""
means = tips.groupby('day')['total_bill'].mean()
errors = tips.groupby('day')['total_bill'].std()
plt.bar(means.index, means.values, yerr=errors, capsize=12, color='#004d40', alpha=0.8)
plt.title('Daily Average Revenue (with Variance)', fontsize=14)
plt.ylabel('Mean Bill Amount ($)')
plt.show()
""".strip()))

# --- SEABORN ---
cells.append(create_markdown_cell("# 🌊 Section 2: Seaborn (Statistical Beauty)"))
cells.append(create_markdown_cell("### 2.1 Split Violin Plot"))
cells.append(create_code_cell("""
sns.violinplot(data=tips, x='day', y='total_bill', hue='sex', split=True, palette='coolwarm')
plt.title('Distribution of Customer Bills: Day vs. Gender', fontsize=14)
plt.show()
""".strip()))

cells.append(create_markdown_cell("### 2.2 Multi-Variable Correlation Heatmap"))
cells.append(create_code_cell("""
corr = iris.drop('species', axis=1).corr()
sns.heatmap(corr, annot=True, cmap='YlGnBu', fmt=".2f")
plt.title('Inter-Feature Correlation Matrix', fontsize=14)
plt.show()
""".strip()))

cells.append(create_markdown_cell("### 2.3 Joint Regression Analysis"))
cells.append(create_code_cell("""
sns.jointplot(data=tips, x='total_bill', y='tip', kind='reg', color='#00796b')
plt.show()
""".strip()))

# --- PLOTLY ---
cells.append(create_markdown_cell("# 🎇 Section 3: Plotly (Interactive Mastery)"))
cells.append(create_markdown_cell("### 3.1 Animated Spatio-Temporal Bubble Chart"))
cells.append(create_code_cell("""
fig = px.scatter(px.data.gapminder(), x="gdpPercap", y="lifeExp", animation_frame="year", 
                 size="pop", color="continent", hover_name="country", log_x=True, size_max=50,
                 title="Global Evolution: GDP vs Life Expectancy")
fig.show()
""".strip()))

cells.append(create_markdown_cell("### 3.2 Hierarchical Sunburst Chart"))
cells.append(create_code_cell("""
fig = px.sunburst(tips, path=['day', 'time', 'sex'], values='total_bill', 
                  color='total_bill', color_continuous_scale='Viridis',
                  title="Revenue Breakdown: Day > Time > Gender")
fig.show()
""".strip()))

cells.append(create_markdown_cell("### 3.3 Interactive 3D Feature Space"))
cells.append(create_code_cell("""
fig = px.scatter_3d(iris, x='sepal_length', y='sepal_width', z='petal_width', color='species',
                    symbol='species', title="3D Spectral Analysis of Species Distribution")
fig.show()
""".strip()))

# --- ALTAIR ---
cells.append(create_markdown_cell("# 📊 Section 4: Altair (Declarative Elegance)"))
cells.append(create_markdown_cell("### 4.1 Linked Selection (Interactive Brushing)"))
cells.append(create_code_cell("""
brush = alt.selection_interval()
alt.Chart(iris).mark_point().encode(
    x='sepal_length',
    y='sepal_width',
    color=alt.condition(brush, 'species', alt.value('lightgray'))
).add_params(brush).properties(title="Interactive Cluster Exploration (Select Area)")
""".strip()))

cells.append(create_markdown_cell("### 4.2 Categorical Ranking with Sorting"))
cells.append(create_code_cell("""
alt.Chart(tips).mark_bar().encode(
    x='mean(total_bill):Q',
    y=alt.Y('day:N', sort='-x'),
    color='day:N'
).properties(title="Ranked Business Performance (Highest to Lowest)")
""".strip()))

cells.append(create_markdown_cell("### 4.3 Faceted Component Area Chart"))
cells.append(create_code_cell("""
alt.Chart(tips).mark_area(opacity=0.6).encode(
    x="total_bill:Q", y="tip:Q", color="day:N"
).facet(column='sex:N').properties(title="Cumulative Tip Analysis by Gender")
""".strip()))

# --- PLOTNINE ---
cells.append(create_markdown_cell("# 🏗️ Section 5: Plotnine (GoG Purist)"))
cells.append(create_markdown_cell("### 5.1 Faceted Regression Patterns"))
cells.append(create_code_cell("""
(ggplot(tips, aes(x='total_bill', y='tip', color='time'))
 + geom_point(alpha=0.6)
 + geom_smooth(method='lm')
 + facet_wrap('~day')
 + theme_minimal()
 + labs(title='Tip Trends Across Different Days and Times'))
""".strip()))

cells.append(create_markdown_cell("### 5.2 Probability Density Ridges"))
cells.append(create_code_cell("""
(ggplot(tips, aes(x='total_bill', fill='day'))
 + geom_density(alpha=0.6)
 + scale_fill_brewer(type='qual', palette='Set1')
 + theme_minimal()
 + labs(title='Spending Intensity Profiles per Day'))
""".strip()))

cells.append(create_markdown_cell("### 5.3 Automated Outlier Detection Grid"))
cells.append(create_code_cell("""
(ggplot(tips, aes(x='time', y='total_bill', fill='time'))
 + geom_boxplot(show_legend=False)
 + facet_wrap('~day')
 + theme_classic()
 + labs(title='Revenue Stability & Outlier Mapping'))
""".strip()))

# --- FOLIUM ---
cells.append(create_markdown_cell("# 🌍 Section 6: Folium (Geospatial Intelligence)"))

# NEW FOLIUM DATA
folium_data_setup = """
# Detailed Pakistan City Data
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
### 6.1 Geographic Hub Clustering
**Purpose**: Visualizing urban center density. Marker clustering prevents the map from becoming cluttered when viewing multiple cities.
**Interpretation**: The clusters (numbered circles) represent groups of cities. Clicking a cluster expands it, revealing individual city markers with population details.
**Kaggle Tip**: Essential for logistics and urban planning projects where data is spread across geographic coordinates.
""".strip()))
cells.append(create_code_cell("""
m1 = folium.Map(location=[30.3753, 69.3451], zoom_start=5, tiles='cartodbpositron')
cluster = MarkerCluster().add_to(m1)
for i, row in df_pak.iterrows():
    folium.Marker(
        [row['Lat'], row['Lon']],
        popup=f"<b>{row['City']}</b><br>Pop: {row['Population_M']}M<br>Prov: {row['Province']}"
    ).add_to(cluster)
m1
""".strip()))

# 6.2 Heatmap
cells.append(create_markdown_cell("""
### 6.2 Urban Intensity Heatmap
**Purpose**: Visualizing the concentration of population density across Pakistan's territory.
**Interpretation**: The intensity of the "heat" (red areas) is weighted by each city's population. It clearly highlights major socioeconomic hubs like Karachi and the Punjab heartland.
**Kaggle Tip**: Use this for demographic analysis or identifying market potential in different regional zones.
""".strip()))
cells.append(create_code_cell("""
m2 = folium.Map(location=[30, 70], zoom_start=5, tiles='cartodbpositron')
heat_data = df_pak[['Lat', 'Lon', 'Population_M']].values.tolist()
HeatMap(heat_data, radius=25, blur=15).add_to(m2)
m2
""".strip()))

# 6.3 Circle
cells.append(create_markdown_cell("""
### 6.3 Proportional Urban Comparison Maps
**Purpose**: Scaling markers proportionally to quantitative values (population) for direct visual comparison.
**Interpretation**: The radius of each circle is directly tied to the city's population. Larger circles (Karachi, Lahore) indicate larger urban magnitudes.
**Kaggle Tip**: A great alternative to choropleth maps when you have point-source data instead of regional boundary data.
""".strip()))
cells.append(create_code_cell("""
m3 = folium.Map(location=[30, 70], zoom_start=5, tiles='openstreetmap')
for i, row in df_pak.iterrows():
    folium.Circle(
        location=[row['Lat'], row['Lon']],
        radius=row['Population_M'] * 10000, # Scale for visibility
        color='#004d40',
        fill=True,
        fill_opacity=0.6,
        popup=f"{row['City']}: {row['Population_M']}M"
    ).add_to(m3)
m3
""".strip()))

# FINAL FOOTER
cells.append(create_markdown_cell("""
<div style='background-color: #004d40; color: white; padding: 25px; border-radius: 15px; text-align: center;'>
    <h3>🌟 Masterclass Complete: Lead with Data Visuals</h3>
    You now possess a professional toolkit of 18 diverse visualizations with real-world Pakistani geospatial contexts.
    <br><br>
    <i>"Visualizing the future of data, one coordinate at a time." — Muhammad Usman</i>
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

print("Notebook updated with detailed Pakistan city data for Folium.")
