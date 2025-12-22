import tkinter as tk

from plotly import express as px
from tkhtmlview import HTMLText, RenderHTML

HTML_FILEPATH = 'gdpPerCapVsLifeExpGraph.html'


# 1) Create a Plotly graph + HTML file
#    found from this site:https://matteoguzzo.com/blog/embed-html-graphs-plotly/
gapminder = px.data.gapminder()
fig = px.scatter(
    gapminder.query("year==2007"),
    x="gdpPercap",
    y="lifeExp",
    size="pop",
    color="continent",
    hover_name="country",
    log_x=True,
    size_max=60,
    height=600,
    width=975,
)
# fig.show()
with open(HTML_FILEPATH, 'w') as f:
    f.write(fig.to_html(include_plotlyjs='cdn'))


# 2) Put HTML file inside tkhtmlview widgets. Run the GUI.
root = tk.Tk()
html_label = HTMLText(root, html=RenderHTML(HTML_FILEPATH))
html_label.pack(fill="both", expand=True)
html_label.fit_height()
root.mainloop()