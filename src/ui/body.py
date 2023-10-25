import streamlit as st
from prometheus.client import Prometheus


class Prom4SeenBody:
    """Encolses the applications body"""

    def __init__(self, client: Prometheus):
        self.client = client
        self.title = st.write("# Prom4seen")
        self.line_chart = st.line_chart()
