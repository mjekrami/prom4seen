import streamlit as st


class Prom4SeenSidebar:
    def __init__(self) -> None:
        with st.sidebar:
            st.markdown("## Promethues Instances")
            self.prom_instances = st.container()
            self.prom_all = st.checkbox("Select all")
            self._prom_all_check_handler(self.prom_all)

            st.markdown("## Hello World")
            # Model Section
            model = st.selectbox(
                "Models", options=["SimpleAR", "SimpleEMR", "Other Model"]
            )
            self._change_model_handler(model)

    def _change_model_handler(self, model):
        st.markdown(f"# Model: {model}")

    def _prom_all_check_handler(self, check_val):
        if check_val:
            self.selected_prom = self.prom_instances.multiselect(
                "Select one or more prometheus instances",
                ["prom1", "prom2", "prom3"],
                ["prom1", "prom2", "prom3"],
            )
        else:
            self.selected_prom = self.prom_instances.multiselect(
                "Select on or more options", ["prom1", "prom2", "prom3"]
            )
